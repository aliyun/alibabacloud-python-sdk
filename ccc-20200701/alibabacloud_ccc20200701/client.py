# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ccc20200701 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'ccc.aliyuncs.com',
            'ap-south-1': 'ccc.aliyuncs.com',
            'ap-southeast-1': 'ccc.aliyuncs.com',
            'ap-southeast-2': 'ccc.aliyuncs.com',
            'ap-southeast-3': 'ccc.aliyuncs.com',
            'ap-southeast-5': 'ccc.aliyuncs.com',
            'cn-beijing': 'ccc.aliyuncs.com',
            'cn-chengdu': 'ccc.aliyuncs.com',
            'cn-hongkong': 'ccc.aliyuncs.com',
            'cn-huhehaote': 'ccc.aliyuncs.com',
            'cn-qingdao': 'ccc.aliyuncs.com',
            'cn-shenzhen': 'ccc.aliyuncs.com',
            'cn-zhangjiakou': 'ccc.aliyuncs.com',
            'eu-central-1': 'ccc.aliyuncs.com',
            'eu-west-1': 'ccc.aliyuncs.com',
            'me-east-1': 'ccc.aliyuncs.com',
            'us-east-1': 'ccc.aliyuncs.com',
            'us-west-1': 'ccc.aliyuncs.com',
            'cn-hangzhou-finance': 'ccc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ccc.aliyuncs.com',
            'cn-shanghai-finance-1': 'ccc.aliyuncs.com',
            'cn-north-2-gov-1': 'ccc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ccc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_campaign_with_options(
        self,
        request: main_models.AbortCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbortCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_campaign_with_options_async(
        self,
        request: main_models.AbortCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbortCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_campaign(
        self,
        request: main_models.AbortCampaignRequest,
    ) -> main_models.AbortCampaignResponse:
        runtime = RuntimeOptions()
        return self.abort_campaign_with_options(request, runtime)

    async def abort_campaign_async(
        self,
        request: main_models.AbortCampaignRequest,
    ) -> main_models.AbortCampaignResponse:
        runtime = RuntimeOptions()
        return await self.abort_campaign_with_options_async(request, runtime)

    def accept_chat_with_options(
        self,
        request: main_models.AcceptChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_chat_with_options_async(
        self,
        request: main_models.AcceptChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_chat(
        self,
        request: main_models.AcceptChatRequest,
    ) -> main_models.AcceptChatResponse:
        runtime = RuntimeOptions()
        return self.accept_chat_with_options(request, runtime)

    async def accept_chat_async(
        self,
        request: main_models.AcceptChatRequest,
    ) -> main_models.AcceptChatResponse:
        runtime = RuntimeOptions()
        return await self.accept_chat_with_options_async(request, runtime)

    def add_blacklist_call_tagging_with_options(
        self,
        request: main_models.AddBlacklistCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBlacklistCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBlacklistCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBlacklistCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_blacklist_call_tagging_with_options_async(
        self,
        request: main_models.AddBlacklistCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBlacklistCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBlacklistCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBlacklistCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_blacklist_call_tagging(
        self,
        request: main_models.AddBlacklistCallTaggingRequest,
    ) -> main_models.AddBlacklistCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.add_blacklist_call_tagging_with_options(request, runtime)

    async def add_blacklist_call_tagging_async(
        self,
        request: main_models.AddBlacklistCallTaggingRequest,
    ) -> main_models.AddBlacklistCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.add_blacklist_call_tagging_with_options_async(request, runtime)

    def add_cases_with_options(
        self,
        tmp_req: main_models.AddCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCasesResponse:
        tmp_req.validate()
        request = main_models.AddCasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.case_list):
            request.case_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cases_with_options_async(
        self,
        tmp_req: main_models.AddCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCasesResponse:
        tmp_req.validate()
        request = main_models.AddCasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.case_list):
            request.case_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cases(
        self,
        request: main_models.AddCasesRequest,
    ) -> main_models.AddCasesResponse:
        runtime = RuntimeOptions()
        return self.add_cases_with_options(request, runtime)

    async def add_cases_async(
        self,
        request: main_models.AddCasesRequest,
    ) -> main_models.AddCasesResponse:
        runtime = RuntimeOptions()
        return await self.add_cases_with_options_async(request, runtime)

    def add_feedback_with_options(
        self,
        request: main_models.AddFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rating):
            query['Rating'] = request.rating
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFeedback',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_feedback_with_options_async(
        self,
        request: main_models.AddFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rating):
            query['Rating'] = request.rating
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFeedback',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_feedback(
        self,
        request: main_models.AddFeedbackRequest,
    ) -> main_models.AddFeedbackResponse:
        runtime = RuntimeOptions()
        return self.add_feedback_with_options(request, runtime)

    async def add_feedback_async(
        self,
        request: main_models.AddFeedbackRequest,
    ) -> main_models.AddFeedbackResponse:
        runtime = RuntimeOptions()
        return await self.add_feedback_with_options_async(request, runtime)

    def add_numbers_to_skill_group_with_options(
        self,
        request: main_models.AddNumbersToSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddNumbersToSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inst_number_group_id_list):
            query['InstNumberGroupIdList'] = request.inst_number_group_id_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddNumbersToSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddNumbersToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_numbers_to_skill_group_with_options_async(
        self,
        request: main_models.AddNumbersToSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddNumbersToSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inst_number_group_id_list):
            query['InstNumberGroupIdList'] = request.inst_number_group_id_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddNumbersToSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddNumbersToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_numbers_to_skill_group(
        self,
        request: main_models.AddNumbersToSkillGroupRequest,
    ) -> main_models.AddNumbersToSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.add_numbers_to_skill_group_with_options(request, runtime)

    async def add_numbers_to_skill_group_async(
        self,
        request: main_models.AddNumbersToSkillGroupRequest,
    ) -> main_models.AddNumbersToSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_numbers_to_skill_group_with_options_async(request, runtime)

    def add_personal_numbers_to_user_with_options(
        self,
        request: main_models.AddPersonalNumbersToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPersonalNumbersToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPersonalNumbersToUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPersonalNumbersToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_personal_numbers_to_user_with_options_async(
        self,
        request: main_models.AddPersonalNumbersToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPersonalNumbersToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPersonalNumbersToUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPersonalNumbersToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_personal_numbers_to_user(
        self,
        request: main_models.AddPersonalNumbersToUserRequest,
    ) -> main_models.AddPersonalNumbersToUserResponse:
        runtime = RuntimeOptions()
        return self.add_personal_numbers_to_user_with_options(request, runtime)

    async def add_personal_numbers_to_user_async(
        self,
        request: main_models.AddPersonalNumbersToUserRequest,
    ) -> main_models.AddPersonalNumbersToUserResponse:
        runtime = RuntimeOptions()
        return await self.add_personal_numbers_to_user_with_options_async(request, runtime)

    def add_phone_number_to_skill_groups_with_options(
        self,
        request: main_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPhoneNumberToSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPhoneNumberToSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPhoneNumberToSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_phone_number_to_skill_groups_with_options_async(
        self,
        request: main_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPhoneNumberToSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPhoneNumberToSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPhoneNumberToSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_phone_number_to_skill_groups(
        self,
        request: main_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> main_models.AddPhoneNumberToSkillGroupsResponse:
        runtime = RuntimeOptions()
        return self.add_phone_number_to_skill_groups_with_options(request, runtime)

    async def add_phone_number_to_skill_groups_async(
        self,
        request: main_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> main_models.AddPhoneNumberToSkillGroupsResponse:
        runtime = RuntimeOptions()
        return await self.add_phone_number_to_skill_groups_with_options_async(request, runtime)

    def add_phone_numbers_with_options(
        self,
        request: main_models.AddPhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_group_id):
            query['NumberGroupId'] = request.number_group_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPhoneNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_phone_numbers_with_options_async(
        self,
        request: main_models.AddPhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_group_id):
            query['NumberGroupId'] = request.number_group_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPhoneNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_phone_numbers(
        self,
        request: main_models.AddPhoneNumbersRequest,
    ) -> main_models.AddPhoneNumbersResponse:
        runtime = RuntimeOptions()
        return self.add_phone_numbers_with_options(request, runtime)

    async def add_phone_numbers_async(
        self,
        request: main_models.AddPhoneNumbersRequest,
    ) -> main_models.AddPhoneNumbersResponse:
        runtime = RuntimeOptions()
        return await self.add_phone_numbers_with_options_async(request, runtime)

    def add_schema_property_with_options(
        self,
        tmp_req: main_models.AddSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSchemaPropertyResponse:
        tmp_req.validate()
        request = main_models.AddSchemaPropertyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.property):
            request.property_shrink = Utils.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_shrink):
            body['Property'] = request.property_shrink
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_schema_property_with_options_async(
        self,
        tmp_req: main_models.AddSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSchemaPropertyResponse:
        tmp_req.validate()
        request = main_models.AddSchemaPropertyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.property):
            request.property_shrink = Utils.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_shrink):
            body['Property'] = request.property_shrink
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_schema_property(
        self,
        request: main_models.AddSchemaPropertyRequest,
    ) -> main_models.AddSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return self.add_schema_property_with_options(request, runtime)

    async def add_schema_property_async(
        self,
        request: main_models.AddSchemaPropertyRequest,
    ) -> main_models.AddSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return await self.add_schema_property_with_options_async(request, runtime)

    def add_skill_groups_to_user_with_options(
        self,
        request: main_models.AddSkillGroupsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSkillGroupsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSkillGroupsToUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSkillGroupsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_skill_groups_to_user_with_options_async(
        self,
        request: main_models.AddSkillGroupsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSkillGroupsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSkillGroupsToUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSkillGroupsToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_skill_groups_to_user(
        self,
        request: main_models.AddSkillGroupsToUserRequest,
    ) -> main_models.AddSkillGroupsToUserResponse:
        runtime = RuntimeOptions()
        return self.add_skill_groups_to_user_with_options(request, runtime)

    async def add_skill_groups_to_user_async(
        self,
        request: main_models.AddSkillGroupsToUserRequest,
    ) -> main_models.AddSkillGroupsToUserResponse:
        runtime = RuntimeOptions()
        return await self.add_skill_groups_to_user_with_options_async(request, runtime)

    def add_ticket_task_with_options(
        self,
        request: main_models.AddTicketTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTicketTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.position):
            query['Position'] = request.position
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTicketTask',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTicketTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ticket_task_with_options_async(
        self,
        request: main_models.AddTicketTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTicketTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.position):
            query['Position'] = request.position
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTicketTask',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTicketTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ticket_task(
        self,
        request: main_models.AddTicketTaskRequest,
    ) -> main_models.AddTicketTaskResponse:
        runtime = RuntimeOptions()
        return self.add_ticket_task_with_options(request, runtime)

    async def add_ticket_task_async(
        self,
        request: main_models.AddTicketTaskRequest,
    ) -> main_models.AddTicketTaskResponse:
        runtime = RuntimeOptions()
        return await self.add_ticket_task_with_options_async(request, runtime)

    def add_users_to_skill_group_with_options(
        self,
        request: main_models.AddUsersToSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUsersToSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.user_skill_level_list):
            query['UserSkillLevelList'] = request.user_skill_level_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUsersToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_to_skill_group_with_options_async(
        self,
        request: main_models.AddUsersToSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUsersToSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.user_skill_level_list):
            query['UserSkillLevelList'] = request.user_skill_level_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUsersToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users_to_skill_group(
        self,
        request: main_models.AddUsersToSkillGroupRequest,
    ) -> main_models.AddUsersToSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.add_users_to_skill_group_with_options(request, runtime)

    async def add_users_to_skill_group_async(
        self,
        request: main_models.AddUsersToSkillGroupRequest,
    ) -> main_models.AddUsersToSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_users_to_skill_group_with_options_async(request, runtime)

    def analyze_conversation_with_options(
        self,
        request: main_models.AnalyzeConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeConversationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.field_list_json):
            query['FieldListJson'] = request.field_list_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_list_json):
            query['TaskListJson'] = request.task_list_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeConversation',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_conversation_with_options_async(
        self,
        request: main_models.AnalyzeConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeConversationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.field_list_json):
            query['FieldListJson'] = request.field_list_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_list_json):
            query['TaskListJson'] = request.task_list_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeConversation',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_conversation(
        self,
        request: main_models.AnalyzeConversationRequest,
    ) -> main_models.AnalyzeConversationResponse:
        runtime = RuntimeOptions()
        return self.analyze_conversation_with_options(request, runtime)

    async def analyze_conversation_async(
        self,
        request: main_models.AnalyzeConversationRequest,
    ) -> main_models.AnalyzeConversationResponse:
        runtime = RuntimeOptions()
        return await self.analyze_conversation_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: main_models.AnswerCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnswerCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnswerCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnswerCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: main_models.AnswerCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnswerCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnswerCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnswerCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def answer_call(
        self,
        request: main_models.AnswerCallRequest,
    ) -> main_models.AnswerCallResponse:
        runtime = RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: main_models.AnswerCallRequest,
    ) -> main_models.AnswerCallResponse:
        runtime = RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def append_cases_with_options(
        self,
        tmp_req: main_models.AppendCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AppendCasesResponse:
        tmp_req.validate()
        request = main_models.AppendCasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AppendCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppendCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def append_cases_with_options_async(
        self,
        tmp_req: main_models.AppendCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AppendCasesResponse:
        tmp_req.validate()
        request = main_models.AppendCasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AppendCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppendCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def append_cases(
        self,
        request: main_models.AppendCasesRequest,
    ) -> main_models.AppendCasesResponse:
        runtime = RuntimeOptions()
        return self.append_cases_with_options(request, runtime)

    async def append_cases_async(
        self,
        request: main_models.AppendCasesRequest,
    ) -> main_models.AppendCasesResponse:
        runtime = RuntimeOptions()
        return await self.append_cases_with_options_async(request, runtime)

    def assign_users_with_options(
        self,
        request: main_models.AssignUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_users_with_options_async(
        self,
        request: main_models.AssignUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_users(
        self,
        request: main_models.AssignUsersRequest,
    ) -> main_models.AssignUsersResponse:
        runtime = RuntimeOptions()
        return self.assign_users_with_options(request, runtime)

    async def assign_users_async(
        self,
        request: main_models.AssignUsersRequest,
    ) -> main_models.AssignUsersResponse:
        runtime = RuntimeOptions()
        return await self.assign_users_with_options_async(request, runtime)

    def barge_in_call_with_options(
        self,
        request: main_models.BargeInCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BargeInCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.barged_user_id):
            query['BargedUserId'] = request.barged_user_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BargeInCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BargeInCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def barge_in_call_with_options_async(
        self,
        request: main_models.BargeInCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BargeInCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.barged_user_id):
            query['BargedUserId'] = request.barged_user_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BargeInCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BargeInCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def barge_in_call(
        self,
        request: main_models.BargeInCallRequest,
    ) -> main_models.BargeInCallResponse:
        runtime = RuntimeOptions()
        return self.barge_in_call_with_options(request, runtime)

    async def barge_in_call_async(
        self,
        request: main_models.BargeInCallRequest,
    ) -> main_models.BargeInCallResponse:
        runtime = RuntimeOptions()
        return await self.barge_in_call_with_options_async(request, runtime)

    def blind_transfer_with_options(
        self,
        request: main_models.BlindTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BlindTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not DaraCore.is_null(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not DaraCore.is_null(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not DaraCore.is_null(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.transferee):
            query['Transferee'] = request.transferee
        if not DaraCore.is_null(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not DaraCore.is_null(request.transferor):
            query['Transferor'] = request.transferor
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BlindTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BlindTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def blind_transfer_with_options_async(
        self,
        request: main_models.BlindTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BlindTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not DaraCore.is_null(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not DaraCore.is_null(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not DaraCore.is_null(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.transferee):
            query['Transferee'] = request.transferee
        if not DaraCore.is_null(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not DaraCore.is_null(request.transferor):
            query['Transferor'] = request.transferor
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BlindTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BlindTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def blind_transfer(
        self,
        request: main_models.BlindTransferRequest,
    ) -> main_models.BlindTransferResponse:
        runtime = RuntimeOptions()
        return self.blind_transfer_with_options(request, runtime)

    async def blind_transfer_async(
        self,
        request: main_models.BlindTransferRequest,
    ) -> main_models.BlindTransferResponse:
        runtime = RuntimeOptions()
        return await self.blind_transfer_with_options_async(request, runtime)

    def bridge_rtc_call_with_options(
        self,
        request: main_models.BridgeRtcCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BridgeRtcCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.service_provider):
            query['ServiceProvider'] = request.service_provider
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.video_enabled):
            query['VideoEnabled'] = request.video_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BridgeRtcCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BridgeRtcCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def bridge_rtc_call_with_options_async(
        self,
        request: main_models.BridgeRtcCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BridgeRtcCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.service_provider):
            query['ServiceProvider'] = request.service_provider
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.video_enabled):
            query['VideoEnabled'] = request.video_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BridgeRtcCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BridgeRtcCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bridge_rtc_call(
        self,
        request: main_models.BridgeRtcCallRequest,
    ) -> main_models.BridgeRtcCallResponse:
        runtime = RuntimeOptions()
        return self.bridge_rtc_call_with_options(request, runtime)

    async def bridge_rtc_call_async(
        self,
        request: main_models.BridgeRtcCallRequest,
    ) -> main_models.BridgeRtcCallResponse:
        runtime = RuntimeOptions()
        return await self.bridge_rtc_call_with_options_async(request, runtime)

    def cancel_attended_transfer_with_options(
        self,
        request: main_models.CancelAttendedTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAttendedTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAttendedTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_attended_transfer_with_options_async(
        self,
        request: main_models.CancelAttendedTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAttendedTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAttendedTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_attended_transfer(
        self,
        request: main_models.CancelAttendedTransferRequest,
    ) -> main_models.CancelAttendedTransferResponse:
        runtime = RuntimeOptions()
        return self.cancel_attended_transfer_with_options(request, runtime)

    async def cancel_attended_transfer_async(
        self,
        request: main_models.CancelAttendedTransferRequest,
    ) -> main_models.CancelAttendedTransferResponse:
        runtime = RuntimeOptions()
        return await self.cancel_attended_transfer_with_options_async(request, runtime)

    def change_visibility_with_options(
        self,
        request: main_models.ChangeVisibilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeVisibilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invisible):
            query['Invisible'] = request.invisible
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeVisibility',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_visibility_with_options_async(
        self,
        request: main_models.ChangeVisibilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeVisibilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invisible):
            query['Invisible'] = request.invisible
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeVisibility',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeVisibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_visibility(
        self,
        request: main_models.ChangeVisibilityRequest,
    ) -> main_models.ChangeVisibilityResponse:
        runtime = RuntimeOptions()
        return self.change_visibility_with_options(request, runtime)

    async def change_visibility_async(
        self,
        request: main_models.ChangeVisibilityRequest,
    ) -> main_models.ChangeVisibilityResponse:
        runtime = RuntimeOptions()
        return await self.change_visibility_with_options_async(request, runtime)

    def change_work_mode_with_options(
        self,
        request: main_models.ChangeWorkModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeWorkModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeWorkMode',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeWorkModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_work_mode_with_options_async(
        self,
        request: main_models.ChangeWorkModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeWorkModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeWorkMode',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeWorkModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_work_mode(
        self,
        request: main_models.ChangeWorkModeRequest,
    ) -> main_models.ChangeWorkModeResponse:
        runtime = RuntimeOptions()
        return self.change_work_mode_with_options(request, runtime)

    async def change_work_mode_async(
        self,
        request: main_models.ChangeWorkModeRequest,
    ) -> main_models.ChangeWorkModeResponse:
        runtime = RuntimeOptions()
        return await self.change_work_mode_with_options_async(request, runtime)

    def claim_chat_with_options(
        self,
        request: main_models.ClaimChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClaimChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClaimChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClaimChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def claim_chat_with_options_async(
        self,
        request: main_models.ClaimChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClaimChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClaimChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClaimChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def claim_chat(
        self,
        request: main_models.ClaimChatRequest,
    ) -> main_models.ClaimChatResponse:
        runtime = RuntimeOptions()
        return self.claim_chat_with_options(request, runtime)

    async def claim_chat_async(
        self,
        request: main_models.ClaimChatRequest,
    ) -> main_models.ClaimChatResponse:
        runtime = RuntimeOptions()
        return await self.claim_chat_with_options_async(request, runtime)

    def coach_call_with_options(
        self,
        request: main_models.CoachCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CoachCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coached_user_id):
            query['CoachedUserId'] = request.coached_user_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CoachCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CoachCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def coach_call_with_options_async(
        self,
        request: main_models.CoachCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CoachCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coached_user_id):
            query['CoachedUserId'] = request.coached_user_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CoachCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CoachCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def coach_call(
        self,
        request: main_models.CoachCallRequest,
    ) -> main_models.CoachCallResponse:
        runtime = RuntimeOptions()
        return self.coach_call_with_options(request, runtime)

    async def coach_call_async(
        self,
        request: main_models.CoachCallRequest,
    ) -> main_models.CoachCallResponse:
        runtime = RuntimeOptions()
        return await self.coach_call_with_options_async(request, runtime)

    def commit_contact_flow_with_options(
        self,
        request: main_models.CommitContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CommitContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CommitContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CommitContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_contact_flow_with_options_async(
        self,
        request: main_models.CommitContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CommitContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CommitContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CommitContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_contact_flow(
        self,
        request: main_models.CommitContactFlowRequest,
    ) -> main_models.CommitContactFlowResponse:
        runtime = RuntimeOptions()
        return self.commit_contact_flow_with_options(request, runtime)

    async def commit_contact_flow_async(
        self,
        request: main_models.CommitContactFlowRequest,
    ) -> main_models.CommitContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.commit_contact_flow_with_options_async(request, runtime)

    def complete_attended_transfer_with_options(
        self,
        request: main_models.CompleteAttendedTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteAttendedTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompleteAttendedTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_attended_transfer_with_options_async(
        self,
        request: main_models.CompleteAttendedTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteAttendedTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompleteAttendedTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_attended_transfer(
        self,
        request: main_models.CompleteAttendedTransferRequest,
    ) -> main_models.CompleteAttendedTransferResponse:
        runtime = RuntimeOptions()
        return self.complete_attended_transfer_with_options(request, runtime)

    async def complete_attended_transfer_async(
        self,
        request: main_models.CompleteAttendedTransferRequest,
    ) -> main_models.CompleteAttendedTransferResponse:
        runtime = RuntimeOptions()
        return await self.complete_attended_transfer_with_options_async(request, runtime)

    def create_audio_file_with_options(
        self,
        request: main_models.CreateAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_audio_file_with_options_async(
        self,
        request: main_models.CreateAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_audio_file(
        self,
        request: main_models.CreateAudioFileRequest,
    ) -> main_models.CreateAudioFileResponse:
        runtime = RuntimeOptions()
        return self.create_audio_file_with_options(request, runtime)

    async def create_audio_file_async(
        self,
        request: main_models.CreateAudioFileRequest,
    ) -> main_models.CreateAudioFileResponse:
        runtime = RuntimeOptions()
        return await self.create_audio_file_with_options_async(request, runtime)

    def create_call_summary_with_options(
        self,
        request: main_models.CreateCallSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallSummary',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_call_summary_with_options_async(
        self,
        request: main_models.CreateCallSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallSummary',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_call_summary(
        self,
        request: main_models.CreateCallSummaryRequest,
    ) -> main_models.CreateCallSummaryResponse:
        runtime = RuntimeOptions()
        return self.create_call_summary_with_options(request, runtime)

    async def create_call_summary_async(
        self,
        request: main_models.CreateCallSummaryRequest,
    ) -> main_models.CreateCallSummaryResponse:
        runtime = RuntimeOptions()
        return await self.create_call_summary_with_options_async(request, runtime)

    def create_call_tags_with_options(
        self,
        request: main_models.CreateCallTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallTags',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_call_tags_with_options_async(
        self,
        request: main_models.CreateCallTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallTags',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_call_tags(
        self,
        request: main_models.CreateCallTagsRequest,
    ) -> main_models.CreateCallTagsResponse:
        runtime = RuntimeOptions()
        return self.create_call_tags_with_options(request, runtime)

    async def create_call_tags_async(
        self,
        request: main_models.CreateCallTagsRequest,
    ) -> main_models.CreateCallTagsResponse:
        runtime = RuntimeOptions()
        return await self.create_call_tags_with_options_async(request, runtime)

    def create_campaign_with_options(
        self,
        tmp_req: main_models.CreateCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCampaignResponse:
        tmp_req.validate()
        request = main_models.CreateCampaignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.case_list):
            request.case_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        if not DaraCore.is_null(tmp_req.number_list):
            request.number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.number_list, 'NumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not DaraCore.is_null(request.case_file_key):
            query['CaseFileKey'] = request.case_file_key
        if not DaraCore.is_null(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.executing_until_timeout):
            query['ExecutingUntilTimeout'] = request.executing_until_timeout
        if not DaraCore.is_null(request.flash_sms_parameters):
            query['FlashSmsParameters'] = request.flash_sms_parameters
        if not DaraCore.is_null(request.inst_group_id):
            query['InstGroupId'] = request.inst_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_attempt_count):
            query['MaxAttemptCount'] = request.max_attempt_count
        if not DaraCore.is_null(request.min_attempt_interval):
            query['MinAttemptInterval'] = request.min_attempt_interval
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.number_list_shrink):
            query['NumberList'] = request.number_list_shrink
        if not DaraCore.is_null(request.queue_id):
            query['QueueId'] = request.queue_id
        if not DaraCore.is_null(request.simulation):
            query['Simulation'] = request.simulation
        if not DaraCore.is_null(request.simulation_parameters):
            query['SimulationParameters'] = request.simulation_parameters
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        if not DaraCore.is_null(request.strategy_type):
            query['StrategyType'] = request.strategy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_campaign_with_options_async(
        self,
        tmp_req: main_models.CreateCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCampaignResponse:
        tmp_req.validate()
        request = main_models.CreateCampaignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.case_list):
            request.case_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        if not DaraCore.is_null(tmp_req.number_list):
            request.number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.number_list, 'NumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not DaraCore.is_null(request.case_file_key):
            query['CaseFileKey'] = request.case_file_key
        if not DaraCore.is_null(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.executing_until_timeout):
            query['ExecutingUntilTimeout'] = request.executing_until_timeout
        if not DaraCore.is_null(request.flash_sms_parameters):
            query['FlashSmsParameters'] = request.flash_sms_parameters
        if not DaraCore.is_null(request.inst_group_id):
            query['InstGroupId'] = request.inst_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_attempt_count):
            query['MaxAttemptCount'] = request.max_attempt_count
        if not DaraCore.is_null(request.min_attempt_interval):
            query['MinAttemptInterval'] = request.min_attempt_interval
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.number_list_shrink):
            query['NumberList'] = request.number_list_shrink
        if not DaraCore.is_null(request.queue_id):
            query['QueueId'] = request.queue_id
        if not DaraCore.is_null(request.simulation):
            query['Simulation'] = request.simulation
        if not DaraCore.is_null(request.simulation_parameters):
            query['SimulationParameters'] = request.simulation_parameters
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        if not DaraCore.is_null(request.strategy_type):
            query['StrategyType'] = request.strategy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_campaign(
        self,
        request: main_models.CreateCampaignRequest,
    ) -> main_models.CreateCampaignResponse:
        runtime = RuntimeOptions()
        return self.create_campaign_with_options(request, runtime)

    async def create_campaign_async(
        self,
        request: main_models.CreateCampaignRequest,
    ) -> main_models.CreateCampaignResponse:
        runtime = RuntimeOptions()
        return await self.create_campaign_with_options_async(request, runtime)

    def create_chat_media_url_with_options(
        self,
        request: main_models.CreateChatMediaUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatMediaUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mime_type):
            body['MimeType'] = request.mime_type
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatMediaUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatMediaUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_media_url_with_options_async(
        self,
        request: main_models.CreateChatMediaUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatMediaUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mime_type):
            body['MimeType'] = request.mime_type
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatMediaUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatMediaUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_media_url(
        self,
        request: main_models.CreateChatMediaUrlRequest,
    ) -> main_models.CreateChatMediaUrlResponse:
        runtime = RuntimeOptions()
        return self.create_chat_media_url_with_options(request, runtime)

    async def create_chat_media_url_async(
        self,
        request: main_models.CreateChatMediaUrlRequest,
    ) -> main_models.CreateChatMediaUrlResponse:
        runtime = RuntimeOptions()
        return await self.create_chat_media_url_with_options_async(request, runtime)

    def create_contact_flow_with_options(
        self,
        request: main_models.CreateContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_contact_flow_with_options_async(
        self,
        request: main_models.CreateContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_contact_flow(
        self,
        request: main_models.CreateContactFlowRequest,
    ) -> main_models.CreateContactFlowResponse:
        runtime = RuntimeOptions()
        return self.create_contact_flow_with_options(request, runtime)

    async def create_contact_flow_async(
        self,
        request: main_models.CreateContactFlowRequest,
    ) -> main_models.CreateContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.create_contact_flow_with_options_async(request, runtime)

    def create_custom_call_tagging_with_options(
        self,
        request: main_models.CreateCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_number_list):
            query['CustomNumberList'] = request.custom_number_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_call_tagging_with_options_async(
        self,
        request: main_models.CreateCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_number_list):
            query['CustomNumberList'] = request.custom_number_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_call_tagging(
        self,
        request: main_models.CreateCustomCallTaggingRequest,
    ) -> main_models.CreateCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.create_custom_call_tagging_with_options(request, runtime)

    async def create_custom_call_tagging_async(
        self,
        request: main_models.CreateCustomCallTaggingRequest,
    ) -> main_models.CreateCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_call_tagging_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_ram_id_list):
            query['AdminRamIdList'] = request.admin_ram_id_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_ram_id_list):
            query['AdminRamIdList'] = request.admin_ram_id_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_schema_with_options(
        self,
        tmp_req: main_models.CreateSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchemaResponse:
        tmp_req.validate()
        request = main_models.CreateSchemaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.properties):
            request.properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchema',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schema_with_options_async(
        self,
        tmp_req: main_models.CreateSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchemaResponse:
        tmp_req.validate()
        request = main_models.CreateSchemaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.properties):
            request.properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchema',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schema(
        self,
        request: main_models.CreateSchemaRequest,
    ) -> main_models.CreateSchemaResponse:
        runtime = RuntimeOptions()
        return self.create_schema_with_options(request, runtime)

    async def create_schema_async(
        self,
        request: main_models.CreateSchemaRequest,
    ) -> main_models.CreateSchemaResponse:
        runtime = RuntimeOptions()
        return await self.create_schema_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: main_models.CreateSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: main_models.CreateSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_group(
        self,
        request: main_models.CreateSkillGroupRequest,
    ) -> main_models.CreateSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: main_models.CreateSkillGroupRequest,
    ) -> main_models.CreateSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def create_ticket_with_options(
        self,
        request: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    async def create_ticket_async(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        return await self.create_ticket_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not DaraCore.is_null(request.display_id):
            query['DisplayId'] = request.display_id
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_name):
            query['LoginName'] = request.login_name
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.need_email_notification):
            query['NeedEmailNotification'] = request.need_email_notification
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.reset_password):
            query['ResetPassword'] = request.reset_password
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not DaraCore.is_null(request.display_id):
            query['DisplayId'] = request.display_id
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_name):
            query['LoginName'] = request.login_name
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.need_email_notification):
            query['NeedEmailNotification'] = request.need_email_notification
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.reset_password):
            query['ResetPassword'] = request.reset_password
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def delete_audio_file_with_options(
        self,
        request: main_models.DeleteAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_audio_file_with_options_async(
        self,
        request: main_models.DeleteAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_audio_file(
        self,
        request: main_models.DeleteAudioFileRequest,
    ) -> main_models.DeleteAudioFileResponse:
        runtime = RuntimeOptions()
        return self.delete_audio_file_with_options(request, runtime)

    async def delete_audio_file_async(
        self,
        request: main_models.DeleteAudioFileRequest,
    ) -> main_models.DeleteAudioFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_audio_file_with_options_async(request, runtime)

    def delete_call_tag_with_options(
        self,
        request: main_models.DeleteCallTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCallTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCallTag',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCallTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_call_tag_with_options_async(
        self,
        request: main_models.DeleteCallTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCallTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCallTag',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCallTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_call_tag(
        self,
        request: main_models.DeleteCallTagRequest,
    ) -> main_models.DeleteCallTagResponse:
        runtime = RuntimeOptions()
        return self.delete_call_tag_with_options(request, runtime)

    async def delete_call_tag_async(
        self,
        request: main_models.DeleteCallTagRequest,
    ) -> main_models.DeleteCallTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_call_tag_with_options_async(request, runtime)

    def delete_contact_flow_with_options(
        self,
        request: main_models.DeleteContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_flow_with_options_async(
        self,
        request: main_models.DeleteContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_flow(
        self,
        request: main_models.DeleteContactFlowRequest,
    ) -> main_models.DeleteContactFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_flow_with_options(request, runtime)

    async def delete_contact_flow_async(
        self,
        request: main_models.DeleteContactFlowRequest,
    ) -> main_models.DeleteContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_flow_with_options_async(request, runtime)

    def delete_custom_call_tagging_with_options(
        self,
        request: main_models.DeleteCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_call_tagging_with_options_async(
        self,
        request: main_models.DeleteCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_call_tagging(
        self,
        request: main_models.DeleteCustomCallTaggingRequest,
    ) -> main_models.DeleteCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_call_tagging_with_options(request, runtime)

    async def delete_custom_call_tagging_async(
        self,
        request: main_models.DeleteCustomCallTaggingRequest,
    ) -> main_models.DeleteCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_call_tagging_with_options_async(request, runtime)

    def delete_document_with_options(
        self,
        request: main_models.DeleteDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_id):
            body['DocumentId'] = request.document_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        request: main_models.DeleteDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_id):
            body['DocumentId'] = request.document_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        return self.delete_document_with_options(request, runtime)

    async def delete_document_async(
        self,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        return await self.delete_document_with_options_async(request, runtime)

    def delete_documents_with_options(
        self,
        tmp_req: main_models.DeleteDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentsResponse:
        tmp_req.validate()
        request = main_models.DeleteDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        body = {}
        if not DaraCore.is_null(request.document_ids_shrink):
            body['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocuments',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_documents_with_options_async(
        self,
        tmp_req: main_models.DeleteDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentsResponse:
        tmp_req.validate()
        request = main_models.DeleteDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        body = {}
        if not DaraCore.is_null(request.document_ids_shrink):
            body['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocuments',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_documents(
        self,
        request: main_models.DeleteDocumentsRequest,
    ) -> main_models.DeleteDocumentsResponse:
        runtime = RuntimeOptions()
        return self.delete_documents_with_options(request, runtime)

    async def delete_documents_async(
        self,
        request: main_models.DeleteDocumentsRequest,
    ) -> main_models.DeleteDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.delete_documents_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_schema_with_options(
        self,
        request: main_models.DeleteSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchema',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schema_with_options_async(
        self,
        request: main_models.DeleteSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchema',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schema(
        self,
        request: main_models.DeleteSchemaRequest,
    ) -> main_models.DeleteSchemaResponse:
        runtime = RuntimeOptions()
        return self.delete_schema_with_options(request, runtime)

    async def delete_schema_async(
        self,
        request: main_models.DeleteSchemaRequest,
    ) -> main_models.DeleteSchemaResponse:
        runtime = RuntimeOptions()
        return await self.delete_schema_with_options_async(request, runtime)

    def delete_schema_property_with_options(
        self,
        request: main_models.DeleteSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemaPropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_name):
            body['PropertyName'] = request.property_name
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schema_property_with_options_async(
        self,
        request: main_models.DeleteSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemaPropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_name):
            body['PropertyName'] = request.property_name
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schema_property(
        self,
        request: main_models.DeleteSchemaPropertyRequest,
    ) -> main_models.DeleteSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return self.delete_schema_property_with_options(request, runtime)

    async def delete_schema_property_async(
        self,
        request: main_models.DeleteSchemaPropertyRequest,
    ) -> main_models.DeleteSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return await self.delete_schema_property_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: main_models.DeleteSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: main_models.DeleteSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_group(
        self,
        request: main_models.DeleteSkillGroupRequest,
    ) -> main_models.DeleteSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: main_models.DeleteSkillGroupRequest,
    ) -> main_models.DeleteSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def delete_ticket_with_options(
        self,
        request: main_models.DeleteTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ticket_with_options_async(
        self,
        request: main_models.DeleteTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ticket(
        self,
        request: main_models.DeleteTicketRequest,
    ) -> main_models.DeleteTicketResponse:
        runtime = RuntimeOptions()
        return self.delete_ticket_with_options(request, runtime)

    async def delete_ticket_async(
        self,
        request: main_models.DeleteTicketRequest,
    ) -> main_models.DeleteTicketResponse:
        runtime = RuntimeOptions()
        return await self.delete_ticket_with_options_async(request, runtime)

    def delete_ticket_template_with_options(
        self,
        request: main_models.DeleteTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTicketTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ticket_template_with_options_async(
        self,
        request: main_models.DeleteTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTicketTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ticket_template(
        self,
        request: main_models.DeleteTicketTemplateRequest,
    ) -> main_models.DeleteTicketTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_ticket_template_with_options(request, runtime)

    async def delete_ticket_template_async(
        self,
        request: main_models.DeleteTicketTemplateRequest,
    ) -> main_models.DeleteTicketTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_ticket_template_with_options_async(request, runtime)

    def disable_schema_property_with_options(
        self,
        request: main_models.DisableSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSchemaPropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_name):
            body['PropertyName'] = request.property_name
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_schema_property_with_options_async(
        self,
        request: main_models.DisableSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSchemaPropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_name):
            body['PropertyName'] = request.property_name
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_schema_property(
        self,
        request: main_models.DisableSchemaPropertyRequest,
    ) -> main_models.DisableSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return self.disable_schema_property_with_options(request, runtime)

    async def disable_schema_property_async(
        self,
        request: main_models.DisableSchemaPropertyRequest,
    ) -> main_models.DisableSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return await self.disable_schema_property_with_options_async(request, runtime)

    def disable_ticket_template_with_options(
        self,
        request: main_models.DisableTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableTicketTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_ticket_template_with_options_async(
        self,
        request: main_models.DisableTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableTicketTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_ticket_template(
        self,
        request: main_models.DisableTicketTemplateRequest,
    ) -> main_models.DisableTicketTemplateResponse:
        runtime = RuntimeOptions()
        return self.disable_ticket_template_with_options(request, runtime)

    async def disable_ticket_template_async(
        self,
        request: main_models.DisableTicketTemplateRequest,
    ) -> main_models.DisableTicketTemplateResponse:
        runtime = RuntimeOptions()
        return await self.disable_ticket_template_with_options_async(request, runtime)

    def discard_editing_contact_flow_with_options(
        self,
        request: main_models.DiscardEditingContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiscardEditingContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DiscardEditingContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiscardEditingContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def discard_editing_contact_flow_with_options_async(
        self,
        request: main_models.DiscardEditingContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiscardEditingContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DiscardEditingContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiscardEditingContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def discard_editing_contact_flow(
        self,
        request: main_models.DiscardEditingContactFlowRequest,
    ) -> main_models.DiscardEditingContactFlowResponse:
        runtime = RuntimeOptions()
        return self.discard_editing_contact_flow_with_options(request, runtime)

    async def discard_editing_contact_flow_async(
        self,
        request: main_models.DiscardEditingContactFlowRequest,
    ) -> main_models.DiscardEditingContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.discard_editing_contact_flow_with_options_async(request, runtime)

    def enable_schema_property_with_options(
        self,
        request: main_models.EnableSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSchemaPropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_name):
            body['PropertyName'] = request.property_name
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_schema_property_with_options_async(
        self,
        request: main_models.EnableSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSchemaPropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_name):
            body['PropertyName'] = request.property_name
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_schema_property(
        self,
        request: main_models.EnableSchemaPropertyRequest,
    ) -> main_models.EnableSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return self.enable_schema_property_with_options(request, runtime)

    async def enable_schema_property_async(
        self,
        request: main_models.EnableSchemaPropertyRequest,
    ) -> main_models.EnableSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return await self.enable_schema_property_with_options_async(request, runtime)

    def enable_ticket_template_with_options(
        self,
        request: main_models.EnableTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableTicketTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_ticket_template_with_options_async(
        self,
        request: main_models.EnableTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableTicketTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_ticket_template(
        self,
        request: main_models.EnableTicketTemplateRequest,
    ) -> main_models.EnableTicketTemplateResponse:
        runtime = RuntimeOptions()
        return self.enable_ticket_template_with_options(request, runtime)

    async def enable_ticket_template_async(
        self,
        request: main_models.EnableTicketTemplateRequest,
    ) -> main_models.EnableTicketTemplateResponse:
        runtime = RuntimeOptions()
        return await self.enable_ticket_template_with_options_async(request, runtime)

    def end_conference_with_options(
        self,
        request: main_models.EndConferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndConferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndConference',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_conference_with_options_async(
        self,
        request: main_models.EndConferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndConferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndConference',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_conference(
        self,
        request: main_models.EndConferenceRequest,
    ) -> main_models.EndConferenceResponse:
        runtime = RuntimeOptions()
        return self.end_conference_with_options(request, runtime)

    async def end_conference_async(
        self,
        request: main_models.EndConferenceRequest,
    ) -> main_models.EndConferenceResponse:
        runtime = RuntimeOptions()
        return await self.end_conference_with_options_async(request, runtime)

    def export_contact_flow_with_options(
        self,
        request: main_models.ExportContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportContactFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_id):
            body['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_contact_flow_with_options_async(
        self,
        request: main_models.ExportContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportContactFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_id):
            body['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_contact_flow(
        self,
        request: main_models.ExportContactFlowRequest,
    ) -> main_models.ExportContactFlowResponse:
        runtime = RuntimeOptions()
        return self.export_contact_flow_with_options(request, runtime)

    async def export_contact_flow_async(
        self,
        request: main_models.ExportContactFlowRequest,
    ) -> main_models.ExportContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.export_contact_flow_with_options_async(request, runtime)

    def export_custom_call_tagging_with_options(
        self,
        request: main_models.ExportCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_custom_call_tagging_with_options_async(
        self,
        request: main_models.ExportCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_custom_call_tagging(
        self,
        request: main_models.ExportCustomCallTaggingRequest,
    ) -> main_models.ExportCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.export_custom_call_tagging_with_options(request, runtime)

    async def export_custom_call_tagging_async(
        self,
        request: main_models.ExportCustomCallTaggingRequest,
    ) -> main_models.ExportCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.export_custom_call_tagging_with_options_async(request, runtime)

    def export_do_not_call_numbers_with_options(
        self,
        request: main_models.ExportDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_do_not_call_numbers_with_options_async(
        self,
        request: main_models.ExportDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_do_not_call_numbers(
        self,
        request: main_models.ExportDoNotCallNumbersRequest,
    ) -> main_models.ExportDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return self.export_do_not_call_numbers_with_options(request, runtime)

    async def export_do_not_call_numbers_async(
        self,
        request: main_models.ExportDoNotCallNumbersRequest,
    ) -> main_models.ExportDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return await self.export_do_not_call_numbers_with_options_async(request, runtime)

    def finish_ticket_task_with_options(
        self,
        request: main_models.FinishTicketTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishTicketTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishTicketTask',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishTicketTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_ticket_task_with_options_async(
        self,
        request: main_models.FinishTicketTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FinishTicketTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishTicketTask',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishTicketTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_ticket_task(
        self,
        request: main_models.FinishTicketTaskRequest,
    ) -> main_models.FinishTicketTaskResponse:
        runtime = RuntimeOptions()
        return self.finish_ticket_task_with_options(request, runtime)

    async def finish_ticket_task_async(
        self,
        request: main_models.FinishTicketTaskRequest,
    ) -> main_models.FinishTicketTaskResponse:
        runtime = RuntimeOptions()
        return await self.finish_ticket_task_with_options_async(request, runtime)

    def get_access_channel_of_staging_with_options(
        self,
        request: main_models.GetAccessChannelOfStagingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessChannelOfStagingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessChannelOfStaging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessChannelOfStagingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_channel_of_staging_with_options_async(
        self,
        request: main_models.GetAccessChannelOfStagingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessChannelOfStagingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessChannelOfStaging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessChannelOfStagingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_channel_of_staging(
        self,
        request: main_models.GetAccessChannelOfStagingRequest,
    ) -> main_models.GetAccessChannelOfStagingResponse:
        runtime = RuntimeOptions()
        return self.get_access_channel_of_staging_with_options(request, runtime)

    async def get_access_channel_of_staging_async(
        self,
        request: main_models.GetAccessChannelOfStagingRequest,
    ) -> main_models.GetAccessChannelOfStagingResponse:
        runtime = RuntimeOptions()
        return await self.get_access_channel_of_staging_with_options_async(request, runtime)

    def get_audio_file_with_options(
        self,
        request: main_models.GetAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audio_file_with_options_async(
        self,
        request: main_models.GetAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audio_file(
        self,
        request: main_models.GetAudioFileRequest,
    ) -> main_models.GetAudioFileResponse:
        runtime = RuntimeOptions()
        return self.get_audio_file_with_options(request, runtime)

    async def get_audio_file_async(
        self,
        request: main_models.GetAudioFileRequest,
    ) -> main_models.GetAudioFileResponse:
        runtime = RuntimeOptions()
        return await self.get_audio_file_with_options_async(request, runtime)

    def get_audio_file_download_url_with_options(
        self,
        request: main_models.GetAudioFileDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioFileDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioFileDownloadUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioFileDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audio_file_download_url_with_options_async(
        self,
        request: main_models.GetAudioFileDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioFileDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioFileDownloadUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioFileDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audio_file_download_url(
        self,
        request: main_models.GetAudioFileDownloadUrlRequest,
    ) -> main_models.GetAudioFileDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.get_audio_file_download_url_with_options(request, runtime)

    async def get_audio_file_download_url_async(
        self,
        request: main_models.GetAudioFileDownloadUrlRequest,
    ) -> main_models.GetAudioFileDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_audio_file_download_url_with_options_async(request, runtime)

    def get_audio_file_upload_parameters_with_options(
        self,
        request: main_models.GetAudioFileUploadParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioFileUploadParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioFileUploadParameters',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioFileUploadParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audio_file_upload_parameters_with_options_async(
        self,
        request: main_models.GetAudioFileUploadParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioFileUploadParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioFileUploadParameters',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioFileUploadParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audio_file_upload_parameters(
        self,
        request: main_models.GetAudioFileUploadParametersRequest,
    ) -> main_models.GetAudioFileUploadParametersResponse:
        runtime = RuntimeOptions()
        return self.get_audio_file_upload_parameters_with_options(request, runtime)

    async def get_audio_file_upload_parameters_async(
        self,
        request: main_models.GetAudioFileUploadParametersRequest,
    ) -> main_models.GetAudioFileUploadParametersResponse:
        runtime = RuntimeOptions()
        return await self.get_audio_file_upload_parameters_with_options_async(request, runtime)

    def get_call_detail_record_with_options(
        self,
        request: main_models.GetCallDetailRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallDetailRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallDetailRecord',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallDetailRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_detail_record_with_options_async(
        self,
        request: main_models.GetCallDetailRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallDetailRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallDetailRecord',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallDetailRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_detail_record(
        self,
        request: main_models.GetCallDetailRecordRequest,
    ) -> main_models.GetCallDetailRecordResponse:
        runtime = RuntimeOptions()
        return self.get_call_detail_record_with_options(request, runtime)

    async def get_call_detail_record_async(
        self,
        request: main_models.GetCallDetailRecordRequest,
    ) -> main_models.GetCallDetailRecordResponse:
        runtime = RuntimeOptions()
        return await self.get_call_detail_record_with_options_async(request, runtime)

    def get_campaign_with_options(
        self,
        request: main_models.GetCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_campaign_with_options_async(
        self,
        request: main_models.GetCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_campaign(
        self,
        request: main_models.GetCampaignRequest,
    ) -> main_models.GetCampaignResponse:
        runtime = RuntimeOptions()
        return self.get_campaign_with_options(request, runtime)

    async def get_campaign_async(
        self,
        request: main_models.GetCampaignRequest,
    ) -> main_models.GetCampaignResponse:
        runtime = RuntimeOptions()
        return await self.get_campaign_with_options_async(request, runtime)

    def get_case_file_upload_url_with_options(
        self,
        request: main_models.GetCaseFileUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCaseFileUploadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCaseFileUploadUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCaseFileUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_case_file_upload_url_with_options_async(
        self,
        request: main_models.GetCaseFileUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCaseFileUploadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCaseFileUploadUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCaseFileUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_case_file_upload_url(
        self,
        request: main_models.GetCaseFileUploadUrlRequest,
    ) -> main_models.GetCaseFileUploadUrlResponse:
        runtime = RuntimeOptions()
        return self.get_case_file_upload_url_with_options(request, runtime)

    async def get_case_file_upload_url_async(
        self,
        request: main_models.GetCaseFileUploadUrlRequest,
    ) -> main_models.GetCaseFileUploadUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_case_file_upload_url_with_options_async(request, runtime)

    def get_chat_media_url_with_options(
        self,
        request: main_models.GetChatMediaUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatMediaUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_id):
            body['MediaId'] = request.media_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatMediaUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatMediaUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_media_url_with_options_async(
        self,
        request: main_models.GetChatMediaUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatMediaUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_id):
            body['MediaId'] = request.media_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatMediaUrl',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatMediaUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_media_url(
        self,
        request: main_models.GetChatMediaUrlRequest,
    ) -> main_models.GetChatMediaUrlResponse:
        runtime = RuntimeOptions()
        return self.get_chat_media_url_with_options(request, runtime)

    async def get_chat_media_url_async(
        self,
        request: main_models.GetChatMediaUrlRequest,
    ) -> main_models.GetChatMediaUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_chat_media_url_with_options_async(request, runtime)

    def get_chat_routing_profile_with_options(
        self,
        request: main_models.GetChatRoutingProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatRoutingProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatRoutingProfile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatRoutingProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_routing_profile_with_options_async(
        self,
        request: main_models.GetChatRoutingProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatRoutingProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatRoutingProfile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatRoutingProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_routing_profile(
        self,
        request: main_models.GetChatRoutingProfileRequest,
    ) -> main_models.GetChatRoutingProfileResponse:
        runtime = RuntimeOptions()
        return self.get_chat_routing_profile_with_options(request, runtime)

    async def get_chat_routing_profile_async(
        self,
        request: main_models.GetChatRoutingProfileRequest,
    ) -> main_models.GetChatRoutingProfileResponse:
        runtime = RuntimeOptions()
        return await self.get_chat_routing_profile_with_options_async(request, runtime)

    def get_contact_flow_with_options(
        self,
        request: main_models.GetContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contact_flow_with_options_async(
        self,
        request: main_models.GetContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contact_flow(
        self,
        request: main_models.GetContactFlowRequest,
    ) -> main_models.GetContactFlowResponse:
        runtime = RuntimeOptions()
        return self.get_contact_flow_with_options(request, runtime)

    async def get_contact_flow_async(
        self,
        request: main_models.GetContactFlowRequest,
    ) -> main_models.GetContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.get_contact_flow_with_options_async(request, runtime)

    def get_conversation_detail_with_options(
        self,
        request: main_models.GetConversationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConversationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConversationDetail',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConversationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversation_detail_with_options_async(
        self,
        request: main_models.GetConversationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConversationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConversationDetail',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConversationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conversation_detail(
        self,
        request: main_models.GetConversationDetailRequest,
    ) -> main_models.GetConversationDetailResponse:
        runtime = RuntimeOptions()
        return self.get_conversation_detail_with_options(request, runtime)

    async def get_conversation_detail_async(
        self,
        request: main_models.GetConversationDetailRequest,
    ) -> main_models.GetConversationDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_conversation_detail_with_options_async(request, runtime)

    def get_data_channel_credentials_with_options(
        self,
        request: main_models.GetDataChannelCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataChannelCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataChannelCredentials',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataChannelCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_channel_credentials_with_options_async(
        self,
        request: main_models.GetDataChannelCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataChannelCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataChannelCredentials',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataChannelCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_channel_credentials(
        self,
        request: main_models.GetDataChannelCredentialsRequest,
    ) -> main_models.GetDataChannelCredentialsResponse:
        runtime = RuntimeOptions()
        return self.get_data_channel_credentials_with_options(request, runtime)

    async def get_data_channel_credentials_async(
        self,
        request: main_models.GetDataChannelCredentialsRequest,
    ) -> main_models.GetDataChannelCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.get_data_channel_credentials_with_options_async(request, runtime)

    def get_do_not_call_file_upload_parameters_with_options(
        self,
        request: main_models.GetDoNotCallFileUploadParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoNotCallFileUploadParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoNotCallFileUploadParameters',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoNotCallFileUploadParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_do_not_call_file_upload_parameters_with_options_async(
        self,
        request: main_models.GetDoNotCallFileUploadParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoNotCallFileUploadParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoNotCallFileUploadParameters',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoNotCallFileUploadParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_do_not_call_file_upload_parameters(
        self,
        request: main_models.GetDoNotCallFileUploadParametersRequest,
    ) -> main_models.GetDoNotCallFileUploadParametersResponse:
        runtime = RuntimeOptions()
        return self.get_do_not_call_file_upload_parameters_with_options(request, runtime)

    async def get_do_not_call_file_upload_parameters_async(
        self,
        request: main_models.GetDoNotCallFileUploadParametersRequest,
    ) -> main_models.GetDoNotCallFileUploadParametersResponse:
        runtime = RuntimeOptions()
        return await self.get_do_not_call_file_upload_parameters_with_options_async(request, runtime)

    def get_document_upload_parameters_with_options(
        self,
        request: main_models.GetDocumentUploadParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentUploadParametersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentUploadParameters',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentUploadParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_upload_parameters_with_options_async(
        self,
        request: main_models.GetDocumentUploadParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentUploadParametersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentUploadParameters',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentUploadParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_upload_parameters(
        self,
        request: main_models.GetDocumentUploadParametersRequest,
    ) -> main_models.GetDocumentUploadParametersResponse:
        runtime = RuntimeOptions()
        return self.get_document_upload_parameters_with_options(request, runtime)

    async def get_document_upload_parameters_async(
        self,
        request: main_models.GetDocumentUploadParametersRequest,
    ) -> main_models.GetDocumentUploadParametersResponse:
        runtime = RuntimeOptions()
        return await self.get_document_upload_parameters_with_options_async(request, runtime)

    def get_early_media_recording_with_options(
        self,
        request: main_models.GetEarlyMediaRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEarlyMediaRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEarlyMediaRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEarlyMediaRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_early_media_recording_with_options_async(
        self,
        request: main_models.GetEarlyMediaRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEarlyMediaRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEarlyMediaRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEarlyMediaRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_early_media_recording(
        self,
        request: main_models.GetEarlyMediaRecordingRequest,
    ) -> main_models.GetEarlyMediaRecordingResponse:
        runtime = RuntimeOptions()
        return self.get_early_media_recording_with_options(request, runtime)

    async def get_early_media_recording_async(
        self,
        request: main_models.GetEarlyMediaRecordingRequest,
    ) -> main_models.GetEarlyMediaRecordingResponse:
        runtime = RuntimeOptions()
        return await self.get_early_media_recording_with_options_async(request, runtime)

    def get_historical_caller_report_with_options(
        self,
        request: main_models.GetHistoricalCallerReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoricalCallerReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stop_time):
            query['StopTime'] = request.stop_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoricalCallerReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoricalCallerReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_caller_report_with_options_async(
        self,
        request: main_models.GetHistoricalCallerReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoricalCallerReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stop_time):
            query['StopTime'] = request.stop_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoricalCallerReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoricalCallerReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_caller_report(
        self,
        request: main_models.GetHistoricalCallerReportRequest,
    ) -> main_models.GetHistoricalCallerReportResponse:
        runtime = RuntimeOptions()
        return self.get_historical_caller_report_with_options(request, runtime)

    async def get_historical_caller_report_async(
        self,
        request: main_models.GetHistoricalCallerReportRequest,
    ) -> main_models.GetHistoricalCallerReportResponse:
        runtime = RuntimeOptions()
        return await self.get_historical_caller_report_with_options_async(request, runtime)

    def get_historical_campaign_report_with_options(
        self,
        request: main_models.GetHistoricalCampaignReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoricalCampaignReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoricalCampaignReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoricalCampaignReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_campaign_report_with_options_async(
        self,
        request: main_models.GetHistoricalCampaignReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoricalCampaignReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoricalCampaignReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoricalCampaignReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_campaign_report(
        self,
        request: main_models.GetHistoricalCampaignReportRequest,
    ) -> main_models.GetHistoricalCampaignReportResponse:
        runtime = RuntimeOptions()
        return self.get_historical_campaign_report_with_options(request, runtime)

    async def get_historical_campaign_report_async(
        self,
        request: main_models.GetHistoricalCampaignReportRequest,
    ) -> main_models.GetHistoricalCampaignReportResponse:
        runtime = RuntimeOptions()
        return await self.get_historical_campaign_report_with_options_async(request, runtime)

    def get_historical_instance_report_with_options(
        self,
        request: main_models.GetHistoricalInstanceReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoricalInstanceReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoricalInstanceReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoricalInstanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_instance_report_with_options_async(
        self,
        request: main_models.GetHistoricalInstanceReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoricalInstanceReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoricalInstanceReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoricalInstanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_instance_report(
        self,
        request: main_models.GetHistoricalInstanceReportRequest,
    ) -> main_models.GetHistoricalInstanceReportResponse:
        runtime = RuntimeOptions()
        return self.get_historical_instance_report_with_options(request, runtime)

    async def get_historical_instance_report_async(
        self,
        request: main_models.GetHistoricalInstanceReportRequest,
    ) -> main_models.GetHistoricalInstanceReportResponse:
        runtime = RuntimeOptions()
        return await self.get_historical_instance_report_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_trending_report_with_options(
        self,
        request: main_models.GetInstanceTrendingReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceTrendingReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceTrendingReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceTrendingReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_trending_report_with_options_async(
        self,
        request: main_models.GetInstanceTrendingReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceTrendingReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceTrendingReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceTrendingReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_trending_report(
        self,
        request: main_models.GetInstanceTrendingReportRequest,
    ) -> main_models.GetInstanceTrendingReportResponse:
        runtime = RuntimeOptions()
        return self.get_instance_trending_report_with_options(request, runtime)

    async def get_instance_trending_report_async(
        self,
        request: main_models.GetInstanceTrendingReportRequest,
    ) -> main_models.GetInstanceTrendingReportResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_trending_report_with_options_async(request, runtime)

    def get_ivr_tracking_summary_with_options(
        self,
        request: main_models.GetIvrTrackingSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIvrTrackingSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIvrTrackingSummary',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIvrTrackingSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ivr_tracking_summary_with_options_async(
        self,
        request: main_models.GetIvrTrackingSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIvrTrackingSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIvrTrackingSummary',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIvrTrackingSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ivr_tracking_summary(
        self,
        request: main_models.GetIvrTrackingSummaryRequest,
    ) -> main_models.GetIvrTrackingSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_ivr_tracking_summary_with_options(request, runtime)

    async def get_ivr_tracking_summary_async(
        self,
        request: main_models.GetIvrTrackingSummaryRequest,
    ) -> main_models.GetIvrTrackingSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_ivr_tracking_summary_with_options_async(request, runtime)

    def get_login_details_with_options(
        self,
        request: main_models.GetLoginDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginDetails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_details_with_options_async(
        self,
        request: main_models.GetLoginDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginDetails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_details(
        self,
        request: main_models.GetLoginDetailsRequest,
    ) -> main_models.GetLoginDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_login_details_with_options(request, runtime)

    async def get_login_details_async(
        self,
        request: main_models.GetLoginDetailsRequest,
    ) -> main_models.GetLoginDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_login_details_with_options_async(request, runtime)

    def get_mono_recording_with_options(
        self,
        request: main_models.GetMonoRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMonoRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonoRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonoRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mono_recording_with_options_async(
        self,
        request: main_models.GetMonoRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMonoRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonoRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonoRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mono_recording(
        self,
        request: main_models.GetMonoRecordingRequest,
    ) -> main_models.GetMonoRecordingResponse:
        runtime = RuntimeOptions()
        return self.get_mono_recording_with_options(request, runtime)

    async def get_mono_recording_async(
        self,
        request: main_models.GetMonoRecordingRequest,
    ) -> main_models.GetMonoRecordingResponse:
        runtime = RuntimeOptions()
        return await self.get_mono_recording_with_options_async(request, runtime)

    def get_multi_channel_recording_with_options(
        self,
        request: main_models.GetMultiChannelRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiChannelRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiChannelRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiChannelRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_channel_recording_with_options_async(
        self,
        request: main_models.GetMultiChannelRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiChannelRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiChannelRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiChannelRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_channel_recording(
        self,
        request: main_models.GetMultiChannelRecordingRequest,
    ) -> main_models.GetMultiChannelRecordingResponse:
        runtime = RuntimeOptions()
        return self.get_multi_channel_recording_with_options(request, runtime)

    async def get_multi_channel_recording_async(
        self,
        request: main_models.GetMultiChannelRecordingRequest,
    ) -> main_models.GetMultiChannelRecordingResponse:
        runtime = RuntimeOptions()
        return await self.get_multi_channel_recording_with_options_async(request, runtime)

    def get_number_location_with_options(
        self,
        request: main_models.GetNumberLocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNumberLocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNumberLocation',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNumberLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_number_location_with_options_async(
        self,
        request: main_models.GetNumberLocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNumberLocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNumberLocation',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNumberLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_number_location(
        self,
        request: main_models.GetNumberLocationRequest,
    ) -> main_models.GetNumberLocationResponse:
        runtime = RuntimeOptions()
        return self.get_number_location_with_options(request, runtime)

    async def get_number_location_async(
        self,
        request: main_models.GetNumberLocationRequest,
    ) -> main_models.GetNumberLocationResponse:
        runtime = RuntimeOptions()
        return await self.get_number_location_with_options_async(request, runtime)

    def get_realtime_campaign_stats_with_options(
        self,
        request: main_models.GetRealtimeCampaignStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeCampaignStatsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeCampaignStats',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealtimeCampaignStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_campaign_stats_with_options_async(
        self,
        request: main_models.GetRealtimeCampaignStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeCampaignStatsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeCampaignStats',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealtimeCampaignStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_campaign_stats(
        self,
        request: main_models.GetRealtimeCampaignStatsRequest,
    ) -> main_models.GetRealtimeCampaignStatsResponse:
        runtime = RuntimeOptions()
        return self.get_realtime_campaign_stats_with_options(request, runtime)

    async def get_realtime_campaign_stats_async(
        self,
        request: main_models.GetRealtimeCampaignStatsRequest,
    ) -> main_models.GetRealtimeCampaignStatsResponse:
        runtime = RuntimeOptions()
        return await self.get_realtime_campaign_stats_with_options_async(request, runtime)

    def get_realtime_instance_states_with_options(
        self,
        request: main_models.GetRealtimeInstanceStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeInstanceStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeInstanceStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealtimeInstanceStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_instance_states_with_options_async(
        self,
        request: main_models.GetRealtimeInstanceStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeInstanceStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeInstanceStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealtimeInstanceStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_instance_states(
        self,
        request: main_models.GetRealtimeInstanceStatesRequest,
    ) -> main_models.GetRealtimeInstanceStatesResponse:
        runtime = RuntimeOptions()
        return self.get_realtime_instance_states_with_options(request, runtime)

    async def get_realtime_instance_states_async(
        self,
        request: main_models.GetRealtimeInstanceStatesRequest,
    ) -> main_models.GetRealtimeInstanceStatesResponse:
        runtime = RuntimeOptions()
        return await self.get_realtime_instance_states_with_options_async(request, runtime)

    def get_schema_with_options(
        self,
        request: main_models.GetSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSchema',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schema_with_options_async(
        self,
        request: main_models.GetSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSchema',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schema(
        self,
        request: main_models.GetSchemaRequest,
    ) -> main_models.GetSchemaResponse:
        runtime = RuntimeOptions()
        return self.get_schema_with_options(request, runtime)

    async def get_schema_async(
        self,
        request: main_models.GetSchemaRequest,
    ) -> main_models.GetSchemaResponse:
        runtime = RuntimeOptions()
        return await self.get_schema_with_options_async(request, runtime)

    def get_skill_group_with_options(
        self,
        request: main_models.GetSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_with_options_async(
        self,
        request: main_models.GetSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group(
        self,
        request: main_models.GetSkillGroupRequest,
    ) -> main_models.GetSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_with_options(request, runtime)

    async def get_skill_group_async(
        self,
        request: main_models.GetSkillGroupRequest,
    ) -> main_models.GetSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_with_options_async(request, runtime)

    def get_summary_template_with_options(
        self,
        request: main_models.GetSummaryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSummaryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSummaryTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSummaryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_template_with_options_async(
        self,
        request: main_models.GetSummaryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSummaryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSummaryTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSummaryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_template(
        self,
        request: main_models.GetSummaryTemplateRequest,
    ) -> main_models.GetSummaryTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_summary_template_with_options(request, runtime)

    async def get_summary_template_async(
        self,
        request: main_models.GetSummaryTemplateRequest,
    ) -> main_models.GetSummaryTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_summary_template_with_options_async(request, runtime)

    def get_ticket_with_options(
        self,
        request: main_models.GetTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ticket_with_options_async(
        self,
        request: main_models.GetTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ticket(
        self,
        request: main_models.GetTicketRequest,
    ) -> main_models.GetTicketResponse:
        runtime = RuntimeOptions()
        return self.get_ticket_with_options(request, runtime)

    async def get_ticket_async(
        self,
        request: main_models.GetTicketRequest,
    ) -> main_models.GetTicketResponse:
        runtime = RuntimeOptions()
        return await self.get_ticket_with_options_async(request, runtime)

    def get_ticket_summary_report_with_options(
        self,
        request: main_models.GetTicketSummaryReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketSummaryReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.assignee_type):
            query['AssigneeType'] = request.assignee_type
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.participant):
            query['Participant'] = request.participant
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicketSummaryReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketSummaryReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ticket_summary_report_with_options_async(
        self,
        request: main_models.GetTicketSummaryReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketSummaryReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.assignee_type):
            query['AssigneeType'] = request.assignee_type
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.participant):
            query['Participant'] = request.participant
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicketSummaryReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketSummaryReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ticket_summary_report(
        self,
        request: main_models.GetTicketSummaryReportRequest,
    ) -> main_models.GetTicketSummaryReportResponse:
        runtime = RuntimeOptions()
        return self.get_ticket_summary_report_with_options(request, runtime)

    async def get_ticket_summary_report_async(
        self,
        request: main_models.GetTicketSummaryReportRequest,
    ) -> main_models.GetTicketSummaryReportResponse:
        runtime = RuntimeOptions()
        return await self.get_ticket_summary_report_with_options_async(request, runtime)

    def get_ticket_template_with_options(
        self,
        request: main_models.GetTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ticket_template_with_options_async(
        self,
        request: main_models.GetTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicketTemplate',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ticket_template(
        self,
        request: main_models.GetTicketTemplateRequest,
    ) -> main_models.GetTicketTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_ticket_template_with_options(request, runtime)

    async def get_ticket_template_async(
        self,
        request: main_models.GetTicketTemplateRequest,
    ) -> main_models.GetTicketTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_ticket_template_with_options_async(request, runtime)

    def get_turn_credentials_with_options(
        self,
        request: main_models.GetTurnCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTurnCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTurnCredentials',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTurnCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_turn_credentials_with_options_async(
        self,
        request: main_models.GetTurnCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTurnCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTurnCredentials',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTurnCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_turn_credentials(
        self,
        request: main_models.GetTurnCredentialsRequest,
    ) -> main_models.GetTurnCredentialsResponse:
        runtime = RuntimeOptions()
        return self.get_turn_credentials_with_options(request, runtime)

    async def get_turn_credentials_async(
        self,
        request: main_models.GetTurnCredentialsRequest,
    ) -> main_models.GetTurnCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.get_turn_credentials_with_options_async(request, runtime)

    def get_turn_server_list_with_options(
        self,
        request: main_models.GetTurnServerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTurnServerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTurnServerList',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTurnServerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_turn_server_list_with_options_async(
        self,
        request: main_models.GetTurnServerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTurnServerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTurnServerList',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTurnServerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_turn_server_list(
        self,
        request: main_models.GetTurnServerListRequest,
    ) -> main_models.GetTurnServerListResponse:
        runtime = RuntimeOptions()
        return self.get_turn_server_list_with_options(request, runtime)

    async def get_turn_server_list_async(
        self,
        request: main_models.GetTurnServerListRequest,
    ) -> main_models.GetTurnServerListResponse:
        runtime = RuntimeOptions()
        return await self.get_turn_server_list_with_options_async(request, runtime)

    def get_upload_audio_data_params_with_options(
        self,
        request: main_models.GetUploadAudioDataParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadAudioDataParamsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadAudioDataParams',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadAudioDataParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_audio_data_params_with_options_async(
        self,
        request: main_models.GetUploadAudioDataParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadAudioDataParamsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadAudioDataParams',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadAudioDataParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_audio_data_params(
        self,
        request: main_models.GetUploadAudioDataParamsRequest,
    ) -> main_models.GetUploadAudioDataParamsResponse:
        runtime = RuntimeOptions()
        return self.get_upload_audio_data_params_with_options(request, runtime)

    async def get_upload_audio_data_params_async(
        self,
        request: main_models.GetUploadAudioDataParamsRequest,
    ) -> main_models.GetUploadAudioDataParamsResponse:
        runtime = RuntimeOptions()
        return await self.get_upload_audio_data_params_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_video_with_options(
        self,
        request: main_models.GetVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideo',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_with_options_async(
        self,
        request: main_models.GetVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideo',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video(
        self,
        request: main_models.GetVideoRequest,
    ) -> main_models.GetVideoResponse:
        runtime = RuntimeOptions()
        return self.get_video_with_options(request, runtime)

    async def get_video_async(
        self,
        request: main_models.GetVideoRequest,
    ) -> main_models.GetVideoResponse:
        runtime = RuntimeOptions()
        return await self.get_video_with_options_async(request, runtime)

    def get_visitor_login_details_with_options(
        self,
        request: main_models.GetVisitorLoginDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVisitorLoginDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.visitor_id):
            query['VisitorId'] = request.visitor_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVisitorLoginDetails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVisitorLoginDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_visitor_login_details_with_options_async(
        self,
        request: main_models.GetVisitorLoginDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVisitorLoginDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.visitor_id):
            query['VisitorId'] = request.visitor_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVisitorLoginDetails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVisitorLoginDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_visitor_login_details(
        self,
        request: main_models.GetVisitorLoginDetailsRequest,
    ) -> main_models.GetVisitorLoginDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_visitor_login_details_with_options(request, runtime)

    async def get_visitor_login_details_async(
        self,
        request: main_models.GetVisitorLoginDetailsRequest,
    ) -> main_models.GetVisitorLoginDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_visitor_login_details_with_options_async(request, runtime)

    def get_voicemail_recording_with_options(
        self,
        request: main_models.GetVoicemailRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVoicemailRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVoicemailRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVoicemailRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_voicemail_recording_with_options_async(
        self,
        request: main_models.GetVoicemailRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVoicemailRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVoicemailRecording',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVoicemailRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_voicemail_recording(
        self,
        request: main_models.GetVoicemailRecordingRequest,
    ) -> main_models.GetVoicemailRecordingResponse:
        runtime = RuntimeOptions()
        return self.get_voicemail_recording_with_options(request, runtime)

    async def get_voicemail_recording_async(
        self,
        request: main_models.GetVoicemailRecordingRequest,
    ) -> main_models.GetVoicemailRecordingResponse:
        runtime = RuntimeOptions()
        return await self.get_voicemail_recording_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: main_models.HoldCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HoldCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.music):
            query['Music'] = request.music
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HoldCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HoldCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: main_models.HoldCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HoldCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.music):
            query['Music'] = request.music
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HoldCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HoldCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hold_call(
        self,
        request: main_models.HoldCallRequest,
    ) -> main_models.HoldCallResponse:
        runtime = RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: main_models.HoldCallRequest,
    ) -> main_models.HoldCallResponse:
        runtime = RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def import_admins_with_options(
        self,
        request: main_models.ImportAdminsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportAdminsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportAdmins',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportAdminsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_admins_with_options_async(
        self,
        request: main_models.ImportAdminsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportAdminsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportAdmins',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportAdminsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_admins(
        self,
        request: main_models.ImportAdminsRequest,
    ) -> main_models.ImportAdminsResponse:
        runtime = RuntimeOptions()
        return self.import_admins_with_options(request, runtime)

    async def import_admins_async(
        self,
        request: main_models.ImportAdminsRequest,
    ) -> main_models.ImportAdminsResponse:
        runtime = RuntimeOptions()
        return await self.import_admins_with_options_async(request, runtime)

    def import_contact_flow_with_options(
        self,
        request: main_models.ImportContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportContactFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_package_data):
            body['FlowPackageData'] = request.flow_package_data
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_contact_flow_with_options_async(
        self,
        request: main_models.ImportContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportContactFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_package_data):
            body['FlowPackageData'] = request.flow_package_data
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_contact_flow(
        self,
        request: main_models.ImportContactFlowRequest,
    ) -> main_models.ImportContactFlowResponse:
        runtime = RuntimeOptions()
        return self.import_contact_flow_with_options(request, runtime)

    async def import_contact_flow_async(
        self,
        request: main_models.ImportContactFlowRequest,
    ) -> main_models.ImportContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.import_contact_flow_with_options_async(request, runtime)

    def import_corp_numbers_with_options(
        self,
        request: main_models.ImportCorpNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCorpNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCorpNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCorpNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_corp_numbers_with_options_async(
        self,
        request: main_models.ImportCorpNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCorpNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCorpNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCorpNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_corp_numbers(
        self,
        request: main_models.ImportCorpNumbersRequest,
    ) -> main_models.ImportCorpNumbersResponse:
        runtime = RuntimeOptions()
        return self.import_corp_numbers_with_options(request, runtime)

    async def import_corp_numbers_async(
        self,
        request: main_models.ImportCorpNumbersRequest,
    ) -> main_models.ImportCorpNumbersResponse:
        runtime = RuntimeOptions()
        return await self.import_corp_numbers_with_options_async(request, runtime)

    def import_custom_call_tagging_with_options(
        self,
        request: main_models.ImportCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_custom_call_tagging_with_options_async(
        self,
        request: main_models.ImportCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_custom_call_tagging(
        self,
        request: main_models.ImportCustomCallTaggingRequest,
    ) -> main_models.ImportCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.import_custom_call_tagging_with_options(request, runtime)

    async def import_custom_call_tagging_async(
        self,
        request: main_models.ImportCustomCallTaggingRequest,
    ) -> main_models.ImportCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.import_custom_call_tagging_with_options_async(request, runtime)

    def import_do_not_call_numbers_with_options(
        self,
        request: main_models.ImportDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_do_not_call_numbers_with_options_async(
        self,
        request: main_models.ImportDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_do_not_call_numbers(
        self,
        request: main_models.ImportDoNotCallNumbersRequest,
    ) -> main_models.ImportDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return self.import_do_not_call_numbers_with_options(request, runtime)

    async def import_do_not_call_numbers_async(
        self,
        request: main_models.ImportDoNotCallNumbersRequest,
    ) -> main_models.ImportDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return await self.import_do_not_call_numbers_with_options_async(request, runtime)

    def import_documents_with_options(
        self,
        request: main_models.ImportDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oss_file_key):
            body['OssFileKey'] = request.oss_file_key
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportDocuments',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_documents_with_options_async(
        self,
        request: main_models.ImportDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oss_file_key):
            body['OssFileKey'] = request.oss_file_key
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportDocuments',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_documents(
        self,
        request: main_models.ImportDocumentsRequest,
    ) -> main_models.ImportDocumentsResponse:
        runtime = RuntimeOptions()
        return self.import_documents_with_options(request, runtime)

    async def import_documents_async(
        self,
        request: main_models.ImportDocumentsRequest,
    ) -> main_models.ImportDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.import_documents_with_options_async(request, runtime)

    def import_ram_users_with_options(
        self,
        request: main_models.ImportRamUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportRamUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportRamUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportRamUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_ram_users_with_options_async(
        self,
        request: main_models.ImportRamUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportRamUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportRamUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportRamUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_ram_users(
        self,
        request: main_models.ImportRamUsersRequest,
    ) -> main_models.ImportRamUsersResponse:
        runtime = RuntimeOptions()
        return self.import_ram_users_with_options(request, runtime)

    async def import_ram_users_async(
        self,
        request: main_models.ImportRamUsersRequest,
    ) -> main_models.ImportRamUsersResponse:
        runtime = RuntimeOptions()
        return await self.import_ram_users_with_options_async(request, runtime)

    def initiate_attended_transfer_with_options(
        self,
        request: main_models.InitiateAttendedTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitiateAttendedTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not DaraCore.is_null(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not DaraCore.is_null(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not DaraCore.is_null(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.transferee):
            query['Transferee'] = request.transferee
        if not DaraCore.is_null(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not DaraCore.is_null(request.transferor):
            query['Transferor'] = request.transferor
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitiateAttendedTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitiateAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def initiate_attended_transfer_with_options_async(
        self,
        request: main_models.InitiateAttendedTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitiateAttendedTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not DaraCore.is_null(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not DaraCore.is_null(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not DaraCore.is_null(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.transferee):
            query['Transferee'] = request.transferee
        if not DaraCore.is_null(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not DaraCore.is_null(request.transferor):
            query['Transferor'] = request.transferor
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitiateAttendedTransfer',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitiateAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initiate_attended_transfer(
        self,
        request: main_models.InitiateAttendedTransferRequest,
    ) -> main_models.InitiateAttendedTransferResponse:
        runtime = RuntimeOptions()
        return self.initiate_attended_transfer_with_options(request, runtime)

    async def initiate_attended_transfer_async(
        self,
        request: main_models.InitiateAttendedTransferRequest,
    ) -> main_models.InitiateAttendedTransferResponse:
        runtime = RuntimeOptions()
        return await self.initiate_attended_transfer_with_options_async(request, runtime)

    def intercept_call_with_options(
        self,
        request: main_models.InterceptCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InterceptCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intercepted_user_id):
            query['InterceptedUserId'] = request.intercepted_user_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InterceptCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InterceptCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def intercept_call_with_options_async(
        self,
        request: main_models.InterceptCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InterceptCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intercepted_user_id):
            query['InterceptedUserId'] = request.intercepted_user_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InterceptCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InterceptCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def intercept_call(
        self,
        request: main_models.InterceptCallRequest,
    ) -> main_models.InterceptCallResponse:
        runtime = RuntimeOptions()
        return self.intercept_call_with_options(request, runtime)

    async def intercept_call_async(
        self,
        request: main_models.InterceptCallRequest,
    ) -> main_models.InterceptCallResponse:
        runtime = RuntimeOptions()
        return await self.intercept_call_with_options_async(request, runtime)

    def launch_authentication_with_options(
        self,
        request: main_models.LaunchAuthenticationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchAuthenticationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchAuthentication',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_authentication_with_options_async(
        self,
        request: main_models.LaunchAuthenticationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchAuthenticationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchAuthentication',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_authentication(
        self,
        request: main_models.LaunchAuthenticationRequest,
    ) -> main_models.LaunchAuthenticationResponse:
        runtime = RuntimeOptions()
        return self.launch_authentication_with_options(request, runtime)

    async def launch_authentication_async(
        self,
        request: main_models.LaunchAuthenticationRequest,
    ) -> main_models.LaunchAuthenticationResponse:
        runtime = RuntimeOptions()
        return await self.launch_authentication_with_options_async(request, runtime)

    def launch_survey_with_options(
        self,
        request: main_models.LaunchSurveyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchSurveyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.sms_metadata_id):
            query['SmsMetadataId'] = request.sms_metadata_id
        if not DaraCore.is_null(request.survey_channel):
            query['SurveyChannel'] = request.survey_channel
        if not DaraCore.is_null(request.survey_template_id):
            query['SurveyTemplateId'] = request.survey_template_id
        if not DaraCore.is_null(request.survey_template_variables):
            query['SurveyTemplateVariables'] = request.survey_template_variables
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchSurvey',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchSurveyResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_survey_with_options_async(
        self,
        request: main_models.LaunchSurveyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchSurveyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.sms_metadata_id):
            query['SmsMetadataId'] = request.sms_metadata_id
        if not DaraCore.is_null(request.survey_channel):
            query['SurveyChannel'] = request.survey_channel
        if not DaraCore.is_null(request.survey_template_id):
            query['SurveyTemplateId'] = request.survey_template_id
        if not DaraCore.is_null(request.survey_template_variables):
            query['SurveyTemplateVariables'] = request.survey_template_variables
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchSurvey',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchSurveyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_survey(
        self,
        request: main_models.LaunchSurveyRequest,
    ) -> main_models.LaunchSurveyResponse:
        runtime = RuntimeOptions()
        return self.launch_survey_with_options(request, runtime)

    async def launch_survey_async(
        self,
        request: main_models.LaunchSurveyRequest,
    ) -> main_models.LaunchSurveyResponse:
        runtime = RuntimeOptions()
        return await self.launch_survey_with_options_async(request, runtime)

    def list_agent_state_logs_with_options(
        self,
        request: main_models.ListAgentStateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentStateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentStateLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentStateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_state_logs_with_options_async(
        self,
        request: main_models.ListAgentStateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentStateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentStateLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentStateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_state_logs(
        self,
        request: main_models.ListAgentStateLogsRequest,
    ) -> main_models.ListAgentStateLogsResponse:
        runtime = RuntimeOptions()
        return self.list_agent_state_logs_with_options(request, runtime)

    async def list_agent_state_logs_async(
        self,
        request: main_models.ListAgentStateLogsRequest,
    ) -> main_models.ListAgentStateLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_agent_state_logs_with_options_async(request, runtime)

    def list_agent_states_with_options(
        self,
        request: main_models.ListAgentStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_ids):
            query['AgentIds'] = request.agent_ids
        if not DaraCore.is_null(request.exclude_offline_users):
            query['ExcludeOfflineUsers'] = request.exclude_offline_users
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_states_with_options_async(
        self,
        request: main_models.ListAgentStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_ids):
            query['AgentIds'] = request.agent_ids
        if not DaraCore.is_null(request.exclude_offline_users):
            query['ExcludeOfflineUsers'] = request.exclude_offline_users
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_states(
        self,
        request: main_models.ListAgentStatesRequest,
    ) -> main_models.ListAgentStatesResponse:
        runtime = RuntimeOptions()
        return self.list_agent_states_with_options(request, runtime)

    async def list_agent_states_async(
        self,
        request: main_models.ListAgentStatesRequest,
    ) -> main_models.ListAgentStatesResponse:
        runtime = RuntimeOptions()
        return await self.list_agent_states_with_options_async(request, runtime)

    def list_agent_summary_reports_since_midnight_with_options(
        self,
        request: main_models.ListAgentSummaryReportsSinceMidnightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSummaryReportsSinceMidnightResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSummaryReportsSinceMidnight',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSummaryReportsSinceMidnightResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_summary_reports_since_midnight_with_options_async(
        self,
        request: main_models.ListAgentSummaryReportsSinceMidnightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSummaryReportsSinceMidnightResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSummaryReportsSinceMidnight',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSummaryReportsSinceMidnightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_summary_reports_since_midnight(
        self,
        request: main_models.ListAgentSummaryReportsSinceMidnightRequest,
    ) -> main_models.ListAgentSummaryReportsSinceMidnightResponse:
        runtime = RuntimeOptions()
        return self.list_agent_summary_reports_since_midnight_with_options(request, runtime)

    async def list_agent_summary_reports_since_midnight_async(
        self,
        request: main_models.ListAgentSummaryReportsSinceMidnightRequest,
    ) -> main_models.ListAgentSummaryReportsSinceMidnightResponse:
        runtime = RuntimeOptions()
        return await self.list_agent_summary_reports_since_midnight_with_options_async(request, runtime)

    def list_attempts_with_options(
        self,
        request: main_models.ListAttemptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAttemptsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAttempts',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAttemptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_attempts_with_options_async(
        self,
        request: main_models.ListAttemptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAttemptsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAttempts',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAttemptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_attempts(
        self,
        request: main_models.ListAttemptsRequest,
    ) -> main_models.ListAttemptsResponse:
        runtime = RuntimeOptions()
        return self.list_attempts_with_options(request, runtime)

    async def list_attempts_async(
        self,
        request: main_models.ListAttemptsRequest,
    ) -> main_models.ListAttemptsResponse:
        runtime = RuntimeOptions()
        return await self.list_attempts_with_options_async(request, runtime)

    def list_audio_files_with_options(
        self,
        request: main_models.ListAudioFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAudioFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAudioFiles',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAudioFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_audio_files_with_options_async(
        self,
        request: main_models.ListAudioFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAudioFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAudioFiles',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAudioFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_audio_files(
        self,
        request: main_models.ListAudioFilesRequest,
    ) -> main_models.ListAudioFilesResponse:
        runtime = RuntimeOptions()
        return self.list_audio_files_with_options(request, runtime)

    async def list_audio_files_async(
        self,
        request: main_models.ListAudioFilesRequest,
    ) -> main_models.ListAudioFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_audio_files_with_options_async(request, runtime)

    def list_blacklist_call_taggings_with_options(
        self,
        request: main_models.ListBlacklistCallTaggingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBlacklistCallTaggingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBlacklistCallTaggings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBlacklistCallTaggingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_blacklist_call_taggings_with_options_async(
        self,
        request: main_models.ListBlacklistCallTaggingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBlacklistCallTaggingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBlacklistCallTaggings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBlacklistCallTaggingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_blacklist_call_taggings(
        self,
        request: main_models.ListBlacklistCallTaggingsRequest,
    ) -> main_models.ListBlacklistCallTaggingsResponse:
        runtime = RuntimeOptions()
        return self.list_blacklist_call_taggings_with_options(request, runtime)

    async def list_blacklist_call_taggings_async(
        self,
        request: main_models.ListBlacklistCallTaggingsRequest,
    ) -> main_models.ListBlacklistCallTaggingsResponse:
        runtime = RuntimeOptions()
        return await self.list_blacklist_call_taggings_with_options_async(request, runtime)

    def list_brief_skill_groups_with_options(
        self,
        request: main_models.ListBriefSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBriefSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBriefSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBriefSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_brief_skill_groups_with_options_async(
        self,
        request: main_models.ListBriefSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBriefSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBriefSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBriefSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_brief_skill_groups(
        self,
        request: main_models.ListBriefSkillGroupsRequest,
    ) -> main_models.ListBriefSkillGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_brief_skill_groups_with_options(request, runtime)

    async def list_brief_skill_groups_async(
        self,
        request: main_models.ListBriefSkillGroupsRequest,
    ) -> main_models.ListBriefSkillGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_brief_skill_groups_with_options_async(request, runtime)

    def list_call_detail_records_with_options(
        self,
        request: main_models.ListCallDetailRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallDetailRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.contact_disposition):
            query['ContactDisposition'] = request.contact_disposition
        if not DaraCore.is_null(request.contact_disposition_list):
            query['ContactDispositionList'] = request.contact_disposition_list
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.contact_type_list):
            query['ContactTypeList'] = request.contact_type_list
        if not DaraCore.is_null(request.criteria):
            query['Criteria'] = request.criteria
        if not DaraCore.is_null(request.early_media_state_list):
            query['EarlyMediaStateList'] = request.early_media_state_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.satisfaction_description_list):
            query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        if not DaraCore.is_null(request.satisfaction_list):
            query['SatisfactionList'] = request.satisfaction_list
        if not DaraCore.is_null(request.satisfaction_survey_channel):
            query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallDetailRecords',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallDetailRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_detail_records_with_options_async(
        self,
        request: main_models.ListCallDetailRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallDetailRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.contact_disposition):
            query['ContactDisposition'] = request.contact_disposition
        if not DaraCore.is_null(request.contact_disposition_list):
            query['ContactDispositionList'] = request.contact_disposition_list
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.contact_type_list):
            query['ContactTypeList'] = request.contact_type_list
        if not DaraCore.is_null(request.criteria):
            query['Criteria'] = request.criteria
        if not DaraCore.is_null(request.early_media_state_list):
            query['EarlyMediaStateList'] = request.early_media_state_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.satisfaction_description_list):
            query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        if not DaraCore.is_null(request.satisfaction_list):
            query['SatisfactionList'] = request.satisfaction_list
        if not DaraCore.is_null(request.satisfaction_survey_channel):
            query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallDetailRecords',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallDetailRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_detail_records(
        self,
        request: main_models.ListCallDetailRecordsRequest,
    ) -> main_models.ListCallDetailRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    async def list_call_detail_records_async(
        self,
        request: main_models.ListCallDetailRecordsRequest,
    ) -> main_models.ListCallDetailRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_call_detail_records_with_options_async(request, runtime)

    def list_call_detail_records_v2with_options(
        self,
        request: main_models.ListCallDetailRecordsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallDetailRecordsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_channel_type_list):
            query['AccessChannelTypeList'] = request.access_channel_type_list
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.analytics_report_ready):
            query['AnalyticsReportReady'] = request.analytics_report_ready
        if not DaraCore.is_null(request.broker):
            query['Broker'] = request.broker
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.contact_disposition_list):
            query['ContactDispositionList'] = request.contact_disposition_list
        if not DaraCore.is_null(request.contact_id_list):
            query['ContactIdList'] = request.contact_id_list
        if not DaraCore.is_null(request.contact_type_list):
            query['ContactTypeList'] = request.contact_type_list
        if not DaraCore.is_null(request.early_media_state_list):
            query['EarlyMediaStateList'] = request.early_media_state_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.first_agent_id):
            query['FirstAgentId'] = request.first_agent_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.release_initiator_list):
            query['ReleaseInitiatorList'] = request.release_initiator_list
        if not DaraCore.is_null(request.release_reason_list):
            query['ReleaseReasonList'] = request.release_reason_list
        if not DaraCore.is_null(request.satisfaction_description_list):
            query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        if not DaraCore.is_null(request.satisfaction_rate_list):
            query['SatisfactionRateList'] = request.satisfaction_rate_list
        if not DaraCore.is_null(request.satisfaction_survey_channel):
            query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallDetailRecordsV2',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallDetailRecordsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_call_detail_records_v2with_options_async(
        self,
        request: main_models.ListCallDetailRecordsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallDetailRecordsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_channel_type_list):
            query['AccessChannelTypeList'] = request.access_channel_type_list
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.analytics_report_ready):
            query['AnalyticsReportReady'] = request.analytics_report_ready
        if not DaraCore.is_null(request.broker):
            query['Broker'] = request.broker
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.contact_disposition_list):
            query['ContactDispositionList'] = request.contact_disposition_list
        if not DaraCore.is_null(request.contact_id_list):
            query['ContactIdList'] = request.contact_id_list
        if not DaraCore.is_null(request.contact_type_list):
            query['ContactTypeList'] = request.contact_type_list
        if not DaraCore.is_null(request.early_media_state_list):
            query['EarlyMediaStateList'] = request.early_media_state_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.first_agent_id):
            query['FirstAgentId'] = request.first_agent_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.release_initiator_list):
            query['ReleaseInitiatorList'] = request.release_initiator_list
        if not DaraCore.is_null(request.release_reason_list):
            query['ReleaseReasonList'] = request.release_reason_list
        if not DaraCore.is_null(request.satisfaction_description_list):
            query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        if not DaraCore.is_null(request.satisfaction_rate_list):
            query['SatisfactionRateList'] = request.satisfaction_rate_list
        if not DaraCore.is_null(request.satisfaction_survey_channel):
            query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallDetailRecordsV2',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallDetailRecordsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_detail_records_v2(
        self,
        request: main_models.ListCallDetailRecordsV2Request,
    ) -> main_models.ListCallDetailRecordsV2Response:
        runtime = RuntimeOptions()
        return self.list_call_detail_records_v2with_options(request, runtime)

    async def list_call_detail_records_v2_async(
        self,
        request: main_models.ListCallDetailRecordsV2Request,
    ) -> main_models.ListCallDetailRecordsV2Response:
        runtime = RuntimeOptions()
        return await self.list_call_detail_records_v2with_options_async(request, runtime)

    def list_call_summaries_with_options(
        self,
        tmp_req: main_models.ListCallSummariesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallSummariesResponse:
        tmp_req.validate()
        request = main_models.ListCallSummariesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact_id_list):
            request.contact_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact_id_list, 'ContactIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.contact_id_list_shrink):
            query['ContactIdList'] = request.contact_id_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallSummaries',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_summaries_with_options_async(
        self,
        tmp_req: main_models.ListCallSummariesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallSummariesResponse:
        tmp_req.validate()
        request = main_models.ListCallSummariesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact_id_list):
            request.contact_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact_id_list, 'ContactIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.contact_id_list_shrink):
            query['ContactIdList'] = request.contact_id_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallSummaries',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_summaries(
        self,
        request: main_models.ListCallSummariesRequest,
    ) -> main_models.ListCallSummariesResponse:
        runtime = RuntimeOptions()
        return self.list_call_summaries_with_options(request, runtime)

    async def list_call_summaries_async(
        self,
        request: main_models.ListCallSummariesRequest,
    ) -> main_models.ListCallSummariesResponse:
        runtime = RuntimeOptions()
        return await self.list_call_summaries_with_options_async(request, runtime)

    def list_call_tags_with_options(
        self,
        request: main_models.ListCallTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallTags',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_tags_with_options_async(
        self,
        request: main_models.ListCallTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallTags',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_tags(
        self,
        request: main_models.ListCallTagsRequest,
    ) -> main_models.ListCallTagsResponse:
        runtime = RuntimeOptions()
        return self.list_call_tags_with_options(request, runtime)

    async def list_call_tags_async(
        self,
        request: main_models.ListCallTagsRequest,
    ) -> main_models.ListCallTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_call_tags_with_options_async(request, runtime)

    def list_campaign_trending_report_with_options(
        self,
        request: main_models.ListCampaignTrendingReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCampaignTrendingReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCampaignTrendingReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCampaignTrendingReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_campaign_trending_report_with_options_async(
        self,
        request: main_models.ListCampaignTrendingReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCampaignTrendingReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCampaignTrendingReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCampaignTrendingReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_campaign_trending_report(
        self,
        request: main_models.ListCampaignTrendingReportRequest,
    ) -> main_models.ListCampaignTrendingReportResponse:
        runtime = RuntimeOptions()
        return self.list_campaign_trending_report_with_options(request, runtime)

    async def list_campaign_trending_report_async(
        self,
        request: main_models.ListCampaignTrendingReportRequest,
    ) -> main_models.ListCampaignTrendingReportResponse:
        runtime = RuntimeOptions()
        return await self.list_campaign_trending_report_with_options_async(request, runtime)

    def list_campaigns_with_options(
        self,
        request: main_models.ListCampaignsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCampaignsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.actual_start_time_from):
            query['ActualStartTimeFrom'] = request.actual_start_time_from
        if not DaraCore.is_null(request.actual_start_time_to):
            query['ActualStartTimeTo'] = request.actual_start_time_to
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.planed_start_time_from):
            query['PlanedStartTimeFrom'] = request.planed_start_time_from
        if not DaraCore.is_null(request.planed_start_time_to):
            query['PlanedStartTimeTo'] = request.planed_start_time_to
        if not DaraCore.is_null(request.queue_id):
            query['QueueId'] = request.queue_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCampaigns',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCampaignsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_campaigns_with_options_async(
        self,
        request: main_models.ListCampaignsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCampaignsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.actual_start_time_from):
            query['ActualStartTimeFrom'] = request.actual_start_time_from
        if not DaraCore.is_null(request.actual_start_time_to):
            query['ActualStartTimeTo'] = request.actual_start_time_to
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.planed_start_time_from):
            query['PlanedStartTimeFrom'] = request.planed_start_time_from
        if not DaraCore.is_null(request.planed_start_time_to):
            query['PlanedStartTimeTo'] = request.planed_start_time_to
        if not DaraCore.is_null(request.queue_id):
            query['QueueId'] = request.queue_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCampaigns',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCampaignsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_campaigns(
        self,
        request: main_models.ListCampaignsRequest,
    ) -> main_models.ListCampaignsResponse:
        runtime = RuntimeOptions()
        return self.list_campaigns_with_options(request, runtime)

    async def list_campaigns_async(
        self,
        request: main_models.ListCampaignsRequest,
    ) -> main_models.ListCampaignsResponse:
        runtime = RuntimeOptions()
        return await self.list_campaigns_with_options_async(request, runtime)

    def list_cases_with_options(
        self,
        request: main_models.ListCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cases_with_options_async(
        self,
        request: main_models.ListCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cases(
        self,
        request: main_models.ListCasesRequest,
    ) -> main_models.ListCasesResponse:
        runtime = RuntimeOptions()
        return self.list_cases_with_options(request, runtime)

    async def list_cases_async(
        self,
        request: main_models.ListCasesRequest,
    ) -> main_models.ListCasesResponse:
        runtime = RuntimeOptions()
        return await self.list_cases_with_options_async(request, runtime)

    def list_categories_with_options(
        self,
        request: main_models.ListCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_categories_with_options_async(
        self,
        request: main_models.ListCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_categories(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        return self.list_categories_with_options(request, runtime)

    async def list_categories_async(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_categories_with_options_async(request, runtime)

    def list_common_ticket_fields_with_options(
        self,
        request: main_models.ListCommonTicketFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonTicketFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonTicketFields',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonTicketFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_ticket_fields_with_options_async(
        self,
        request: main_models.ListCommonTicketFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonTicketFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonTicketFields',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonTicketFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_ticket_fields(
        self,
        request: main_models.ListCommonTicketFieldsRequest,
    ) -> main_models.ListCommonTicketFieldsResponse:
        runtime = RuntimeOptions()
        return self.list_common_ticket_fields_with_options(request, runtime)

    async def list_common_ticket_fields_async(
        self,
        request: main_models.ListCommonTicketFieldsRequest,
    ) -> main_models.ListCommonTicketFieldsResponse:
        runtime = RuntimeOptions()
        return await self.list_common_ticket_fields_with_options_async(request, runtime)

    def list_config_items_with_options(
        self,
        request: main_models.ListConfigItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigItems',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_items_with_options_async(
        self,
        request: main_models.ListConfigItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigItems',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_items(
        self,
        request: main_models.ListConfigItemsRequest,
    ) -> main_models.ListConfigItemsResponse:
        runtime = RuntimeOptions()
        return self.list_config_items_with_options(request, runtime)

    async def list_config_items_async(
        self,
        request: main_models.ListConfigItemsRequest,
    ) -> main_models.ListConfigItemsResponse:
        runtime = RuntimeOptions()
        return await self.list_config_items_with_options_async(request, runtime)

    def list_contact_flows_with_options(
        self,
        request: main_models.ListContactFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListContactFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContactFlows',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContactFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contact_flows_with_options_async(
        self,
        request: main_models.ListContactFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListContactFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContactFlows',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContactFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contact_flows(
        self,
        request: main_models.ListContactFlowsRequest,
    ) -> main_models.ListContactFlowsResponse:
        runtime = RuntimeOptions()
        return self.list_contact_flows_with_options(request, runtime)

    async def list_contact_flows_async(
        self,
        request: main_models.ListContactFlowsRequest,
    ) -> main_models.ListContactFlowsResponse:
        runtime = RuntimeOptions()
        return await self.list_contact_flows_with_options_async(request, runtime)

    def list_custom_call_tagging_with_options(
        self,
        request: main_models.ListCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_call_tagging_with_options_async(
        self,
        request: main_models.ListCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_call_tagging(
        self,
        request: main_models.ListCustomCallTaggingRequest,
    ) -> main_models.ListCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.list_custom_call_tagging_with_options(request, runtime)

    async def list_custom_call_tagging_async(
        self,
        request: main_models.ListCustomCallTaggingRequest,
    ) -> main_models.ListCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_call_tagging_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: main_models.ListDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDevices',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: main_models.ListDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDevices',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_devices(
        self,
        request: main_models.ListDevicesRequest,
    ) -> main_models.ListDevicesResponse:
        runtime = RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: main_models.ListDevicesRequest,
    ) -> main_models.ListDevicesResponse:
        runtime = RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def list_do_not_call_numbers_with_options(
        self,
        request: main_models.ListDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_do_not_call_numbers_with_options_async(
        self,
        request: main_models.ListDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_do_not_call_numbers(
        self,
        request: main_models.ListDoNotCallNumbersRequest,
    ) -> main_models.ListDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return self.list_do_not_call_numbers_with_options(request, runtime)

    async def list_do_not_call_numbers_async(
        self,
        request: main_models.ListDoNotCallNumbersRequest,
    ) -> main_models.ListDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return await self.list_do_not_call_numbers_with_options_async(request, runtime)

    def list_documents_with_options(
        self,
        tmp_req: main_models.ListDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentsResponse:
        tmp_req.validate()
        request = main_models.ListDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sorts):
            request.sorts_shrink = Utils.array_to_string_with_specified_style(tmp_req.sorts, 'Sorts', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not DaraCore.is_null(request.search_pattern):
            body['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.sorts_shrink):
            body['Sorts'] = request.sorts_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocuments',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_documents_with_options_async(
        self,
        tmp_req: main_models.ListDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentsResponse:
        tmp_req.validate()
        request = main_models.ListDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sorts):
            request.sorts_shrink = Utils.array_to_string_with_specified_style(tmp_req.sorts, 'Sorts', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not DaraCore.is_null(request.search_pattern):
            body['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.sorts_shrink):
            body['Sorts'] = request.sorts_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocuments',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_documents(
        self,
        request: main_models.ListDocumentsRequest,
    ) -> main_models.ListDocumentsResponse:
        runtime = RuntimeOptions()
        return self.list_documents_with_options(request, runtime)

    async def list_documents_async(
        self,
        request: main_models.ListDocumentsRequest,
    ) -> main_models.ListDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.list_documents_with_options_async(request, runtime)

    def list_feedbacks_with_options(
        self,
        request: main_models.ListFeedbacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFeedbacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id_list):
            query['TaskIdList'] = request.task_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeedbacks',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeedbacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feedbacks_with_options_async(
        self,
        request: main_models.ListFeedbacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFeedbacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id_list):
            query['TaskIdList'] = request.task_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeedbacks',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeedbacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feedbacks(
        self,
        request: main_models.ListFeedbacksRequest,
    ) -> main_models.ListFeedbacksResponse:
        runtime = RuntimeOptions()
        return self.list_feedbacks_with_options(request, runtime)

    async def list_feedbacks_async(
        self,
        request: main_models.ListFeedbacksRequest,
    ) -> main_models.ListFeedbacksResponse:
        runtime = RuntimeOptions()
        return await self.list_feedbacks_with_options_async(request, runtime)

    def list_flash_sms_applications_with_options(
        self,
        request: main_models.ListFlashSmsApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider_id):
            query['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsApplications',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flash_sms_applications_with_options_async(
        self,
        request: main_models.ListFlashSmsApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider_id):
            query['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsApplications',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flash_sms_applications(
        self,
        request: main_models.ListFlashSmsApplicationsRequest,
    ) -> main_models.ListFlashSmsApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_flash_sms_applications_with_options(request, runtime)

    async def list_flash_sms_applications_async(
        self,
        request: main_models.ListFlashSmsApplicationsRequest,
    ) -> main_models.ListFlashSmsApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_flash_sms_applications_with_options_async(request, runtime)

    def list_flash_sms_settings_with_options(
        self,
        tmp_req: main_models.ListFlashSmsSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsSettingsResponse:
        tmp_req.validate()
        request = main_models.ListFlashSmsSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.skill_group_id_list):
            request.skill_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.skill_group_id_list, 'SkillGroupIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id_list_shrink):
            query['SkillGroupIdList'] = request.skill_group_id_list_shrink
        if not DaraCore.is_null(request.skill_group_name):
            query['SkillGroupName'] = request.skill_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsSettings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flash_sms_settings_with_options_async(
        self,
        tmp_req: main_models.ListFlashSmsSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsSettingsResponse:
        tmp_req.validate()
        request = main_models.ListFlashSmsSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.skill_group_id_list):
            request.skill_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.skill_group_id_list, 'SkillGroupIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id_list_shrink):
            query['SkillGroupIdList'] = request.skill_group_id_list_shrink
        if not DaraCore.is_null(request.skill_group_name):
            query['SkillGroupName'] = request.skill_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsSettings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flash_sms_settings(
        self,
        request: main_models.ListFlashSmsSettingsRequest,
    ) -> main_models.ListFlashSmsSettingsResponse:
        runtime = RuntimeOptions()
        return self.list_flash_sms_settings_with_options(request, runtime)

    async def list_flash_sms_settings_async(
        self,
        request: main_models.ListFlashSmsSettingsRequest,
    ) -> main_models.ListFlashSmsSettingsResponse:
        runtime = RuntimeOptions()
        return await self.list_flash_sms_settings_with_options_async(request, runtime)

    def list_flash_sms_templates_with_options(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            query['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsTemplates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flash_sms_templates_with_options_async(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.provider_id):
            query['ProviderId'] = request.provider_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsTemplates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlashSmsTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flash_sms_templates(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_flash_sms_templates_with_options(request, runtime)

    async def list_flash_sms_templates_async(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_flash_sms_templates_with_options_async(request, runtime)

    def list_group_chat_messages_with_options(
        self,
        request: main_models.ListGroupChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupChatMessages',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupChatMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_chat_messages_with_options_async(
        self,
        request: main_models.ListGroupChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupChatMessages',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupChatMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_chat_messages(
        self,
        request: main_models.ListGroupChatMessagesRequest,
    ) -> main_models.ListGroupChatMessagesResponse:
        runtime = RuntimeOptions()
        return self.list_group_chat_messages_with_options(request, runtime)

    async def list_group_chat_messages_async(
        self,
        request: main_models.ListGroupChatMessagesRequest,
    ) -> main_models.ListGroupChatMessagesResponse:
        runtime = RuntimeOptions()
        return await self.list_group_chat_messages_with_options_async(request, runtime)

    def list_historical_agent_report_with_options(
        self,
        request: main_models.ListHistoricalAgentReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoricalAgentReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stop_time):
            query['StopTime'] = request.stop_time
        body = {}
        if not DaraCore.is_null(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoricalAgentReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoricalAgentReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_agent_report_with_options_async(
        self,
        request: main_models.ListHistoricalAgentReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoricalAgentReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stop_time):
            query['StopTime'] = request.stop_time
        body = {}
        if not DaraCore.is_null(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoricalAgentReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoricalAgentReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_agent_report(
        self,
        request: main_models.ListHistoricalAgentReportRequest,
    ) -> main_models.ListHistoricalAgentReportResponse:
        runtime = RuntimeOptions()
        return self.list_historical_agent_report_with_options(request, runtime)

    async def list_historical_agent_report_async(
        self,
        request: main_models.ListHistoricalAgentReportRequest,
    ) -> main_models.ListHistoricalAgentReportResponse:
        runtime = RuntimeOptions()
        return await self.list_historical_agent_report_with_options_async(request, runtime)

    def list_historical_agent_skill_group_report_with_options(
        self,
        request: main_models.ListHistoricalAgentSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoricalAgentSkillGroupReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoricalAgentSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoricalAgentSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_agent_skill_group_report_with_options_async(
        self,
        request: main_models.ListHistoricalAgentSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoricalAgentSkillGroupReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoricalAgentSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoricalAgentSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_agent_skill_group_report(
        self,
        request: main_models.ListHistoricalAgentSkillGroupReportRequest,
    ) -> main_models.ListHistoricalAgentSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return self.list_historical_agent_skill_group_report_with_options(request, runtime)

    async def list_historical_agent_skill_group_report_async(
        self,
        request: main_models.ListHistoricalAgentSkillGroupReportRequest,
    ) -> main_models.ListHistoricalAgentSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return await self.list_historical_agent_skill_group_report_with_options_async(request, runtime)

    def list_historical_skill_group_report_with_options(
        self,
        request: main_models.ListHistoricalSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoricalSkillGroupReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoricalSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoricalSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_skill_group_report_with_options_async(
        self,
        request: main_models.ListHistoricalSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoricalSkillGroupReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoricalSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoricalSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_skill_group_report(
        self,
        request: main_models.ListHistoricalSkillGroupReportRequest,
    ) -> main_models.ListHistoricalSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return self.list_historical_skill_group_report_with_options(request, runtime)

    async def list_historical_skill_group_report_async(
        self,
        request: main_models.ListHistoricalSkillGroupReportRequest,
    ) -> main_models.ListHistoricalSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return await self.list_historical_skill_group_report_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
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
            action = 'ListInstances',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
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
            action = 'ListInstances',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_instances_of_user_with_options(
        self,
        request: main_models.ListInstancesOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesOfUserResponse:
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
            action = 'ListInstancesOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_of_user_with_options_async(
        self,
        request: main_models.ListInstancesOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesOfUserResponse:
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
            action = 'ListInstancesOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_of_user(
        self,
        request: main_models.ListInstancesOfUserRequest,
    ) -> main_models.ListInstancesOfUserResponse:
        runtime = RuntimeOptions()
        return self.list_instances_of_user_with_options(request, runtime)

    async def list_instances_of_user_async(
        self,
        request: main_models.ListInstancesOfUserRequest,
    ) -> main_models.ListInstancesOfUserResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_of_user_with_options_async(request, runtime)

    def list_interval_agent_report_with_options(
        self,
        request: main_models.ListIntervalAgentReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalAgentReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalAgentReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalAgentReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_agent_report_with_options_async(
        self,
        request: main_models.ListIntervalAgentReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalAgentReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalAgentReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalAgentReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_agent_report(
        self,
        request: main_models.ListIntervalAgentReportRequest,
    ) -> main_models.ListIntervalAgentReportResponse:
        runtime = RuntimeOptions()
        return self.list_interval_agent_report_with_options(request, runtime)

    async def list_interval_agent_report_async(
        self,
        request: main_models.ListIntervalAgentReportRequest,
    ) -> main_models.ListIntervalAgentReportResponse:
        runtime = RuntimeOptions()
        return await self.list_interval_agent_report_with_options_async(request, runtime)

    def list_interval_agent_skill_group_report_with_options(
        self,
        request: main_models.ListIntervalAgentSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalAgentSkillGroupReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalAgentSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalAgentSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_agent_skill_group_report_with_options_async(
        self,
        request: main_models.ListIntervalAgentSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalAgentSkillGroupReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalAgentSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalAgentSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_agent_skill_group_report(
        self,
        request: main_models.ListIntervalAgentSkillGroupReportRequest,
    ) -> main_models.ListIntervalAgentSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return self.list_interval_agent_skill_group_report_with_options(request, runtime)

    async def list_interval_agent_skill_group_report_async(
        self,
        request: main_models.ListIntervalAgentSkillGroupReportRequest,
    ) -> main_models.ListIntervalAgentSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return await self.list_interval_agent_skill_group_report_with_options_async(request, runtime)

    def list_interval_instance_report_with_options(
        self,
        request: main_models.ListIntervalInstanceReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalInstanceReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalInstanceReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalInstanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_instance_report_with_options_async(
        self,
        request: main_models.ListIntervalInstanceReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalInstanceReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalInstanceReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalInstanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_instance_report(
        self,
        request: main_models.ListIntervalInstanceReportRequest,
    ) -> main_models.ListIntervalInstanceReportResponse:
        runtime = RuntimeOptions()
        return self.list_interval_instance_report_with_options(request, runtime)

    async def list_interval_instance_report_async(
        self,
        request: main_models.ListIntervalInstanceReportRequest,
    ) -> main_models.ListIntervalInstanceReportResponse:
        runtime = RuntimeOptions()
        return await self.list_interval_instance_report_with_options_async(request, runtime)

    def list_interval_skill_group_report_with_options(
        self,
        request: main_models.ListIntervalSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalSkillGroupReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_skill_group_report_with_options_async(
        self,
        request: main_models.ListIntervalSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalSkillGroupReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervalSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_skill_group_report(
        self,
        request: main_models.ListIntervalSkillGroupReportRequest,
    ) -> main_models.ListIntervalSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return self.list_interval_skill_group_report_with_options(request, runtime)

    async def list_interval_skill_group_report_async(
        self,
        request: main_models.ListIntervalSkillGroupReportRequest,
    ) -> main_models.ListIntervalSkillGroupReportResponse:
        runtime = RuntimeOptions()
        return await self.list_interval_skill_group_report_with_options_async(request, runtime)

    def list_ivr_tracking_details_with_options(
        self,
        request: main_models.ListIvrTrackingDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIvrTrackingDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIvrTrackingDetails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIvrTrackingDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ivr_tracking_details_with_options_async(
        self,
        request: main_models.ListIvrTrackingDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIvrTrackingDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIvrTrackingDetails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIvrTrackingDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ivr_tracking_details(
        self,
        request: main_models.ListIvrTrackingDetailsRequest,
    ) -> main_models.ListIvrTrackingDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_ivr_tracking_details_with_options(request, runtime)

    async def list_ivr_tracking_details_async(
        self,
        request: main_models.ListIvrTrackingDetailsRequest,
    ) -> main_models.ListIvrTrackingDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_ivr_tracking_details_with_options_async(request, runtime)

    def list_legacy_agent_event_logs_with_options(
        self,
        request: main_models.ListLegacyAgentEventLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyAgentEventLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyAgentEventLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyAgentEventLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_agent_event_logs_with_options_async(
        self,
        request: main_models.ListLegacyAgentEventLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyAgentEventLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyAgentEventLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyAgentEventLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_agent_event_logs(
        self,
        request: main_models.ListLegacyAgentEventLogsRequest,
    ) -> main_models.ListLegacyAgentEventLogsResponse:
        runtime = RuntimeOptions()
        return self.list_legacy_agent_event_logs_with_options(request, runtime)

    async def list_legacy_agent_event_logs_async(
        self,
        request: main_models.ListLegacyAgentEventLogsRequest,
    ) -> main_models.ListLegacyAgentEventLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_legacy_agent_event_logs_with_options_async(request, runtime)

    def list_legacy_agent_status_logs_with_options(
        self,
        request: main_models.ListLegacyAgentStatusLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyAgentStatusLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyAgentStatusLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyAgentStatusLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_agent_status_logs_with_options_async(
        self,
        request: main_models.ListLegacyAgentStatusLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyAgentStatusLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyAgentStatusLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyAgentStatusLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_agent_status_logs(
        self,
        request: main_models.ListLegacyAgentStatusLogsRequest,
    ) -> main_models.ListLegacyAgentStatusLogsResponse:
        runtime = RuntimeOptions()
        return self.list_legacy_agent_status_logs_with_options(request, runtime)

    async def list_legacy_agent_status_logs_async(
        self,
        request: main_models.ListLegacyAgentStatusLogsRequest,
    ) -> main_models.ListLegacyAgentStatusLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_legacy_agent_status_logs_with_options_async(request, runtime)

    def list_legacy_appraise_logs_with_options(
        self,
        request: main_models.ListLegacyAppraiseLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyAppraiseLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyAppraiseLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyAppraiseLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_appraise_logs_with_options_async(
        self,
        request: main_models.ListLegacyAppraiseLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyAppraiseLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyAppraiseLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyAppraiseLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_appraise_logs(
        self,
        request: main_models.ListLegacyAppraiseLogsRequest,
    ) -> main_models.ListLegacyAppraiseLogsResponse:
        runtime = RuntimeOptions()
        return self.list_legacy_appraise_logs_with_options(request, runtime)

    async def list_legacy_appraise_logs_async(
        self,
        request: main_models.ListLegacyAppraiseLogsRequest,
    ) -> main_models.ListLegacyAppraiseLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_legacy_appraise_logs_with_options_async(request, runtime)

    def list_legacy_queue_event_logs_with_options(
        self,
        request: main_models.ListLegacyQueueEventLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyQueueEventLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyQueueEventLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyQueueEventLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_queue_event_logs_with_options_async(
        self,
        request: main_models.ListLegacyQueueEventLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLegacyQueueEventLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLegacyQueueEventLogs',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLegacyQueueEventLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_queue_event_logs(
        self,
        request: main_models.ListLegacyQueueEventLogsRequest,
    ) -> main_models.ListLegacyQueueEventLogsResponse:
        runtime = RuntimeOptions()
        return self.list_legacy_queue_event_logs_with_options(request, runtime)

    async def list_legacy_queue_event_logs_async(
        self,
        request: main_models.ListLegacyQueueEventLogsRequest,
    ) -> main_models.ListLegacyQueueEventLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_legacy_queue_event_logs_with_options_async(request, runtime)

    def list_mono_recordings_with_options(
        self,
        request: main_models.ListMonoRecordingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMonoRecordingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_channel_id):
            query['AgentChannelId'] = request.agent_channel_id
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonoRecordings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonoRecordingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mono_recordings_with_options_async(
        self,
        request: main_models.ListMonoRecordingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMonoRecordingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_channel_id):
            query['AgentChannelId'] = request.agent_channel_id
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonoRecordings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonoRecordingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mono_recordings(
        self,
        request: main_models.ListMonoRecordingsRequest,
    ) -> main_models.ListMonoRecordingsResponse:
        runtime = RuntimeOptions()
        return self.list_mono_recordings_with_options(request, runtime)

    async def list_mono_recordings_async(
        self,
        request: main_models.ListMonoRecordingsRequest,
    ) -> main_models.ListMonoRecordingsResponse:
        runtime = RuntimeOptions()
        return await self.list_mono_recordings_with_options_async(request, runtime)

    def list_multi_channel_recordings_with_options(
        self,
        request: main_models.ListMultiChannelRecordingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiChannelRecordingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_channel_id):
            query['AgentChannelId'] = request.agent_channel_id
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiChannelRecordings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiChannelRecordingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_channel_recordings_with_options_async(
        self,
        request: main_models.ListMultiChannelRecordingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiChannelRecordingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_channel_id):
            query['AgentChannelId'] = request.agent_channel_id
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiChannelRecordings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiChannelRecordingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_channel_recordings(
        self,
        request: main_models.ListMultiChannelRecordingsRequest,
    ) -> main_models.ListMultiChannelRecordingsResponse:
        runtime = RuntimeOptions()
        return self.list_multi_channel_recordings_with_options(request, runtime)

    async def list_multi_channel_recordings_async(
        self,
        request: main_models.ListMultiChannelRecordingsRequest,
    ) -> main_models.ListMultiChannelRecordingsResponse:
        runtime = RuntimeOptions()
        return await self.list_multi_channel_recordings_with_options_async(request, runtime)

    def list_notification_records_with_options(
        self,
        request: main_models.ListNotificationRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNotificationRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.notification_keys):
            query['NotificationKeys'] = request.notification_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNotificationRecords',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNotificationRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_notification_records_with_options_async(
        self,
        request: main_models.ListNotificationRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNotificationRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.notification_keys):
            query['NotificationKeys'] = request.notification_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNotificationRecords',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNotificationRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_notification_records(
        self,
        request: main_models.ListNotificationRecordsRequest,
    ) -> main_models.ListNotificationRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_notification_records_with_options(request, runtime)

    async def list_notification_records_async(
        self,
        request: main_models.ListNotificationRecordsRequest,
    ) -> main_models.ListNotificationRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_notification_records_with_options_async(request, runtime)

    def list_outbound_numbers_of_user_with_options(
        self,
        request: main_models.ListOutboundNumbersOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundNumbersOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOutboundNumbersOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundNumbersOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_numbers_of_user_with_options_async(
        self,
        request: main_models.ListOutboundNumbersOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundNumbersOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOutboundNumbersOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundNumbersOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_numbers_of_user(
        self,
        request: main_models.ListOutboundNumbersOfUserRequest,
    ) -> main_models.ListOutboundNumbersOfUserResponse:
        runtime = RuntimeOptions()
        return self.list_outbound_numbers_of_user_with_options(request, runtime)

    async def list_outbound_numbers_of_user_async(
        self,
        request: main_models.ListOutboundNumbersOfUserRequest,
    ) -> main_models.ListOutboundNumbersOfUserResponse:
        runtime = RuntimeOptions()
        return await self.list_outbound_numbers_of_user_with_options_async(request, runtime)

    def list_personal_numbers_of_user_with_options(
        self,
        request: main_models.ListPersonalNumbersOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPersonalNumbersOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPersonalNumbersOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPersonalNumbersOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_personal_numbers_of_user_with_options_async(
        self,
        request: main_models.ListPersonalNumbersOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPersonalNumbersOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPersonalNumbersOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPersonalNumbersOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_personal_numbers_of_user(
        self,
        request: main_models.ListPersonalNumbersOfUserRequest,
    ) -> main_models.ListPersonalNumbersOfUserResponse:
        runtime = RuntimeOptions()
        return self.list_personal_numbers_of_user_with_options(request, runtime)

    async def list_personal_numbers_of_user_async(
        self,
        request: main_models.ListPersonalNumbersOfUserRequest,
    ) -> main_models.ListPersonalNumbersOfUserResponse:
        runtime = RuntimeOptions()
        return await self.list_personal_numbers_of_user_with_options_async(request, runtime)

    def list_phone_numbers_with_options(
        self,
        request: main_models.ListPhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPhoneNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_numbers_with_options_async(
        self,
        request: main_models.ListPhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPhoneNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_numbers(
        self,
        request: main_models.ListPhoneNumbersRequest,
    ) -> main_models.ListPhoneNumbersResponse:
        runtime = RuntimeOptions()
        return self.list_phone_numbers_with_options(request, runtime)

    async def list_phone_numbers_async(
        self,
        request: main_models.ListPhoneNumbersRequest,
    ) -> main_models.ListPhoneNumbersResponse:
        runtime = RuntimeOptions()
        return await self.list_phone_numbers_with_options_async(request, runtime)

    def list_phone_numbers_of_skill_group_with_options(
        self,
        request: main_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPhoneNumbersOfSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPhoneNumbersOfSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPhoneNumbersOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_numbers_of_skill_group_with_options_async(
        self,
        request: main_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPhoneNumbersOfSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPhoneNumbersOfSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPhoneNumbersOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_numbers_of_skill_group(
        self,
        request: main_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> main_models.ListPhoneNumbersOfSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.list_phone_numbers_of_skill_group_with_options(request, runtime)

    async def list_phone_numbers_of_skill_group_async(
        self,
        request: main_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> main_models.ListPhoneNumbersOfSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_phone_numbers_of_skill_group_with_options_async(request, runtime)

    def list_privileges_of_user_with_options(
        self,
        request: main_models.ListPrivilegesOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivilegesOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivilegesOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivilegesOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_privileges_of_user_with_options_async(
        self,
        request: main_models.ListPrivilegesOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivilegesOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivilegesOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivilegesOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_privileges_of_user(
        self,
        request: main_models.ListPrivilegesOfUserRequest,
    ) -> main_models.ListPrivilegesOfUserResponse:
        runtime = RuntimeOptions()
        return self.list_privileges_of_user_with_options(request, runtime)

    async def list_privileges_of_user_async(
        self,
        request: main_models.ListPrivilegesOfUserRequest,
    ) -> main_models.ListPrivilegesOfUserResponse:
        runtime = RuntimeOptions()
        return await self.list_privileges_of_user_with_options_async(request, runtime)

    def list_ram_users_with_options(
        self,
        request: main_models.ListRamUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRamUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRamUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRamUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ram_users_with_options_async(
        self,
        request: main_models.ListRamUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRamUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRamUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRamUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ram_users(
        self,
        request: main_models.ListRamUsersRequest,
    ) -> main_models.ListRamUsersResponse:
        runtime = RuntimeOptions()
        return self.list_ram_users_with_options(request, runtime)

    async def list_ram_users_async(
        self,
        request: main_models.ListRamUsersRequest,
    ) -> main_models.ListRamUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_ram_users_with_options_async(request, runtime)

    def list_realtime_agent_states_with_options(
        self,
        request: main_models.ListRealtimeAgentStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeAgentStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.work_mode_list):
            query['WorkModeList'] = request.work_mode_list
        body = {}
        if not DaraCore.is_null(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        if not DaraCore.is_null(request.state_list):
            body['StateList'] = request.state_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRealtimeAgentStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeAgentStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_agent_states_with_options_async(
        self,
        request: main_models.ListRealtimeAgentStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeAgentStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.work_mode_list):
            query['WorkModeList'] = request.work_mode_list
        body = {}
        if not DaraCore.is_null(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        if not DaraCore.is_null(request.state_list):
            body['StateList'] = request.state_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRealtimeAgentStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeAgentStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_agent_states(
        self,
        request: main_models.ListRealtimeAgentStatesRequest,
    ) -> main_models.ListRealtimeAgentStatesResponse:
        runtime = RuntimeOptions()
        return self.list_realtime_agent_states_with_options(request, runtime)

    async def list_realtime_agent_states_async(
        self,
        request: main_models.ListRealtimeAgentStatesRequest,
    ) -> main_models.ListRealtimeAgentStatesResponse:
        runtime = RuntimeOptions()
        return await self.list_realtime_agent_states_with_options_async(request, runtime)

    def list_realtime_skill_group_states_with_options(
        self,
        request: main_models.ListRealtimeSkillGroupStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeSkillGroupStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRealtimeSkillGroupStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeSkillGroupStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_skill_group_states_with_options_async(
        self,
        request: main_models.ListRealtimeSkillGroupStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeSkillGroupStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRealtimeSkillGroupStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeSkillGroupStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_skill_group_states(
        self,
        request: main_models.ListRealtimeSkillGroupStatesRequest,
    ) -> main_models.ListRealtimeSkillGroupStatesResponse:
        runtime = RuntimeOptions()
        return self.list_realtime_skill_group_states_with_options(request, runtime)

    async def list_realtime_skill_group_states_async(
        self,
        request: main_models.ListRealtimeSkillGroupStatesRequest,
    ) -> main_models.ListRealtimeSkillGroupStatesResponse:
        runtime = RuntimeOptions()
        return await self.list_realtime_skill_group_states_with_options_async(request, runtime)

    def list_recent_call_detail_records_with_options(
        self,
        request: main_models.ListRecentCallDetailRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentCallDetailRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.criteria):
            query['Criteria'] = request.criteria
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentCallDetailRecords',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentCallDetailRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_call_detail_records_with_options_async(
        self,
        request: main_models.ListRecentCallDetailRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentCallDetailRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.criteria):
            query['Criteria'] = request.criteria
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentCallDetailRecords',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentCallDetailRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_call_detail_records(
        self,
        request: main_models.ListRecentCallDetailRecordsRequest,
    ) -> main_models.ListRecentCallDetailRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_recent_call_detail_records_with_options(request, runtime)

    async def list_recent_call_detail_records_async(
        self,
        request: main_models.ListRecentCallDetailRecordsRequest,
    ) -> main_models.ListRecentCallDetailRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_recent_call_detail_records_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_skill_group_states_with_options(
        self,
        request: main_models.ListSkillGroupStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupStatesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroupStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_states_with_options_async(
        self,
        request: main_models.ListSkillGroupStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupStatesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroupStates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group_states(
        self,
        request: main_models.ListSkillGroupStatesRequest,
    ) -> main_models.ListSkillGroupStatesResponse:
        runtime = RuntimeOptions()
        return self.list_skill_group_states_with_options(request, runtime)

    async def list_skill_group_states_async(
        self,
        request: main_models.ListSkillGroupStatesRequest,
    ) -> main_models.ListSkillGroupStatesResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_group_states_with_options_async(request, runtime)

    def list_skill_group_summary_reports_since_midnight_with_options(
        self,
        request: main_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroupSummaryReportsSinceMidnight',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupSummaryReportsSinceMidnightResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_summary_reports_since_midnight_with_options_async(
        self,
        request: main_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroupSummaryReportsSinceMidnight',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupSummaryReportsSinceMidnightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group_summary_reports_since_midnight(
        self,
        request: main_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
    ) -> main_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        runtime = RuntimeOptions()
        return self.list_skill_group_summary_reports_since_midnight_with_options(request, runtime)

    async def list_skill_group_summary_reports_since_midnight_async(
        self,
        request: main_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
    ) -> main_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_group_summary_reports_since_midnight_with_options_async(request, runtime)

    def list_skill_groups_with_options(
        self,
        request: main_models.ListSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_groups_with_options_async(
        self,
        request: main_models.ListSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_groups(
        self,
        request: main_models.ListSkillGroupsRequest,
    ) -> main_models.ListSkillGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_skill_groups_with_options(request, runtime)

    async def list_skill_groups_async(
        self,
        request: main_models.ListSkillGroupsRequest,
    ) -> main_models.ListSkillGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_groups_with_options_async(request, runtime)

    def list_skill_levels_of_user_with_options(
        self,
        request: main_models.ListSkillLevelsOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillLevelsOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillLevelsOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillLevelsOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_levels_of_user_with_options_async(
        self,
        request: main_models.ListSkillLevelsOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillLevelsOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillLevelsOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillLevelsOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_levels_of_user(
        self,
        request: main_models.ListSkillLevelsOfUserRequest,
    ) -> main_models.ListSkillLevelsOfUserResponse:
        runtime = RuntimeOptions()
        return self.list_skill_levels_of_user_with_options(request, runtime)

    async def list_skill_levels_of_user_async(
        self,
        request: main_models.ListSkillLevelsOfUserRequest,
    ) -> main_models.ListSkillLevelsOfUserResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_levels_of_user_with_options_async(request, runtime)

    def list_sms_metadata_with_options(
        self,
        request: main_models.ListSmsMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmsMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scenario_list_json):
            query['ScenarioListJson'] = request.scenario_list_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmsMetadata',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmsMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sms_metadata_with_options_async(
        self,
        request: main_models.ListSmsMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmsMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scenario_list_json):
            query['ScenarioListJson'] = request.scenario_list_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmsMetadata',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmsMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sms_metadata(
        self,
        request: main_models.ListSmsMetadataRequest,
    ) -> main_models.ListSmsMetadataResponse:
        runtime = RuntimeOptions()
        return self.list_sms_metadata_with_options(request, runtime)

    async def list_sms_metadata_async(
        self,
        request: main_models.ListSmsMetadataRequest,
    ) -> main_models.ListSmsMetadataResponse:
        runtime = RuntimeOptions()
        return await self.list_sms_metadata_with_options_async(request, runtime)

    def list_ticket_tasks_with_options(
        self,
        request: main_models.ListTicketTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketTasks',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ticket_tasks_with_options_async(
        self,
        request: main_models.ListTicketTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketTasks',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ticket_tasks(
        self,
        request: main_models.ListTicketTasksRequest,
    ) -> main_models.ListTicketTasksResponse:
        runtime = RuntimeOptions()
        return self.list_ticket_tasks_with_options(request, runtime)

    async def list_ticket_tasks_async(
        self,
        request: main_models.ListTicketTasksRequest,
    ) -> main_models.ListTicketTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_ticket_tasks_with_options_async(request, runtime)

    def list_ticket_templates_with_options(
        self,
        request: main_models.ListTicketTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketTemplates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ticket_templates_with_options_async(
        self,
        request: main_models.ListTicketTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTicketTemplates',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ticket_templates(
        self,
        request: main_models.ListTicketTemplatesRequest,
    ) -> main_models.ListTicketTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_ticket_templates_with_options(request, runtime)

    async def list_ticket_templates_async(
        self,
        request: main_models.ListTicketTemplatesRequest,
    ) -> main_models.ListTicketTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_ticket_templates_with_options_async(request, runtime)

    def list_tickets_with_options(
        self,
        request: main_models.ListTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.assignee_type):
            query['AssigneeType'] = request.assignee_type
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id_list):
            query['JobIdList'] = request.job_id_list
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.participant):
            query['Participant'] = request.participant
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tickets_with_options_async(
        self,
        request: main_models.ListTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTicketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.assignee_type):
            query['AssigneeType'] = request.assignee_type
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id_list):
            query['JobIdList'] = request.job_id_list
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.participant):
            query['Participant'] = request.participant
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTickets',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tickets(
        self,
        request: main_models.ListTicketsRequest,
    ) -> main_models.ListTicketsResponse:
        runtime = RuntimeOptions()
        return self.list_tickets_with_options(request, runtime)

    async def list_tickets_async(
        self,
        request: main_models.ListTicketsRequest,
    ) -> main_models.ListTicketsResponse:
        runtime = RuntimeOptions()
        return await self.list_tickets_with_options_async(request, runtime)

    def list_unassigned_numbers_with_options(
        self,
        request: main_models.ListUnassignedNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUnassignedNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUnassignedNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUnassignedNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_unassigned_numbers_with_options_async(
        self,
        request: main_models.ListUnassignedNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUnassignedNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUnassignedNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUnassignedNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_unassigned_numbers(
        self,
        request: main_models.ListUnassignedNumbersRequest,
    ) -> main_models.ListUnassignedNumbersResponse:
        runtime = RuntimeOptions()
        return self.list_unassigned_numbers_with_options(request, runtime)

    async def list_unassigned_numbers_async(
        self,
        request: main_models.ListUnassignedNumbersRequest,
    ) -> main_models.ListUnassignedNumbersResponse:
        runtime = RuntimeOptions()
        return await self.list_unassigned_numbers_with_options_async(request, runtime)

    def list_user_levels_of_skill_group_with_options(
        self,
        request: main_models.ListUserLevelsOfSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserLevelsOfSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserLevelsOfSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserLevelsOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_levels_of_skill_group_with_options_async(
        self,
        request: main_models.ListUserLevelsOfSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserLevelsOfSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_member):
            query['IsMember'] = request.is_member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserLevelsOfSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserLevelsOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_levels_of_skill_group(
        self,
        request: main_models.ListUserLevelsOfSkillGroupRequest,
    ) -> main_models.ListUserLevelsOfSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.list_user_levels_of_skill_group_with_options(request, runtime)

    async def list_user_levels_of_skill_group_async(
        self,
        request: main_models.ListUserLevelsOfSkillGroupRequest,
    ) -> main_models.ListUserLevelsOfSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_user_levels_of_skill_group_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_visitor_chat_messages_with_options(
        self,
        request: main_models.ListVisitorChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVisitorChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.visitor_id):
            query['VisitorId'] = request.visitor_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVisitorChatMessages',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVisitorChatMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_visitor_chat_messages_with_options_async(
        self,
        request: main_models.ListVisitorChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVisitorChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.visitor_id):
            query['VisitorId'] = request.visitor_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVisitorChatMessages',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVisitorChatMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_visitor_chat_messages(
        self,
        request: main_models.ListVisitorChatMessagesRequest,
    ) -> main_models.ListVisitorChatMessagesResponse:
        runtime = RuntimeOptions()
        return self.list_visitor_chat_messages_with_options(request, runtime)

    async def list_visitor_chat_messages_async(
        self,
        request: main_models.ListVisitorChatMessagesRequest,
    ) -> main_models.ListVisitorChatMessagesResponse:
        runtime = RuntimeOptions()
        return await self.list_visitor_chat_messages_with_options_async(request, runtime)

    def list_voicemails_with_options(
        self,
        request: main_models.ListVoicemailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoicemailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVoicemails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVoicemailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voicemails_with_options_async(
        self,
        request: main_models.ListVoicemailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVoicemailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVoicemails',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVoicemailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voicemails(
        self,
        request: main_models.ListVoicemailsRequest,
    ) -> main_models.ListVoicemailsResponse:
        runtime = RuntimeOptions()
        return self.list_voicemails_with_options(request, runtime)

    async def list_voicemails_async(
        self,
        request: main_models.ListVoicemailsRequest,
    ) -> main_models.ListVoicemailsResponse:
        runtime = RuntimeOptions()
        return await self.list_voicemails_with_options_async(request, runtime)

    def list_waiting_chats_with_options(
        self,
        request: main_models.ListWaitingChatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWaitingChatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWaitingChats',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWaitingChatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waiting_chats_with_options_async(
        self,
        request: main_models.ListWaitingChatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWaitingChatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWaitingChats',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWaitingChatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waiting_chats(
        self,
        request: main_models.ListWaitingChatsRequest,
    ) -> main_models.ListWaitingChatsResponse:
        runtime = RuntimeOptions()
        return self.list_waiting_chats_with_options(request, runtime)

    async def list_waiting_chats_async(
        self,
        request: main_models.ListWaitingChatsRequest,
    ) -> main_models.ListWaitingChatsResponse:
        runtime = RuntimeOptions()
        return await self.list_waiting_chats_with_options_async(request, runtime)

    def make_call_with_options(
        self,
        request: main_models.MakeCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MakeCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.flash_sms_variables):
            query['FlashSmsVariables'] = request.flash_sms_variables
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MakeCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MakeCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_call_with_options_async(
        self,
        request: main_models.MakeCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MakeCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.flash_sms_variables):
            query['FlashSmsVariables'] = request.flash_sms_variables
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MakeCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MakeCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_call(
        self,
        request: main_models.MakeCallRequest,
    ) -> main_models.MakeCallResponse:
        runtime = RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    async def make_call_async(
        self,
        request: main_models.MakeCallRequest,
    ) -> main_models.MakeCallResponse:
        runtime = RuntimeOptions()
        return await self.make_call_with_options_async(request, runtime)

    def modify_audio_file_with_options(
        self,
        request: main_models.ModifyAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audio_file_with_options_async(
        self,
        request: main_models.ModifyAudioFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAudioFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not DaraCore.is_null(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAudioFile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audio_file(
        self,
        request: main_models.ModifyAudioFileRequest,
    ) -> main_models.ModifyAudioFileResponse:
        runtime = RuntimeOptions()
        return self.modify_audio_file_with_options(request, runtime)

    async def modify_audio_file_async(
        self,
        request: main_models.ModifyAudioFileRequest,
    ) -> main_models.ModifyAudioFileResponse:
        runtime = RuntimeOptions()
        return await self.modify_audio_file_with_options_async(request, runtime)

    def modify_campaign_numbers_with_options(
        self,
        tmp_req: main_models.ModifyCampaignNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCampaignNumbersResponse:
        tmp_req.validate()
        request = main_models.ModifyCampaignNumbersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.number_list):
            request.number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.number_list, 'NumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.inst_group_id):
            query['InstGroupId'] = request.inst_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list_shrink):
            query['NumberList'] = request.number_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCampaignNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCampaignNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_campaign_numbers_with_options_async(
        self,
        tmp_req: main_models.ModifyCampaignNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCampaignNumbersResponse:
        tmp_req.validate()
        request = main_models.ModifyCampaignNumbersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.number_list):
            request.number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.number_list, 'NumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.inst_group_id):
            query['InstGroupId'] = request.inst_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list_shrink):
            query['NumberList'] = request.number_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCampaignNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCampaignNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_campaign_numbers(
        self,
        request: main_models.ModifyCampaignNumbersRequest,
    ) -> main_models.ModifyCampaignNumbersResponse:
        runtime = RuntimeOptions()
        return self.modify_campaign_numbers_with_options(request, runtime)

    async def modify_campaign_numbers_async(
        self,
        request: main_models.ModifyCampaignNumbersRequest,
    ) -> main_models.ModifyCampaignNumbersResponse:
        runtime = RuntimeOptions()
        return await self.modify_campaign_numbers_with_options_async(request, runtime)

    def modify_custom_call_tagging_with_options(
        self,
        request: main_models.ModifyCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_call_tagging_with_options_async(
        self,
        request: main_models.ModifyCustomCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_call_tagging(
        self,
        request: main_models.ModifyCustomCallTaggingRequest,
    ) -> main_models.ModifyCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.modify_custom_call_tagging_with_options(request, runtime)

    async def modify_custom_call_tagging_async(
        self,
        request: main_models.ModifyCustomCallTaggingRequest,
    ) -> main_models.ModifyCustomCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.modify_custom_call_tagging_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_phone_number_with_options(
        self,
        request: main_models.ModifyPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPhoneNumber',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_phone_number_with_options_async(
        self,
        request: main_models.ModifyPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.usage):
            query['Usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPhoneNumber',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_phone_number(
        self,
        request: main_models.ModifyPhoneNumberRequest,
    ) -> main_models.ModifyPhoneNumberResponse:
        runtime = RuntimeOptions()
        return self.modify_phone_number_with_options(request, runtime)

    async def modify_phone_number_async(
        self,
        request: main_models.ModifyPhoneNumberRequest,
    ) -> main_models.ModifyPhoneNumberResponse:
        runtime = RuntimeOptions()
        return await self.modify_phone_number_with_options_async(request, runtime)

    def modify_skill_group_with_options(
        self,
        request: main_models.ModifySkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_skill_group_with_options_async(
        self,
        request: main_models.ModifySkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_skill_group(
        self,
        request: main_models.ModifySkillGroupRequest,
    ) -> main_models.ModifySkillGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_skill_group_with_options(request, runtime)

    async def modify_skill_group_async(
        self,
        request: main_models.ModifySkillGroupRequest,
    ) -> main_models.ModifySkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_skill_group_with_options_async(request, runtime)

    def modify_skill_levels_of_user_with_options(
        self,
        request: main_models.ModifySkillLevelsOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySkillLevelsOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySkillLevelsOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySkillLevelsOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_skill_levels_of_user_with_options_async(
        self,
        request: main_models.ModifySkillLevelsOfUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySkillLevelsOfUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySkillLevelsOfUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySkillLevelsOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_skill_levels_of_user(
        self,
        request: main_models.ModifySkillLevelsOfUserRequest,
    ) -> main_models.ModifySkillLevelsOfUserResponse:
        runtime = RuntimeOptions()
        return self.modify_skill_levels_of_user_with_options(request, runtime)

    async def modify_skill_levels_of_user_async(
        self,
        request: main_models.ModifySkillLevelsOfUserRequest,
    ) -> main_models.ModifySkillLevelsOfUserResponse:
        runtime = RuntimeOptions()
        return await self.modify_skill_levels_of_user_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: main_models.ModifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not DaraCore.is_null(request.display_id):
            query['DisplayId'] = request.display_id
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: main_models.ModifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not DaraCore.is_null(request.display_id):
            query['DisplayId'] = request.display_id
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user(
        self,
        request: main_models.ModifyUserRequest,
    ) -> main_models.ModifyUserResponse:
        runtime = RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: main_models.ModifyUserRequest,
    ) -> main_models.ModifyUserResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def modify_user_levels_of_skill_group_with_options(
        self,
        request: main_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserLevelsOfSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.user_level_list):
            query['UserLevelList'] = request.user_level_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserLevelsOfSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserLevelsOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_levels_of_skill_group_with_options_async(
        self,
        request: main_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserLevelsOfSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.user_level_list):
            query['UserLevelList'] = request.user_level_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserLevelsOfSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserLevelsOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_levels_of_skill_group(
        self,
        request: main_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> main_models.ModifyUserLevelsOfSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_user_levels_of_skill_group_with_options(request, runtime)

    async def modify_user_levels_of_skill_group_async(
        self,
        request: main_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> main_models.ModifyUserLevelsOfSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_levels_of_skill_group_with_options_async(request, runtime)

    def monitor_call_with_options(
        self,
        request: main_models.MonitorCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MonitorCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.monitored_user_id):
            query['MonitoredUserId'] = request.monitored_user_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MonitorCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MonitorCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def monitor_call_with_options_async(
        self,
        request: main_models.MonitorCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MonitorCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.monitored_user_id):
            query['MonitoredUserId'] = request.monitored_user_id
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MonitorCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MonitorCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def monitor_call(
        self,
        request: main_models.MonitorCallRequest,
    ) -> main_models.MonitorCallResponse:
        runtime = RuntimeOptions()
        return self.monitor_call_with_options(request, runtime)

    async def monitor_call_async(
        self,
        request: main_models.MonitorCallRequest,
    ) -> main_models.MonitorCallResponse:
        runtime = RuntimeOptions()
        return await self.monitor_call_with_options_async(request, runtime)

    def mute_call_with_options(
        self,
        request: main_models.MuteCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MuteCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MuteCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MuteCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def mute_call_with_options_async(
        self,
        request: main_models.MuteCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MuteCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MuteCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MuteCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mute_call(
        self,
        request: main_models.MuteCallRequest,
    ) -> main_models.MuteCallResponse:
        runtime = RuntimeOptions()
        return self.mute_call_with_options(request, runtime)

    async def mute_call_async(
        self,
        request: main_models.MuteCallRequest,
    ) -> main_models.MuteCallResponse:
        runtime = RuntimeOptions()
        return await self.mute_call_with_options_async(request, runtime)

    def pause_campaign_with_options(
        self,
        request: main_models.PauseCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_campaign_with_options_async(
        self,
        request: main_models.PauseCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_campaign(
        self,
        request: main_models.PauseCampaignRequest,
    ) -> main_models.PauseCampaignResponse:
        runtime = RuntimeOptions()
        return self.pause_campaign_with_options(request, runtime)

    async def pause_campaign_async(
        self,
        request: main_models.PauseCampaignRequest,
    ) -> main_models.PauseCampaignResponse:
        runtime = RuntimeOptions()
        return await self.pause_campaign_with_options_async(request, runtime)

    def pick_outbound_numbers_with_options(
        self,
        request: main_models.PickOutboundNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PickOutboundNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PickOutboundNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PickOutboundNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def pick_outbound_numbers_with_options_async(
        self,
        request: main_models.PickOutboundNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PickOutboundNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PickOutboundNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PickOutboundNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pick_outbound_numbers(
        self,
        request: main_models.PickOutboundNumbersRequest,
    ) -> main_models.PickOutboundNumbersResponse:
        runtime = RuntimeOptions()
        return self.pick_outbound_numbers_with_options(request, runtime)

    async def pick_outbound_numbers_async(
        self,
        request: main_models.PickOutboundNumbersRequest,
    ) -> main_models.PickOutboundNumbersResponse:
        runtime = RuntimeOptions()
        return await self.pick_outbound_numbers_with_options_async(request, runtime)

    def poll_user_status_with_options(
        self,
        request: main_models.PollUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PollUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PollUserStatus',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PollUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_user_status_with_options_async(
        self,
        request: main_models.PollUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PollUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PollUserStatus',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PollUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_user_status(
        self,
        request: main_models.PollUserStatusRequest,
    ) -> main_models.PollUserStatusResponse:
        runtime = RuntimeOptions()
        return self.poll_user_status_with_options(request, runtime)

    async def poll_user_status_async(
        self,
        request: main_models.PollUserStatusRequest,
    ) -> main_models.PollUserStatusResponse:
        runtime = RuntimeOptions()
        return await self.poll_user_status_with_options_async(request, runtime)

    def process_ali_me_callback_of_staging_with_options(
        self,
        request: main_models.ProcessAliMeCallbackOfStagingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProcessAliMeCallbackOfStagingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProcessAliMeCallbackOfStaging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProcessAliMeCallbackOfStagingResponse(),
            self.call_api(params, req, runtime)
        )

    async def process_ali_me_callback_of_staging_with_options_async(
        self,
        request: main_models.ProcessAliMeCallbackOfStagingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProcessAliMeCallbackOfStagingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProcessAliMeCallbackOfStaging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProcessAliMeCallbackOfStagingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def process_ali_me_callback_of_staging(
        self,
        request: main_models.ProcessAliMeCallbackOfStagingRequest,
    ) -> main_models.ProcessAliMeCallbackOfStagingResponse:
        runtime = RuntimeOptions()
        return self.process_ali_me_callback_of_staging_with_options(request, runtime)

    async def process_ali_me_callback_of_staging_async(
        self,
        request: main_models.ProcessAliMeCallbackOfStagingRequest,
    ) -> main_models.ProcessAliMeCallbackOfStagingResponse:
        runtime = RuntimeOptions()
        return await self.process_ali_me_callback_of_staging_with_options_async(request, runtime)

    def process_custom_imcallback_with_options(
        self,
        request: main_models.ProcessCustomIMCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProcessCustomIMCallbackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_channel_id):
            body['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_content):
            body['MessageContent'] = request.message_content
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.sender_avatar_media_id):
            body['SenderAvatarMediaId'] = request.sender_avatar_media_id
        if not DaraCore.is_null(request.sender_id):
            body['SenderId'] = request.sender_id
        if not DaraCore.is_null(request.sender_name):
            body['SenderName'] = request.sender_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ProcessCustomIMCallback',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProcessCustomIMCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def process_custom_imcallback_with_options_async(
        self,
        request: main_models.ProcessCustomIMCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProcessCustomIMCallbackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_channel_id):
            body['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_content):
            body['MessageContent'] = request.message_content
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.sender_avatar_media_id):
            body['SenderAvatarMediaId'] = request.sender_avatar_media_id
        if not DaraCore.is_null(request.sender_id):
            body['SenderId'] = request.sender_id
        if not DaraCore.is_null(request.sender_name):
            body['SenderName'] = request.sender_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ProcessCustomIMCallback',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProcessCustomIMCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def process_custom_imcallback(
        self,
        request: main_models.ProcessCustomIMCallbackRequest,
    ) -> main_models.ProcessCustomIMCallbackResponse:
        runtime = RuntimeOptions()
        return self.process_custom_imcallback_with_options(request, runtime)

    async def process_custom_imcallback_async(
        self,
        request: main_models.ProcessCustomIMCallbackRequest,
    ) -> main_models.ProcessCustomIMCallbackResponse:
        runtime = RuntimeOptions()
        return await self.process_custom_imcallback_with_options_async(request, runtime)

    def publish_contact_flow_with_options(
        self,
        request: main_models.PublishContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_contact_flow_with_options_async(
        self,
        request: main_models.PublishContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.draft_id):
            query['DraftId'] = request.draft_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_contact_flow(
        self,
        request: main_models.PublishContactFlowRequest,
    ) -> main_models.PublishContactFlowResponse:
        runtime = RuntimeOptions()
        return self.publish_contact_flow_with_options(request, runtime)

    async def publish_contact_flow_async(
        self,
        request: main_models.PublishContactFlowRequest,
    ) -> main_models.PublishContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.publish_contact_flow_with_options_async(request, runtime)

    def ready_for_service_with_options(
        self,
        request: main_models.ReadyForServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadyForServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadyForService',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadyForServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def ready_for_service_with_options_async(
        self,
        request: main_models.ReadyForServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadyForServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadyForService',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadyForServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ready_for_service(
        self,
        request: main_models.ReadyForServiceRequest,
    ) -> main_models.ReadyForServiceResponse:
        runtime = RuntimeOptions()
        return self.ready_for_service_with_options(request, runtime)

    async def ready_for_service_async(
        self,
        request: main_models.ReadyForServiceRequest,
    ) -> main_models.ReadyForServiceResponse:
        runtime = RuntimeOptions()
        return await self.ready_for_service_with_options_async(request, runtime)

    def redial_call_with_options(
        self,
        request: main_models.RedialCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RedialCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RedialCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RedialCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def redial_call_with_options_async(
        self,
        request: main_models.RedialCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RedialCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RedialCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RedialCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def redial_call(
        self,
        request: main_models.RedialCallRequest,
    ) -> main_models.RedialCallResponse:
        runtime = RuntimeOptions()
        return self.redial_call_with_options(request, runtime)

    async def redial_call_async(
        self,
        request: main_models.RedialCallRequest,
    ) -> main_models.RedialCallResponse:
        runtime = RuntimeOptions()
        return await self.redial_call_with_options_async(request, runtime)

    def register_device_with_options(
        self,
        request: main_models.RegisterDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDevice',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: main_models.RegisterDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDevice',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_device(
        self,
        request: main_models.RegisterDeviceRequest,
    ) -> main_models.RegisterDeviceResponse:
        runtime = RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: main_models.RegisterDeviceRequest,
    ) -> main_models.RegisterDeviceResponse:
        runtime = RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)

    def register_devices_with_options(
        self,
        request: main_models.RegisterDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_id_list_json):
            query['UserIdListJson'] = request.user_id_list_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDevices',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_devices_with_options_async(
        self,
        request: main_models.RegisterDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_id_list_json):
            query['UserIdListJson'] = request.user_id_list_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDevices',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_devices(
        self,
        request: main_models.RegisterDevicesRequest,
    ) -> main_models.RegisterDevicesResponse:
        runtime = RuntimeOptions()
        return self.register_devices_with_options(request, runtime)

    async def register_devices_async(
        self,
        request: main_models.RegisterDevicesRequest,
    ) -> main_models.RegisterDevicesResponse:
        runtime = RuntimeOptions()
        return await self.register_devices_with_options_async(request, runtime)

    def reject_chat_with_options(
        self,
        request: main_models.RejectChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_chat_with_options_async(
        self,
        request: main_models.RejectChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_chat(
        self,
        request: main_models.RejectChatRequest,
    ) -> main_models.RejectChatResponse:
        runtime = RuntimeOptions()
        return self.reject_chat_with_options(request, runtime)

    async def reject_chat_async(
        self,
        request: main_models.RejectChatRequest,
    ) -> main_models.RejectChatResponse:
        runtime = RuntimeOptions()
        return await self.reject_chat_with_options_async(request, runtime)

    def reject_ticket_with_options(
        self,
        request: main_models.RejectTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_ticket_with_options_async(
        self,
        request: main_models.RejectTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_ticket(
        self,
        request: main_models.RejectTicketRequest,
    ) -> main_models.RejectTicketResponse:
        runtime = RuntimeOptions()
        return self.reject_ticket_with_options(request, runtime)

    async def reject_ticket_async(
        self,
        request: main_models.RejectTicketRequest,
    ) -> main_models.RejectTicketResponse:
        runtime = RuntimeOptions()
        return await self.reject_ticket_with_options_async(request, runtime)

    def release_call_with_options(
        self,
        request: main_models.ReleaseCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_call_with_options_async(
        self,
        request: main_models.ReleaseCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_call(
        self,
        request: main_models.ReleaseCallRequest,
    ) -> main_models.ReleaseCallResponse:
        runtime = RuntimeOptions()
        return self.release_call_with_options(request, runtime)

    async def release_call_async(
        self,
        request: main_models.ReleaseCallRequest,
    ) -> main_models.ReleaseCallResponse:
        runtime = RuntimeOptions()
        return await self.release_call_with_options_async(request, runtime)

    def release_chat_with_options(
        self,
        request: main_models.ReleaseChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_chat_with_options_async(
        self,
        request: main_models.ReleaseChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_chat(
        self,
        request: main_models.ReleaseChatRequest,
    ) -> main_models.ReleaseChatResponse:
        runtime = RuntimeOptions()
        return self.release_chat_with_options(request, runtime)

    async def release_chat_async(
        self,
        request: main_models.ReleaseChatRequest,
    ) -> main_models.ReleaseChatResponse:
        runtime = RuntimeOptions()
        return await self.release_chat_with_options_async(request, runtime)

    def remove_blacklist_call_tagging_with_options(
        self,
        request: main_models.RemoveBlacklistCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveBlacklistCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveBlacklistCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveBlacklistCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_blacklist_call_tagging_with_options_async(
        self,
        request: main_models.RemoveBlacklistCallTaggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveBlacklistCallTaggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveBlacklistCallTagging',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveBlacklistCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_blacklist_call_tagging(
        self,
        request: main_models.RemoveBlacklistCallTaggingRequest,
    ) -> main_models.RemoveBlacklistCallTaggingResponse:
        runtime = RuntimeOptions()
        return self.remove_blacklist_call_tagging_with_options(request, runtime)

    async def remove_blacklist_call_tagging_async(
        self,
        request: main_models.RemoveBlacklistCallTaggingRequest,
    ) -> main_models.RemoveBlacklistCallTaggingResponse:
        runtime = RuntimeOptions()
        return await self.remove_blacklist_call_tagging_with_options_async(request, runtime)

    def remove_do_not_call_numbers_with_options(
        self,
        request: main_models.RemoveDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_do_not_call_numbers_with_options_async(
        self,
        request: main_models.RemoveDoNotCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDoNotCallNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDoNotCallNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_do_not_call_numbers(
        self,
        request: main_models.RemoveDoNotCallNumbersRequest,
    ) -> main_models.RemoveDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return self.remove_do_not_call_numbers_with_options(request, runtime)

    async def remove_do_not_call_numbers_async(
        self,
        request: main_models.RemoveDoNotCallNumbersRequest,
    ) -> main_models.RemoveDoNotCallNumbersResponse:
        runtime = RuntimeOptions()
        return await self.remove_do_not_call_numbers_with_options_async(request, runtime)

    def remove_personal_numbers_from_user_with_options(
        self,
        request: main_models.RemovePersonalNumbersFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePersonalNumbersFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePersonalNumbersFromUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePersonalNumbersFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_personal_numbers_from_user_with_options_async(
        self,
        request: main_models.RemovePersonalNumbersFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePersonalNumbersFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePersonalNumbersFromUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePersonalNumbersFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_personal_numbers_from_user(
        self,
        request: main_models.RemovePersonalNumbersFromUserRequest,
    ) -> main_models.RemovePersonalNumbersFromUserResponse:
        runtime = RuntimeOptions()
        return self.remove_personal_numbers_from_user_with_options(request, runtime)

    async def remove_personal_numbers_from_user_async(
        self,
        request: main_models.RemovePersonalNumbersFromUserRequest,
    ) -> main_models.RemovePersonalNumbersFromUserResponse:
        runtime = RuntimeOptions()
        return await self.remove_personal_numbers_from_user_with_options_async(request, runtime)

    def remove_phone_number_from_skill_groups_with_options(
        self,
        request: main_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePhoneNumberFromSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePhoneNumberFromSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePhoneNumberFromSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_number_from_skill_groups_with_options_async(
        self,
        request: main_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePhoneNumberFromSkillGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePhoneNumberFromSkillGroups',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePhoneNumberFromSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_number_from_skill_groups(
        self,
        request: main_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> main_models.RemovePhoneNumberFromSkillGroupsResponse:
        runtime = RuntimeOptions()
        return self.remove_phone_number_from_skill_groups_with_options(request, runtime)

    async def remove_phone_number_from_skill_groups_async(
        self,
        request: main_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> main_models.RemovePhoneNumberFromSkillGroupsResponse:
        runtime = RuntimeOptions()
        return await self.remove_phone_number_from_skill_groups_with_options_async(request, runtime)

    def remove_phone_numbers_with_options(
        self,
        request: main_models.RemovePhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePhoneNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_numbers_with_options_async(
        self,
        request: main_models.RemovePhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePhoneNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_numbers(
        self,
        request: main_models.RemovePhoneNumbersRequest,
    ) -> main_models.RemovePhoneNumbersResponse:
        runtime = RuntimeOptions()
        return self.remove_phone_numbers_with_options(request, runtime)

    async def remove_phone_numbers_async(
        self,
        request: main_models.RemovePhoneNumbersRequest,
    ) -> main_models.RemovePhoneNumbersResponse:
        runtime = RuntimeOptions()
        return await self.remove_phone_numbers_with_options_async(request, runtime)

    def remove_phone_numbers_from_skill_group_with_options(
        self,
        request: main_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePhoneNumbersFromSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePhoneNumbersFromSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePhoneNumbersFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_numbers_from_skill_group_with_options_async(
        self,
        request: main_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePhoneNumbersFromSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePhoneNumbersFromSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePhoneNumbersFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_numbers_from_skill_group(
        self,
        request: main_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> main_models.RemovePhoneNumbersFromSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_phone_numbers_from_skill_group_with_options(request, runtime)

    async def remove_phone_numbers_from_skill_group_async(
        self,
        request: main_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> main_models.RemovePhoneNumbersFromSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_phone_numbers_from_skill_group_with_options_async(request, runtime)

    def remove_skill_groups_from_user_with_options(
        self,
        request: main_models.RemoveSkillGroupsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSkillGroupsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSkillGroupsFromUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSkillGroupsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_skill_groups_from_user_with_options_async(
        self,
        request: main_models.RemoveSkillGroupsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSkillGroupsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSkillGroupsFromUser',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSkillGroupsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_skill_groups_from_user(
        self,
        request: main_models.RemoveSkillGroupsFromUserRequest,
    ) -> main_models.RemoveSkillGroupsFromUserResponse:
        runtime = RuntimeOptions()
        return self.remove_skill_groups_from_user_with_options(request, runtime)

    async def remove_skill_groups_from_user_async(
        self,
        request: main_models.RemoveSkillGroupsFromUserRequest,
    ) -> main_models.RemoveSkillGroupsFromUserResponse:
        runtime = RuntimeOptions()
        return await self.remove_skill_groups_from_user_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: main_models.RemoveUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.notification_email):
            query['NotificationEmail'] = request.notification_email
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: main_models.RemoveUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.notification_email):
            query['NotificationEmail'] = request.notification_email
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users(
        self,
        request: main_models.RemoveUsersRequest,
    ) -> main_models.RemoveUsersResponse:
        runtime = RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: main_models.RemoveUsersRequest,
    ) -> main_models.RemoveUsersResponse:
        runtime = RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def remove_users_from_skill_group_with_options(
        self,
        request: main_models.RemoveUsersFromSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersFromSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_from_skill_group_with_options_async(
        self,
        request: main_models.RemoveUsersFromSkillGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersFromSkillGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromSkillGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users_from_skill_group(
        self,
        request: main_models.RemoveUsersFromSkillGroupRequest,
    ) -> main_models.RemoveUsersFromSkillGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_users_from_skill_group_with_options(request, runtime)

    async def remove_users_from_skill_group_async(
        self,
        request: main_models.RemoveUsersFromSkillGroupRequest,
    ) -> main_models.RemoveUsersFromSkillGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_users_from_skill_group_with_options_async(request, runtime)

    def reset_agent_state_with_options(
        self,
        request: main_models.ResetAgentStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAgentStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAgentState',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAgentStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_agent_state_with_options_async(
        self,
        request: main_models.ResetAgentStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAgentStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAgentState',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAgentStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_agent_state(
        self,
        request: main_models.ResetAgentStateRequest,
    ) -> main_models.ResetAgentStateResponse:
        runtime = RuntimeOptions()
        return self.reset_agent_state_with_options(request, runtime)

    async def reset_agent_state_async(
        self,
        request: main_models.ResetAgentStateRequest,
    ) -> main_models.ResetAgentStateResponse:
        runtime = RuntimeOptions()
        return await self.reset_agent_state_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: main_models.ResetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: main_models.ResetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def restore_archived_recordings_with_options(
        self,
        request: main_models.RestoreArchivedRecordingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreArchivedRecordingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreArchivedRecordings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreArchivedRecordingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_archived_recordings_with_options_async(
        self,
        request: main_models.RestoreArchivedRecordingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreArchivedRecordingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreArchivedRecordings',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreArchivedRecordingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_archived_recordings(
        self,
        request: main_models.RestoreArchivedRecordingsRequest,
    ) -> main_models.RestoreArchivedRecordingsResponse:
        runtime = RuntimeOptions()
        return self.restore_archived_recordings_with_options(request, runtime)

    async def restore_archived_recordings_async(
        self,
        request: main_models.RestoreArchivedRecordingsRequest,
    ) -> main_models.RestoreArchivedRecordingsResponse:
        runtime = RuntimeOptions()
        return await self.restore_archived_recordings_with_options_async(request, runtime)

    def resubmit_ticket_with_options(
        self,
        request: main_models.ResubmitTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResubmitTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResubmitTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResubmitTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def resubmit_ticket_with_options_async(
        self,
        request: main_models.ResubmitTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResubmitTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResubmitTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResubmitTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resubmit_ticket(
        self,
        request: main_models.ResubmitTicketRequest,
    ) -> main_models.ResubmitTicketResponse:
        runtime = RuntimeOptions()
        return self.resubmit_ticket_with_options(request, runtime)

    async def resubmit_ticket_async(
        self,
        request: main_models.ResubmitTicketRequest,
    ) -> main_models.ResubmitTicketResponse:
        runtime = RuntimeOptions()
        return await self.resubmit_ticket_with_options_async(request, runtime)

    def resume_campaign_with_options(
        self,
        request: main_models.ResumeCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_campaign_with_options_async(
        self,
        request: main_models.ResumeCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_campaign(
        self,
        request: main_models.ResumeCampaignRequest,
    ) -> main_models.ResumeCampaignResponse:
        runtime = RuntimeOptions()
        return self.resume_campaign_with_options(request, runtime)

    async def resume_campaign_async(
        self,
        request: main_models.ResumeCampaignRequest,
    ) -> main_models.ResumeCampaignResponse:
        runtime = RuntimeOptions()
        return await self.resume_campaign_with_options_async(request, runtime)

    def retrieve_call_with_options(
        self,
        request: main_models.RetrieveCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_call_with_options_async(
        self,
        request: main_models.RetrieveCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_call(
        self,
        request: main_models.RetrieveCallRequest,
    ) -> main_models.RetrieveCallResponse:
        runtime = RuntimeOptions()
        return self.retrieve_call_with_options(request, runtime)

    async def retrieve_call_async(
        self,
        request: main_models.RetrieveCallRequest,
    ) -> main_models.RetrieveCallResponse:
        runtime = RuntimeOptions()
        return await self.retrieve_call_with_options_async(request, runtime)

    def save_document_with_options(
        self,
        request: main_models.SaveDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_id):
            body['DocumentId'] = request.document_id
        if not DaraCore.is_null(request.document_json):
            body['DocumentJson'] = request.document_json
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveDocument',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_document_with_options_async(
        self,
        request: main_models.SaveDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_id):
            body['DocumentId'] = request.document_id
        if not DaraCore.is_null(request.document_json):
            body['DocumentJson'] = request.document_json
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveDocument',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_document(
        self,
        request: main_models.SaveDocumentRequest,
    ) -> main_models.SaveDocumentResponse:
        runtime = RuntimeOptions()
        return self.save_document_with_options(request, runtime)

    async def save_document_async(
        self,
        request: main_models.SaveDocumentRequest,
    ) -> main_models.SaveDocumentResponse:
        runtime = RuntimeOptions()
        return await self.save_document_with_options_async(request, runtime)

    def save_rtcstats_v2with_options(
        self,
        request: main_models.SaveRTCStatsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRTCStatsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not DaraCore.is_null(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not DaraCore.is_null(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRTCStatsV2',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRTCStatsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def save_rtcstats_v2with_options_async(
        self,
        request: main_models.SaveRTCStatsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRTCStatsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not DaraCore.is_null(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not DaraCore.is_null(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRTCStatsV2',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRTCStatsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def save_rtcstats_v2(
        self,
        request: main_models.SaveRTCStatsV2Request,
    ) -> main_models.SaveRTCStatsV2Response:
        runtime = RuntimeOptions()
        return self.save_rtcstats_v2with_options(request, runtime)

    async def save_rtcstats_v2_async(
        self,
        request: main_models.SaveRTCStatsV2Request,
    ) -> main_models.SaveRTCStatsV2Response:
        runtime = RuntimeOptions()
        return await self.save_rtcstats_v2with_options_async(request, runtime)

    def save_terminal_log_with_options(
        self,
        request: main_models.SaveTerminalLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTerminalLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.method_name):
            query['MethodName'] = request.method_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.unique_request_id):
            query['UniqueRequestId'] = request.unique_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTerminalLog',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTerminalLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_terminal_log_with_options_async(
        self,
        request: main_models.SaveTerminalLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTerminalLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.method_name):
            query['MethodName'] = request.method_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.unique_request_id):
            query['UniqueRequestId'] = request.unique_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTerminalLog',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTerminalLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_terminal_log(
        self,
        request: main_models.SaveTerminalLogRequest,
    ) -> main_models.SaveTerminalLogResponse:
        runtime = RuntimeOptions()
        return self.save_terminal_log_with_options(request, runtime)

    async def save_terminal_log_async(
        self,
        request: main_models.SaveTerminalLogRequest,
    ) -> main_models.SaveTerminalLogResponse:
        runtime = RuntimeOptions()
        return await self.save_terminal_log_with_options_async(request, runtime)

    def save_web_rtcstats_with_options(
        self,
        request: main_models.SaveWebRTCStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveWebRTCStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not DaraCore.is_null(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not DaraCore.is_null(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveWebRTCStats',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveWebRTCStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_web_rtcstats_with_options_async(
        self,
        request: main_models.SaveWebRTCStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveWebRTCStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not DaraCore.is_null(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not DaraCore.is_null(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveWebRTCStats',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveWebRTCStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_web_rtcstats(
        self,
        request: main_models.SaveWebRTCStatsRequest,
    ) -> main_models.SaveWebRTCStatsResponse:
        runtime = RuntimeOptions()
        return self.save_web_rtcstats_with_options(request, runtime)

    async def save_web_rtcstats_async(
        self,
        request: main_models.SaveWebRTCStatsRequest,
    ) -> main_models.SaveWebRTCStatsResponse:
        runtime = RuntimeOptions()
        return await self.save_web_rtcstats_with_options_async(request, runtime)

    def save_web_rtc_info_with_options(
        self,
        request: main_models.SaveWebRtcInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveWebRtcInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveWebRtcInfo',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveWebRtcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_web_rtc_info_with_options_async(
        self,
        request: main_models.SaveWebRtcInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveWebRtcInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveWebRtcInfo',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveWebRtcInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_web_rtc_info(
        self,
        request: main_models.SaveWebRtcInfoRequest,
    ) -> main_models.SaveWebRtcInfoResponse:
        runtime = RuntimeOptions()
        return self.save_web_rtc_info_with_options(request, runtime)

    async def save_web_rtc_info_async(
        self,
        request: main_models.SaveWebRtcInfoRequest,
    ) -> main_models.SaveWebRtcInfoResponse:
        runtime = RuntimeOptions()
        return await self.save_web_rtc_info_with_options_async(request, runtime)

    def send_dtmf_signaling_with_options(
        self,
        request: main_models.SendDtmfSignalingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendDtmfSignalingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.dtmf):
            query['Dtmf'] = request.dtmf
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendDtmfSignaling',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendDtmfSignalingResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_dtmf_signaling_with_options_async(
        self,
        request: main_models.SendDtmfSignalingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendDtmfSignalingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.dtmf):
            query['Dtmf'] = request.dtmf
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendDtmfSignaling',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendDtmfSignalingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_dtmf_signaling(
        self,
        request: main_models.SendDtmfSignalingRequest,
    ) -> main_models.SendDtmfSignalingResponse:
        runtime = RuntimeOptions()
        return self.send_dtmf_signaling_with_options(request, runtime)

    async def send_dtmf_signaling_async(
        self,
        request: main_models.SendDtmfSignalingRequest,
    ) -> main_models.SendDtmfSignalingResponse:
        runtime = RuntimeOptions()
        return await self.send_dtmf_signaling_with_options_async(request, runtime)

    def send_notification_with_options(
        self,
        request: main_models.SendNotificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_body):
            query['MessageBody'] = request.message_body
        if not DaraCore.is_null(request.notification_target):
            query['NotificationTarget'] = request.notification_target
        if not DaraCore.is_null(request.notification_type):
            query['NotificationType'] = request.notification_type
        if not DaraCore.is_null(request.sharding_key):
            query['ShardingKey'] = request.sharding_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendNotification',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_notification_with_options_async(
        self,
        request: main_models.SendNotificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_body):
            query['MessageBody'] = request.message_body
        if not DaraCore.is_null(request.notification_target):
            query['NotificationTarget'] = request.notification_target
        if not DaraCore.is_null(request.notification_type):
            query['NotificationType'] = request.notification_type
        if not DaraCore.is_null(request.sharding_key):
            query['ShardingKey'] = request.sharding_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendNotification',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_notification(
        self,
        request: main_models.SendNotificationRequest,
    ) -> main_models.SendNotificationResponse:
        runtime = RuntimeOptions()
        return self.send_notification_with_options(request, runtime)

    async def send_notification_async(
        self,
        request: main_models.SendNotificationRequest,
    ) -> main_models.SendNotificationResponse:
        runtime = RuntimeOptions()
        return await self.send_notification_with_options_async(request, runtime)

    def sign_in_group_with_options(
        self,
        request: main_models.SignInGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignInGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additivity):
            query['Additivity'] = request.additivity
        if not DaraCore.is_null(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignInGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_in_group_with_options_async(
        self,
        request: main_models.SignInGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignInGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additivity):
            query['Additivity'] = request.additivity
        if not DaraCore.is_null(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignInGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign_in_group(
        self,
        request: main_models.SignInGroupRequest,
    ) -> main_models.SignInGroupResponse:
        runtime = RuntimeOptions()
        return self.sign_in_group_with_options(request, runtime)

    async def sign_in_group_async(
        self,
        request: main_models.SignInGroupRequest,
    ) -> main_models.SignInGroupResponse:
        runtime = RuntimeOptions()
        return await self.sign_in_group_with_options_async(request, runtime)

    def sign_out_group_with_options(
        self,
        request: main_models.SignOutGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignOutGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignOutGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignOutGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_out_group_with_options_async(
        self,
        request: main_models.SignOutGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignOutGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignOutGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignOutGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign_out_group(
        self,
        request: main_models.SignOutGroupRequest,
    ) -> main_models.SignOutGroupResponse:
        runtime = RuntimeOptions()
        return self.sign_out_group_with_options(request, runtime)

    async def sign_out_group_async(
        self,
        request: main_models.SignOutGroupRequest,
    ) -> main_models.SignOutGroupResponse:
        runtime = RuntimeOptions()
        return await self.sign_out_group_with_options_async(request, runtime)

    def start_back_2back_call_with_options(
        self,
        request: main_models.StartBack2BackCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBack2BackCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_broker):
            query['AdditionalBroker'] = request.additional_broker
        if not DaraCore.is_null(request.broker):
            query['Broker'] = request.broker
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBack2BackCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBack2BackCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_back_2back_call_with_options_async(
        self,
        request: main_models.StartBack2BackCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBack2BackCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_broker):
            query['AdditionalBroker'] = request.additional_broker
        if not DaraCore.is_null(request.broker):
            query['Broker'] = request.broker
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBack2BackCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBack2BackCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_back_2back_call(
        self,
        request: main_models.StartBack2BackCallRequest,
    ) -> main_models.StartBack2BackCallResponse:
        runtime = RuntimeOptions()
        return self.start_back_2back_call_with_options(request, runtime)

    async def start_back_2back_call_async(
        self,
        request: main_models.StartBack2BackCallRequest,
    ) -> main_models.StartBack2BackCallResponse:
        runtime = RuntimeOptions()
        return await self.start_back_2back_call_with_options_async(request, runtime)

    def start_chat_with_options(
        self,
        tmp_req: main_models.StartChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartChatResponse:
        tmp_req.validate()
        request = main_models.StartChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_list):
            request.user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not DaraCore.is_null(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_chat_with_options_async(
        self,
        tmp_req: main_models.StartChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartChatResponse:
        tmp_req.validate()
        request = main_models.StartChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_list):
            request.user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not DaraCore.is_null(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartChat',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_chat(
        self,
        request: main_models.StartChatRequest,
    ) -> main_models.StartChatResponse:
        runtime = RuntimeOptions()
        return self.start_chat_with_options(request, runtime)

    async def start_chat_async(
        self,
        request: main_models.StartChatRequest,
    ) -> main_models.StartChatResponse:
        runtime = RuntimeOptions()
        return await self.start_chat_with_options_async(request, runtime)

    def start_conference_with_options(
        self,
        request: main_models.StartConferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartConferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.participant_list_json):
            query['ParticipantListJson'] = request.participant_list_json
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartConference',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_conference_with_options_async(
        self,
        request: main_models.StartConferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartConferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.participant_list_json):
            query['ParticipantListJson'] = request.participant_list_json
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartConference',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_conference(
        self,
        request: main_models.StartConferenceRequest,
    ) -> main_models.StartConferenceResponse:
        runtime = RuntimeOptions()
        return self.start_conference_with_options(request, runtime)

    async def start_conference_async(
        self,
        request: main_models.StartConferenceRequest,
    ) -> main_models.StartConferenceResponse:
        runtime = RuntimeOptions()
        return await self.start_conference_with_options_async(request, runtime)

    def start_edit_contact_flow_with_options(
        self,
        request: main_models.StartEditContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartEditContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartEditContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartEditContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_edit_contact_flow_with_options_async(
        self,
        request: main_models.StartEditContactFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartEditContactFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartEditContactFlow',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartEditContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_edit_contact_flow(
        self,
        request: main_models.StartEditContactFlowRequest,
    ) -> main_models.StartEditContactFlowResponse:
        runtime = RuntimeOptions()
        return self.start_edit_contact_flow_with_options(request, runtime)

    async def start_edit_contact_flow_async(
        self,
        request: main_models.StartEditContactFlowRequest,
    ) -> main_models.StartEditContactFlowResponse:
        runtime = RuntimeOptions()
        return await self.start_edit_contact_flow_with_options_async(request, runtime)

    def start_predictive_call_with_options(
        self,
        request: main_models.StartPredictiveCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPredictiveCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPredictiveCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPredictiveCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_predictive_call_with_options_async(
        self,
        request: main_models.StartPredictiveCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPredictiveCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPredictiveCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPredictiveCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_predictive_call(
        self,
        request: main_models.StartPredictiveCallRequest,
    ) -> main_models.StartPredictiveCallResponse:
        runtime = RuntimeOptions()
        return self.start_predictive_call_with_options(request, runtime)

    async def start_predictive_call_async(
        self,
        request: main_models.StartPredictiveCallRequest,
    ) -> main_models.StartPredictiveCallResponse:
        runtime = RuntimeOptions()
        return await self.start_predictive_call_with_options_async(request, runtime)

    def start_privacy_call_with_options(
        self,
        request: main_models.StartPrivacyCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPrivacyCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPrivacyCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPrivacyCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_privacy_call_with_options_async(
        self,
        request: main_models.StartPrivacyCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPrivacyCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPrivacyCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPrivacyCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_privacy_call(
        self,
        request: main_models.StartPrivacyCallRequest,
    ) -> main_models.StartPrivacyCallResponse:
        runtime = RuntimeOptions()
        return self.start_privacy_call_with_options(request, runtime)

    async def start_privacy_call_async(
        self,
        request: main_models.StartPrivacyCallRequest,
    ) -> main_models.StartPrivacyCallResponse:
        runtime = RuntimeOptions()
        return await self.start_privacy_call_with_options_async(request, runtime)

    def submit_campaign_with_options(
        self,
        request: main_models.SubmitCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_campaign_with_options_async(
        self,
        request: main_models.SubmitCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_campaign(
        self,
        request: main_models.SubmitCampaignRequest,
    ) -> main_models.SubmitCampaignResponse:
        runtime = RuntimeOptions()
        return self.submit_campaign_with_options(request, runtime)

    async def submit_campaign_async(
        self,
        request: main_models.SubmitCampaignRequest,
    ) -> main_models.SubmitCampaignResponse:
        runtime = RuntimeOptions()
        return await self.submit_campaign_with_options_async(request, runtime)

    def switch_to_conference_with_options(
        self,
        request: main_models.SwitchToConferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchToConferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchToConference',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchToConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_to_conference_with_options_async(
        self,
        request: main_models.SwitchToConferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchToConferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchToConference',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchToConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_to_conference(
        self,
        request: main_models.SwitchToConferenceRequest,
    ) -> main_models.SwitchToConferenceResponse:
        runtime = RuntimeOptions()
        return self.switch_to_conference_with_options(request, runtime)

    async def switch_to_conference_async(
        self,
        request: main_models.SwitchToConferenceRequest,
    ) -> main_models.SwitchToConferenceResponse:
        runtime = RuntimeOptions()
        return await self.switch_to_conference_with_options_async(request, runtime)

    def take_break_with_options(
        self,
        request: main_models.TakeBreakRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TakeBreakResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TakeBreak',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TakeBreakResponse(),
            self.call_api(params, req, runtime)
        )

    async def take_break_with_options_async(
        self,
        request: main_models.TakeBreakRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TakeBreakResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TakeBreak',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TakeBreakResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def take_break(
        self,
        request: main_models.TakeBreakRequest,
    ) -> main_models.TakeBreakResponse:
        runtime = RuntimeOptions()
        return self.take_break_with_options(request, runtime)

    async def take_break_async(
        self,
        request: main_models.TakeBreakRequest,
    ) -> main_models.TakeBreakResponse:
        runtime = RuntimeOptions()
        return await self.take_break_with_options_async(request, runtime)

    def terminate_ticket_with_options(
        self,
        request: main_models.TerminateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_ticket_with_options_async(
        self,
        request: main_models.TerminateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_ticket(
        self,
        request: main_models.TerminateTicketRequest,
    ) -> main_models.TerminateTicketResponse:
        runtime = RuntimeOptions()
        return self.terminate_ticket_with_options(request, runtime)

    async def terminate_ticket_async(
        self,
        request: main_models.TerminateTicketRequest,
    ) -> main_models.TerminateTicketResponse:
        runtime = RuntimeOptions()
        return await self.terminate_ticket_with_options_async(request, runtime)

    def transfer_ticket_task_with_options(
        self,
        request: main_models.TransferTicketTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferTicketTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferTicketTask',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferTicketTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_ticket_task_with_options_async(
        self,
        request: main_models.TransferTicketTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferTicketTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assignee):
            query['Assignee'] = request.assignee
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferTicketTask',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferTicketTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_ticket_task(
        self,
        request: main_models.TransferTicketTaskRequest,
    ) -> main_models.TransferTicketTaskResponse:
        runtime = RuntimeOptions()
        return self.transfer_ticket_task_with_options(request, runtime)

    async def transfer_ticket_task_async(
        self,
        request: main_models.TransferTicketTaskRequest,
    ) -> main_models.TransferTicketTaskResponse:
        runtime = RuntimeOptions()
        return await self.transfer_ticket_task_with_options_async(request, runtime)

    def unmute_call_with_options(
        self,
        request: main_models.UnmuteCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnmuteCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnmuteCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnmuteCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def unmute_call_with_options_async(
        self,
        request: main_models.UnmuteCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnmuteCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnmuteCall',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnmuteCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unmute_call(
        self,
        request: main_models.UnmuteCallRequest,
    ) -> main_models.UnmuteCallResponse:
        runtime = RuntimeOptions()
        return self.unmute_call_with_options(request, runtime)

    async def unmute_call_async(
        self,
        request: main_models.UnmuteCallRequest,
    ) -> main_models.UnmuteCallResponse:
        runtime = RuntimeOptions()
        return await self.unmute_call_with_options_async(request, runtime)

    def unregister_device_with_options(
        self,
        request: main_models.UnregisterDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnregisterDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnregisterDevice',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnregisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unregister_device_with_options_async(
        self,
        request: main_models.UnregisterDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnregisterDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnregisterDevice',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnregisterDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unregister_device(
        self,
        request: main_models.UnregisterDeviceRequest,
    ) -> main_models.UnregisterDeviceResponse:
        runtime = RuntimeOptions()
        return self.unregister_device_with_options(request, runtime)

    async def unregister_device_async(
        self,
        request: main_models.UnregisterDeviceRequest,
    ) -> main_models.UnregisterDeviceResponse:
        runtime = RuntimeOptions()
        return await self.unregister_device_with_options_async(request, runtime)

    def update_call_summary_with_options(
        self,
        request: main_models.UpdateCallSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCallSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCallSummary',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCallSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_call_summary_with_options_async(
        self,
        request: main_models.UpdateCallSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCallSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCallSummary',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCallSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_call_summary(
        self,
        request: main_models.UpdateCallSummaryRequest,
    ) -> main_models.UpdateCallSummaryResponse:
        runtime = RuntimeOptions()
        return self.update_call_summary_with_options(request, runtime)

    async def update_call_summary_async(
        self,
        request: main_models.UpdateCallSummaryRequest,
    ) -> main_models.UpdateCallSummaryResponse:
        runtime = RuntimeOptions()
        return await self.update_call_summary_with_options_async(request, runtime)

    def update_campaign_with_options(
        self,
        request: main_models.UpdateCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_campaign_with_options_async(
        self,
        request: main_models.UpdateCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCampaign',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_campaign(
        self,
        request: main_models.UpdateCampaignRequest,
    ) -> main_models.UpdateCampaignResponse:
        runtime = RuntimeOptions()
        return self.update_campaign_with_options(request, runtime)

    async def update_campaign_async(
        self,
        request: main_models.UpdateCampaignRequest,
    ) -> main_models.UpdateCampaignResponse:
        runtime = RuntimeOptions()
        return await self.update_campaign_with_options_async(request, runtime)

    def update_chat_routing_profile_with_options(
        self,
        request: main_models.UpdateChatRoutingProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatRoutingProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.routing_profiles):
            query['RoutingProfiles'] = request.routing_profiles
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatRoutingProfile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatRoutingProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_routing_profile_with_options_async(
        self,
        request: main_models.UpdateChatRoutingProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatRoutingProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.routing_profiles):
            query['RoutingProfiles'] = request.routing_profiles
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatRoutingProfile',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatRoutingProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_routing_profile(
        self,
        request: main_models.UpdateChatRoutingProfileRequest,
    ) -> main_models.UpdateChatRoutingProfileResponse:
        runtime = RuntimeOptions()
        return self.update_chat_routing_profile_with_options(request, runtime)

    async def update_chat_routing_profile_async(
        self,
        request: main_models.UpdateChatRoutingProfileRequest,
    ) -> main_models.UpdateChatRoutingProfileResponse:
        runtime = RuntimeOptions()
        return await self.update_chat_routing_profile_with_options_async(request, runtime)

    def update_config_items_with_options(
        self,
        request: main_models.UpdateConfigItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_items):
            query['ConfigItems'] = request.config_items
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigItems',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_items_with_options_async(
        self,
        request: main_models.UpdateConfigItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_items):
            query['ConfigItems'] = request.config_items
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigItems',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_items(
        self,
        request: main_models.UpdateConfigItemsRequest,
    ) -> main_models.UpdateConfigItemsResponse:
        runtime = RuntimeOptions()
        return self.update_config_items_with_options(request, runtime)

    async def update_config_items_async(
        self,
        request: main_models.UpdateConfigItemsRequest,
    ) -> main_models.UpdateConfigItemsResponse:
        runtime = RuntimeOptions()
        return await self.update_config_items_with_options_async(request, runtime)

    def update_schema_property_with_options(
        self,
        tmp_req: main_models.UpdateSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSchemaPropertyResponse:
        tmp_req.validate()
        request = main_models.UpdateSchemaPropertyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.property):
            request.property_shrink = Utils.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_shrink):
            body['Property'] = request.property_shrink
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schema_property_with_options_async(
        self,
        tmp_req: main_models.UpdateSchemaPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSchemaPropertyResponse:
        tmp_req.validate()
        request = main_models.UpdateSchemaPropertyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.property):
            request.property_shrink = Utils.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.property_shrink):
            body['Property'] = request.property_shrink
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSchemaProperty',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schema_property(
        self,
        request: main_models.UpdateSchemaPropertyRequest,
    ) -> main_models.UpdateSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return self.update_schema_property_with_options(request, runtime)

    async def update_schema_property_async(
        self,
        request: main_models.UpdateSchemaPropertyRequest,
    ) -> main_models.UpdateSchemaPropertyResponse:
        runtime = RuntimeOptions()
        return await self.update_schema_property_with_options_async(request, runtime)

    def update_subscription_with_options(
        self,
        request: main_models.UpdateSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point):
            query['AccessPoint'] = request.access_point
        if not DaraCore.is_null(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not DaraCore.is_null(request.default_topic):
            query['DefaultTopic'] = request.default_topic
        if not DaraCore.is_null(request.event_subscriptions_json):
            query['EventSubscriptionsJson'] = request.event_subscriptions_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mq_instance_id):
            query['MqInstanceId'] = request.mq_instance_id
        if not DaraCore.is_null(request.mq_type):
            query['MqType'] = request.mq_type
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.producer_id):
            query['ProducerId'] = request.producer_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        request: main_models.UpdateSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point):
            query['AccessPoint'] = request.access_point
        if not DaraCore.is_null(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not DaraCore.is_null(request.default_topic):
            query['DefaultTopic'] = request.default_topic
        if not DaraCore.is_null(request.event_subscriptions_json):
            query['EventSubscriptionsJson'] = request.event_subscriptions_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mq_instance_id):
            query['MqInstanceId'] = request.mq_instance_id
        if not DaraCore.is_null(request.mq_type):
            query['MqType'] = request.mq_type
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.producer_id):
            query['ProducerId'] = request.producer_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription(
        self,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.update_subscription_with_options(request, runtime)

    async def update_subscription_async(
        self,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_subscription_with_options_async(request, runtime)

    def update_ticket_with_options(
        self,
        request: main_models.UpdateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ticket_with_options_async(
        self,
        request: main_models.UpdateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context):
            query['Context'] = request.context
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ticket(
        self,
        request: main_models.UpdateTicketRequest,
    ) -> main_models.UpdateTicketResponse:
        runtime = RuntimeOptions()
        return self.update_ticket_with_options(request, runtime)

    async def update_ticket_async(
        self,
        request: main_models.UpdateTicketRequest,
    ) -> main_models.UpdateTicketResponse:
        runtime = RuntimeOptions()
        return await self.update_ticket_with_options_async(request, runtime)

    def withdraw_ticket_with_options(
        self,
        request: main_models.WithdrawTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_ticket_with_options_async(
        self,
        request: main_models.WithdrawTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawTicket',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_ticket(
        self,
        request: main_models.WithdrawTicketRequest,
    ) -> main_models.WithdrawTicketResponse:
        runtime = RuntimeOptions()
        return self.withdraw_ticket_with_options(request, runtime)

    async def withdraw_ticket_async(
        self,
        request: main_models.WithdrawTicketRequest,
    ) -> main_models.WithdrawTicketResponse:
        runtime = RuntimeOptions()
        return await self.withdraw_ticket_with_options_async(request, runtime)
