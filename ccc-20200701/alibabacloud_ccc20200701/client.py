# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ccc20200701 import models as ccc20200701_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abort_campaign_with_options(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AbortCampaignResponse:
        """
        @summary 废弃预测式外呼活动
        
        @param request: AbortCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AbortCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_campaign_with_options_async(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AbortCampaignResponse:
        """
        @summary 废弃预测式外呼活动
        
        @param request: AbortCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AbortCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_campaign(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
    ) -> ccc20200701_models.AbortCampaignResponse:
        """
        @summary 废弃预测式外呼活动
        
        @param request: AbortCampaignRequest
        @return: AbortCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abort_campaign_with_options(request, runtime)

    async def abort_campaign_async(
        self,
        request: ccc20200701_models.AbortCampaignRequest,
    ) -> ccc20200701_models.AbortCampaignResponse:
        """
        @summary 废弃预测式外呼活动
        
        @param request: AbortCampaignRequest
        @return: AbortCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.abort_campaign_with_options_async(request, runtime)

    def accept_chat_with_options(
        self,
        request: ccc20200701_models.AcceptChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AcceptChatResponse:
        """
        @param request: AcceptChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptChatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptChat',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AcceptChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_chat_with_options_async(
        self,
        request: ccc20200701_models.AcceptChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AcceptChatResponse:
        """
        @param request: AcceptChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptChatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptChat',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AcceptChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_chat(
        self,
        request: ccc20200701_models.AcceptChatRequest,
    ) -> ccc20200701_models.AcceptChatResponse:
        """
        @param request: AcceptChatRequest
        @return: AcceptChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_chat_with_options(request, runtime)

    async def accept_chat_async(
        self,
        request: ccc20200701_models.AcceptChatRequest,
    ) -> ccc20200701_models.AcceptChatResponse:
        """
        @param request: AcceptChatRequest
        @return: AcceptChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.accept_chat_with_options_async(request, runtime)

    def add_blacklist_call_tagging_with_options(
        self,
        request: ccc20200701_models.AddBlacklistCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: AddBlacklistCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBlacklistCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlacklistCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddBlacklistCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_blacklist_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.AddBlacklistCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: AddBlacklistCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBlacklistCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlacklistCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddBlacklistCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_blacklist_call_tagging(
        self,
        request: ccc20200701_models.AddBlacklistCallTaggingRequest,
    ) -> ccc20200701_models.AddBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: AddBlacklistCallTaggingRequest
        @return: AddBlacklistCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_blacklist_call_tagging_with_options(request, runtime)

    async def add_blacklist_call_tagging_async(
        self,
        request: ccc20200701_models.AddBlacklistCallTaggingRequest,
    ) -> ccc20200701_models.AddBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: AddBlacklistCallTaggingRequest
        @return: AddBlacklistCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_blacklist_call_tagging_with_options_async(request, runtime)

    def add_cases_with_options(
        self,
        tmp_req: ccc20200701_models.AddCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddCasesResponse:
        """
        @summary 追加联系人
        
        @param tmp_req: AddCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.AddCasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.case_list):
            request.case_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cases_with_options_async(
        self,
        tmp_req: ccc20200701_models.AddCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddCasesResponse:
        """
        @summary 追加联系人
        
        @param tmp_req: AddCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.AddCasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.case_list):
            request.case_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cases(
        self,
        request: ccc20200701_models.AddCasesRequest,
    ) -> ccc20200701_models.AddCasesResponse:
        """
        @summary 追加联系人
        
        @param request: AddCasesRequest
        @return: AddCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_cases_with_options(request, runtime)

    async def add_cases_async(
        self,
        request: ccc20200701_models.AddCasesRequest,
    ) -> ccc20200701_models.AddCasesResponse:
        """
        @summary 追加联系人
        
        @param request: AddCasesRequest
        @return: AddCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_cases_with_options_async(request, runtime)

    def add_numbers_to_skill_group_with_options(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        """
        @param request: AddNumbersToSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddNumbersToSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inst_number_group_id_list):
            query['InstNumberGroupIdList'] = request.inst_number_group_id_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNumbersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddNumbersToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_numbers_to_skill_group_with_options_async(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        """
        @param request: AddNumbersToSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddNumbersToSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inst_number_group_id_list):
            query['InstNumberGroupIdList'] = request.inst_number_group_id_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNumbersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddNumbersToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_numbers_to_skill_group(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        """
        @param request: AddNumbersToSkillGroupRequest
        @return: AddNumbersToSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_numbers_to_skill_group_with_options(request, runtime)

    async def add_numbers_to_skill_group_async(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        """
        @param request: AddNumbersToSkillGroupRequest
        @return: AddNumbersToSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_numbers_to_skill_group_with_options_async(request, runtime)

    def add_personal_numbers_to_user_with_options(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        """
        @param request: AddPersonalNumbersToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPersonalNumbersToUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPersonalNumbersToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPersonalNumbersToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_personal_numbers_to_user_with_options_async(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        """
        @param request: AddPersonalNumbersToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPersonalNumbersToUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPersonalNumbersToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPersonalNumbersToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_personal_numbers_to_user(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        """
        @param request: AddPersonalNumbersToUserRequest
        @return: AddPersonalNumbersToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_personal_numbers_to_user_with_options(request, runtime)

    async def add_personal_numbers_to_user_async(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        """
        @param request: AddPersonalNumbersToUserRequest
        @return: AddPersonalNumbersToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_personal_numbers_to_user_with_options_async(request, runtime)

    def add_phone_number_to_skill_groups_with_options(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        """
        @param request: AddPhoneNumberToSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPhoneNumberToSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumberToSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumberToSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_phone_number_to_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        """
        @param request: AddPhoneNumberToSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPhoneNumberToSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumberToSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumberToSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_phone_number_to_skill_groups(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        """
        @param request: AddPhoneNumberToSkillGroupsRequest
        @return: AddPhoneNumberToSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_phone_number_to_skill_groups_with_options(request, runtime)

    async def add_phone_number_to_skill_groups_async(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        """
        @param request: AddPhoneNumberToSkillGroupsRequest
        @return: AddPhoneNumberToSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_number_to_skill_groups_with_options_async(request, runtime)

    def add_phone_numbers_with_options(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        """
        @param request: AddPhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_group_id):
            query['NumberGroupId'] = request.number_group_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        """
        @param request: AddPhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_group_id):
            query['NumberGroupId'] = request.number_group_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_phone_numbers(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        """
        @param request: AddPhoneNumbersRequest
        @return: AddPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_phone_numbers_with_options(request, runtime)

    async def add_phone_numbers_async(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        """
        @param request: AddPhoneNumbersRequest
        @return: AddPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_numbers_with_options_async(request, runtime)

    def add_schema_property_with_options(
        self,
        tmp_req: ccc20200701_models.AddSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSchemaPropertyResponse:
        """
        @param tmp_req: AddSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSchemaPropertyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.AddSchemaPropertyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.property):
            request.property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_shrink):
            body['Property'] = request.property_shrink
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_schema_property_with_options_async(
        self,
        tmp_req: ccc20200701_models.AddSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSchemaPropertyResponse:
        """
        @param tmp_req: AddSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSchemaPropertyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.AddSchemaPropertyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.property):
            request.property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_shrink):
            body['Property'] = request.property_shrink
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_schema_property(
        self,
        request: ccc20200701_models.AddSchemaPropertyRequest,
    ) -> ccc20200701_models.AddSchemaPropertyResponse:
        """
        @param request: AddSchemaPropertyRequest
        @return: AddSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_schema_property_with_options(request, runtime)

    async def add_schema_property_async(
        self,
        request: ccc20200701_models.AddSchemaPropertyRequest,
    ) -> ccc20200701_models.AddSchemaPropertyResponse:
        """
        @param request: AddSchemaPropertyRequest
        @return: AddSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_schema_property_with_options_async(request, runtime)

    def add_skill_groups_to_user_with_options(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        """
        @param request: AddSkillGroupsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSkillGroupsToUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSkillGroupsToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSkillGroupsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_skill_groups_to_user_with_options_async(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        """
        @param request: AddSkillGroupsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSkillGroupsToUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSkillGroupsToUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSkillGroupsToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_skill_groups_to_user(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        """
        @param request: AddSkillGroupsToUserRequest
        @return: AddSkillGroupsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_skill_groups_to_user_with_options(request, runtime)

    async def add_skill_groups_to_user_async(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        """
        @param request: AddSkillGroupsToUserRequest
        @return: AddSkillGroupsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_skill_groups_to_user_with_options_async(request, runtime)

    def add_users_to_skill_group_with_options(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        """
        @param request: AddUsersToSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.user_skill_level_list):
            query['UserSkillLevelList'] = request.user_skill_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddUsersToSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_to_skill_group_with_options_async(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        """
        @param request: AddUsersToSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.user_skill_level_list):
            query['UserSkillLevelList'] = request.user_skill_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AddUsersToSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users_to_skill_group(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        """
        @param request: AddUsersToSkillGroupRequest
        @return: AddUsersToSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_skill_group_with_options(request, runtime)

    async def add_users_to_skill_group_async(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        """
        @param request: AddUsersToSkillGroupRequest
        @return: AddUsersToSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_users_to_skill_group_with_options_async(request, runtime)

    def analyze_conversation_with_options(
        self,
        request: ccc20200701_models.AnalyzeConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnalyzeConversationResponse:
        """
        @param request: AnalyzeConversationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeConversationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.field_list_json):
            query['FieldListJson'] = request.field_list_json
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_list_json):
            query['TaskListJson'] = request.task_list_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeConversation',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AnalyzeConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_conversation_with_options_async(
        self,
        request: ccc20200701_models.AnalyzeConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnalyzeConversationResponse:
        """
        @param request: AnalyzeConversationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeConversationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.field_list_json):
            query['FieldListJson'] = request.field_list_json
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_list_json):
            query['TaskListJson'] = request.task_list_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeConversation',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AnalyzeConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_conversation(
        self,
        request: ccc20200701_models.AnalyzeConversationRequest,
    ) -> ccc20200701_models.AnalyzeConversationResponse:
        """
        @param request: AnalyzeConversationRequest
        @return: AnalyzeConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.analyze_conversation_with_options(request, runtime)

    async def analyze_conversation_async(
        self,
        request: ccc20200701_models.AnalyzeConversationRequest,
    ) -> ccc20200701_models.AnalyzeConversationResponse:
        """
        @param request: AnalyzeConversationRequest
        @return: AnalyzeConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.analyze_conversation_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: ccc20200701_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnswerCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnswerCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AnswerCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: ccc20200701_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnswerCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnswerCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AnswerCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def answer_call(
        self,
        request: ccc20200701_models.AnswerCallRequest,
    ) -> ccc20200701_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @return: AnswerCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: ccc20200701_models.AnswerCallRequest,
    ) -> ccc20200701_models.AnswerCallResponse:
        """
        @param request: AnswerCallRequest
        @return: AnswerCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def append_cases_with_options(
        self,
        tmp_req: ccc20200701_models.AppendCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AppendCasesResponse:
        """
        @summary 追加联系人
        
        @param tmp_req: AppendCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppendCasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.AppendCasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppendCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AppendCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def append_cases_with_options_async(
        self,
        tmp_req: ccc20200701_models.AppendCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AppendCasesResponse:
        """
        @summary 追加联系人
        
        @param tmp_req: AppendCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppendCasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.AppendCasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppendCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AppendCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def append_cases(
        self,
        request: ccc20200701_models.AppendCasesRequest,
    ) -> ccc20200701_models.AppendCasesResponse:
        """
        @summary 追加联系人
        
        @param request: AppendCasesRequest
        @return: AppendCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.append_cases_with_options(request, runtime)

    async def append_cases_async(
        self,
        request: ccc20200701_models.AppendCasesRequest,
    ) -> ccc20200701_models.AppendCasesResponse:
        """
        @summary 追加联系人
        
        @param request: AppendCasesRequest
        @return: AppendCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.append_cases_with_options_async(request, runtime)

    def assign_users_with_options(
        self,
        request: ccc20200701_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AssignUsersResponse:
        """
        @deprecated OpenAPI AssignUsers is deprecated, please use CCC::2020-07-01::ImportRamUsers instead.
        
        @param request: AssignUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignUsersResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AssignUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_users_with_options_async(
        self,
        request: ccc20200701_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AssignUsersResponse:
        """
        @deprecated OpenAPI AssignUsers is deprecated, please use CCC::2020-07-01::ImportRamUsers instead.
        
        @param request: AssignUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignUsersResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.AssignUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_users(
        self,
        request: ccc20200701_models.AssignUsersRequest,
    ) -> ccc20200701_models.AssignUsersResponse:
        """
        @deprecated OpenAPI AssignUsers is deprecated, please use CCC::2020-07-01::ImportRamUsers instead.
        
        @param request: AssignUsersRequest
        @return: AssignUsersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_users_with_options(request, runtime)

    async def assign_users_async(
        self,
        request: ccc20200701_models.AssignUsersRequest,
    ) -> ccc20200701_models.AssignUsersResponse:
        """
        @deprecated OpenAPI AssignUsers is deprecated, please use CCC::2020-07-01::ImportRamUsers instead.
        
        @param request: AssignUsersRequest
        @return: AssignUsersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_users_with_options_async(request, runtime)

    def barge_in_call_with_options(
        self,
        request: ccc20200701_models.BargeInCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BargeInCallResponse:
        """
        @param request: BargeInCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BargeInCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.barged_user_id):
            query['BargedUserId'] = request.barged_user_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BargeInCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BargeInCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def barge_in_call_with_options_async(
        self,
        request: ccc20200701_models.BargeInCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BargeInCallResponse:
        """
        @param request: BargeInCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BargeInCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.barged_user_id):
            query['BargedUserId'] = request.barged_user_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BargeInCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BargeInCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def barge_in_call(
        self,
        request: ccc20200701_models.BargeInCallRequest,
    ) -> ccc20200701_models.BargeInCallResponse:
        """
        @param request: BargeInCallRequest
        @return: BargeInCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.barge_in_call_with_options(request, runtime)

    async def barge_in_call_async(
        self,
        request: ccc20200701_models.BargeInCallRequest,
    ) -> ccc20200701_models.BargeInCallResponse:
        """
        @param request: BargeInCallRequest
        @return: BargeInCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.barge_in_call_with_options_async(request, runtime)

    def blind_transfer_with_options(
        self,
        request: ccc20200701_models.BlindTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BlindTransferResponse:
        """
        @param request: BlindTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BlindTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not UtilClient.is_unset(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not UtilClient.is_unset(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not UtilClient.is_unset(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.transferee):
            query['Transferee'] = request.transferee
        if not UtilClient.is_unset(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not UtilClient.is_unset(request.transferor):
            query['Transferor'] = request.transferor
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlindTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BlindTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def blind_transfer_with_options_async(
        self,
        request: ccc20200701_models.BlindTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BlindTransferResponse:
        """
        @param request: BlindTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BlindTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not UtilClient.is_unset(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not UtilClient.is_unset(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not UtilClient.is_unset(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.transferee):
            query['Transferee'] = request.transferee
        if not UtilClient.is_unset(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not UtilClient.is_unset(request.transferor):
            query['Transferor'] = request.transferor
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlindTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BlindTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def blind_transfer(
        self,
        request: ccc20200701_models.BlindTransferRequest,
    ) -> ccc20200701_models.BlindTransferResponse:
        """
        @param request: BlindTransferRequest
        @return: BlindTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.blind_transfer_with_options(request, runtime)

    async def blind_transfer_async(
        self,
        request: ccc20200701_models.BlindTransferRequest,
    ) -> ccc20200701_models.BlindTransferResponse:
        """
        @param request: BlindTransferRequest
        @return: BlindTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.blind_transfer_with_options_async(request, runtime)

    def bridge_rtc_call_with_options(
        self,
        request: ccc20200701_models.BridgeRtcCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BridgeRtcCallResponse:
        """
        @param request: BridgeRtcCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BridgeRtcCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.service_provider):
            query['ServiceProvider'] = request.service_provider
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.video_enabled):
            query['VideoEnabled'] = request.video_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BridgeRtcCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BridgeRtcCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def bridge_rtc_call_with_options_async(
        self,
        request: ccc20200701_models.BridgeRtcCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BridgeRtcCallResponse:
        """
        @param request: BridgeRtcCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BridgeRtcCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.service_provider):
            query['ServiceProvider'] = request.service_provider
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.video_enabled):
            query['VideoEnabled'] = request.video_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BridgeRtcCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.BridgeRtcCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bridge_rtc_call(
        self,
        request: ccc20200701_models.BridgeRtcCallRequest,
    ) -> ccc20200701_models.BridgeRtcCallResponse:
        """
        @param request: BridgeRtcCallRequest
        @return: BridgeRtcCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bridge_rtc_call_with_options(request, runtime)

    async def bridge_rtc_call_async(
        self,
        request: ccc20200701_models.BridgeRtcCallRequest,
    ) -> ccc20200701_models.BridgeRtcCallResponse:
        """
        @param request: BridgeRtcCallRequest
        @return: BridgeRtcCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bridge_rtc_call_with_options_async(request, runtime)

    def cancel_attended_transfer_with_options(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        """
        @param request: CancelAttendedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAttendedTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CancelAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        """
        @param request: CancelAttendedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAttendedTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CancelAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_attended_transfer(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        """
        @param request: CancelAttendedTransferRequest
        @return: CancelAttendedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_attended_transfer_with_options(request, runtime)

    async def cancel_attended_transfer_async(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        """
        @param request: CancelAttendedTransferRequest
        @return: CancelAttendedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_attended_transfer_with_options_async(request, runtime)

    def change_visibility_with_options(
        self,
        request: ccc20200701_models.ChangeVisibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeVisibilityResponse:
        """
        @param request: ChangeVisibilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeVisibilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invisible):
            query['Invisible'] = request.invisible
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeVisibility',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_visibility_with_options_async(
        self,
        request: ccc20200701_models.ChangeVisibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeVisibilityResponse:
        """
        @param request: ChangeVisibilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeVisibilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invisible):
            query['Invisible'] = request.invisible
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeVisibility',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeVisibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_visibility(
        self,
        request: ccc20200701_models.ChangeVisibilityRequest,
    ) -> ccc20200701_models.ChangeVisibilityResponse:
        """
        @param request: ChangeVisibilityRequest
        @return: ChangeVisibilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_visibility_with_options(request, runtime)

    async def change_visibility_async(
        self,
        request: ccc20200701_models.ChangeVisibilityRequest,
    ) -> ccc20200701_models.ChangeVisibilityResponse:
        """
        @param request: ChangeVisibilityRequest
        @return: ChangeVisibilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_visibility_with_options_async(request, runtime)

    def change_work_mode_with_options(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        """
        @param request: ChangeWorkModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeWorkModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeWorkMode',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeWorkModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_work_mode_with_options_async(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        """
        @param request: ChangeWorkModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeWorkModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeWorkMode',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeWorkModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_work_mode(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        """
        @param request: ChangeWorkModeRequest
        @return: ChangeWorkModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_work_mode_with_options(request, runtime)

    async def change_work_mode_async(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        """
        @param request: ChangeWorkModeRequest
        @return: ChangeWorkModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_work_mode_with_options_async(request, runtime)

    def claim_chat_with_options(
        self,
        request: ccc20200701_models.ClaimChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ClaimChatResponse:
        """
        @param request: ClaimChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClaimChatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClaimChat',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ClaimChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def claim_chat_with_options_async(
        self,
        request: ccc20200701_models.ClaimChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ClaimChatResponse:
        """
        @param request: ClaimChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClaimChatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClaimChat',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ClaimChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def claim_chat(
        self,
        request: ccc20200701_models.ClaimChatRequest,
    ) -> ccc20200701_models.ClaimChatResponse:
        """
        @param request: ClaimChatRequest
        @return: ClaimChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.claim_chat_with_options(request, runtime)

    async def claim_chat_async(
        self,
        request: ccc20200701_models.ClaimChatRequest,
    ) -> ccc20200701_models.ClaimChatResponse:
        """
        @param request: ClaimChatRequest
        @return: ClaimChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.claim_chat_with_options_async(request, runtime)

    def coach_call_with_options(
        self,
        request: ccc20200701_models.CoachCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CoachCallResponse:
        """
        @param request: CoachCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CoachCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coached_user_id):
            query['CoachedUserId'] = request.coached_user_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CoachCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CoachCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def coach_call_with_options_async(
        self,
        request: ccc20200701_models.CoachCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CoachCallResponse:
        """
        @param request: CoachCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CoachCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coached_user_id):
            query['CoachedUserId'] = request.coached_user_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CoachCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CoachCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def coach_call(
        self,
        request: ccc20200701_models.CoachCallRequest,
    ) -> ccc20200701_models.CoachCallResponse:
        """
        @param request: CoachCallRequest
        @return: CoachCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.coach_call_with_options(request, runtime)

    async def coach_call_async(
        self,
        request: ccc20200701_models.CoachCallRequest,
    ) -> ccc20200701_models.CoachCallResponse:
        """
        @param request: CoachCallRequest
        @return: CoachCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.coach_call_with_options_async(request, runtime)

    def commit_contact_flow_with_options(
        self,
        request: ccc20200701_models.CommitContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CommitContactFlowResponse:
        """
        @param request: CommitContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommitContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CommitContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_contact_flow_with_options_async(
        self,
        request: ccc20200701_models.CommitContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CommitContactFlowResponse:
        """
        @param request: CommitContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommitContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CommitContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_contact_flow(
        self,
        request: ccc20200701_models.CommitContactFlowRequest,
    ) -> ccc20200701_models.CommitContactFlowResponse:
        """
        @param request: CommitContactFlowRequest
        @return: CommitContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.commit_contact_flow_with_options(request, runtime)

    async def commit_contact_flow_async(
        self,
        request: ccc20200701_models.CommitContactFlowRequest,
    ) -> ccc20200701_models.CommitContactFlowResponse:
        """
        @param request: CommitContactFlowRequest
        @return: CommitContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.commit_contact_flow_with_options_async(request, runtime)

    def complete_attended_transfer_with_options(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        """
        @param request: CompleteAttendedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteAttendedTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CompleteAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        """
        @param request: CompleteAttendedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteAttendedTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CompleteAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_attended_transfer(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        """
        @param request: CompleteAttendedTransferRequest
        @return: CompleteAttendedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.complete_attended_transfer_with_options(request, runtime)

    async def complete_attended_transfer_async(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        """
        @param request: CompleteAttendedTransferRequest
        @return: CompleteAttendedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.complete_attended_transfer_with_options_async(request, runtime)

    def create_audio_file_with_options(
        self,
        request: ccc20200701_models.CreateAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateAudioFileResponse:
        """
        @param request: CreateAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_audio_file_with_options_async(
        self,
        request: ccc20200701_models.CreateAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateAudioFileResponse:
        """
        @param request: CreateAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_audio_file(
        self,
        request: ccc20200701_models.CreateAudioFileRequest,
    ) -> ccc20200701_models.CreateAudioFileResponse:
        """
        @param request: CreateAudioFileRequest
        @return: CreateAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_audio_file_with_options(request, runtime)

    async def create_audio_file_async(
        self,
        request: ccc20200701_models.CreateAudioFileRequest,
    ) -> ccc20200701_models.CreateAudioFileResponse:
        """
        @param request: CreateAudioFileRequest
        @return: CreateAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_audio_file_with_options_async(request, runtime)

    def create_call_tags_with_options(
        self,
        request: ccc20200701_models.CreateCallTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCallTagsResponse:
        """
        @summary 批量创建号码标签
        
        @param request: CreateCallTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCallTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCallTags',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCallTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_call_tags_with_options_async(
        self,
        request: ccc20200701_models.CreateCallTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCallTagsResponse:
        """
        @summary 批量创建号码标签
        
        @param request: CreateCallTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCallTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCallTags',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCallTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_call_tags(
        self,
        request: ccc20200701_models.CreateCallTagsRequest,
    ) -> ccc20200701_models.CreateCallTagsResponse:
        """
        @summary 批量创建号码标签
        
        @param request: CreateCallTagsRequest
        @return: CreateCallTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_call_tags_with_options(request, runtime)

    async def create_call_tags_async(
        self,
        request: ccc20200701_models.CreateCallTagsRequest,
    ) -> ccc20200701_models.CreateCallTagsResponse:
        """
        @summary 批量创建号码标签
        
        @param request: CreateCallTagsRequest
        @return: CreateCallTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_call_tags_with_options_async(request, runtime)

    def create_campaign_with_options(
        self,
        tmp_req: ccc20200701_models.CreateCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCampaignResponse:
        """
        @summary 创建预测式外呼活动
        
        @param tmp_req: CreateCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCampaignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.CreateCampaignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.case_list):
            request.case_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        if not UtilClient.is_unset(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not UtilClient.is_unset(request.case_file_key):
            query['CaseFileKey'] = request.case_file_key
        if not UtilClient.is_unset(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.executing_until_timeout):
            query['ExecutingUntilTimeout'] = request.executing_until_timeout
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_attempt_count):
            query['MaxAttemptCount'] = request.max_attempt_count
        if not UtilClient.is_unset(request.min_attempt_interval):
            query['MinAttemptInterval'] = request.min_attempt_interval
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.queue_id):
            query['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.simulation):
            query['Simulation'] = request.simulation
        if not UtilClient.is_unset(request.simulation_parameters):
            query['SimulationParameters'] = request.simulation_parameters
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        if not UtilClient.is_unset(request.strategy_type):
            query['StrategyType'] = request.strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_campaign_with_options_async(
        self,
        tmp_req: ccc20200701_models.CreateCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCampaignResponse:
        """
        @summary 创建预测式外呼活动
        
        @param tmp_req: CreateCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCampaignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.CreateCampaignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.case_list):
            request.case_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        if not UtilClient.is_unset(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not UtilClient.is_unset(request.case_file_key):
            query['CaseFileKey'] = request.case_file_key
        if not UtilClient.is_unset(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.executing_until_timeout):
            query['ExecutingUntilTimeout'] = request.executing_until_timeout
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_attempt_count):
            query['MaxAttemptCount'] = request.max_attempt_count
        if not UtilClient.is_unset(request.min_attempt_interval):
            query['MinAttemptInterval'] = request.min_attempt_interval
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.queue_id):
            query['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.simulation):
            query['Simulation'] = request.simulation
        if not UtilClient.is_unset(request.simulation_parameters):
            query['SimulationParameters'] = request.simulation_parameters
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        if not UtilClient.is_unset(request.strategy_type):
            query['StrategyType'] = request.strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_campaign(
        self,
        request: ccc20200701_models.CreateCampaignRequest,
    ) -> ccc20200701_models.CreateCampaignResponse:
        """
        @summary 创建预测式外呼活动
        
        @param request: CreateCampaignRequest
        @return: CreateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_campaign_with_options(request, runtime)

    async def create_campaign_async(
        self,
        request: ccc20200701_models.CreateCampaignRequest,
    ) -> ccc20200701_models.CreateCampaignResponse:
        """
        @summary 创建预测式外呼活动
        
        @param request: CreateCampaignRequest
        @return: CreateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_campaign_with_options_async(request, runtime)

    def create_contact_flow_with_options(
        self,
        request: ccc20200701_models.CreateContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateContactFlowResponse:
        """
        @param request: CreateContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_contact_flow_with_options_async(
        self,
        request: ccc20200701_models.CreateContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateContactFlowResponse:
        """
        @param request: CreateContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_contact_flow(
        self,
        request: ccc20200701_models.CreateContactFlowRequest,
    ) -> ccc20200701_models.CreateContactFlowResponse:
        """
        @param request: CreateContactFlowRequest
        @return: CreateContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_contact_flow_with_options(request, runtime)

    async def create_contact_flow_async(
        self,
        request: ccc20200701_models.CreateContactFlowRequest,
    ) -> ccc20200701_models.CreateContactFlowResponse:
        """
        @param request: CreateContactFlowRequest
        @return: CreateContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_contact_flow_with_options_async(request, runtime)

    def create_custom_call_tagging_with_options(
        self,
        request: ccc20200701_models.CreateCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCustomCallTaggingResponse:
        """
        @deprecated OpenAPI CreateCustomCallTagging is deprecated, please use CCC::2020-07-01::CreateCustomCallTaggings instead.
        
        @summary 创建呼入控制号码
        
        @param request: CreateCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_number_list):
            query['CustomNumberList'] = request.custom_number_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.CreateCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateCustomCallTaggingResponse:
        """
        @deprecated OpenAPI CreateCustomCallTagging is deprecated, please use CCC::2020-07-01::CreateCustomCallTaggings instead.
        
        @summary 创建呼入控制号码
        
        @param request: CreateCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_number_list):
            query['CustomNumberList'] = request.custom_number_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_call_tagging(
        self,
        request: ccc20200701_models.CreateCustomCallTaggingRequest,
    ) -> ccc20200701_models.CreateCustomCallTaggingResponse:
        """
        @deprecated OpenAPI CreateCustomCallTagging is deprecated, please use CCC::2020-07-01::CreateCustomCallTaggings instead.
        
        @summary 创建呼入控制号码
        
        @param request: CreateCustomCallTaggingRequest
        @return: CreateCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_call_tagging_with_options(request, runtime)

    async def create_custom_call_tagging_async(
        self,
        request: ccc20200701_models.CreateCustomCallTaggingRequest,
    ) -> ccc20200701_models.CreateCustomCallTaggingResponse:
        """
        @deprecated OpenAPI CreateCustomCallTagging is deprecated, please use CCC::2020-07-01::CreateCustomCallTaggings instead.
        
        @summary 创建呼入控制号码
        
        @param request: CreateCustomCallTaggingRequest
        @return: CreateCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_call_tagging_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_ram_id_list):
            query['AdminRamIdList'] = request.admin_ram_id_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_ram_id_list):
            query['AdminRamIdList'] = request.admin_ram_id_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
    ) -> ccc20200701_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
    ) -> ccc20200701_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_schema_with_options(
        self,
        tmp_req: ccc20200701_models.CreateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSchemaResponse:
        """
        @param tmp_req: CreateSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchemaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.CreateSchemaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchema',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schema_with_options_async(
        self,
        tmp_req: ccc20200701_models.CreateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSchemaResponse:
        """
        @param tmp_req: CreateSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchemaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.CreateSchemaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchema',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schema(
        self,
        request: ccc20200701_models.CreateSchemaRequest,
    ) -> ccc20200701_models.CreateSchemaResponse:
        """
        @param request: CreateSchemaRequest
        @return: CreateSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_schema_with_options(request, runtime)

    async def create_schema_async(
        self,
        request: ccc20200701_models.CreateSchemaRequest,
    ) -> ccc20200701_models.CreateSchemaResponse:
        """
        @param request: CreateSchemaRequest
        @return: CreateSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_schema_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_group(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @return: CreateSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        """
        @param request: CreateSkillGroupRequest
        @return: CreateSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ccc20200701_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateUserResponse:
        """
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.display_id):
            query['DisplayId'] = request.display_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.login_name):
            query['LoginName'] = request.login_name
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.nickname):
            query['Nickname'] = request.nickname
        if not UtilClient.is_unset(request.reset_password):
            query['ResetPassword'] = request.reset_password
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ccc20200701_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateUserResponse:
        """
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.display_id):
            query['DisplayId'] = request.display_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.login_name):
            query['LoginName'] = request.login_name
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.nickname):
            query['Nickname'] = request.nickname
        if not UtilClient.is_unset(request.reset_password):
            query['ResetPassword'] = request.reset_password
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: ccc20200701_models.CreateUserRequest,
    ) -> ccc20200701_models.CreateUserResponse:
        """
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ccc20200701_models.CreateUserRequest,
    ) -> ccc20200701_models.CreateUserResponse:
        """
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def delete_audio_file_with_options(
        self,
        request: ccc20200701_models.DeleteAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteAudioFileResponse:
        """
        @param request: DeleteAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_audio_file_with_options_async(
        self,
        request: ccc20200701_models.DeleteAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteAudioFileResponse:
        """
        @param request: DeleteAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_audio_file(
        self,
        request: ccc20200701_models.DeleteAudioFileRequest,
    ) -> ccc20200701_models.DeleteAudioFileResponse:
        """
        @param request: DeleteAudioFileRequest
        @return: DeleteAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_audio_file_with_options(request, runtime)

    async def delete_audio_file_async(
        self,
        request: ccc20200701_models.DeleteAudioFileRequest,
    ) -> ccc20200701_models.DeleteAudioFileResponse:
        """
        @param request: DeleteAudioFileRequest
        @return: DeleteAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_audio_file_with_options_async(request, runtime)

    def delete_call_tag_with_options(
        self,
        request: ccc20200701_models.DeleteCallTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteCallTagResponse:
        """
        @summary 删除号码标签
        
        @param request: DeleteCallTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCallTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCallTag',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteCallTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_call_tag_with_options_async(
        self,
        request: ccc20200701_models.DeleteCallTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteCallTagResponse:
        """
        @summary 删除号码标签
        
        @param request: DeleteCallTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCallTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCallTag',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteCallTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_call_tag(
        self,
        request: ccc20200701_models.DeleteCallTagRequest,
    ) -> ccc20200701_models.DeleteCallTagResponse:
        """
        @summary 删除号码标签
        
        @param request: DeleteCallTagRequest
        @return: DeleteCallTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_call_tag_with_options(request, runtime)

    async def delete_call_tag_async(
        self,
        request: ccc20200701_models.DeleteCallTagRequest,
    ) -> ccc20200701_models.DeleteCallTagResponse:
        """
        @summary 删除号码标签
        
        @param request: DeleteCallTagRequest
        @return: DeleteCallTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_call_tag_with_options_async(request, runtime)

    def delete_contact_flow_with_options(
        self,
        request: ccc20200701_models.DeleteContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteContactFlowResponse:
        """
        @param request: DeleteContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_flow_with_options_async(
        self,
        request: ccc20200701_models.DeleteContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteContactFlowResponse:
        """
        @param request: DeleteContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_flow(
        self,
        request: ccc20200701_models.DeleteContactFlowRequest,
    ) -> ccc20200701_models.DeleteContactFlowResponse:
        """
        @param request: DeleteContactFlowRequest
        @return: DeleteContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_flow_with_options(request, runtime)

    async def delete_contact_flow_async(
        self,
        request: ccc20200701_models.DeleteContactFlowRequest,
    ) -> ccc20200701_models.DeleteContactFlowResponse:
        """
        @param request: DeleteContactFlowRequest
        @return: DeleteContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_flow_with_options_async(request, runtime)

    def delete_custom_call_tagging_with_options(
        self,
        request: ccc20200701_models.DeleteCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteCustomCallTaggingResponse:
        """
        @summary 删除呼入控制号码
        
        @param request: DeleteCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.DeleteCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteCustomCallTaggingResponse:
        """
        @summary 删除呼入控制号码
        
        @param request: DeleteCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_call_tagging(
        self,
        request: ccc20200701_models.DeleteCustomCallTaggingRequest,
    ) -> ccc20200701_models.DeleteCustomCallTaggingResponse:
        """
        @summary 删除呼入控制号码
        
        @param request: DeleteCustomCallTaggingRequest
        @return: DeleteCustomCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_call_tagging_with_options(request, runtime)

    async def delete_custom_call_tagging_async(
        self,
        request: ccc20200701_models.DeleteCustomCallTaggingRequest,
    ) -> ccc20200701_models.DeleteCustomCallTaggingResponse:
        """
        @summary 删除呼入控制号码
        
        @param request: DeleteCustomCallTaggingRequest
        @return: DeleteCustomCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_call_tagging_with_options_async(request, runtime)

    def delete_document_with_options(
        self,
        request: ccc20200701_models.DeleteDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteDocumentResponse:
        """
        @param request: DeleteDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document_id):
            body['DocumentId'] = request.document_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        request: ccc20200701_models.DeleteDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteDocumentResponse:
        """
        @param request: DeleteDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document_id):
            body['DocumentId'] = request.document_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        request: ccc20200701_models.DeleteDocumentRequest,
    ) -> ccc20200701_models.DeleteDocumentResponse:
        """
        @param request: DeleteDocumentRequest
        @return: DeleteDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_document_with_options(request, runtime)

    async def delete_document_async(
        self,
        request: ccc20200701_models.DeleteDocumentRequest,
    ) -> ccc20200701_models.DeleteDocumentResponse:
        """
        @param request: DeleteDocumentRequest
        @return: DeleteDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_document_with_options_async(request, runtime)

    def delete_documents_with_options(
        self,
        tmp_req: ccc20200701_models.DeleteDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteDocumentsResponse:
        """
        @param tmp_req: DeleteDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.DeleteDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.document_ids_shrink):
            body['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocuments',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_documents_with_options_async(
        self,
        tmp_req: ccc20200701_models.DeleteDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteDocumentsResponse:
        """
        @param tmp_req: DeleteDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.DeleteDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.document_ids_shrink):
            body['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocuments',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_documents(
        self,
        request: ccc20200701_models.DeleteDocumentsRequest,
    ) -> ccc20200701_models.DeleteDocumentsResponse:
        """
        @param request: DeleteDocumentsRequest
        @return: DeleteDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_documents_with_options(request, runtime)

    async def delete_documents_async(
        self,
        request: ccc20200701_models.DeleteDocumentsRequest,
    ) -> ccc20200701_models.DeleteDocumentsResponse:
        """
        @param request: DeleteDocumentsRequest
        @return: DeleteDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_documents_with_options_async(request, runtime)

    def delete_schema_with_options(
        self,
        request: ccc20200701_models.DeleteSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSchemaResponse:
        """
        @param request: DeleteSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchemaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSchema',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schema_with_options_async(
        self,
        request: ccc20200701_models.DeleteSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSchemaResponse:
        """
        @param request: DeleteSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchemaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSchema',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schema(
        self,
        request: ccc20200701_models.DeleteSchemaRequest,
    ) -> ccc20200701_models.DeleteSchemaResponse:
        """
        @param request: DeleteSchemaRequest
        @return: DeleteSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_schema_with_options(request, runtime)

    async def delete_schema_async(
        self,
        request: ccc20200701_models.DeleteSchemaRequest,
    ) -> ccc20200701_models.DeleteSchemaResponse:
        """
        @param request: DeleteSchemaRequest
        @return: DeleteSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_schema_with_options_async(request, runtime)

    def delete_schema_property_with_options(
        self,
        request: ccc20200701_models.DeleteSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSchemaPropertyResponse:
        """
        @param request: DeleteSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchemaPropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schema_property_with_options_async(
        self,
        request: ccc20200701_models.DeleteSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSchemaPropertyResponse:
        """
        @param request: DeleteSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchemaPropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schema_property(
        self,
        request: ccc20200701_models.DeleteSchemaPropertyRequest,
    ) -> ccc20200701_models.DeleteSchemaPropertyResponse:
        """
        @param request: DeleteSchemaPropertyRequest
        @return: DeleteSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_schema_property_with_options(request, runtime)

    async def delete_schema_property_async(
        self,
        request: ccc20200701_models.DeleteSchemaPropertyRequest,
    ) -> ccc20200701_models.DeleteSchemaPropertyResponse:
        """
        @param request: DeleteSchemaPropertyRequest
        @return: DeleteSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_schema_property_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_group(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @return: DeleteSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        """
        @param request: DeleteSkillGroupRequest
        @return: DeleteSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def disable_schema_property_with_options(
        self,
        request: ccc20200701_models.DisableSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DisableSchemaPropertyResponse:
        """
        @param request: DisableSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSchemaPropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DisableSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_schema_property_with_options_async(
        self,
        request: ccc20200701_models.DisableSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DisableSchemaPropertyResponse:
        """
        @param request: DisableSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSchemaPropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DisableSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_schema_property(
        self,
        request: ccc20200701_models.DisableSchemaPropertyRequest,
    ) -> ccc20200701_models.DisableSchemaPropertyResponse:
        """
        @param request: DisableSchemaPropertyRequest
        @return: DisableSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_schema_property_with_options(request, runtime)

    async def disable_schema_property_async(
        self,
        request: ccc20200701_models.DisableSchemaPropertyRequest,
    ) -> ccc20200701_models.DisableSchemaPropertyResponse:
        """
        @param request: DisableSchemaPropertyRequest
        @return: DisableSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_schema_property_with_options_async(request, runtime)

    def discard_editing_contact_flow_with_options(
        self,
        request: ccc20200701_models.DiscardEditingContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DiscardEditingContactFlowResponse:
        """
        @param request: DiscardEditingContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DiscardEditingContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DiscardEditingContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DiscardEditingContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def discard_editing_contact_flow_with_options_async(
        self,
        request: ccc20200701_models.DiscardEditingContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DiscardEditingContactFlowResponse:
        """
        @param request: DiscardEditingContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DiscardEditingContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DiscardEditingContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.DiscardEditingContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def discard_editing_contact_flow(
        self,
        request: ccc20200701_models.DiscardEditingContactFlowRequest,
    ) -> ccc20200701_models.DiscardEditingContactFlowResponse:
        """
        @param request: DiscardEditingContactFlowRequest
        @return: DiscardEditingContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.discard_editing_contact_flow_with_options(request, runtime)

    async def discard_editing_contact_flow_async(
        self,
        request: ccc20200701_models.DiscardEditingContactFlowRequest,
    ) -> ccc20200701_models.DiscardEditingContactFlowResponse:
        """
        @param request: DiscardEditingContactFlowRequest
        @return: DiscardEditingContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.discard_editing_contact_flow_with_options_async(request, runtime)

    def enable_schema_property_with_options(
        self,
        request: ccc20200701_models.EnableSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.EnableSchemaPropertyResponse:
        """
        @param request: EnableSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSchemaPropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.EnableSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_schema_property_with_options_async(
        self,
        request: ccc20200701_models.EnableSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.EnableSchemaPropertyResponse:
        """
        @param request: EnableSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSchemaPropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.EnableSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_schema_property(
        self,
        request: ccc20200701_models.EnableSchemaPropertyRequest,
    ) -> ccc20200701_models.EnableSchemaPropertyResponse:
        """
        @param request: EnableSchemaPropertyRequest
        @return: EnableSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_schema_property_with_options(request, runtime)

    async def enable_schema_property_async(
        self,
        request: ccc20200701_models.EnableSchemaPropertyRequest,
    ) -> ccc20200701_models.EnableSchemaPropertyResponse:
        """
        @param request: EnableSchemaPropertyRequest
        @return: EnableSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_schema_property_with_options_async(request, runtime)

    def end_conference_with_options(
        self,
        request: ccc20200701_models.EndConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.EndConferenceResponse:
        """
        @param request: EndConferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndConferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndConference',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.EndConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_conference_with_options_async(
        self,
        request: ccc20200701_models.EndConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.EndConferenceResponse:
        """
        @param request: EndConferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndConferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndConference',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.EndConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_conference(
        self,
        request: ccc20200701_models.EndConferenceRequest,
    ) -> ccc20200701_models.EndConferenceResponse:
        """
        @param request: EndConferenceRequest
        @return: EndConferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.end_conference_with_options(request, runtime)

    async def end_conference_async(
        self,
        request: ccc20200701_models.EndConferenceRequest,
    ) -> ccc20200701_models.EndConferenceResponse:
        """
        @param request: EndConferenceRequest
        @return: EndConferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.end_conference_with_options_async(request, runtime)

    def export_custom_call_tagging_with_options(
        self,
        request: ccc20200701_models.ExportCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ExportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ExportCustomCallTagging is deprecated, please use CCC::2020-07-01::ExportCustomCallTaggings instead.
        
        @summary 导出全部呼入号码标签
        
        @param request: ExportCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ExportCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_custom_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.ExportCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ExportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ExportCustomCallTagging is deprecated, please use CCC::2020-07-01::ExportCustomCallTaggings instead.
        
        @summary 导出全部呼入号码标签
        
        @param request: ExportCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ExportCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_custom_call_tagging(
        self,
        request: ccc20200701_models.ExportCustomCallTaggingRequest,
    ) -> ccc20200701_models.ExportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ExportCustomCallTagging is deprecated, please use CCC::2020-07-01::ExportCustomCallTaggings instead.
        
        @summary 导出全部呼入号码标签
        
        @param request: ExportCustomCallTaggingRequest
        @return: ExportCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.export_custom_call_tagging_with_options(request, runtime)

    async def export_custom_call_tagging_async(
        self,
        request: ccc20200701_models.ExportCustomCallTaggingRequest,
    ) -> ccc20200701_models.ExportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ExportCustomCallTagging is deprecated, please use CCC::2020-07-01::ExportCustomCallTaggings instead.
        
        @summary 导出全部呼入号码标签
        
        @param request: ExportCustomCallTaggingRequest
        @return: ExportCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_custom_call_tagging_with_options_async(request, runtime)

    def export_do_not_call_numbers_with_options(
        self,
        request: ccc20200701_models.ExportDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ExportDoNotCallNumbersResponse:
        """
        @summary 导出黑名单号码
        
        @param request: ExportDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ExportDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_do_not_call_numbers_with_options_async(
        self,
        request: ccc20200701_models.ExportDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ExportDoNotCallNumbersResponse:
        """
        @summary 导出黑名单号码
        
        @param request: ExportDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ExportDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_do_not_call_numbers(
        self,
        request: ccc20200701_models.ExportDoNotCallNumbersRequest,
    ) -> ccc20200701_models.ExportDoNotCallNumbersResponse:
        """
        @summary 导出黑名单号码
        
        @param request: ExportDoNotCallNumbersRequest
        @return: ExportDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_do_not_call_numbers_with_options(request, runtime)

    async def export_do_not_call_numbers_async(
        self,
        request: ccc20200701_models.ExportDoNotCallNumbersRequest,
    ) -> ccc20200701_models.ExportDoNotCallNumbersResponse:
        """
        @summary 导出黑名单号码
        
        @param request: ExportDoNotCallNumbersRequest
        @return: ExportDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_do_not_call_numbers_with_options_async(request, runtime)

    def get_access_channel_of_staging_with_options(
        self,
        request: ccc20200701_models.GetAccessChannelOfStagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAccessChannelOfStagingResponse:
        """
        @summary GetAccessChannelOfStaging
        
        @param request: GetAccessChannelOfStagingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessChannelOfStagingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessChannelOfStaging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAccessChannelOfStagingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_channel_of_staging_with_options_async(
        self,
        request: ccc20200701_models.GetAccessChannelOfStagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAccessChannelOfStagingResponse:
        """
        @summary GetAccessChannelOfStaging
        
        @param request: GetAccessChannelOfStagingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessChannelOfStagingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessChannelOfStaging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAccessChannelOfStagingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_channel_of_staging(
        self,
        request: ccc20200701_models.GetAccessChannelOfStagingRequest,
    ) -> ccc20200701_models.GetAccessChannelOfStagingResponse:
        """
        @summary GetAccessChannelOfStaging
        
        @param request: GetAccessChannelOfStagingRequest
        @return: GetAccessChannelOfStagingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_channel_of_staging_with_options(request, runtime)

    async def get_access_channel_of_staging_async(
        self,
        request: ccc20200701_models.GetAccessChannelOfStagingRequest,
    ) -> ccc20200701_models.GetAccessChannelOfStagingResponse:
        """
        @summary GetAccessChannelOfStaging
        
        @param request: GetAccessChannelOfStagingRequest
        @return: GetAccessChannelOfStagingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_channel_of_staging_with_options_async(request, runtime)

    def get_audio_file_with_options(
        self,
        request: ccc20200701_models.GetAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAudioFileResponse:
        """
        @summary 获取音频文件
        
        @param request: GetAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audio_file_with_options_async(
        self,
        request: ccc20200701_models.GetAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAudioFileResponse:
        """
        @summary 获取音频文件
        
        @param request: GetAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audio_file(
        self,
        request: ccc20200701_models.GetAudioFileRequest,
    ) -> ccc20200701_models.GetAudioFileResponse:
        """
        @summary 获取音频文件
        
        @param request: GetAudioFileRequest
        @return: GetAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_audio_file_with_options(request, runtime)

    async def get_audio_file_async(
        self,
        request: ccc20200701_models.GetAudioFileRequest,
    ) -> ccc20200701_models.GetAudioFileResponse:
        """
        @summary 获取音频文件
        
        @param request: GetAudioFileRequest
        @return: GetAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_file_with_options_async(request, runtime)

    def get_audio_file_download_url_with_options(
        self,
        request: ccc20200701_models.GetAudioFileDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAudioFileDownloadUrlResponse:
        """
        @param request: GetAudioFileDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAudioFileDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAudioFileDownloadUrl',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAudioFileDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audio_file_download_url_with_options_async(
        self,
        request: ccc20200701_models.GetAudioFileDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAudioFileDownloadUrlResponse:
        """
        @param request: GetAudioFileDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAudioFileDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAudioFileDownloadUrl',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAudioFileDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audio_file_download_url(
        self,
        request: ccc20200701_models.GetAudioFileDownloadUrlRequest,
    ) -> ccc20200701_models.GetAudioFileDownloadUrlResponse:
        """
        @param request: GetAudioFileDownloadUrlRequest
        @return: GetAudioFileDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_audio_file_download_url_with_options(request, runtime)

    async def get_audio_file_download_url_async(
        self,
        request: ccc20200701_models.GetAudioFileDownloadUrlRequest,
    ) -> ccc20200701_models.GetAudioFileDownloadUrlResponse:
        """
        @param request: GetAudioFileDownloadUrlRequest
        @return: GetAudioFileDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_file_download_url_with_options_async(request, runtime)

    def get_audio_file_upload_parameters_with_options(
        self,
        request: ccc20200701_models.GetAudioFileUploadParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAudioFileUploadParametersResponse:
        """
        @param request: GetAudioFileUploadParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAudioFileUploadParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAudioFileUploadParameters',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAudioFileUploadParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audio_file_upload_parameters_with_options_async(
        self,
        request: ccc20200701_models.GetAudioFileUploadParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetAudioFileUploadParametersResponse:
        """
        @param request: GetAudioFileUploadParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAudioFileUploadParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAudioFileUploadParameters',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetAudioFileUploadParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audio_file_upload_parameters(
        self,
        request: ccc20200701_models.GetAudioFileUploadParametersRequest,
    ) -> ccc20200701_models.GetAudioFileUploadParametersResponse:
        """
        @param request: GetAudioFileUploadParametersRequest
        @return: GetAudioFileUploadParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_audio_file_upload_parameters_with_options(request, runtime)

    async def get_audio_file_upload_parameters_async(
        self,
        request: ccc20200701_models.GetAudioFileUploadParametersRequest,
    ) -> ccc20200701_models.GetAudioFileUploadParametersResponse:
        """
        @param request: GetAudioFileUploadParametersRequest
        @return: GetAudioFileUploadParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_file_upload_parameters_with_options_async(request, runtime)

    def get_call_detail_record_with_options(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        """
        @param request: GetCallDetailRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCallDetailRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallDetailRecord',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCallDetailRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_detail_record_with_options_async(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        """
        @param request: GetCallDetailRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCallDetailRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCallDetailRecord',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCallDetailRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_detail_record(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        """
        @param request: GetCallDetailRecordRequest
        @return: GetCallDetailRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_call_detail_record_with_options(request, runtime)

    async def get_call_detail_record_async(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        """
        @param request: GetCallDetailRecordRequest
        @return: GetCallDetailRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_call_detail_record_with_options_async(request, runtime)

    def get_campaign_with_options(
        self,
        request: ccc20200701_models.GetCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCampaignResponse:
        """
        @summary 获取预测式外呼活动信息
        
        @param request: GetCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_campaign_with_options_async(
        self,
        request: ccc20200701_models.GetCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCampaignResponse:
        """
        @summary 获取预测式外呼活动信息
        
        @param request: GetCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_campaign(
        self,
        request: ccc20200701_models.GetCampaignRequest,
    ) -> ccc20200701_models.GetCampaignResponse:
        """
        @summary 获取预测式外呼活动信息
        
        @param request: GetCampaignRequest
        @return: GetCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_campaign_with_options(request, runtime)

    async def get_campaign_async(
        self,
        request: ccc20200701_models.GetCampaignRequest,
    ) -> ccc20200701_models.GetCampaignResponse:
        """
        @summary 获取预测式外呼活动信息
        
        @param request: GetCampaignRequest
        @return: GetCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_campaign_with_options_async(request, runtime)

    def get_case_file_upload_url_with_options(
        self,
        request: ccc20200701_models.GetCaseFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCaseFileUploadUrlResponse:
        """
        @param request: GetCaseFileUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCaseFileUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCaseFileUploadUrl',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCaseFileUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_case_file_upload_url_with_options_async(
        self,
        request: ccc20200701_models.GetCaseFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCaseFileUploadUrlResponse:
        """
        @param request: GetCaseFileUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCaseFileUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCaseFileUploadUrl',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCaseFileUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_case_file_upload_url(
        self,
        request: ccc20200701_models.GetCaseFileUploadUrlRequest,
    ) -> ccc20200701_models.GetCaseFileUploadUrlResponse:
        """
        @param request: GetCaseFileUploadUrlRequest
        @return: GetCaseFileUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_case_file_upload_url_with_options(request, runtime)

    async def get_case_file_upload_url_async(
        self,
        request: ccc20200701_models.GetCaseFileUploadUrlRequest,
    ) -> ccc20200701_models.GetCaseFileUploadUrlResponse:
        """
        @param request: GetCaseFileUploadUrlRequest
        @return: GetCaseFileUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_case_file_upload_url_with_options_async(request, runtime)

    def get_contact_flow_with_options(
        self,
        request: ccc20200701_models.GetContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetContactFlowResponse:
        """
        @param request: GetContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contact_flow_with_options_async(
        self,
        request: ccc20200701_models.GetContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetContactFlowResponse:
        """
        @param request: GetContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contact_flow(
        self,
        request: ccc20200701_models.GetContactFlowRequest,
    ) -> ccc20200701_models.GetContactFlowResponse:
        """
        @param request: GetContactFlowRequest
        @return: GetContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_contact_flow_with_options(request, runtime)

    async def get_contact_flow_async(
        self,
        request: ccc20200701_models.GetContactFlowRequest,
    ) -> ccc20200701_models.GetContactFlowResponse:
        """
        @param request: GetContactFlowRequest
        @return: GetContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_contact_flow_with_options_async(request, runtime)

    def get_conversation_detail_with_options(
        self,
        request: ccc20200701_models.GetConversationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetConversationDetailResponse:
        """
        @summary 获取通话文本信息
        
        @param request: GetConversationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConversationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConversationDetail',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetConversationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversation_detail_with_options_async(
        self,
        request: ccc20200701_models.GetConversationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetConversationDetailResponse:
        """
        @summary 获取通话文本信息
        
        @param request: GetConversationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConversationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConversationDetail',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetConversationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conversation_detail(
        self,
        request: ccc20200701_models.GetConversationDetailRequest,
    ) -> ccc20200701_models.GetConversationDetailResponse:
        """
        @summary 获取通话文本信息
        
        @param request: GetConversationDetailRequest
        @return: GetConversationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_detail_with_options(request, runtime)

    async def get_conversation_detail_async(
        self,
        request: ccc20200701_models.GetConversationDetailRequest,
    ) -> ccc20200701_models.GetConversationDetailResponse:
        """
        @summary 获取通话文本信息
        
        @param request: GetConversationDetailRequest
        @return: GetConversationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_conversation_detail_with_options_async(request, runtime)

    def get_data_channel_credentials_with_options(
        self,
        request: ccc20200701_models.GetDataChannelCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetDataChannelCredentialsResponse:
        """
        @param request: GetDataChannelCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataChannelCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataChannelCredentials',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetDataChannelCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_channel_credentials_with_options_async(
        self,
        request: ccc20200701_models.GetDataChannelCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetDataChannelCredentialsResponse:
        """
        @param request: GetDataChannelCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataChannelCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataChannelCredentials',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetDataChannelCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_channel_credentials(
        self,
        request: ccc20200701_models.GetDataChannelCredentialsRequest,
    ) -> ccc20200701_models.GetDataChannelCredentialsResponse:
        """
        @param request: GetDataChannelCredentialsRequest
        @return: GetDataChannelCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_channel_credentials_with_options(request, runtime)

    async def get_data_channel_credentials_async(
        self,
        request: ccc20200701_models.GetDataChannelCredentialsRequest,
    ) -> ccc20200701_models.GetDataChannelCredentialsResponse:
        """
        @param request: GetDataChannelCredentialsRequest
        @return: GetDataChannelCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_channel_credentials_with_options_async(request, runtime)

    def get_do_not_call_file_upload_parameters_with_options(
        self,
        request: ccc20200701_models.GetDoNotCallFileUploadParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetDoNotCallFileUploadParametersResponse:
        """
        @summary 获取黑名单文件上传地址
        
        @param request: GetDoNotCallFileUploadParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoNotCallFileUploadParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoNotCallFileUploadParameters',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetDoNotCallFileUploadParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_do_not_call_file_upload_parameters_with_options_async(
        self,
        request: ccc20200701_models.GetDoNotCallFileUploadParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetDoNotCallFileUploadParametersResponse:
        """
        @summary 获取黑名单文件上传地址
        
        @param request: GetDoNotCallFileUploadParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoNotCallFileUploadParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoNotCallFileUploadParameters',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetDoNotCallFileUploadParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_do_not_call_file_upload_parameters(
        self,
        request: ccc20200701_models.GetDoNotCallFileUploadParametersRequest,
    ) -> ccc20200701_models.GetDoNotCallFileUploadParametersResponse:
        """
        @summary 获取黑名单文件上传地址
        
        @param request: GetDoNotCallFileUploadParametersRequest
        @return: GetDoNotCallFileUploadParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_do_not_call_file_upload_parameters_with_options(request, runtime)

    async def get_do_not_call_file_upload_parameters_async(
        self,
        request: ccc20200701_models.GetDoNotCallFileUploadParametersRequest,
    ) -> ccc20200701_models.GetDoNotCallFileUploadParametersResponse:
        """
        @summary 获取黑名单文件上传地址
        
        @param request: GetDoNotCallFileUploadParametersRequest
        @return: GetDoNotCallFileUploadParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_do_not_call_file_upload_parameters_with_options_async(request, runtime)

    def get_document_upload_parameters_with_options(
        self,
        request: ccc20200701_models.GetDocumentUploadParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetDocumentUploadParametersResponse:
        """
        @param request: GetDocumentUploadParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentUploadParametersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentUploadParameters',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetDocumentUploadParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_upload_parameters_with_options_async(
        self,
        request: ccc20200701_models.GetDocumentUploadParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetDocumentUploadParametersResponse:
        """
        @param request: GetDocumentUploadParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentUploadParametersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentUploadParameters',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetDocumentUploadParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_upload_parameters(
        self,
        request: ccc20200701_models.GetDocumentUploadParametersRequest,
    ) -> ccc20200701_models.GetDocumentUploadParametersResponse:
        """
        @param request: GetDocumentUploadParametersRequest
        @return: GetDocumentUploadParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_document_upload_parameters_with_options(request, runtime)

    async def get_document_upload_parameters_async(
        self,
        request: ccc20200701_models.GetDocumentUploadParametersRequest,
    ) -> ccc20200701_models.GetDocumentUploadParametersResponse:
        """
        @param request: GetDocumentUploadParametersRequest
        @return: GetDocumentUploadParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_document_upload_parameters_with_options_async(request, runtime)

    def get_early_media_recording_with_options(
        self,
        request: ccc20200701_models.GetEarlyMediaRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetEarlyMediaRecordingResponse:
        """
        @summary 获取早媒体音频
        
        @param request: GetEarlyMediaRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEarlyMediaRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEarlyMediaRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetEarlyMediaRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_early_media_recording_with_options_async(
        self,
        request: ccc20200701_models.GetEarlyMediaRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetEarlyMediaRecordingResponse:
        """
        @summary 获取早媒体音频
        
        @param request: GetEarlyMediaRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEarlyMediaRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEarlyMediaRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetEarlyMediaRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_early_media_recording(
        self,
        request: ccc20200701_models.GetEarlyMediaRecordingRequest,
    ) -> ccc20200701_models.GetEarlyMediaRecordingResponse:
        """
        @summary 获取早媒体音频
        
        @param request: GetEarlyMediaRecordingRequest
        @return: GetEarlyMediaRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_early_media_recording_with_options(request, runtime)

    async def get_early_media_recording_async(
        self,
        request: ccc20200701_models.GetEarlyMediaRecordingRequest,
    ) -> ccc20200701_models.GetEarlyMediaRecordingResponse:
        """
        @summary 获取早媒体音频
        
        @param request: GetEarlyMediaRecordingRequest
        @return: GetEarlyMediaRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_early_media_recording_with_options_async(request, runtime)

    def get_historical_caller_report_with_options(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        """
        @param request: GetHistoricalCallerReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoricalCallerReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['StopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalCallerReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCallerReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_caller_report_with_options_async(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        """
        @param request: GetHistoricalCallerReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoricalCallerReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['StopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalCallerReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCallerReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_caller_report(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        """
        @param request: GetHistoricalCallerReportRequest
        @return: GetHistoricalCallerReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_historical_caller_report_with_options(request, runtime)

    async def get_historical_caller_report_async(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        """
        @param request: GetHistoricalCallerReportRequest
        @return: GetHistoricalCallerReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_historical_caller_report_with_options_async(request, runtime)

    def get_historical_campaign_report_with_options(
        self,
        request: ccc20200701_models.GetHistoricalCampaignReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCampaignReportResponse:
        """
        @summary 获取预测式外呼活动历史报表
        
        @param request: GetHistoricalCampaignReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoricalCampaignReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalCampaignReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCampaignReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_campaign_report_with_options_async(
        self,
        request: ccc20200701_models.GetHistoricalCampaignReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCampaignReportResponse:
        """
        @summary 获取预测式外呼活动历史报表
        
        @param request: GetHistoricalCampaignReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoricalCampaignReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalCampaignReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCampaignReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_campaign_report(
        self,
        request: ccc20200701_models.GetHistoricalCampaignReportRequest,
    ) -> ccc20200701_models.GetHistoricalCampaignReportResponse:
        """
        @summary 获取预测式外呼活动历史报表
        
        @param request: GetHistoricalCampaignReportRequest
        @return: GetHistoricalCampaignReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_historical_campaign_report_with_options(request, runtime)

    async def get_historical_campaign_report_async(
        self,
        request: ccc20200701_models.GetHistoricalCampaignReportRequest,
    ) -> ccc20200701_models.GetHistoricalCampaignReportResponse:
        """
        @summary 获取预测式外呼活动历史报表
        
        @param request: GetHistoricalCampaignReportRequest
        @return: GetHistoricalCampaignReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_historical_campaign_report_with_options_async(request, runtime)

    def get_historical_instance_report_with_options(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        """
        @param request: GetHistoricalInstanceReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoricalInstanceReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalInstanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_historical_instance_report_with_options_async(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        """
        @param request: GetHistoricalInstanceReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoricalInstanceReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalInstanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_historical_instance_report(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        """
        @param request: GetHistoricalInstanceReportRequest
        @return: GetHistoricalInstanceReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_historical_instance_report_with_options(request, runtime)

    async def get_historical_instance_report_async(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        """
        @param request: GetHistoricalInstanceReportRequest
        @return: GetHistoricalInstanceReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_historical_instance_report_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: ccc20200701_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceResponse:
        """
        @param request: GetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: ccc20200701_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceResponse:
        """
        @param request: GetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: ccc20200701_models.GetInstanceRequest,
    ) -> ccc20200701_models.GetInstanceResponse:
        """
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: ccc20200701_models.GetInstanceRequest,
    ) -> ccc20200701_models.GetInstanceResponse:
        """
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_trending_report_with_options(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        """
        @param request: GetInstanceTrendingReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceTrendingReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceTrendingReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_trending_report_with_options_async(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        """
        @param request: GetInstanceTrendingReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceTrendingReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceTrendingReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_trending_report(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        """
        @param request: GetInstanceTrendingReportRequest
        @return: GetInstanceTrendingReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_trending_report_with_options(request, runtime)

    async def get_instance_trending_report_async(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        """
        @param request: GetInstanceTrendingReportRequest
        @return: GetInstanceTrendingReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_trending_report_with_options_async(request, runtime)

    def get_login_details_with_options(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        """
        @param request: GetLoginDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetLoginDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_details_with_options_async(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        """
        @param request: GetLoginDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetLoginDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_details(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        """
        @param request: GetLoginDetailsRequest
        @return: GetLoginDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_login_details_with_options(request, runtime)

    async def get_login_details_async(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        """
        @param request: GetLoginDetailsRequest
        @return: GetLoginDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_login_details_with_options_async(request, runtime)

    def get_mono_recording_with_options(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        """
        @param request: GetMonoRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonoRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonoRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMonoRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mono_recording_with_options_async(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        """
        @param request: GetMonoRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonoRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonoRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMonoRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mono_recording(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        """
        @param request: GetMonoRecordingRequest
        @return: GetMonoRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mono_recording_with_options(request, runtime)

    async def get_mono_recording_async(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        """
        @param request: GetMonoRecordingRequest
        @return: GetMonoRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mono_recording_with_options_async(request, runtime)

    def get_multi_channel_recording_with_options(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        """
        @param request: GetMultiChannelRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiChannelRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiChannelRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMultiChannelRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_channel_recording_with_options_async(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        """
        @param request: GetMultiChannelRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiChannelRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiChannelRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMultiChannelRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_channel_recording(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        """
        @param request: GetMultiChannelRecordingRequest
        @return: GetMultiChannelRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_multi_channel_recording_with_options(request, runtime)

    async def get_multi_channel_recording_async(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        """
        @param request: GetMultiChannelRecordingRequest
        @return: GetMultiChannelRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_channel_recording_with_options_async(request, runtime)

    def get_number_location_with_options(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        """
        @param request: GetNumberLocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNumberLocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNumberLocation',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetNumberLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_number_location_with_options_async(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        """
        @param request: GetNumberLocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNumberLocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNumberLocation',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetNumberLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_number_location(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        """
        @param request: GetNumberLocationRequest
        @return: GetNumberLocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_number_location_with_options(request, runtime)

    async def get_number_location_async(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        """
        @param request: GetNumberLocationRequest
        @return: GetNumberLocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_number_location_with_options_async(request, runtime)

    def get_realtime_campaign_stats_with_options(
        self,
        request: ccc20200701_models.GetRealtimeCampaignStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeCampaignStatsResponse:
        """
        @summary 获取预测式外呼实时状态
        
        @param request: GetRealtimeCampaignStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeCampaignStatsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeCampaignStats',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeCampaignStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_campaign_stats_with_options_async(
        self,
        request: ccc20200701_models.GetRealtimeCampaignStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeCampaignStatsResponse:
        """
        @summary 获取预测式外呼实时状态
        
        @param request: GetRealtimeCampaignStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeCampaignStatsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeCampaignStats',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeCampaignStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_campaign_stats(
        self,
        request: ccc20200701_models.GetRealtimeCampaignStatsRequest,
    ) -> ccc20200701_models.GetRealtimeCampaignStatsResponse:
        """
        @summary 获取预测式外呼实时状态
        
        @param request: GetRealtimeCampaignStatsRequest
        @return: GetRealtimeCampaignStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_campaign_stats_with_options(request, runtime)

    async def get_realtime_campaign_stats_async(
        self,
        request: ccc20200701_models.GetRealtimeCampaignStatsRequest,
    ) -> ccc20200701_models.GetRealtimeCampaignStatsResponse:
        """
        @summary 获取预测式外呼实时状态
        
        @param request: GetRealtimeCampaignStatsRequest
        @return: GetRealtimeCampaignStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_campaign_stats_with_options_async(request, runtime)

    def get_realtime_instance_states_with_options(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        """
        @param request: GetRealtimeInstanceStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeInstanceStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeInstanceStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeInstanceStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_instance_states_with_options_async(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        """
        @param request: GetRealtimeInstanceStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeInstanceStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeInstanceStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeInstanceStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_instance_states(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        """
        @param request: GetRealtimeInstanceStatesRequest
        @return: GetRealtimeInstanceStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_instance_states_with_options(request, runtime)

    async def get_realtime_instance_states_async(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        """
        @param request: GetRealtimeInstanceStatesRequest
        @return: GetRealtimeInstanceStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_instance_states_with_options_async(request, runtime)

    def get_schema_with_options(
        self,
        request: ccc20200701_models.GetSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetSchemaResponse:
        """
        @param request: GetSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSchemaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSchema',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schema_with_options_async(
        self,
        request: ccc20200701_models.GetSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetSchemaResponse:
        """
        @param request: GetSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSchemaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSchema',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schema(
        self,
        request: ccc20200701_models.GetSchemaRequest,
    ) -> ccc20200701_models.GetSchemaResponse:
        """
        @param request: GetSchemaRequest
        @return: GetSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_schema_with_options(request, runtime)

    async def get_schema_async(
        self,
        request: ccc20200701_models.GetSchemaRequest,
    ) -> ccc20200701_models.GetSchemaResponse:
        """
        @param request: GetSchemaRequest
        @return: GetSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_schema_with_options_async(request, runtime)

    def get_skill_group_with_options(
        self,
        request: ccc20200701_models.GetSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetSkillGroupResponse:
        """
        @summary 查询技能组
        
        @param request: GetSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_with_options_async(
        self,
        request: ccc20200701_models.GetSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetSkillGroupResponse:
        """
        @summary 查询技能组
        
        @param request: GetSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group(
        self,
        request: ccc20200701_models.GetSkillGroupRequest,
    ) -> ccc20200701_models.GetSkillGroupResponse:
        """
        @summary 查询技能组
        
        @param request: GetSkillGroupRequest
        @return: GetSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_with_options(request, runtime)

    async def get_skill_group_async(
        self,
        request: ccc20200701_models.GetSkillGroupRequest,
    ) -> ccc20200701_models.GetSkillGroupResponse:
        """
        @summary 查询技能组
        
        @param request: GetSkillGroupRequest
        @return: GetSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_with_options_async(request, runtime)

    def get_turn_credentials_with_options(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        """
        @param request: GetTurnCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTurnCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnCredentials',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_turn_credentials_with_options_async(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        """
        @param request: GetTurnCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTurnCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnCredentials',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_turn_credentials(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        """
        @param request: GetTurnCredentialsRequest
        @return: GetTurnCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_turn_credentials_with_options(request, runtime)

    async def get_turn_credentials_async(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        """
        @param request: GetTurnCredentialsRequest
        @return: GetTurnCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_turn_credentials_with_options_async(request, runtime)

    def get_turn_server_list_with_options(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        """
        @param request: GetTurnServerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTurnServerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnServerList',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnServerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_turn_server_list_with_options_async(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        """
        @param request: GetTurnServerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTurnServerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTurnServerList',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnServerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_turn_server_list(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        """
        @param request: GetTurnServerListRequest
        @return: GetTurnServerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_turn_server_list_with_options(request, runtime)

    async def get_turn_server_list_async(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        """
        @param request: GetTurnServerListRequest
        @return: GetTurnServerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_turn_server_list_with_options_async(request, runtime)

    def get_upload_audio_data_params_with_options(
        self,
        request: ccc20200701_models.GetUploadAudioDataParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUploadAudioDataParamsResponse:
        """
        @summary 获取质检参数
        
        @param request: GetUploadAudioDataParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadAudioDataParamsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadAudioDataParams',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUploadAudioDataParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_audio_data_params_with_options_async(
        self,
        request: ccc20200701_models.GetUploadAudioDataParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUploadAudioDataParamsResponse:
        """
        @summary 获取质检参数
        
        @param request: GetUploadAudioDataParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadAudioDataParamsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadAudioDataParams',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUploadAudioDataParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_audio_data_params(
        self,
        request: ccc20200701_models.GetUploadAudioDataParamsRequest,
    ) -> ccc20200701_models.GetUploadAudioDataParamsResponse:
        """
        @summary 获取质检参数
        
        @param request: GetUploadAudioDataParamsRequest
        @return: GetUploadAudioDataParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_audio_data_params_with_options(request, runtime)

    async def get_upload_audio_data_params_async(
        self,
        request: ccc20200701_models.GetUploadAudioDataParamsRequest,
    ) -> ccc20200701_models.GetUploadAudioDataParamsResponse:
        """
        @summary 获取质检参数
        
        @param request: GetUploadAudioDataParamsRequest
        @return: GetUploadAudioDataParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_audio_data_params_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: ccc20200701_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ccc20200701_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: ccc20200701_models.GetUserRequest,
    ) -> ccc20200701_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ccc20200701_models.GetUserRequest,
    ) -> ccc20200701_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_video_with_options(
        self,
        request: ccc20200701_models.GetVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetVideoResponse:
        """
        @summary 获取视频
        
        @param request: GetVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_with_options_async(
        self,
        request: ccc20200701_models.GetVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetVideoResponse:
        """
        @summary 获取视频
        
        @param request: GetVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video(
        self,
        request: ccc20200701_models.GetVideoRequest,
    ) -> ccc20200701_models.GetVideoResponse:
        """
        @summary 获取视频
        
        @param request: GetVideoRequest
        @return: GetVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_with_options(request, runtime)

    async def get_video_async(
        self,
        request: ccc20200701_models.GetVideoRequest,
    ) -> ccc20200701_models.GetVideoResponse:
        """
        @summary 获取视频
        
        @param request: GetVideoRequest
        @return: GetVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_video_with_options_async(request, runtime)

    def get_visitor_login_details_with_options(
        self,
        request: ccc20200701_models.GetVisitorLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetVisitorLoginDetailsResponse:
        """
        @param request: GetVisitorLoginDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVisitorLoginDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.visitor_id):
            query['VisitorId'] = request.visitor_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVisitorLoginDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetVisitorLoginDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_visitor_login_details_with_options_async(
        self,
        request: ccc20200701_models.GetVisitorLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetVisitorLoginDetailsResponse:
        """
        @param request: GetVisitorLoginDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVisitorLoginDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.visitor_id):
            query['VisitorId'] = request.visitor_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVisitorLoginDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetVisitorLoginDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_visitor_login_details(
        self,
        request: ccc20200701_models.GetVisitorLoginDetailsRequest,
    ) -> ccc20200701_models.GetVisitorLoginDetailsResponse:
        """
        @param request: GetVisitorLoginDetailsRequest
        @return: GetVisitorLoginDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_visitor_login_details_with_options(request, runtime)

    async def get_visitor_login_details_async(
        self,
        request: ccc20200701_models.GetVisitorLoginDetailsRequest,
    ) -> ccc20200701_models.GetVisitorLoginDetailsResponse:
        """
        @param request: GetVisitorLoginDetailsRequest
        @return: GetVisitorLoginDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_visitor_login_details_with_options_async(request, runtime)

    def get_voicemail_recording_with_options(
        self,
        request: ccc20200701_models.GetVoicemailRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetVoicemailRecordingResponse:
        """
        @param request: GetVoicemailRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVoicemailRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVoicemailRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetVoicemailRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_voicemail_recording_with_options_async(
        self,
        request: ccc20200701_models.GetVoicemailRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetVoicemailRecordingResponse:
        """
        @param request: GetVoicemailRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVoicemailRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVoicemailRecording',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.GetVoicemailRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_voicemail_recording(
        self,
        request: ccc20200701_models.GetVoicemailRecordingRequest,
    ) -> ccc20200701_models.GetVoicemailRecordingResponse:
        """
        @param request: GetVoicemailRecordingRequest
        @return: GetVoicemailRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_voicemail_recording_with_options(request, runtime)

    async def get_voicemail_recording_async(
        self,
        request: ccc20200701_models.GetVoicemailRecordingRequest,
    ) -> ccc20200701_models.GetVoicemailRecordingResponse:
        """
        @param request: GetVoicemailRecordingRequest
        @return: GetVoicemailRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_voicemail_recording_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: ccc20200701_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HoldCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.music):
            query['Music'] = request.music
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HoldCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.HoldCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: ccc20200701_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HoldCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.music):
            query['Music'] = request.music
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HoldCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.HoldCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hold_call(
        self,
        request: ccc20200701_models.HoldCallRequest,
    ) -> ccc20200701_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @return: HoldCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: ccc20200701_models.HoldCallRequest,
    ) -> ccc20200701_models.HoldCallResponse:
        """
        @param request: HoldCallRequest
        @return: HoldCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def import_admins_with_options(
        self,
        request: ccc20200701_models.ImportAdminsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportAdminsResponse:
        """
        @param request: ImportAdminsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportAdminsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportAdmins',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportAdminsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_admins_with_options_async(
        self,
        request: ccc20200701_models.ImportAdminsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportAdminsResponse:
        """
        @param request: ImportAdminsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportAdminsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportAdmins',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportAdminsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_admins(
        self,
        request: ccc20200701_models.ImportAdminsRequest,
    ) -> ccc20200701_models.ImportAdminsResponse:
        """
        @param request: ImportAdminsRequest
        @return: ImportAdminsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_admins_with_options(request, runtime)

    async def import_admins_async(
        self,
        request: ccc20200701_models.ImportAdminsRequest,
    ) -> ccc20200701_models.ImportAdminsResponse:
        """
        @param request: ImportAdminsRequest
        @return: ImportAdminsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_admins_with_options_async(request, runtime)

    def import_corp_numbers_with_options(
        self,
        request: ccc20200701_models.ImportCorpNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportCorpNumbersResponse:
        """
        @param request: ImportCorpNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportCorpNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.corp_name):
            query['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportCorpNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportCorpNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_corp_numbers_with_options_async(
        self,
        request: ccc20200701_models.ImportCorpNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportCorpNumbersResponse:
        """
        @param request: ImportCorpNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportCorpNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.corp_name):
            query['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportCorpNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportCorpNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_corp_numbers(
        self,
        request: ccc20200701_models.ImportCorpNumbersRequest,
    ) -> ccc20200701_models.ImportCorpNumbersResponse:
        """
        @param request: ImportCorpNumbersRequest
        @return: ImportCorpNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_corp_numbers_with_options(request, runtime)

    async def import_corp_numbers_async(
        self,
        request: ccc20200701_models.ImportCorpNumbersRequest,
    ) -> ccc20200701_models.ImportCorpNumbersResponse:
        """
        @param request: ImportCorpNumbersRequest
        @return: ImportCorpNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_corp_numbers_with_options_async(request, runtime)

    def import_custom_call_tagging_with_options(
        self,
        request: ccc20200701_models.ImportCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ImportCustomCallTagging is deprecated, please use CCC::2020-07-01::ImportCustomCallTaggings instead.
        
        @summary 文件导入呼入控制号码
        
        @param request: ImportCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_custom_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.ImportCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ImportCustomCallTagging is deprecated, please use CCC::2020-07-01::ImportCustomCallTaggings instead.
        
        @summary 文件导入呼入控制号码
        
        @param request: ImportCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_custom_call_tagging(
        self,
        request: ccc20200701_models.ImportCustomCallTaggingRequest,
    ) -> ccc20200701_models.ImportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ImportCustomCallTagging is deprecated, please use CCC::2020-07-01::ImportCustomCallTaggings instead.
        
        @summary 文件导入呼入控制号码
        
        @param request: ImportCustomCallTaggingRequest
        @return: ImportCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.import_custom_call_tagging_with_options(request, runtime)

    async def import_custom_call_tagging_async(
        self,
        request: ccc20200701_models.ImportCustomCallTaggingRequest,
    ) -> ccc20200701_models.ImportCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ImportCustomCallTagging is deprecated, please use CCC::2020-07-01::ImportCustomCallTaggings instead.
        
        @summary 文件导入呼入控制号码
        
        @param request: ImportCustomCallTaggingRequest
        @return: ImportCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_custom_call_tagging_with_options_async(request, runtime)

    def import_do_not_call_numbers_with_options(
        self,
        request: ccc20200701_models.ImportDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportDoNotCallNumbersResponse:
        """
        @summary 添加黑名单号码
        
        @param request: ImportDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_do_not_call_numbers_with_options_async(
        self,
        request: ccc20200701_models.ImportDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportDoNotCallNumbersResponse:
        """
        @summary 添加黑名单号码
        
        @param request: ImportDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_do_not_call_numbers(
        self,
        request: ccc20200701_models.ImportDoNotCallNumbersRequest,
    ) -> ccc20200701_models.ImportDoNotCallNumbersResponse:
        """
        @summary 添加黑名单号码
        
        @param request: ImportDoNotCallNumbersRequest
        @return: ImportDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_do_not_call_numbers_with_options(request, runtime)

    async def import_do_not_call_numbers_async(
        self,
        request: ccc20200701_models.ImportDoNotCallNumbersRequest,
    ) -> ccc20200701_models.ImportDoNotCallNumbersResponse:
        """
        @summary 添加黑名单号码
        
        @param request: ImportDoNotCallNumbersRequest
        @return: ImportDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_do_not_call_numbers_with_options_async(request, runtime)

    def import_documents_with_options(
        self,
        request: ccc20200701_models.ImportDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportDocumentsResponse:
        """
        @param request: ImportDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportDocumentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_file_key):
            body['OssFileKey'] = request.oss_file_key
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportDocuments',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_documents_with_options_async(
        self,
        request: ccc20200701_models.ImportDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ImportDocumentsResponse:
        """
        @param request: ImportDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportDocumentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_file_key):
            body['OssFileKey'] = request.oss_file_key
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportDocuments',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ImportDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_documents(
        self,
        request: ccc20200701_models.ImportDocumentsRequest,
    ) -> ccc20200701_models.ImportDocumentsResponse:
        """
        @param request: ImportDocumentsRequest
        @return: ImportDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_documents_with_options(request, runtime)

    async def import_documents_async(
        self,
        request: ccc20200701_models.ImportDocumentsRequest,
    ) -> ccc20200701_models.ImportDocumentsResponse:
        """
        @param request: ImportDocumentsRequest
        @return: ImportDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_documents_with_options_async(request, runtime)

    def initiate_attended_transfer_with_options(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        """
        @param request: InitiateAttendedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitiateAttendedTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not UtilClient.is_unset(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not UtilClient.is_unset(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not UtilClient.is_unset(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.transferee):
            query['Transferee'] = request.transferee
        if not UtilClient.is_unset(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not UtilClient.is_unset(request.transferor):
            query['Transferor'] = request.transferor
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitiateAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InitiateAttendedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def initiate_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        """
        @param request: InitiateAttendedTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitiateAttendedTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_priority):
            query['CallPriority'] = request.call_priority
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.queuing_overflow_threshold):
            query['QueuingOverflowThreshold'] = request.queuing_overflow_threshold
        if not UtilClient.is_unset(request.queuing_timeout_seconds):
            query['QueuingTimeoutSeconds'] = request.queuing_timeout_seconds
        if not UtilClient.is_unset(request.routing_type):
            query['RoutingType'] = request.routing_type
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        if not UtilClient.is_unset(request.strategy_params):
            query['StrategyParams'] = request.strategy_params
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.transferee):
            query['Transferee'] = request.transferee
        if not UtilClient.is_unset(request.transferee_type):
            query['TransfereeType'] = request.transferee_type
        if not UtilClient.is_unset(request.transferor):
            query['Transferor'] = request.transferor
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitiateAttendedTransfer',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InitiateAttendedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initiate_attended_transfer(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        """
        @param request: InitiateAttendedTransferRequest
        @return: InitiateAttendedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initiate_attended_transfer_with_options(request, runtime)

    async def initiate_attended_transfer_async(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        """
        @param request: InitiateAttendedTransferRequest
        @return: InitiateAttendedTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initiate_attended_transfer_with_options_async(request, runtime)

    def intercept_call_with_options(
        self,
        request: ccc20200701_models.InterceptCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InterceptCallResponse:
        """
        @param request: InterceptCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InterceptCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intercepted_user_id):
            query['InterceptedUserId'] = request.intercepted_user_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InterceptCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InterceptCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def intercept_call_with_options_async(
        self,
        request: ccc20200701_models.InterceptCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InterceptCallResponse:
        """
        @param request: InterceptCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InterceptCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intercepted_user_id):
            query['InterceptedUserId'] = request.intercepted_user_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InterceptCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.InterceptCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def intercept_call(
        self,
        request: ccc20200701_models.InterceptCallRequest,
    ) -> ccc20200701_models.InterceptCallResponse:
        """
        @param request: InterceptCallRequest
        @return: InterceptCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.intercept_call_with_options(request, runtime)

    async def intercept_call_async(
        self,
        request: ccc20200701_models.InterceptCallRequest,
    ) -> ccc20200701_models.InterceptCallResponse:
        """
        @param request: InterceptCallRequest
        @return: InterceptCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.intercept_call_with_options_async(request, runtime)

    def launch_authentication_with_options(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        """
        @param request: LaunchAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LaunchAuthenticationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchAuthentication',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_authentication_with_options_async(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        """
        @param request: LaunchAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LaunchAuthenticationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchAuthentication',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_authentication(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        """
        @param request: LaunchAuthenticationRequest
        @return: LaunchAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.launch_authentication_with_options(request, runtime)

    async def launch_authentication_async(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        """
        @param request: LaunchAuthenticationRequest
        @return: LaunchAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.launch_authentication_with_options_async(request, runtime)

    def launch_survey_with_options(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        """
        @param request: LaunchSurveyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LaunchSurveyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.sms_metadata_id):
            query['SmsMetadataId'] = request.sms_metadata_id
        if not UtilClient.is_unset(request.survey_channel):
            query['SurveyChannel'] = request.survey_channel
        if not UtilClient.is_unset(request.survey_template_id):
            query['SurveyTemplateId'] = request.survey_template_id
        if not UtilClient.is_unset(request.survey_template_variables):
            query['SurveyTemplateVariables'] = request.survey_template_variables
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchSurvey',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchSurveyResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_survey_with_options_async(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        """
        @param request: LaunchSurveyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LaunchSurveyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.sms_metadata_id):
            query['SmsMetadataId'] = request.sms_metadata_id
        if not UtilClient.is_unset(request.survey_channel):
            query['SurveyChannel'] = request.survey_channel
        if not UtilClient.is_unset(request.survey_template_id):
            query['SurveyTemplateId'] = request.survey_template_id
        if not UtilClient.is_unset(request.survey_template_variables):
            query['SurveyTemplateVariables'] = request.survey_template_variables
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LaunchSurvey',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchSurveyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_survey(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        """
        @param request: LaunchSurveyRequest
        @return: LaunchSurveyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.launch_survey_with_options(request, runtime)

    async def launch_survey_async(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        """
        @param request: LaunchSurveyRequest
        @return: LaunchSurveyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.launch_survey_with_options_async(request, runtime)

    def list_agent_state_logs_with_options(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        """
        @param request: ListAgentStateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentStateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentStateLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_state_logs_with_options_async(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        """
        @param request: ListAgentStateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentStateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentStateLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_state_logs(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        """
        @param request: ListAgentStateLogsRequest
        @return: ListAgentStateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_agent_state_logs_with_options(request, runtime)

    async def list_agent_state_logs_async(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        """
        @param request: ListAgentStateLogsRequest
        @return: ListAgentStateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_state_logs_with_options_async(request, runtime)

    def list_agent_states_with_options(
        self,
        request: ccc20200701_models.ListAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStatesResponse:
        """
        @deprecated OpenAPI ListAgentStates is deprecated, please use CCC::2020-07-01::ListRealtimeAgentStates instead.
        
        @summary ListAgentStates for ACC
        
        @param request: ListAgentStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentStatesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_ids):
            query['AgentIds'] = request.agent_ids
        if not UtilClient.is_unset(request.exclude_offline_users):
            query['ExcludeOfflineUsers'] = request.exclude_offline_users
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_states_with_options_async(
        self,
        request: ccc20200701_models.ListAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStatesResponse:
        """
        @deprecated OpenAPI ListAgentStates is deprecated, please use CCC::2020-07-01::ListRealtimeAgentStates instead.
        
        @summary ListAgentStates for ACC
        
        @param request: ListAgentStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentStatesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_ids):
            query['AgentIds'] = request.agent_ids
        if not UtilClient.is_unset(request.exclude_offline_users):
            query['ExcludeOfflineUsers'] = request.exclude_offline_users
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_states(
        self,
        request: ccc20200701_models.ListAgentStatesRequest,
    ) -> ccc20200701_models.ListAgentStatesResponse:
        """
        @deprecated OpenAPI ListAgentStates is deprecated, please use CCC::2020-07-01::ListRealtimeAgentStates instead.
        
        @summary ListAgentStates for ACC
        
        @param request: ListAgentStatesRequest
        @return: ListAgentStatesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_agent_states_with_options(request, runtime)

    async def list_agent_states_async(
        self,
        request: ccc20200701_models.ListAgentStatesRequest,
    ) -> ccc20200701_models.ListAgentStatesResponse:
        """
        @deprecated OpenAPI ListAgentStates is deprecated, please use CCC::2020-07-01::ListRealtimeAgentStates instead.
        
        @summary ListAgentStates for ACC
        
        @param request: ListAgentStatesRequest
        @return: ListAgentStatesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_states_with_options_async(request, runtime)

    def list_agent_summary_reports_since_midnight_with_options(
        self,
        request: ccc20200701_models.ListAgentSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListAgentSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalAgentReport instead.
        
        @summary ListAgentSummaryReportsSinceMidnight for acc
        
        @param request: ListAgentSummaryReportsSinceMidnightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentSummaryReportsSinceMidnightResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentSummaryReportsSinceMidnight',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentSummaryReportsSinceMidnightResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_summary_reports_since_midnight_with_options_async(
        self,
        request: ccc20200701_models.ListAgentSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListAgentSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalAgentReport instead.
        
        @summary ListAgentSummaryReportsSinceMidnight for acc
        
        @param request: ListAgentSummaryReportsSinceMidnightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentSummaryReportsSinceMidnightResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentSummaryReportsSinceMidnight',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentSummaryReportsSinceMidnightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_summary_reports_since_midnight(
        self,
        request: ccc20200701_models.ListAgentSummaryReportsSinceMidnightRequest,
    ) -> ccc20200701_models.ListAgentSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListAgentSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalAgentReport instead.
        
        @summary ListAgentSummaryReportsSinceMidnight for acc
        
        @param request: ListAgentSummaryReportsSinceMidnightRequest
        @return: ListAgentSummaryReportsSinceMidnightResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_agent_summary_reports_since_midnight_with_options(request, runtime)

    async def list_agent_summary_reports_since_midnight_async(
        self,
        request: ccc20200701_models.ListAgentSummaryReportsSinceMidnightRequest,
    ) -> ccc20200701_models.ListAgentSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListAgentSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalAgentReport instead.
        
        @summary ListAgentSummaryReportsSinceMidnight for acc
        
        @param request: ListAgentSummaryReportsSinceMidnightRequest
        @return: ListAgentSummaryReportsSinceMidnightResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_summary_reports_since_midnight_with_options_async(request, runtime)

    def list_attempts_with_options(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAttemptsResponse:
        """
        @summary 获取预测式外呼呼叫记录
        
        @param request: ListAttemptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAttemptsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAttempts',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAttemptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_attempts_with_options_async(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAttemptsResponse:
        """
        @summary 获取预测式外呼呼叫记录
        
        @param request: ListAttemptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAttemptsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAttempts',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAttemptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_attempts(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
    ) -> ccc20200701_models.ListAttemptsResponse:
        """
        @summary 获取预测式外呼呼叫记录
        
        @param request: ListAttemptsRequest
        @return: ListAttemptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_attempts_with_options(request, runtime)

    async def list_attempts_async(
        self,
        request: ccc20200701_models.ListAttemptsRequest,
    ) -> ccc20200701_models.ListAttemptsResponse:
        """
        @summary 获取预测式外呼呼叫记录
        
        @param request: ListAttemptsRequest
        @return: ListAttemptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_attempts_with_options_async(request, runtime)

    def list_audio_files_with_options(
        self,
        request: ccc20200701_models.ListAudioFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAudioFilesResponse:
        """
        @summary 获取音频文件列表
        
        @param request: ListAudioFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAudioFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAudioFiles',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAudioFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_audio_files_with_options_async(
        self,
        request: ccc20200701_models.ListAudioFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAudioFilesResponse:
        """
        @summary 获取音频文件列表
        
        @param request: ListAudioFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAudioFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAudioFiles',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAudioFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_audio_files(
        self,
        request: ccc20200701_models.ListAudioFilesRequest,
    ) -> ccc20200701_models.ListAudioFilesResponse:
        """
        @summary 获取音频文件列表
        
        @param request: ListAudioFilesRequest
        @return: ListAudioFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_audio_files_with_options(request, runtime)

    async def list_audio_files_async(
        self,
        request: ccc20200701_models.ListAudioFilesRequest,
    ) -> ccc20200701_models.ListAudioFilesResponse:
        """
        @summary 获取音频文件列表
        
        @param request: ListAudioFilesRequest
        @return: ListAudioFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_audio_files_with_options_async(request, runtime)

    def list_blacklist_call_taggings_with_options(
        self,
        request: ccc20200701_models.ListBlacklistCallTaggingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBlacklistCallTaggingsResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ListBlacklistCallTaggingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBlacklistCallTaggingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBlacklistCallTaggings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBlacklistCallTaggingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_blacklist_call_taggings_with_options_async(
        self,
        request: ccc20200701_models.ListBlacklistCallTaggingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBlacklistCallTaggingsResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ListBlacklistCallTaggingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBlacklistCallTaggingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBlacklistCallTaggings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBlacklistCallTaggingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_blacklist_call_taggings(
        self,
        request: ccc20200701_models.ListBlacklistCallTaggingsRequest,
    ) -> ccc20200701_models.ListBlacklistCallTaggingsResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ListBlacklistCallTaggingsRequest
        @return: ListBlacklistCallTaggingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_blacklist_call_taggings_with_options(request, runtime)

    async def list_blacklist_call_taggings_async(
        self,
        request: ccc20200701_models.ListBlacklistCallTaggingsRequest,
    ) -> ccc20200701_models.ListBlacklistCallTaggingsResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ListBlacklistCallTaggingsRequest
        @return: ListBlacklistCallTaggingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_blacklist_call_taggings_with_options_async(request, runtime)

    def list_brief_skill_groups_with_options(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        """
        @param request: ListBriefSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBriefSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBriefSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBriefSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_brief_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        """
        @param request: ListBriefSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBriefSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBriefSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBriefSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_brief_skill_groups(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        """
        @param request: ListBriefSkillGroupsRequest
        @return: ListBriefSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_brief_skill_groups_with_options(request, runtime)

    async def list_brief_skill_groups_async(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        """
        @param request: ListBriefSkillGroupsRequest
        @return: ListBriefSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_brief_skill_groups_with_options_async(request, runtime)

    def list_call_detail_records_with_options(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        """
        @param request: ListCallDetailRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCallDetailRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.contact_disposition):
            query['ContactDisposition'] = request.contact_disposition
        if not UtilClient.is_unset(request.contact_disposition_list):
            query['ContactDispositionList'] = request.contact_disposition_list
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.contact_type_list):
            query['ContactTypeList'] = request.contact_type_list
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.early_media_state_list):
            query['EarlyMediaStateList'] = request.early_media_state_list
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.satisfaction_description_list):
            query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        if not UtilClient.is_unset(request.satisfaction_list):
            query['SatisfactionList'] = request.satisfaction_list
        if not UtilClient.is_unset(request.satisfaction_survey_channel):
            query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallDetailRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_detail_records_with_options_async(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        """
        @param request: ListCallDetailRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCallDetailRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.contact_disposition):
            query['ContactDisposition'] = request.contact_disposition
        if not UtilClient.is_unset(request.contact_disposition_list):
            query['ContactDispositionList'] = request.contact_disposition_list
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.contact_type_list):
            query['ContactTypeList'] = request.contact_type_list
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.early_media_state_list):
            query['EarlyMediaStateList'] = request.early_media_state_list
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.satisfaction_description_list):
            query['SatisfactionDescriptionList'] = request.satisfaction_description_list
        if not UtilClient.is_unset(request.satisfaction_list):
            query['SatisfactionList'] = request.satisfaction_list
        if not UtilClient.is_unset(request.satisfaction_survey_channel):
            query['SatisfactionSurveyChannel'] = request.satisfaction_survey_channel
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallDetailRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_detail_records(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        """
        @param request: ListCallDetailRecordsRequest
        @return: ListCallDetailRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    async def list_call_detail_records_async(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        """
        @param request: ListCallDetailRecordsRequest
        @return: ListCallDetailRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_call_detail_records_with_options_async(request, runtime)

    def list_call_tags_with_options(
        self,
        request: ccc20200701_models.ListCallTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallTagsResponse:
        """
        @summary 列出号码标签
        
        @param request: ListCallTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCallTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallTags',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_tags_with_options_async(
        self,
        request: ccc20200701_models.ListCallTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallTagsResponse:
        """
        @summary 列出号码标签
        
        @param request: ListCallTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCallTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallTags',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_tags(
        self,
        request: ccc20200701_models.ListCallTagsRequest,
    ) -> ccc20200701_models.ListCallTagsResponse:
        """
        @summary 列出号码标签
        
        @param request: ListCallTagsRequest
        @return: ListCallTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_call_tags_with_options(request, runtime)

    async def list_call_tags_async(
        self,
        request: ccc20200701_models.ListCallTagsRequest,
    ) -> ccc20200701_models.ListCallTagsResponse:
        """
        @summary 列出号码标签
        
        @param request: ListCallTagsRequest
        @return: ListCallTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_call_tags_with_options_async(request, runtime)

    def list_campaign_trending_report_with_options(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        """
        @summary 获取预测式外呼活动趋势报表
        
        @param request: ListCampaignTrendingReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCampaignTrendingReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaignTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignTrendingReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_campaign_trending_report_with_options_async(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        """
        @summary 获取预测式外呼活动趋势报表
        
        @param request: ListCampaignTrendingReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCampaignTrendingReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaignTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignTrendingReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_campaign_trending_report(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        """
        @summary 获取预测式外呼活动趋势报表
        
        @param request: ListCampaignTrendingReportRequest
        @return: ListCampaignTrendingReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_campaign_trending_report_with_options(request, runtime)

    async def list_campaign_trending_report_async(
        self,
        request: ccc20200701_models.ListCampaignTrendingReportRequest,
    ) -> ccc20200701_models.ListCampaignTrendingReportResponse:
        """
        @summary 获取预测式外呼活动趋势报表
        
        @param request: ListCampaignTrendingReportRequest
        @return: ListCampaignTrendingReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_campaign_trending_report_with_options_async(request, runtime)

    def list_campaigns_with_options(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignsResponse:
        """
        @summary 获取预测式外呼活动列表
        
        @param request: ListCampaignsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCampaignsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actual_start_time_from):
            query['ActualStartTimeFrom'] = request.actual_start_time_from
        if not UtilClient.is_unset(request.actual_start_time_to):
            query['ActualStartTimeTo'] = request.actual_start_time_to
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.planed_start_time_from):
            query['PlanedStartTimeFrom'] = request.planed_start_time_from
        if not UtilClient.is_unset(request.planed_start_time_to):
            query['PlanedStartTimeTo'] = request.planed_start_time_to
        if not UtilClient.is_unset(request.queue_id):
            query['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaigns',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_campaigns_with_options_async(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCampaignsResponse:
        """
        @summary 获取预测式外呼活动列表
        
        @param request: ListCampaignsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCampaignsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actual_start_time_from):
            query['ActualStartTimeFrom'] = request.actual_start_time_from
        if not UtilClient.is_unset(request.actual_start_time_to):
            query['ActualStartTimeTo'] = request.actual_start_time_to
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.planed_start_time_from):
            query['PlanedStartTimeFrom'] = request.planed_start_time_from
        if not UtilClient.is_unset(request.planed_start_time_to):
            query['PlanedStartTimeTo'] = request.planed_start_time_to
        if not UtilClient.is_unset(request.queue_id):
            query['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaigns',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCampaignsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_campaigns(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
    ) -> ccc20200701_models.ListCampaignsResponse:
        """
        @summary 获取预测式外呼活动列表
        
        @param request: ListCampaignsRequest
        @return: ListCampaignsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_campaigns_with_options(request, runtime)

    async def list_campaigns_async(
        self,
        request: ccc20200701_models.ListCampaignsRequest,
    ) -> ccc20200701_models.ListCampaignsResponse:
        """
        @summary 获取预测式外呼活动列表
        
        @param request: ListCampaignsRequest
        @return: ListCampaignsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_campaigns_with_options_async(request, runtime)

    def list_cases_with_options(
        self,
        request: ccc20200701_models.ListCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCasesResponse:
        """
        @summary 获取预测式外呼活动的联系人呼叫详情
        
        @param request: ListCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cases_with_options_async(
        self,
        request: ccc20200701_models.ListCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCasesResponse:
        """
        @summary 获取预测式外呼活动的联系人呼叫详情
        
        @param request: ListCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cases(
        self,
        request: ccc20200701_models.ListCasesRequest,
    ) -> ccc20200701_models.ListCasesResponse:
        """
        @summary 获取预测式外呼活动的联系人呼叫详情
        
        @param request: ListCasesRequest
        @return: ListCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cases_with_options(request, runtime)

    async def list_cases_async(
        self,
        request: ccc20200701_models.ListCasesRequest,
    ) -> ccc20200701_models.ListCasesResponse:
        """
        @summary 获取预测式外呼活动的联系人呼叫详情
        
        @param request: ListCasesRequest
        @return: ListCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cases_with_options_async(request, runtime)

    def list_config_items_with_options(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        """
        @param request: ListConfigItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListConfigItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_items_with_options_async(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        """
        @param request: ListConfigItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListConfigItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_items(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        """
        @param request: ListConfigItemsRequest
        @return: ListConfigItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_config_items_with_options(request, runtime)

    async def list_config_items_async(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        """
        @param request: ListConfigItemsRequest
        @return: ListConfigItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_config_items_with_options_async(request, runtime)

    def list_contact_flows_with_options(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        """
        @param request: ListContactFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContactFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContactFlows',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListContactFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contact_flows_with_options_async(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        """
        @param request: ListContactFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContactFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContactFlows',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListContactFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contact_flows(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        """
        @param request: ListContactFlowsRequest
        @return: ListContactFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_contact_flows_with_options(request, runtime)

    async def list_contact_flows_async(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        """
        @param request: ListContactFlowsRequest
        @return: ListContactFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_contact_flows_with_options_async(request, runtime)

    def list_custom_call_tagging_with_options(
        self,
        request: ccc20200701_models.ListCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ListCustomCallTagging is deprecated, please use CCC::2020-07-01::ListCustomCallTaggings instead.
        
        @summary 列出呼入控制号码
        
        @param request: ListCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.ListCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ListCustomCallTagging is deprecated, please use CCC::2020-07-01::ListCustomCallTaggings instead.
        
        @summary 列出呼入控制号码
        
        @param request: ListCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomCallTaggingResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_call_tagging(
        self,
        request: ccc20200701_models.ListCustomCallTaggingRequest,
    ) -> ccc20200701_models.ListCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ListCustomCallTagging is deprecated, please use CCC::2020-07-01::ListCustomCallTaggings instead.
        
        @summary 列出呼入控制号码
        
        @param request: ListCustomCallTaggingRequest
        @return: ListCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_call_tagging_with_options(request, runtime)

    async def list_custom_call_tagging_async(
        self,
        request: ccc20200701_models.ListCustomCallTaggingRequest,
    ) -> ccc20200701_models.ListCustomCallTaggingResponse:
        """
        @deprecated OpenAPI ListCustomCallTagging is deprecated, please use CCC::2020-07-01::ListCustomCallTaggings instead.
        
        @summary 列出呼入控制号码
        
        @param request: ListCustomCallTaggingRequest
        @return: ListCustomCallTaggingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_call_tagging_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: ccc20200701_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDevicesResponse:
        """
        @param request: ListDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: ccc20200701_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDevicesResponse:
        """
        @param request: ListDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_devices(
        self,
        request: ccc20200701_models.ListDevicesRequest,
    ) -> ccc20200701_models.ListDevicesResponse:
        """
        @param request: ListDevicesRequest
        @return: ListDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: ccc20200701_models.ListDevicesRequest,
    ) -> ccc20200701_models.ListDevicesResponse:
        """
        @param request: ListDevicesRequest
        @return: ListDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def list_do_not_call_numbers_with_options(
        self,
        request: ccc20200701_models.ListDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDoNotCallNumbersResponse:
        """
        @summary 查询黑名单号码
        
        @param request: ListDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_do_not_call_numbers_with_options_async(
        self,
        request: ccc20200701_models.ListDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDoNotCallNumbersResponse:
        """
        @summary 查询黑名单号码
        
        @param request: ListDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_do_not_call_numbers(
        self,
        request: ccc20200701_models.ListDoNotCallNumbersRequest,
    ) -> ccc20200701_models.ListDoNotCallNumbersResponse:
        """
        @summary 查询黑名单号码
        
        @param request: ListDoNotCallNumbersRequest
        @return: ListDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_do_not_call_numbers_with_options(request, runtime)

    async def list_do_not_call_numbers_async(
        self,
        request: ccc20200701_models.ListDoNotCallNumbersRequest,
    ) -> ccc20200701_models.ListDoNotCallNumbersResponse:
        """
        @summary 查询黑名单号码
        
        @param request: ListDoNotCallNumbersRequest
        @return: ListDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_do_not_call_numbers_with_options_async(request, runtime)

    def list_documents_with_options(
        self,
        tmp_req: ccc20200701_models.ListDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDocumentsResponse:
        """
        @param tmp_req: ListDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.ListDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sorts):
            request.sorts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sorts, 'Sorts', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.search_pattern):
            body['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.sorts_shrink):
            body['Sorts'] = request.sorts_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDocuments',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_documents_with_options_async(
        self,
        tmp_req: ccc20200701_models.ListDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDocumentsResponse:
        """
        @param tmp_req: ListDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.ListDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sorts):
            request.sorts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sorts, 'Sorts', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.search_pattern):
            body['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.sorts_shrink):
            body['Sorts'] = request.sorts_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDocuments',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_documents(
        self,
        request: ccc20200701_models.ListDocumentsRequest,
    ) -> ccc20200701_models.ListDocumentsResponse:
        """
        @param request: ListDocumentsRequest
        @return: ListDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_documents_with_options(request, runtime)

    async def list_documents_async(
        self,
        request: ccc20200701_models.ListDocumentsRequest,
    ) -> ccc20200701_models.ListDocumentsResponse:
        """
        @param request: ListDocumentsRequest
        @return: ListDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_documents_with_options_async(request, runtime)

    def list_historical_agent_report_with_options(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        """
        @param request: ListHistoricalAgentReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoricalAgentReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['StopTime'] = request.stop_time
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_agent_report_with_options_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        """
        @param request: ListHistoricalAgentReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoricalAgentReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['StopTime'] = request.stop_time
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_agent_report(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        """
        @param request: ListHistoricalAgentReportRequest
        @return: ListHistoricalAgentReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_historical_agent_report_with_options(request, runtime)

    async def list_historical_agent_report_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        """
        @param request: ListHistoricalAgentReportRequest
        @return: ListHistoricalAgentReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_historical_agent_report_with_options_async(request, runtime)

    def list_historical_agent_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListHistoricalAgentSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentSkillGroupReportResponse:
        """
        @summary ListHistoricalAgentSkillGroupReport
        
        @param request: ListHistoricalAgentSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoricalAgentSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalAgentSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_agent_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentSkillGroupReportResponse:
        """
        @summary ListHistoricalAgentSkillGroupReport
        
        @param request: ListHistoricalAgentSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoricalAgentSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalAgentSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_agent_skill_group_report(
        self,
        request: ccc20200701_models.ListHistoricalAgentSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentSkillGroupReportResponse:
        """
        @summary ListHistoricalAgentSkillGroupReport
        
        @param request: ListHistoricalAgentSkillGroupReportRequest
        @return: ListHistoricalAgentSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_historical_agent_skill_group_report_with_options(request, runtime)

    async def list_historical_agent_skill_group_report_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentSkillGroupReportResponse:
        """
        @summary ListHistoricalAgentSkillGroupReport
        
        @param request: ListHistoricalAgentSkillGroupReportRequest
        @return: ListHistoricalAgentSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_historical_agent_skill_group_report_with_options_async(request, runtime)

    def list_historical_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        """
        @param request: ListHistoricalSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoricalSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_historical_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        """
        @param request: ListHistoricalSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoricalSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_historical_skill_group_report(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        """
        @param request: ListHistoricalSkillGroupReportRequest
        @return: ListHistoricalSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_historical_skill_group_report_with_options(request, runtime)

    async def list_historical_skill_group_report_async(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        """
        @param request: ListHistoricalSkillGroupReportRequest
        @return: ListHistoricalSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_historical_skill_group_report_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: ccc20200701_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: ccc20200701_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: ccc20200701_models.ListInstancesRequest,
    ) -> ccc20200701_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: ccc20200701_models.ListInstancesRequest,
    ) -> ccc20200701_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_instances_of_user_with_options(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        """
        @param request: ListInstancesOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        """
        @param request: ListInstancesOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_of_user(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        """
        @param request: ListInstancesOfUserRequest
        @return: ListInstancesOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_of_user_with_options(request, runtime)

    async def list_instances_of_user_async(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        """
        @param request: ListInstancesOfUserRequest
        @return: ListInstancesOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_of_user_with_options_async(request, runtime)

    def list_interval_agent_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        """
        @param request: ListIntervalAgentReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalAgentReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_agent_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        """
        @param request: ListIntervalAgentReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalAgentReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalAgentReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_agent_report(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        """
        @param request: ListIntervalAgentReportRequest
        @return: ListIntervalAgentReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_interval_agent_report_with_options(request, runtime)

    async def list_interval_agent_report_async(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        """
        @param request: ListIntervalAgentReportRequest
        @return: ListIntervalAgentReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_agent_report_with_options_async(request, runtime)

    def list_interval_agent_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalAgentSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentSkillGroupReportResponse:
        """
        @summary ListIntervalAgentSkillGroupReport
        
        @param request: ListIntervalAgentSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalAgentSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalAgentSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_agent_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalAgentSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentSkillGroupReportResponse:
        """
        @summary ListIntervalAgentSkillGroupReport
        
        @param request: ListIntervalAgentSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalAgentSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalAgentSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_agent_skill_group_report(
        self,
        request: ccc20200701_models.ListIntervalAgentSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentSkillGroupReportResponse:
        """
        @summary ListIntervalAgentSkillGroupReport
        
        @param request: ListIntervalAgentSkillGroupReportRequest
        @return: ListIntervalAgentSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_interval_agent_skill_group_report_with_options(request, runtime)

    async def list_interval_agent_skill_group_report_async(
        self,
        request: ccc20200701_models.ListIntervalAgentSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentSkillGroupReportResponse:
        """
        @summary ListIntervalAgentSkillGroupReport
        
        @param request: ListIntervalAgentSkillGroupReportRequest
        @return: ListIntervalAgentSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_agent_skill_group_report_with_options_async(request, runtime)

    def list_interval_instance_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        """
        @param request: ListIntervalInstanceReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalInstanceReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalInstanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_instance_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        """
        @param request: ListIntervalInstanceReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalInstanceReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalInstanceReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalInstanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_instance_report(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        """
        @param request: ListIntervalInstanceReportRequest
        @return: ListIntervalInstanceReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_interval_instance_report_with_options(request, runtime)

    async def list_interval_instance_report_async(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        """
        @param request: ListIntervalInstanceReportRequest
        @return: ListIntervalInstanceReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_instance_report_with_options_async(request, runtime)

    def list_interval_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        """
        @param request: ListIntervalSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_interval_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        """
        @param request: ListIntervalSkillGroupReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervalSkillGroupReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalSkillGroupReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_interval_skill_group_report(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        """
        @param request: ListIntervalSkillGroupReportRequest
        @return: ListIntervalSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_interval_skill_group_report_with_options(request, runtime)

    async def list_interval_skill_group_report_async(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        """
        @param request: ListIntervalSkillGroupReportRequest
        @return: ListIntervalSkillGroupReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_skill_group_report_with_options_async(request, runtime)

    def list_ivr_tracking_details_with_options(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        """
        @param request: ListIvrTrackingDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIvrTrackingDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIvrTrackingDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIvrTrackingDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ivr_tracking_details_with_options_async(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        """
        @param request: ListIvrTrackingDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIvrTrackingDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIvrTrackingDetails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIvrTrackingDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ivr_tracking_details(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        """
        @param request: ListIvrTrackingDetailsRequest
        @return: ListIvrTrackingDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ivr_tracking_details_with_options(request, runtime)

    async def list_ivr_tracking_details_async(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        """
        @param request: ListIvrTrackingDetailsRequest
        @return: ListIvrTrackingDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ivr_tracking_details_with_options_async(request, runtime)

    def list_legacy_agent_event_logs_with_options(
        self,
        request: ccc20200701_models.ListLegacyAgentEventLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyAgentEventLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentEventLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentEventLogs
        
        @param request: ListLegacyAgentEventLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyAgentEventLogsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyAgentEventLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyAgentEventLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_agent_event_logs_with_options_async(
        self,
        request: ccc20200701_models.ListLegacyAgentEventLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyAgentEventLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentEventLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentEventLogs
        
        @param request: ListLegacyAgentEventLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyAgentEventLogsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyAgentEventLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyAgentEventLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_agent_event_logs(
        self,
        request: ccc20200701_models.ListLegacyAgentEventLogsRequest,
    ) -> ccc20200701_models.ListLegacyAgentEventLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentEventLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentEventLogs
        
        @param request: ListLegacyAgentEventLogsRequest
        @return: ListLegacyAgentEventLogsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_legacy_agent_event_logs_with_options(request, runtime)

    async def list_legacy_agent_event_logs_async(
        self,
        request: ccc20200701_models.ListLegacyAgentEventLogsRequest,
    ) -> ccc20200701_models.ListLegacyAgentEventLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentEventLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentEventLogs
        
        @param request: ListLegacyAgentEventLogsRequest
        @return: ListLegacyAgentEventLogsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_legacy_agent_event_logs_with_options_async(request, runtime)

    def list_legacy_agent_status_logs_with_options(
        self,
        request: ccc20200701_models.ListLegacyAgentStatusLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyAgentStatusLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentStatusLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentStatusLogs
        
        @param request: ListLegacyAgentStatusLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyAgentStatusLogsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyAgentStatusLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyAgentStatusLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_agent_status_logs_with_options_async(
        self,
        request: ccc20200701_models.ListLegacyAgentStatusLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyAgentStatusLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentStatusLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentStatusLogs
        
        @param request: ListLegacyAgentStatusLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyAgentStatusLogsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyAgentStatusLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyAgentStatusLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_agent_status_logs(
        self,
        request: ccc20200701_models.ListLegacyAgentStatusLogsRequest,
    ) -> ccc20200701_models.ListLegacyAgentStatusLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentStatusLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentStatusLogs
        
        @param request: ListLegacyAgentStatusLogsRequest
        @return: ListLegacyAgentStatusLogsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_legacy_agent_status_logs_with_options(request, runtime)

    async def list_legacy_agent_status_logs_async(
        self,
        request: ccc20200701_models.ListLegacyAgentStatusLogsRequest,
    ) -> ccc20200701_models.ListLegacyAgentStatusLogsResponse:
        """
        @deprecated OpenAPI ListLegacyAgentStatusLogs is deprecated, please use CCC::2020-07-01::ListAgentStateLogs instead.
        
        @summary ListLegacyAgentStatusLogs
        
        @param request: ListLegacyAgentStatusLogsRequest
        @return: ListLegacyAgentStatusLogsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_legacy_agent_status_logs_with_options_async(request, runtime)

    def list_legacy_appraise_logs_with_options(
        self,
        request: ccc20200701_models.ListLegacyAppraiseLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyAppraiseLogsResponse:
        """
        @summary ListLegacyAppraiseLogs
        
        @param request: ListLegacyAppraiseLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyAppraiseLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyAppraiseLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyAppraiseLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_appraise_logs_with_options_async(
        self,
        request: ccc20200701_models.ListLegacyAppraiseLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyAppraiseLogsResponse:
        """
        @summary ListLegacyAppraiseLogs
        
        @param request: ListLegacyAppraiseLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyAppraiseLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyAppraiseLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyAppraiseLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_appraise_logs(
        self,
        request: ccc20200701_models.ListLegacyAppraiseLogsRequest,
    ) -> ccc20200701_models.ListLegacyAppraiseLogsResponse:
        """
        @summary ListLegacyAppraiseLogs
        
        @param request: ListLegacyAppraiseLogsRequest
        @return: ListLegacyAppraiseLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_legacy_appraise_logs_with_options(request, runtime)

    async def list_legacy_appraise_logs_async(
        self,
        request: ccc20200701_models.ListLegacyAppraiseLogsRequest,
    ) -> ccc20200701_models.ListLegacyAppraiseLogsResponse:
        """
        @summary ListLegacyAppraiseLogs
        
        @param request: ListLegacyAppraiseLogsRequest
        @return: ListLegacyAppraiseLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_legacy_appraise_logs_with_options_async(request, runtime)

    def list_legacy_queue_event_logs_with_options(
        self,
        request: ccc20200701_models.ListLegacyQueueEventLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyQueueEventLogsResponse:
        """
        @summary ListLegacyQueueEventLogs
        
        @param request: ListLegacyQueueEventLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyQueueEventLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyQueueEventLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyQueueEventLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_legacy_queue_event_logs_with_options_async(
        self,
        request: ccc20200701_models.ListLegacyQueueEventLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListLegacyQueueEventLogsResponse:
        """
        @summary ListLegacyQueueEventLogs
        
        @param request: ListLegacyQueueEventLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLegacyQueueEventLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLegacyQueueEventLogs',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListLegacyQueueEventLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_legacy_queue_event_logs(
        self,
        request: ccc20200701_models.ListLegacyQueueEventLogsRequest,
    ) -> ccc20200701_models.ListLegacyQueueEventLogsResponse:
        """
        @summary ListLegacyQueueEventLogs
        
        @param request: ListLegacyQueueEventLogsRequest
        @return: ListLegacyQueueEventLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_legacy_queue_event_logs_with_options(request, runtime)

    async def list_legacy_queue_event_logs_async(
        self,
        request: ccc20200701_models.ListLegacyQueueEventLogsRequest,
    ) -> ccc20200701_models.ListLegacyQueueEventLogsResponse:
        """
        @summary ListLegacyQueueEventLogs
        
        @param request: ListLegacyQueueEventLogsRequest
        @return: ListLegacyQueueEventLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_legacy_queue_event_logs_with_options_async(request, runtime)

    def list_mono_recordings_with_options(
        self,
        request: ccc20200701_models.ListMonoRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListMonoRecordingsResponse:
        """
        @param request: ListMonoRecordingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMonoRecordingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMonoRecordings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListMonoRecordingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mono_recordings_with_options_async(
        self,
        request: ccc20200701_models.ListMonoRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListMonoRecordingsResponse:
        """
        @param request: ListMonoRecordingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMonoRecordingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMonoRecordings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListMonoRecordingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mono_recordings(
        self,
        request: ccc20200701_models.ListMonoRecordingsRequest,
    ) -> ccc20200701_models.ListMonoRecordingsResponse:
        """
        @param request: ListMonoRecordingsRequest
        @return: ListMonoRecordingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mono_recordings_with_options(request, runtime)

    async def list_mono_recordings_async(
        self,
        request: ccc20200701_models.ListMonoRecordingsRequest,
    ) -> ccc20200701_models.ListMonoRecordingsResponse:
        """
        @param request: ListMonoRecordingsRequest
        @return: ListMonoRecordingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mono_recordings_with_options_async(request, runtime)

    def list_multi_channel_recordings_with_options(
        self,
        request: ccc20200701_models.ListMultiChannelRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListMultiChannelRecordingsResponse:
        """
        @param request: ListMultiChannelRecordingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiChannelRecordingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiChannelRecordings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListMultiChannelRecordingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_channel_recordings_with_options_async(
        self,
        request: ccc20200701_models.ListMultiChannelRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListMultiChannelRecordingsResponse:
        """
        @param request: ListMultiChannelRecordingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiChannelRecordingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiChannelRecordings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListMultiChannelRecordingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_channel_recordings(
        self,
        request: ccc20200701_models.ListMultiChannelRecordingsRequest,
    ) -> ccc20200701_models.ListMultiChannelRecordingsResponse:
        """
        @param request: ListMultiChannelRecordingsRequest
        @return: ListMultiChannelRecordingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_multi_channel_recordings_with_options(request, runtime)

    async def list_multi_channel_recordings_async(
        self,
        request: ccc20200701_models.ListMultiChannelRecordingsRequest,
    ) -> ccc20200701_models.ListMultiChannelRecordingsResponse:
        """
        @param request: ListMultiChannelRecordingsRequest
        @return: ListMultiChannelRecordingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_multi_channel_recordings_with_options_async(request, runtime)

    def list_outbound_numbers_of_user_with_options(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        """
        @param request: ListOutboundNumbersOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOutboundNumbersOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOutboundNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListOutboundNumbersOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_numbers_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        """
        @param request: ListOutboundNumbersOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOutboundNumbersOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOutboundNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListOutboundNumbersOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_numbers_of_user(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        """
        @param request: ListOutboundNumbersOfUserRequest
        @return: ListOutboundNumbersOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_numbers_of_user_with_options(request, runtime)

    async def list_outbound_numbers_of_user_async(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        """
        @param request: ListOutboundNumbersOfUserRequest
        @return: ListOutboundNumbersOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_numbers_of_user_with_options_async(request, runtime)

    def list_personal_numbers_of_user_with_options(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        """
        @param request: ListPersonalNumbersOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPersonalNumbersOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPersonalNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPersonalNumbersOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_personal_numbers_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        """
        @param request: ListPersonalNumbersOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPersonalNumbersOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPersonalNumbersOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPersonalNumbersOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_personal_numbers_of_user(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        """
        @param request: ListPersonalNumbersOfUserRequest
        @return: ListPersonalNumbersOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_personal_numbers_of_user_with_options(request, runtime)

    async def list_personal_numbers_of_user_async(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        """
        @param request: ListPersonalNumbersOfUserRequest
        @return: ListPersonalNumbersOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_personal_numbers_of_user_with_options_async(request, runtime)

    def list_phone_numbers_with_options(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        """
        @summary 获取号码列表
        
        @param request: ListPhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        """
        @summary 获取号码列表
        
        @param request: ListPhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_numbers(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        """
        @summary 获取号码列表
        
        @param request: ListPhoneNumbersRequest
        @return: ListPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_with_options(request, runtime)

    async def list_phone_numbers_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        """
        @summary 获取号码列表
        
        @param request: ListPhoneNumbersRequest
        @return: ListPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_numbers_with_options_async(request, runtime)

    def list_phone_numbers_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        """
        @param request: ListPhoneNumbersOfSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneNumbersOfSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbersOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_numbers_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        """
        @param request: ListPhoneNumbersOfSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneNumbersOfSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhoneNumbersOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_numbers_of_skill_group(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        """
        @param request: ListPhoneNumbersOfSkillGroupRequest
        @return: ListPhoneNumbersOfSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_of_skill_group_with_options(request, runtime)

    async def list_phone_numbers_of_skill_group_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        """
        @param request: ListPhoneNumbersOfSkillGroupRequest
        @return: ListPhoneNumbersOfSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_numbers_of_skill_group_with_options_async(request, runtime)

    def list_privileges_of_user_with_options(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        """
        @param request: ListPrivilegesOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivilegesOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivilegesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPrivilegesOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_privileges_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        """
        @param request: ListPrivilegesOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivilegesOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivilegesOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPrivilegesOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_privileges_of_user(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        """
        @param request: ListPrivilegesOfUserRequest
        @return: ListPrivilegesOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_privileges_of_user_with_options(request, runtime)

    async def list_privileges_of_user_async(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        """
        @param request: ListPrivilegesOfUserRequest
        @return: ListPrivilegesOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_privileges_of_user_with_options_async(request, runtime)

    def list_ram_users_with_options(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRamUsersResponse:
        """
        @param request: ListRamUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRamUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRamUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ram_users_with_options_async(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRamUsersResponse:
        """
        @param request: ListRamUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRamUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRamUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ram_users(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
    ) -> ccc20200701_models.ListRamUsersResponse:
        """
        @param request: ListRamUsersRequest
        @return: ListRamUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ram_users_with_options(request, runtime)

    async def list_ram_users_async(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
    ) -> ccc20200701_models.ListRamUsersResponse:
        """
        @param request: ListRamUsersRequest
        @return: ListRamUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ram_users_with_options_async(request, runtime)

    def list_realtime_agent_states_with_options(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        """
        @param request: ListRealtimeAgentStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeAgentStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.work_mode_list):
            query['WorkModeList'] = request.work_mode_list
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        if not UtilClient.is_unset(request.state_list):
            body['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeAgentStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeAgentStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_agent_states_with_options_async(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        """
        @param request: ListRealtimeAgentStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeAgentStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.call_type_list):
            query['CallTypeList'] = request.call_type_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.work_mode_list):
            query['WorkModeList'] = request.work_mode_list
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        if not UtilClient.is_unset(request.state_list):
            body['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeAgentStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeAgentStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_agent_states(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        """
        @param request: ListRealtimeAgentStatesRequest
        @return: ListRealtimeAgentStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_agent_states_with_options(request, runtime)

    async def list_realtime_agent_states_async(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        """
        @param request: ListRealtimeAgentStatesRequest
        @return: ListRealtimeAgentStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_agent_states_with_options_async(request, runtime)

    def list_realtime_skill_group_states_with_options(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        """
        @param request: ListRealtimeSkillGroupStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeSkillGroupStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeSkillGroupStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeSkillGroupStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_skill_group_states_with_options_async(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        """
        @param request: ListRealtimeSkillGroupStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeSkillGroupStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.skill_group_id_list):
            body['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRealtimeSkillGroupStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeSkillGroupStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_skill_group_states(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        """
        @param request: ListRealtimeSkillGroupStatesRequest
        @return: ListRealtimeSkillGroupStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_skill_group_states_with_options(request, runtime)

    async def list_realtime_skill_group_states_async(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        """
        @param request: ListRealtimeSkillGroupStatesRequest
        @return: ListRealtimeSkillGroupStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_skill_group_states_with_options_async(request, runtime)

    def list_recent_call_detail_records_with_options(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        """
        @param request: ListRecentCallDetailRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentCallDetailRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecentCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRecentCallDetailRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_call_detail_records_with_options_async(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        """
        @param request: ListRecentCallDetailRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentCallDetailRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecentCallDetailRecords',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRecentCallDetailRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_call_detail_records(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        """
        @param request: ListRecentCallDetailRecordsRequest
        @return: ListRecentCallDetailRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recent_call_detail_records_with_options(request, runtime)

    async def list_recent_call_detail_records_async(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        """
        @param request: ListRecentCallDetailRecordsRequest
        @return: ListRecentCallDetailRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_recent_call_detail_records_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: ccc20200701_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRolesResponse:
        """
        @param request: ListRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: ccc20200701_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRolesResponse:
        """
        @param request: ListRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: ccc20200701_models.ListRolesRequest,
    ) -> ccc20200701_models.ListRolesResponse:
        """
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: ccc20200701_models.ListRolesRequest,
    ) -> ccc20200701_models.ListRolesResponse:
        """
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_skill_group_states_with_options(
        self,
        request: ccc20200701_models.ListSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupStatesResponse:
        """
        @deprecated OpenAPI ListSkillGroupStates is deprecated, please use CCC::2020-07-01::ListRealtimeSkillGroupStates instead.
        
        @summary ListSkillGroupStates for acc
        
        @param request: ListSkillGroupStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupStatesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroupStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_states_with_options_async(
        self,
        request: ccc20200701_models.ListSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupStatesResponse:
        """
        @deprecated OpenAPI ListSkillGroupStates is deprecated, please use CCC::2020-07-01::ListRealtimeSkillGroupStates instead.
        
        @summary ListSkillGroupStates for acc
        
        @param request: ListSkillGroupStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupStatesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroupStates',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group_states(
        self,
        request: ccc20200701_models.ListSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListSkillGroupStatesResponse:
        """
        @deprecated OpenAPI ListSkillGroupStates is deprecated, please use CCC::2020-07-01::ListRealtimeSkillGroupStates instead.
        
        @summary ListSkillGroupStates for acc
        
        @param request: ListSkillGroupStatesRequest
        @return: ListSkillGroupStatesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_states_with_options(request, runtime)

    async def list_skill_group_states_async(
        self,
        request: ccc20200701_models.ListSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListSkillGroupStatesResponse:
        """
        @deprecated OpenAPI ListSkillGroupStates is deprecated, please use CCC::2020-07-01::ListRealtimeSkillGroupStates instead.
        
        @summary ListSkillGroupStates for acc
        
        @param request: ListSkillGroupStatesRequest
        @return: ListSkillGroupStatesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_states_with_options_async(request, runtime)

    def list_skill_group_summary_reports_since_midnight_with_options(
        self,
        request: ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListSkillGroupSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalSkillGroupReport instead.
        
        @summary ListSkillGroupSummaryReportsSinceMidnight for acc
        
        @param request: ListSkillGroupSummaryReportsSinceMidnightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupSummaryReportsSinceMidnightResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroupSummaryReportsSinceMidnight',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_summary_reports_since_midnight_with_options_async(
        self,
        request: ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListSkillGroupSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalSkillGroupReport instead.
        
        @summary ListSkillGroupSummaryReportsSinceMidnight for acc
        
        @param request: ListSkillGroupSummaryReportsSinceMidnightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupSummaryReportsSinceMidnightResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroupSummaryReportsSinceMidnight',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group_summary_reports_since_midnight(
        self,
        request: ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
    ) -> ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListSkillGroupSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalSkillGroupReport instead.
        
        @summary ListSkillGroupSummaryReportsSinceMidnight for acc
        
        @param request: ListSkillGroupSummaryReportsSinceMidnightRequest
        @return: ListSkillGroupSummaryReportsSinceMidnightResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_summary_reports_since_midnight_with_options(request, runtime)

    async def list_skill_group_summary_reports_since_midnight_async(
        self,
        request: ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
    ) -> ccc20200701_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        """
        @deprecated OpenAPI ListSkillGroupSummaryReportsSinceMidnight is deprecated, please use CCC::2020-07-01::ListHistoricalSkillGroupReport instead.
        
        @summary ListSkillGroupSummaryReportsSinceMidnight for acc
        
        @param request: ListSkillGroupSummaryReportsSinceMidnightRequest
        @return: ListSkillGroupSummaryReportsSinceMidnightResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_summary_reports_since_midnight_with_options_async(request, runtime)

    def list_skill_groups_with_options(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        """
        @param request: ListSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        """
        @param request: ListSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_groups(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        """
        @param request: ListSkillGroupsRequest
        @return: ListSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_with_options(request, runtime)

    async def list_skill_groups_async(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        """
        @param request: ListSkillGroupsRequest
        @return: ListSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_groups_with_options_async(request, runtime)

    def list_skill_levels_of_user_with_options(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        """
        @param request: ListSkillLevelsOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillLevelsOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillLevelsOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_levels_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        """
        @param request: ListSkillLevelsOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillLevelsOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillLevelsOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_levels_of_user(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        """
        @param request: ListSkillLevelsOfUserRequest
        @return: ListSkillLevelsOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_skill_levels_of_user_with_options(request, runtime)

    async def list_skill_levels_of_user_async(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        """
        @param request: ListSkillLevelsOfUserRequest
        @return: ListSkillLevelsOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_levels_of_user_with_options_async(request, runtime)

    def list_unassigned_numbers_with_options(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        """
        @summary 获取未分配号码列表
        
        @param request: ListUnassignedNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUnassignedNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUnassignedNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUnassignedNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_unassigned_numbers_with_options_async(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        """
        @summary 获取未分配号码列表
        
        @param request: ListUnassignedNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUnassignedNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUnassignedNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUnassignedNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_unassigned_numbers(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        """
        @summary 获取未分配号码列表
        
        @param request: ListUnassignedNumbersRequest
        @return: ListUnassignedNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_unassigned_numbers_with_options(request, runtime)

    async def list_unassigned_numbers_async(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        """
        @summary 获取未分配号码列表
        
        @param request: ListUnassignedNumbersRequest
        @return: ListUnassignedNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_unassigned_numbers_with_options_async(request, runtime)

    def list_user_levels_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        """
        @param request: ListUserLevelsOfSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserLevelsOfSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUserLevelsOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_levels_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        """
        @param request: ListUserLevelsOfSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserLevelsOfSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUserLevelsOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_levels_of_skill_group(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        """
        @param request: ListUserLevelsOfSkillGroupRequest
        @return: ListUserLevelsOfSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_levels_of_skill_group_with_options(request, runtime)

    async def list_user_levels_of_skill_group_async(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        """
        @param request: ListUserLevelsOfSkillGroupRequest
        @return: ListUserLevelsOfSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_levels_of_skill_group_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ccc20200701_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ccc20200701_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: ccc20200701_models.ListUsersRequest,
    ) -> ccc20200701_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ccc20200701_models.ListUsersRequest,
    ) -> ccc20200701_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_voicemails_with_options(
        self,
        request: ccc20200701_models.ListVoicemailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListVoicemailsResponse:
        """
        @param request: ListVoicemailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVoicemailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoicemails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListVoicemailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voicemails_with_options_async(
        self,
        request: ccc20200701_models.ListVoicemailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListVoicemailsResponse:
        """
        @param request: ListVoicemailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVoicemailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoicemails',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ListVoicemailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voicemails(
        self,
        request: ccc20200701_models.ListVoicemailsRequest,
    ) -> ccc20200701_models.ListVoicemailsResponse:
        """
        @param request: ListVoicemailsRequest
        @return: ListVoicemailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_voicemails_with_options(request, runtime)

    async def list_voicemails_async(
        self,
        request: ccc20200701_models.ListVoicemailsRequest,
    ) -> ccc20200701_models.ListVoicemailsResponse:
        """
        @param request: ListVoicemailsRequest
        @return: ListVoicemailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_voicemails_with_options_async(request, runtime)

    def make_call_with_options(
        self,
        request: ccc20200701_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MakeCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_call_with_options_async(
        self,
        request: ccc20200701_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MakeCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MakeCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_call(
        self,
        request: ccc20200701_models.MakeCallRequest,
    ) -> ccc20200701_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @return: MakeCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    async def make_call_async(
        self,
        request: ccc20200701_models.MakeCallRequest,
    ) -> ccc20200701_models.MakeCallResponse:
        """
        @param request: MakeCallRequest
        @return: MakeCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.make_call_with_options_async(request, runtime)

    def modify_audio_file_with_options(
        self,
        request: ccc20200701_models.ModifyAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyAudioFileResponse:
        """
        @param request: ModifyAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyAudioFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audio_file_with_options_async(
        self,
        request: ccc20200701_models.ModifyAudioFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyAudioFileResponse:
        """
        @param request: ModifyAudioFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAudioFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_file_name):
            query['AudioFileName'] = request.audio_file_name
        if not UtilClient.is_unset(request.audio_resource_id):
            query['AudioResourceId'] = request.audio_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_file_key):
            query['OssFileKey'] = request.oss_file_key
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAudioFile',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyAudioFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audio_file(
        self,
        request: ccc20200701_models.ModifyAudioFileRequest,
    ) -> ccc20200701_models.ModifyAudioFileResponse:
        """
        @param request: ModifyAudioFileRequest
        @return: ModifyAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_audio_file_with_options(request, runtime)

    async def modify_audio_file_async(
        self,
        request: ccc20200701_models.ModifyAudioFileRequest,
    ) -> ccc20200701_models.ModifyAudioFileResponse:
        """
        @param request: ModifyAudioFileRequest
        @return: ModifyAudioFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_audio_file_with_options_async(request, runtime)

    def modify_custom_call_tagging_with_options(
        self,
        request: ccc20200701_models.ModifyCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyCustomCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ModifyCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCustomCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyCustomCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.ModifyCustomCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyCustomCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ModifyCustomCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCustomCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_tag_name_list):
            query['CallTagNameList'] = request.call_tag_name_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyCustomCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_call_tagging(
        self,
        request: ccc20200701_models.ModifyCustomCallTaggingRequest,
    ) -> ccc20200701_models.ModifyCustomCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ModifyCustomCallTaggingRequest
        @return: ModifyCustomCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_custom_call_tagging_with_options(request, runtime)

    async def modify_custom_call_tagging_async(
        self,
        request: ccc20200701_models.ModifyCustomCallTaggingRequest,
    ) -> ccc20200701_models.ModifyCustomCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: ModifyCustomCallTaggingRequest
        @return: ModifyCustomCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_custom_call_tagging_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_phone_number_with_options(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        """
        @param request: ModifyPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhoneNumber',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_phone_number_with_options_async(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        """
        @param request: ModifyPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhoneNumber',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_phone_number(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        """
        @param request: ModifyPhoneNumberRequest
        @return: ModifyPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_number_with_options(request, runtime)

    async def modify_phone_number_async(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        """
        @param request: ModifyPhoneNumberRequest
        @return: ModifyPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_phone_number_with_options_async(request, runtime)

    def modify_skill_group_with_options(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        """
        @param request: ModifySkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        """
        @param request: ModifySkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_skill_group(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        """
        @param request: ModifySkillGroupRequest
        @return: ModifySkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_with_options(request, runtime)

    async def modify_skill_group_async(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        """
        @param request: ModifySkillGroupRequest
        @return: ModifySkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_group_with_options_async(request, runtime)

    def modify_skill_levels_of_user_with_options(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        """
        @param request: ModifySkillLevelsOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySkillLevelsOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillLevelsOfUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_skill_levels_of_user_with_options_async(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        """
        @param request: ModifySkillLevelsOfUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySkillLevelsOfUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_level_list):
            query['SkillLevelList'] = request.skill_level_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySkillLevelsOfUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillLevelsOfUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_skill_levels_of_user(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        """
        @param request: ModifySkillLevelsOfUserRequest
        @return: ModifySkillLevelsOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_levels_of_user_with_options(request, runtime)

    async def modify_skill_levels_of_user_async(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        """
        @param request: ModifySkillLevelsOfUserRequest
        @return: ModifySkillLevelsOfUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_levels_of_user_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: ccc20200701_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserResponse:
        """
        @param request: ModifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.display_id):
            query['DisplayId'] = request.display_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.nickname):
            query['Nickname'] = request.nickname
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: ccc20200701_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserResponse:
        """
        @param request: ModifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_url):
            query['AvatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.display_id):
            query['DisplayId'] = request.display_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.nickname):
            query['Nickname'] = request.nickname
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user(
        self,
        request: ccc20200701_models.ModifyUserRequest,
    ) -> ccc20200701_models.ModifyUserResponse:
        """
        @param request: ModifyUserRequest
        @return: ModifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: ccc20200701_models.ModifyUserRequest,
    ) -> ccc20200701_models.ModifyUserResponse:
        """
        @param request: ModifyUserRequest
        @return: ModifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def modify_user_levels_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        """
        @param request: ModifyUserLevelsOfSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserLevelsOfSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.user_level_list):
            query['UserLevelList'] = request.user_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_levels_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        """
        @param request: ModifyUserLevelsOfSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserLevelsOfSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.user_level_list):
            query['UserLevelList'] = request.user_level_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserLevelsOfSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_levels_of_skill_group(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        """
        @param request: ModifyUserLevelsOfSkillGroupRequest
        @return: ModifyUserLevelsOfSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_levels_of_skill_group_with_options(request, runtime)

    async def modify_user_levels_of_skill_group_async(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        """
        @param request: ModifyUserLevelsOfSkillGroupRequest
        @return: ModifyUserLevelsOfSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_levels_of_skill_group_with_options_async(request, runtime)

    def monitor_call_with_options(
        self,
        request: ccc20200701_models.MonitorCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MonitorCallResponse:
        """
        @param request: MonitorCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MonitorCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.monitored_user_id):
            query['MonitoredUserId'] = request.monitored_user_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MonitorCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MonitorCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def monitor_call_with_options_async(
        self,
        request: ccc20200701_models.MonitorCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MonitorCallResponse:
        """
        @param request: MonitorCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MonitorCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.monitored_user_id):
            query['MonitoredUserId'] = request.monitored_user_id
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MonitorCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MonitorCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def monitor_call(
        self,
        request: ccc20200701_models.MonitorCallRequest,
    ) -> ccc20200701_models.MonitorCallResponse:
        """
        @param request: MonitorCallRequest
        @return: MonitorCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.monitor_call_with_options(request, runtime)

    async def monitor_call_async(
        self,
        request: ccc20200701_models.MonitorCallRequest,
    ) -> ccc20200701_models.MonitorCallResponse:
        """
        @param request: MonitorCallRequest
        @return: MonitorCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.monitor_call_with_options_async(request, runtime)

    def mute_call_with_options(
        self,
        request: ccc20200701_models.MuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MuteCallResponse:
        """
        @param request: MuteCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MuteCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MuteCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def mute_call_with_options_async(
        self,
        request: ccc20200701_models.MuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MuteCallResponse:
        """
        @param request: MuteCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MuteCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.MuteCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mute_call(
        self,
        request: ccc20200701_models.MuteCallRequest,
    ) -> ccc20200701_models.MuteCallResponse:
        """
        @param request: MuteCallRequest
        @return: MuteCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mute_call_with_options(request, runtime)

    async def mute_call_async(
        self,
        request: ccc20200701_models.MuteCallRequest,
    ) -> ccc20200701_models.MuteCallResponse:
        """
        @param request: MuteCallRequest
        @return: MuteCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mute_call_with_options_async(request, runtime)

    def pause_campaign_with_options(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PauseCampaignResponse:
        """
        @summary 暂停预测式外呼活动
        
        @param request: PauseCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PauseCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_campaign_with_options_async(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PauseCampaignResponse:
        """
        @summary 暂停预测式外呼活动
        
        @param request: PauseCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PauseCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_campaign(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
    ) -> ccc20200701_models.PauseCampaignResponse:
        """
        @summary 暂停预测式外呼活动
        
        @param request: PauseCampaignRequest
        @return: PauseCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_campaign_with_options(request, runtime)

    async def pause_campaign_async(
        self,
        request: ccc20200701_models.PauseCampaignRequest,
    ) -> ccc20200701_models.PauseCampaignResponse:
        """
        @summary 暂停预测式外呼活动
        
        @param request: PauseCampaignRequest
        @return: PauseCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pause_campaign_with_options_async(request, runtime)

    def pick_outbound_numbers_with_options(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        """
        @param request: PickOutboundNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PickOutboundNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PickOutboundNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PickOutboundNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def pick_outbound_numbers_with_options_async(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        """
        @param request: PickOutboundNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PickOutboundNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PickOutboundNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PickOutboundNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pick_outbound_numbers(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        """
        @param request: PickOutboundNumbersRequest
        @return: PickOutboundNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pick_outbound_numbers_with_options(request, runtime)

    async def pick_outbound_numbers_async(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        """
        @param request: PickOutboundNumbersRequest
        @return: PickOutboundNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pick_outbound_numbers_with_options_async(request, runtime)

    def poll_user_status_with_options(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PollUserStatusResponse:
        """
        @param request: PollUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PollUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollUserStatus',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PollUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_user_status_with_options_async(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PollUserStatusResponse:
        """
        @param request: PollUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PollUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollUserStatus',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PollUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_user_status(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
    ) -> ccc20200701_models.PollUserStatusResponse:
        """
        @param request: PollUserStatusRequest
        @return: PollUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.poll_user_status_with_options(request, runtime)

    async def poll_user_status_async(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
    ) -> ccc20200701_models.PollUserStatusResponse:
        """
        @param request: PollUserStatusRequest
        @return: PollUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.poll_user_status_with_options_async(request, runtime)

    def process_ali_me_callback_of_staging_with_options(
        self,
        request: ccc20200701_models.ProcessAliMeCallbackOfStagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ProcessAliMeCallbackOfStagingResponse:
        """
        @summary ProcessAliMeCallbackOfStaging
        
        @param request: ProcessAliMeCallbackOfStagingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProcessAliMeCallbackOfStagingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProcessAliMeCallbackOfStaging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ProcessAliMeCallbackOfStagingResponse(),
            self.call_api(params, req, runtime)
        )

    async def process_ali_me_callback_of_staging_with_options_async(
        self,
        request: ccc20200701_models.ProcessAliMeCallbackOfStagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ProcessAliMeCallbackOfStagingResponse:
        """
        @summary ProcessAliMeCallbackOfStaging
        
        @param request: ProcessAliMeCallbackOfStagingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProcessAliMeCallbackOfStagingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProcessAliMeCallbackOfStaging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ProcessAliMeCallbackOfStagingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def process_ali_me_callback_of_staging(
        self,
        request: ccc20200701_models.ProcessAliMeCallbackOfStagingRequest,
    ) -> ccc20200701_models.ProcessAliMeCallbackOfStagingResponse:
        """
        @summary ProcessAliMeCallbackOfStaging
        
        @param request: ProcessAliMeCallbackOfStagingRequest
        @return: ProcessAliMeCallbackOfStagingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.process_ali_me_callback_of_staging_with_options(request, runtime)

    async def process_ali_me_callback_of_staging_async(
        self,
        request: ccc20200701_models.ProcessAliMeCallbackOfStagingRequest,
    ) -> ccc20200701_models.ProcessAliMeCallbackOfStagingResponse:
        """
        @summary ProcessAliMeCallbackOfStaging
        
        @param request: ProcessAliMeCallbackOfStagingRequest
        @return: ProcessAliMeCallbackOfStagingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.process_ali_me_callback_of_staging_with_options_async(request, runtime)

    def publish_contact_flow_with_options(
        self,
        request: ccc20200701_models.PublishContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PublishContactFlowResponse:
        """
        @param request: PublishContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PublishContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_contact_flow_with_options_async(
        self,
        request: ccc20200701_models.PublishContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PublishContactFlowResponse:
        """
        @param request: PublishContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.draft_id):
            query['DraftId'] = request.draft_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.PublishContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_contact_flow(
        self,
        request: ccc20200701_models.PublishContactFlowRequest,
    ) -> ccc20200701_models.PublishContactFlowResponse:
        """
        @param request: PublishContactFlowRequest
        @return: PublishContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_contact_flow_with_options(request, runtime)

    async def publish_contact_flow_async(
        self,
        request: ccc20200701_models.PublishContactFlowRequest,
    ) -> ccc20200701_models.PublishContactFlowResponse:
        """
        @param request: PublishContactFlowRequest
        @return: PublishContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_contact_flow_with_options_async(request, runtime)

    def ready_for_service_with_options(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        """
        @param request: ReadyForServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadyForServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReadyForService',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReadyForServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def ready_for_service_with_options_async(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        """
        @param request: ReadyForServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadyForServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_scenario):
            query['OutboundScenario'] = request.outbound_scenario
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReadyForService',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReadyForServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ready_for_service(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        """
        @param request: ReadyForServiceRequest
        @return: ReadyForServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ready_for_service_with_options(request, runtime)

    async def ready_for_service_async(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        """
        @param request: ReadyForServiceRequest
        @return: ReadyForServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ready_for_service_with_options_async(request, runtime)

    def redial_call_with_options(
        self,
        request: ccc20200701_models.RedialCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RedialCallResponse:
        """
        @param request: RedialCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RedialCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RedialCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RedialCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def redial_call_with_options_async(
        self,
        request: ccc20200701_models.RedialCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RedialCallResponse:
        """
        @param request: RedialCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RedialCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RedialCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RedialCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def redial_call(
        self,
        request: ccc20200701_models.RedialCallRequest,
    ) -> ccc20200701_models.RedialCallResponse:
        """
        @param request: RedialCallRequest
        @return: RedialCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.redial_call_with_options(request, runtime)

    async def redial_call_async(
        self,
        request: ccc20200701_models.RedialCallRequest,
    ) -> ccc20200701_models.RedialCallResponse:
        """
        @param request: RedialCallRequest
        @return: RedialCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.redial_call_with_options_async(request, runtime)

    def register_device_with_options(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        """
        @param request: RegisterDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        """
        @param request: RegisterDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_device(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        """
        @param request: RegisterDeviceRequest
        @return: RegisterDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        """
        @param request: RegisterDeviceRequest
        @return: RegisterDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)

    def register_devices_with_options(
        self,
        request: ccc20200701_models.RegisterDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDevicesResponse:
        """
        @param request: RegisterDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_id_list_json):
            query['UserIdListJson'] = request.user_id_list_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDevices',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_devices_with_options_async(
        self,
        request: ccc20200701_models.RegisterDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDevicesResponse:
        """
        @param request: RegisterDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_id_list_json):
            query['UserIdListJson'] = request.user_id_list_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDevices',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_devices(
        self,
        request: ccc20200701_models.RegisterDevicesRequest,
    ) -> ccc20200701_models.RegisterDevicesResponse:
        """
        @param request: RegisterDevicesRequest
        @return: RegisterDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_devices_with_options(request, runtime)

    async def register_devices_async(
        self,
        request: ccc20200701_models.RegisterDevicesRequest,
    ) -> ccc20200701_models.RegisterDevicesResponse:
        """
        @param request: RegisterDevicesRequest
        @return: RegisterDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_devices_with_options_async(request, runtime)

    def release_call_with_options(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReleaseCallResponse:
        """
        @param request: ReleaseCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReleaseCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_call_with_options_async(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReleaseCallResponse:
        """
        @param request: ReleaseCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ReleaseCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_call(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
    ) -> ccc20200701_models.ReleaseCallResponse:
        """
        @param request: ReleaseCallRequest
        @return: ReleaseCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_call_with_options(request, runtime)

    async def release_call_async(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
    ) -> ccc20200701_models.ReleaseCallResponse:
        """
        @param request: ReleaseCallRequest
        @return: ReleaseCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_call_with_options_async(request, runtime)

    def remove_blacklist_call_tagging_with_options(
        self,
        request: ccc20200701_models.RemoveBlacklistCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: RemoveBlacklistCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveBlacklistCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBlacklistCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveBlacklistCallTaggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_blacklist_call_tagging_with_options_async(
        self,
        request: ccc20200701_models.RemoveBlacklistCallTaggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: RemoveBlacklistCallTaggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveBlacklistCallTaggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBlacklistCallTagging',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveBlacklistCallTaggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_blacklist_call_tagging(
        self,
        request: ccc20200701_models.RemoveBlacklistCallTaggingRequest,
    ) -> ccc20200701_models.RemoveBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: RemoveBlacklistCallTaggingRequest
        @return: RemoveBlacklistCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_blacklist_call_tagging_with_options(request, runtime)

    async def remove_blacklist_call_tagging_async(
        self,
        request: ccc20200701_models.RemoveBlacklistCallTaggingRequest,
    ) -> ccc20200701_models.RemoveBlacklistCallTaggingResponse:
        """
        @summary 编辑呼入控制号码
        
        @param request: RemoveBlacklistCallTaggingRequest
        @return: RemoveBlacklistCallTaggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_blacklist_call_tagging_with_options_async(request, runtime)

    def remove_do_not_call_numbers_with_options(
        self,
        request: ccc20200701_models.RemoveDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveDoNotCallNumbersResponse:
        """
        @summary 删除黑名单号码
        
        @param request: RemoveDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveDoNotCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_do_not_call_numbers_with_options_async(
        self,
        request: ccc20200701_models.RemoveDoNotCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveDoNotCallNumbersResponse:
        """
        @summary 删除黑名单号码
        
        @param request: RemoveDoNotCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDoNotCallNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDoNotCallNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveDoNotCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_do_not_call_numbers(
        self,
        request: ccc20200701_models.RemoveDoNotCallNumbersRequest,
    ) -> ccc20200701_models.RemoveDoNotCallNumbersResponse:
        """
        @summary 删除黑名单号码
        
        @param request: RemoveDoNotCallNumbersRequest
        @return: RemoveDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_do_not_call_numbers_with_options(request, runtime)

    async def remove_do_not_call_numbers_async(
        self,
        request: ccc20200701_models.RemoveDoNotCallNumbersRequest,
    ) -> ccc20200701_models.RemoveDoNotCallNumbersResponse:
        """
        @summary 删除黑名单号码
        
        @param request: RemoveDoNotCallNumbersRequest
        @return: RemoveDoNotCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_do_not_call_numbers_with_options_async(request, runtime)

    def remove_personal_numbers_from_user_with_options(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        """
        @param request: RemovePersonalNumbersFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePersonalNumbersFromUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePersonalNumbersFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePersonalNumbersFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_personal_numbers_from_user_with_options_async(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        """
        @param request: RemovePersonalNumbersFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePersonalNumbersFromUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePersonalNumbersFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePersonalNumbersFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_personal_numbers_from_user(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        """
        @param request: RemovePersonalNumbersFromUserRequest
        @return: RemovePersonalNumbersFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_personal_numbers_from_user_with_options(request, runtime)

    async def remove_personal_numbers_from_user_async(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        """
        @param request: RemovePersonalNumbersFromUserRequest
        @return: RemovePersonalNumbersFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_personal_numbers_from_user_with_options_async(request, runtime)

    def remove_phone_number_from_skill_groups_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        """
        @param request: RemovePhoneNumberFromSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePhoneNumberFromSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumberFromSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_number_from_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        """
        @param request: RemovePhoneNumberFromSkillGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePhoneNumberFromSkillGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumberFromSkillGroups',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_number_from_skill_groups(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        """
        @param request: RemovePhoneNumberFromSkillGroupsRequest
        @return: RemovePhoneNumberFromSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_number_from_skill_groups_with_options(request, runtime)

    async def remove_phone_number_from_skill_groups_async(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        """
        @param request: RemovePhoneNumberFromSkillGroupsRequest
        @return: RemovePhoneNumberFromSkillGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_number_from_skill_groups_with_options_async(request, runtime)

    def remove_phone_numbers_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        """
        @param request: RemovePhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        """
        @param request: RemovePhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_numbers(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        """
        @param request: RemovePhoneNumbersRequest
        @return: RemovePhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_with_options(request, runtime)

    async def remove_phone_numbers_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        """
        @param request: RemovePhoneNumbersRequest
        @return: RemovePhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_numbers_with_options_async(request, runtime)

    def remove_phone_numbers_from_skill_group_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        """
        @param request: RemovePhoneNumbersFromSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePhoneNumbersFromSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_phone_numbers_from_skill_group_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        """
        @param request: RemovePhoneNumbersFromSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePhoneNumbersFromSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePhoneNumbersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_phone_numbers_from_skill_group(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        """
        @param request: RemovePhoneNumbersFromSkillGroupRequest
        @return: RemovePhoneNumbersFromSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_from_skill_group_with_options(request, runtime)

    async def remove_phone_numbers_from_skill_group_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        """
        @param request: RemovePhoneNumbersFromSkillGroupRequest
        @return: RemovePhoneNumbersFromSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_numbers_from_skill_group_with_options_async(request, runtime)

    def remove_skill_groups_from_user_with_options(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        """
        @param request: RemoveSkillGroupsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSkillGroupsFromUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSkillGroupsFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveSkillGroupsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_skill_groups_from_user_with_options_async(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        """
        @param request: RemoveSkillGroupsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSkillGroupsFromUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSkillGroupsFromUser',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveSkillGroupsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_skill_groups_from_user(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        """
        @param request: RemoveSkillGroupsFromUserRequest
        @return: RemoveSkillGroupsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_groups_from_user_with_options(request, runtime)

    async def remove_skill_groups_from_user_async(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        """
        @param request: RemoveSkillGroupsFromUserRequest
        @return: RemoveSkillGroupsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_skill_groups_from_user_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersResponse:
        """
        @param request: RemoveUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.notification_email):
            query['NotificationEmail'] = request.notification_email
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersResponse:
        """
        @param request: RemoveUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.notification_email):
            query['NotificationEmail'] = request.notification_email
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
    ) -> ccc20200701_models.RemoveUsersResponse:
        """
        @param request: RemoveUsersRequest
        @return: RemoveUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
    ) -> ccc20200701_models.RemoveUsersResponse:
        """
        @param request: RemoveUsersRequest
        @return: RemoveUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def remove_users_from_skill_group_with_options(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        """
        @param request: RemoveUsersFromSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersFromSkillGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_from_skill_group_with_options_async(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        """
        @param request: RemoveUsersFromSkillGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromSkillGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromSkillGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersFromSkillGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users_from_skill_group(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        """
        @param request: RemoveUsersFromSkillGroupRequest
        @return: RemoveUsersFromSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_skill_group_with_options(request, runtime)

    async def remove_users_from_skill_group_async(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        """
        @param request: RemoveUsersFromSkillGroupRequest
        @return: RemoveUsersFromSkillGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_from_skill_group_with_options_async(request, runtime)

    def reset_agent_state_with_options(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        """
        @param request: ResetAgentStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAgentStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAgentState',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetAgentStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_agent_state_with_options_async(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        """
        @param request: ResetAgentStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAgentStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAgentState',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetAgentStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_agent_state(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        """
        @param request: ResetAgentStateRequest
        @return: ResetAgentStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_agent_state_with_options(request, runtime)

    async def reset_agent_state_async(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        """
        @param request: ResetAgentStateRequest
        @return: ResetAgentStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_agent_state_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        """
        @param request: ResetUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        """
        @param request: ResetUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        """
        @param request: ResetUserPasswordRequest
        @return: ResetUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        """
        @param request: ResetUserPasswordRequest
        @return: ResetUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def restore_archived_recordings_with_options(
        self,
        request: ccc20200701_models.RestoreArchivedRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RestoreArchivedRecordingsResponse:
        """
        @summary 录音解冻
        
        @param request: RestoreArchivedRecordingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreArchivedRecordingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreArchivedRecordings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RestoreArchivedRecordingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_archived_recordings_with_options_async(
        self,
        request: ccc20200701_models.RestoreArchivedRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RestoreArchivedRecordingsResponse:
        """
        @summary 录音解冻
        
        @param request: RestoreArchivedRecordingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreArchivedRecordingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreArchivedRecordings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RestoreArchivedRecordingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_archived_recordings(
        self,
        request: ccc20200701_models.RestoreArchivedRecordingsRequest,
    ) -> ccc20200701_models.RestoreArchivedRecordingsResponse:
        """
        @summary 录音解冻
        
        @param request: RestoreArchivedRecordingsRequest
        @return: RestoreArchivedRecordingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_archived_recordings_with_options(request, runtime)

    async def restore_archived_recordings_async(
        self,
        request: ccc20200701_models.RestoreArchivedRecordingsRequest,
    ) -> ccc20200701_models.RestoreArchivedRecordingsResponse:
        """
        @summary 录音解冻
        
        @param request: RestoreArchivedRecordingsRequest
        @return: RestoreArchivedRecordingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_archived_recordings_with_options_async(request, runtime)

    def resume_campaign_with_options(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        """
        @summary 恢复预测式外呼活动
        
        @param request: ResumeCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResumeCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_campaign_with_options_async(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        """
        @summary 恢复预测式外呼活动
        
        @param request: ResumeCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.ResumeCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_campaign(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        """
        @summary 恢复预测式外呼活动
        
        @param request: ResumeCampaignRequest
        @return: ResumeCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_campaign_with_options(request, runtime)

    async def resume_campaign_async(
        self,
        request: ccc20200701_models.ResumeCampaignRequest,
    ) -> ccc20200701_models.ResumeCampaignResponse:
        """
        @summary 恢复预测式外呼活动
        
        @param request: ResumeCampaignRequest
        @return: ResumeCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_campaign_with_options_async(request, runtime)

    def retrieve_call_with_options(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RetrieveCallResponse:
        """
        @param request: RetrieveCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetrieveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RetrieveCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_call_with_options_async(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RetrieveCallResponse:
        """
        @param request: RetrieveCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetrieveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.RetrieveCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_call(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
    ) -> ccc20200701_models.RetrieveCallResponse:
        """
        @param request: RetrieveCallRequest
        @return: RetrieveCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retrieve_call_with_options(request, runtime)

    async def retrieve_call_async(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
    ) -> ccc20200701_models.RetrieveCallResponse:
        """
        @param request: RetrieveCallRequest
        @return: RetrieveCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retrieve_call_with_options_async(request, runtime)

    def save_document_with_options(
        self,
        request: ccc20200701_models.SaveDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveDocumentResponse:
        """
        @param request: SaveDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document_id):
            body['DocumentId'] = request.document_id
        if not UtilClient.is_unset(request.document_json):
            body['DocumentJson'] = request.document_json
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveDocument',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_document_with_options_async(
        self,
        request: ccc20200701_models.SaveDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveDocumentResponse:
        """
        @param request: SaveDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document_id):
            body['DocumentId'] = request.document_id
        if not UtilClient.is_unset(request.document_json):
            body['DocumentJson'] = request.document_json
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveDocument',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_document(
        self,
        request: ccc20200701_models.SaveDocumentRequest,
    ) -> ccc20200701_models.SaveDocumentResponse:
        """
        @param request: SaveDocumentRequest
        @return: SaveDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_document_with_options(request, runtime)

    async def save_document_async(
        self,
        request: ccc20200701_models.SaveDocumentRequest,
    ) -> ccc20200701_models.SaveDocumentResponse:
        """
        @param request: SaveDocumentRequest
        @return: SaveDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_document_with_options_async(request, runtime)

    def save_rtcstats_v2with_options(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        """
        @param request: SaveRTCStatsV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRTCStatsV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not UtilClient.is_unset(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not UtilClient.is_unset(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRTCStatsV2',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveRTCStatsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def save_rtcstats_v2with_options_async(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        """
        @param request: SaveRTCStatsV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRTCStatsV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not UtilClient.is_unset(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not UtilClient.is_unset(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRTCStatsV2',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveRTCStatsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def save_rtcstats_v2(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        """
        @param request: SaveRTCStatsV2Request
        @return: SaveRTCStatsV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.save_rtcstats_v2with_options(request, runtime)

    async def save_rtcstats_v2_async(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        """
        @param request: SaveRTCStatsV2Request
        @return: SaveRTCStatsV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_rtcstats_v2with_options_async(request, runtime)

    def save_terminal_log_with_options(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        """
        @param request: SaveTerminalLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTerminalLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.method_name):
            query['MethodName'] = request.method_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unique_request_id):
            query['UniqueRequestId'] = request.unique_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTerminalLog',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveTerminalLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_terminal_log_with_options_async(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        """
        @param request: SaveTerminalLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTerminalLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.method_name):
            query['MethodName'] = request.method_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unique_request_id):
            query['UniqueRequestId'] = request.unique_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTerminalLog',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveTerminalLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_terminal_log(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        """
        @param request: SaveTerminalLogRequest
        @return: SaveTerminalLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_terminal_log_with_options(request, runtime)

    async def save_terminal_log_async(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        """
        @param request: SaveTerminalLogRequest
        @return: SaveTerminalLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_terminal_log_with_options_async(request, runtime)

    def save_web_rtcstats_with_options(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        """
        @param request: SaveWebRTCStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveWebRTCStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not UtilClient.is_unset(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not UtilClient.is_unset(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRTCStats',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRTCStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_web_rtcstats_with_options_async(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        """
        @param request: SaveWebRTCStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveWebRTCStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not UtilClient.is_unset(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not UtilClient.is_unset(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRTCStats',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRTCStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_web_rtcstats(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        """
        @param request: SaveWebRTCStatsRequest
        @return: SaveWebRTCStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtcstats_with_options(request, runtime)

    async def save_web_rtcstats_async(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        """
        @param request: SaveWebRTCStatsRequest
        @return: SaveWebRTCStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_web_rtcstats_with_options_async(request, runtime)

    def save_web_rtc_info_with_options(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        """
        @param request: SaveWebRtcInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveWebRtcInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRtcInfo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRtcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_web_rtc_info_with_options_async(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        """
        @param request: SaveWebRtcInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveWebRtcInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRtcInfo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRtcInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_web_rtc_info(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        """
        @param request: SaveWebRtcInfoRequest
        @return: SaveWebRtcInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtc_info_with_options(request, runtime)

    async def save_web_rtc_info_async(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        """
        @param request: SaveWebRtcInfoRequest
        @return: SaveWebRtcInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_web_rtc_info_with_options_async(request, runtime)

    def send_dtmf_signaling_with_options(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        """
        @param request: SendDtmfSignalingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendDtmfSignalingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.dtmf):
            query['Dtmf'] = request.dtmf
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendDtmfSignaling',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SendDtmfSignalingResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_dtmf_signaling_with_options_async(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        """
        @param request: SendDtmfSignalingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendDtmfSignalingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.dtmf):
            query['Dtmf'] = request.dtmf
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendDtmfSignaling',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SendDtmfSignalingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_dtmf_signaling(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        """
        @param request: SendDtmfSignalingRequest
        @return: SendDtmfSignalingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_dtmf_signaling_with_options(request, runtime)

    async def send_dtmf_signaling_async(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        """
        @param request: SendDtmfSignalingRequest
        @return: SendDtmfSignalingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_dtmf_signaling_with_options_async(request, runtime)

    def sign_in_group_with_options(
        self,
        request: ccc20200701_models.SignInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignInGroupResponse:
        """
        @param request: SignInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additivity):
            query['Additivity'] = request.additivity
        if not UtilClient.is_unset(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignInGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_in_group_with_options_async(
        self,
        request: ccc20200701_models.SignInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignInGroupResponse:
        """
        @param request: SignInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additivity):
            query['Additivity'] = request.additivity
        if not UtilClient.is_unset(request.chat_device_id):
            query['ChatDeviceId'] = request.chat_device_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.signed_skill_group_id_list):
            query['SignedSkillGroupIdList'] = request.signed_skill_group_id_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignInGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign_in_group(
        self,
        request: ccc20200701_models.SignInGroupRequest,
    ) -> ccc20200701_models.SignInGroupResponse:
        """
        @param request: SignInGroupRequest
        @return: SignInGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sign_in_group_with_options(request, runtime)

    async def sign_in_group_async(
        self,
        request: ccc20200701_models.SignInGroupRequest,
    ) -> ccc20200701_models.SignInGroupResponse:
        """
        @param request: SignInGroupRequest
        @return: SignInGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sign_in_group_with_options_async(request, runtime)

    def sign_out_group_with_options(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignOutGroupResponse:
        """
        @param request: SignOutGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignOutGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignOutGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignOutGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_out_group_with_options_async(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignOutGroupResponse:
        """
        @param request: SignOutGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignOutGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignOutGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SignOutGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign_out_group(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
    ) -> ccc20200701_models.SignOutGroupResponse:
        """
        @param request: SignOutGroupRequest
        @return: SignOutGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sign_out_group_with_options(request, runtime)

    async def sign_out_group_async(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
    ) -> ccc20200701_models.SignOutGroupResponse:
        """
        @param request: SignOutGroupRequest
        @return: SignOutGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sign_out_group_with_options_async(request, runtime)

    def start_back_2back_call_with_options(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        """
        @param request: StartBack2BackCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBack2BackCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_broker):
            query['AdditionalBroker'] = request.additional_broker
        if not UtilClient.is_unset(request.broker):
            query['Broker'] = request.broker
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBack2BackCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartBack2BackCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_back_2back_call_with_options_async(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        """
        @param request: StartBack2BackCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBack2BackCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_broker):
            query['AdditionalBroker'] = request.additional_broker
        if not UtilClient.is_unset(request.broker):
            query['Broker'] = request.broker
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBack2BackCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartBack2BackCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_back_2back_call(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        """
        @param request: StartBack2BackCallRequest
        @return: StartBack2BackCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_back_2back_call_with_options(request, runtime)

    async def start_back_2back_call_async(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        """
        @param request: StartBack2BackCallRequest
        @return: StartBack2BackCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_back_2back_call_with_options_async(request, runtime)

    def start_chat_with_options(
        self,
        tmp_req: ccc20200701_models.StartChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartChatResponse:
        """
        @param tmp_req: StartChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.StartChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_list):
            request.user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartChat',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_chat_with_options_async(
        self,
        tmp_req: ccc20200701_models.StartChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartChatResponse:
        """
        @param tmp_req: StartChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.StartChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_list):
            request.user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_channel_id):
            query['AccessChannelId'] = request.access_channel_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartChat',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_chat(
        self,
        request: ccc20200701_models.StartChatRequest,
    ) -> ccc20200701_models.StartChatResponse:
        """
        @param request: StartChatRequest
        @return: StartChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_chat_with_options(request, runtime)

    async def start_chat_async(
        self,
        request: ccc20200701_models.StartChatRequest,
    ) -> ccc20200701_models.StartChatResponse:
        """
        @param request: StartChatRequest
        @return: StartChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_chat_with_options_async(request, runtime)

    def start_conference_with_options(
        self,
        request: ccc20200701_models.StartConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartConferenceResponse:
        """
        @param request: StartConferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartConferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.participant_list_json):
            query['ParticipantListJson'] = request.participant_list_json
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartConference',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_conference_with_options_async(
        self,
        request: ccc20200701_models.StartConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartConferenceResponse:
        """
        @param request: StartConferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartConferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.participant_list_json):
            query['ParticipantListJson'] = request.participant_list_json
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartConference',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_conference(
        self,
        request: ccc20200701_models.StartConferenceRequest,
    ) -> ccc20200701_models.StartConferenceResponse:
        """
        @param request: StartConferenceRequest
        @return: StartConferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_conference_with_options(request, runtime)

    async def start_conference_async(
        self,
        request: ccc20200701_models.StartConferenceRequest,
    ) -> ccc20200701_models.StartConferenceResponse:
        """
        @param request: StartConferenceRequest
        @return: StartConferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_conference_with_options_async(request, runtime)

    def start_edit_contact_flow_with_options(
        self,
        request: ccc20200701_models.StartEditContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartEditContactFlowResponse:
        """
        @param request: StartEditContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEditContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEditContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartEditContactFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_edit_contact_flow_with_options_async(
        self,
        request: ccc20200701_models.StartEditContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartEditContactFlowResponse:
        """
        @param request: StartEditContactFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEditContactFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEditContactFlow',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartEditContactFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_edit_contact_flow(
        self,
        request: ccc20200701_models.StartEditContactFlowRequest,
    ) -> ccc20200701_models.StartEditContactFlowResponse:
        """
        @param request: StartEditContactFlowRequest
        @return: StartEditContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_edit_contact_flow_with_options(request, runtime)

    async def start_edit_contact_flow_async(
        self,
        request: ccc20200701_models.StartEditContactFlowRequest,
    ) -> ccc20200701_models.StartEditContactFlowResponse:
        """
        @param request: StartEditContactFlowRequest
        @return: StartEditContactFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_edit_contact_flow_with_options_async(request, runtime)

    def start_predictive_call_with_options(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        """
        @param request: StartPredictiveCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPredictiveCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPredictiveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPredictiveCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_predictive_call_with_options_async(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        """
        @param request: StartPredictiveCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPredictiveCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.contact_flow_variables):
            query['ContactFlowVariables'] = request.contact_flow_variables
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.masked_callee):
            query['MaskedCallee'] = request.masked_callee
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPredictiveCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPredictiveCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_predictive_call(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        """
        @param request: StartPredictiveCallRequest
        @return: StartPredictiveCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_predictive_call_with_options(request, runtime)

    async def start_predictive_call_async(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        """
        @param request: StartPredictiveCallRequest
        @return: StartPredictiveCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_predictive_call_with_options_async(request, runtime)

    def start_privacy_call_with_options(
        self,
        request: ccc20200701_models.StartPrivacyCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPrivacyCallResponse:
        """
        @summary 发起隐私呼叫
        
        @param request: StartPrivacyCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPrivacyCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPrivacyCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPrivacyCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_privacy_call_with_options_async(
        self,
        request: ccc20200701_models.StartPrivacyCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPrivacyCallResponse:
        """
        @summary 发起隐私呼叫
        
        @param request: StartPrivacyCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPrivacyCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPrivacyCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPrivacyCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_privacy_call(
        self,
        request: ccc20200701_models.StartPrivacyCallRequest,
    ) -> ccc20200701_models.StartPrivacyCallResponse:
        """
        @summary 发起隐私呼叫
        
        @param request: StartPrivacyCallRequest
        @return: StartPrivacyCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_privacy_call_with_options(request, runtime)

    async def start_privacy_call_async(
        self,
        request: ccc20200701_models.StartPrivacyCallRequest,
    ) -> ccc20200701_models.StartPrivacyCallResponse:
        """
        @summary 发起隐私呼叫
        
        @param request: StartPrivacyCallRequest
        @return: StartPrivacyCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_privacy_call_with_options_async(request, runtime)

    def submit_campaign_with_options(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        """
        @summary 提交预测式外呼活动
        
        @param request: SubmitCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SubmitCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_campaign_with_options_async(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        """
        @summary 提交预测式外呼活动
        
        @param request: SubmitCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SubmitCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_campaign(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        """
        @summary 提交预测式外呼活动
        
        @param request: SubmitCampaignRequest
        @return: SubmitCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_campaign_with_options(request, runtime)

    async def submit_campaign_async(
        self,
        request: ccc20200701_models.SubmitCampaignRequest,
    ) -> ccc20200701_models.SubmitCampaignResponse:
        """
        @summary 提交预测式外呼活动
        
        @param request: SubmitCampaignRequest
        @return: SubmitCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_campaign_with_options_async(request, runtime)

    def switch_to_conference_with_options(
        self,
        request: ccc20200701_models.SwitchToConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SwitchToConferenceResponse:
        """
        @param request: SwitchToConferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchToConferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchToConference',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SwitchToConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_to_conference_with_options_async(
        self,
        request: ccc20200701_models.SwitchToConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SwitchToConferenceResponse:
        """
        @param request: SwitchToConferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchToConferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchToConference',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.SwitchToConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_to_conference(
        self,
        request: ccc20200701_models.SwitchToConferenceRequest,
    ) -> ccc20200701_models.SwitchToConferenceResponse:
        """
        @param request: SwitchToConferenceRequest
        @return: SwitchToConferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_to_conference_with_options(request, runtime)

    async def switch_to_conference_async(
        self,
        request: ccc20200701_models.SwitchToConferenceRequest,
    ) -> ccc20200701_models.SwitchToConferenceResponse:
        """
        @param request: SwitchToConferenceRequest
        @return: SwitchToConferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_to_conference_with_options_async(request, runtime)

    def take_break_with_options(
        self,
        request: ccc20200701_models.TakeBreakRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.TakeBreakResponse:
        """
        @param request: TakeBreakRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TakeBreakResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TakeBreak',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.TakeBreakResponse(),
            self.call_api(params, req, runtime)
        )

    async def take_break_with_options_async(
        self,
        request: ccc20200701_models.TakeBreakRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.TakeBreakResponse:
        """
        @param request: TakeBreakRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TakeBreakResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TakeBreak',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.TakeBreakResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def take_break(
        self,
        request: ccc20200701_models.TakeBreakRequest,
    ) -> ccc20200701_models.TakeBreakResponse:
        """
        @param request: TakeBreakRequest
        @return: TakeBreakResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.take_break_with_options(request, runtime)

    async def take_break_async(
        self,
        request: ccc20200701_models.TakeBreakRequest,
    ) -> ccc20200701_models.TakeBreakResponse:
        """
        @param request: TakeBreakRequest
        @return: TakeBreakResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.take_break_with_options_async(request, runtime)

    def unmute_call_with_options(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnmuteCallResponse:
        """
        @param request: UnmuteCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnmuteCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnmuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UnmuteCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def unmute_call_with_options_async(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnmuteCallResponse:
        """
        @param request: UnmuteCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnmuteCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnmuteCall',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UnmuteCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unmute_call(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
    ) -> ccc20200701_models.UnmuteCallResponse:
        """
        @param request: UnmuteCallRequest
        @return: UnmuteCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unmute_call_with_options(request, runtime)

    async def unmute_call_async(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
    ) -> ccc20200701_models.UnmuteCallResponse:
        """
        @param request: UnmuteCallRequest
        @return: UnmuteCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unmute_call_with_options_async(request, runtime)

    def unregister_device_with_options(
        self,
        request: ccc20200701_models.UnregisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnregisterDeviceResponse:
        """
        @summary 删除注册设备
        
        @param request: UnregisterDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnregisterDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterDevice',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UnregisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unregister_device_with_options_async(
        self,
        request: ccc20200701_models.UnregisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnregisterDeviceResponse:
        """
        @summary 删除注册设备
        
        @param request: UnregisterDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnregisterDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterDevice',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UnregisterDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unregister_device(
        self,
        request: ccc20200701_models.UnregisterDeviceRequest,
    ) -> ccc20200701_models.UnregisterDeviceResponse:
        """
        @summary 删除注册设备
        
        @param request: UnregisterDeviceRequest
        @return: UnregisterDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unregister_device_with_options(request, runtime)

    async def unregister_device_async(
        self,
        request: ccc20200701_models.UnregisterDeviceRequest,
    ) -> ccc20200701_models.UnregisterDeviceResponse:
        """
        @summary 删除注册设备
        
        @param request: UnregisterDeviceRequest
        @return: UnregisterDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unregister_device_with_options_async(request, runtime)

    def update_campaign_with_options(
        self,
        request: ccc20200701_models.UpdateCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateCampaignResponse:
        """
        @summary Update campaign
        
        @param request: UpdateCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_campaign_with_options_async(
        self,
        request: ccc20200701_models.UpdateCampaignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateCampaignResponse:
        """
        @summary Update campaign
        
        @param request: UpdateCampaignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCampaignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_campaign(
        self,
        request: ccc20200701_models.UpdateCampaignRequest,
    ) -> ccc20200701_models.UpdateCampaignResponse:
        """
        @summary Update campaign
        
        @param request: UpdateCampaignRequest
        @return: UpdateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_campaign_with_options(request, runtime)

    async def update_campaign_async(
        self,
        request: ccc20200701_models.UpdateCampaignRequest,
    ) -> ccc20200701_models.UpdateCampaignResponse:
        """
        @summary Update campaign
        
        @param request: UpdateCampaignRequest
        @return: UpdateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_campaign_with_options_async(request, runtime)

    def update_config_items_with_options(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        """
        @param request: UpdateConfigItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_items):
            query['ConfigItems'] = request.config_items
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateConfigItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_items_with_options_async(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        """
        @param request: UpdateConfigItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_items):
            query['ConfigItems'] = request.config_items
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConfigItems',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateConfigItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_items(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        """
        @param request: UpdateConfigItemsRequest
        @return: UpdateConfigItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_config_items_with_options(request, runtime)

    async def update_config_items_async(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        """
        @param request: UpdateConfigItemsRequest
        @return: UpdateConfigItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_config_items_with_options_async(request, runtime)

    def update_schema_property_with_options(
        self,
        tmp_req: ccc20200701_models.UpdateSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateSchemaPropertyResponse:
        """
        @param tmp_req: UpdateSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSchemaPropertyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.UpdateSchemaPropertyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.property):
            request.property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_shrink):
            body['Property'] = request.property_shrink
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateSchemaPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schema_property_with_options_async(
        self,
        tmp_req: ccc20200701_models.UpdateSchemaPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateSchemaPropertyResponse:
        """
        @param tmp_req: UpdateSchemaPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSchemaPropertyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ccc20200701_models.UpdateSchemaPropertyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.property):
            request.property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.property, 'Property', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.property_shrink):
            body['Property'] = request.property_shrink
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchemaProperty',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateSchemaPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schema_property(
        self,
        request: ccc20200701_models.UpdateSchemaPropertyRequest,
    ) -> ccc20200701_models.UpdateSchemaPropertyResponse:
        """
        @param request: UpdateSchemaPropertyRequest
        @return: UpdateSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_schema_property_with_options(request, runtime)

    async def update_schema_property_async(
        self,
        request: ccc20200701_models.UpdateSchemaPropertyRequest,
    ) -> ccc20200701_models.UpdateSchemaPropertyResponse:
        """
        @param request: UpdateSchemaPropertyRequest
        @return: UpdateSchemaPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_schema_property_with_options_async(request, runtime)
