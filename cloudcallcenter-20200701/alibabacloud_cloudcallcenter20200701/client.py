# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudcallcenter20200701 import models as main_models
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
        self._endpoint = self.get_endpoint('cloudcallcenter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_cases_with_options(
        self,
        tmp_req: main_models.AbortCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbortCasesResponse:
        tmp_req.validate()
        request = main_models.AbortCasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_number_list):
            request.phone_number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_number_list, 'PhoneNumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.phone_number_list_shrink):
            query['PhoneNumberList'] = request.phone_number_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_cases_with_options_async(
        self,
        tmp_req: main_models.AbortCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbortCasesResponse:
        tmp_req.validate()
        request = main_models.AbortCasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_number_list):
            request.phone_number_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_number_list, 'PhoneNumberList', 'json')
        query = {}
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.phone_number_list_shrink):
            query['PhoneNumberList'] = request.phone_number_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortCases',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_cases(
        self,
        request: main_models.AbortCasesRequest,
    ) -> main_models.AbortCasesResponse:
        runtime = RuntimeOptions()
        return self.abort_cases_with_options(request, runtime)

    async def abort_cases_async(
        self,
        request: main_models.AbortCasesRequest,
    ) -> main_models.AbortCasesResponse:
        runtime = RuntimeOptions()
        return await self.abort_cases_with_options_async(request, runtime)

    def check_demo_instance_exists_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDemoInstanceExistsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckDemoInstanceExists',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDemoInstanceExistsResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_demo_instance_exists_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDemoInstanceExistsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckDemoInstanceExists',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDemoInstanceExistsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_demo_instance_exists(self) -> main_models.CheckDemoInstanceExistsResponse:
        runtime = RuntimeOptions()
        return self.check_demo_instance_exists_with_options(runtime)

    async def check_demo_instance_exists_async(self) -> main_models.CheckDemoInstanceExistsResponse:
        runtime = RuntimeOptions()
        return await self.check_demo_instance_exists_with_options_async(runtime)

    def check_mqrole_assumption_authority_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMQRoleAssumptionAuthorityResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckMQRoleAssumptionAuthority',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMQRoleAssumptionAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_mqrole_assumption_authority_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMQRoleAssumptionAuthorityResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckMQRoleAssumptionAuthority',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMQRoleAssumptionAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_mqrole_assumption_authority(self) -> main_models.CheckMQRoleAssumptionAuthorityResponse:
        runtime = RuntimeOptions()
        return self.check_mqrole_assumption_authority_with_options(runtime)

    async def check_mqrole_assumption_authority_async(self) -> main_models.CheckMQRoleAssumptionAuthorityResponse:
        runtime = RuntimeOptions()
        return await self.check_mqrole_assumption_authority_with_options_async(runtime)

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

    def create_corp_number_group_with_options(
        self,
        request: main_models.CreateCorpNumberGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCorpNumberGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCorpNumberGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCorpNumberGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_corp_number_group_with_options_async(
        self,
        request: main_models.CreateCorpNumberGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCorpNumberGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCorpNumberGroup',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCorpNumberGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_corp_number_group(
        self,
        request: main_models.CreateCorpNumberGroupRequest,
    ) -> main_models.CreateCorpNumberGroupResponse:
        runtime = RuntimeOptions()
        return self.create_corp_number_group_with_options(request, runtime)

    async def create_corp_number_group_async(
        self,
        request: main_models.CreateCorpNumberGroupRequest,
    ) -> main_models.CreateCorpNumberGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_corp_number_group_with_options_async(request, runtime)

    def create_demo_instance_with_options(
        self,
        request: main_models.CreateDemoInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDemoInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.outbound_call_whitelist):
            query['OutboundCallWhitelist'] = request.outbound_call_whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDemoInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDemoInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_demo_instance_with_options_async(
        self,
        request: main_models.CreateDemoInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDemoInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.outbound_call_whitelist):
            query['OutboundCallWhitelist'] = request.outbound_call_whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDemoInstance',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDemoInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_demo_instance(
        self,
        request: main_models.CreateDemoInstanceRequest,
    ) -> main_models.CreateDemoInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_demo_instance_with_options(request, runtime)

    async def create_demo_instance_async(
        self,
        request: main_models.CreateDemoInstanceRequest,
    ) -> main_models.CreateDemoInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_demo_instance_with_options_async(request, runtime)

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

    def get_document_with_options(
        self,
        request: main_models.GetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentResponse:
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
            action = 'GetDocument',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_with_options_async(
        self,
        request: main_models.GetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentResponse:
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
            action = 'GetDocument',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document(
        self,
        request: main_models.GetDocumentRequest,
    ) -> main_models.GetDocumentResponse:
        runtime = RuntimeOptions()
        return self.get_document_with_options(request, runtime)

    async def get_document_async(
        self,
        request: main_models.GetDocumentRequest,
    ) -> main_models.GetDocumentResponse:
        runtime = RuntimeOptions()
        return await self.get_document_with_options_async(request, runtime)

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

    def get_instance_ids_by_aliyun_uid_v2with_options(
        self,
        request: main_models.GetInstanceIdsByAliyunUidV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceIdsByAliyunUidV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceIdsByAliyunUidV2',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceIdsByAliyunUidV2Response(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_ids_by_aliyun_uid_v2with_options_async(
        self,
        request: main_models.GetInstanceIdsByAliyunUidV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceIdsByAliyunUidV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceIdsByAliyunUidV2',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceIdsByAliyunUidV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_ids_by_aliyun_uid_v2(
        self,
        request: main_models.GetInstanceIdsByAliyunUidV2Request,
    ) -> main_models.GetInstanceIdsByAliyunUidV2Response:
        runtime = RuntimeOptions()
        return self.get_instance_ids_by_aliyun_uid_v2with_options(request, runtime)

    async def get_instance_ids_by_aliyun_uid_v2_async(
        self,
        request: main_models.GetInstanceIdsByAliyunUidV2Request,
    ) -> main_models.GetInstanceIdsByAliyunUidV2Response:
        runtime = RuntimeOptions()
        return await self.get_instance_ids_by_aliyun_uid_v2with_options_async(request, runtime)

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

    def issue_softphone_command_with_options(
        self,
        request: main_models.IssueSoftphoneCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IssueSoftphoneCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IssueSoftphoneCommand',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IssueSoftphoneCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def issue_softphone_command_with_options_async(
        self,
        request: main_models.IssueSoftphoneCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IssueSoftphoneCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IssueSoftphoneCommand',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IssueSoftphoneCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def issue_softphone_command(
        self,
        request: main_models.IssueSoftphoneCommandRequest,
    ) -> main_models.IssueSoftphoneCommandResponse:
        runtime = RuntimeOptions()
        return self.issue_softphone_command_with_options(request, runtime)

    async def issue_softphone_command_async(
        self,
        request: main_models.IssueSoftphoneCommandRequest,
    ) -> main_models.IssueSoftphoneCommandResponse:
        runtime = RuntimeOptions()
        return await self.issue_softphone_command_with_options_async(request, runtime)

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

    def list_interval_agent_skill_group_report_with_options(
        self,
        request: main_models.ListIntervalAgentSkillGroupReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervalAgentSkillGroupReportResponse:
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
        if not DaraCore.is_null(request.show_default_if_empty):
            query['ShowDefaultIfEmpty'] = request.show_default_if_empty
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalAgentSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        if not DaraCore.is_null(request.show_default_if_empty):
            query['ShowDefaultIfEmpty'] = request.show_default_if_empty
        if not DaraCore.is_null(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervalAgentSkillGroupReport',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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

    def list_mono_recordings_with_options(
        self,
        request: main_models.ListMonoRecordingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMonoRecordingsResponse:
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

    def replace_migration_available_numbers_with_options(
        self,
        request: main_models.ReplaceMigrationAvailableNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceMigrationAvailableNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operator_name):
            query['OperatorName'] = request.operator_name
        if not DaraCore.is_null(request.operator_uid):
            query['OperatorUid'] = request.operator_uid
        if not DaraCore.is_null(request.v_1numbers):
            query['V1Numbers'] = request.v_1numbers
        if not DaraCore.is_null(request.v_2numbers):
            query['V2Numbers'] = request.v_2numbers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceMigrationAvailableNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceMigrationAvailableNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_migration_available_numbers_with_options_async(
        self,
        request: main_models.ReplaceMigrationAvailableNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceMigrationAvailableNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operator_name):
            query['OperatorName'] = request.operator_name
        if not DaraCore.is_null(request.operator_uid):
            query['OperatorUid'] = request.operator_uid
        if not DaraCore.is_null(request.v_1numbers):
            query['V1Numbers'] = request.v_1numbers
        if not DaraCore.is_null(request.v_2numbers):
            query['V2Numbers'] = request.v_2numbers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceMigrationAvailableNumbers',
            version = '2020-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceMigrationAvailableNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_migration_available_numbers(
        self,
        request: main_models.ReplaceMigrationAvailableNumbersRequest,
    ) -> main_models.ReplaceMigrationAvailableNumbersResponse:
        runtime = RuntimeOptions()
        return self.replace_migration_available_numbers_with_options(request, runtime)

    async def replace_migration_available_numbers_async(
        self,
        request: main_models.ReplaceMigrationAvailableNumbersRequest,
    ) -> main_models.ReplaceMigrationAvailableNumbersResponse:
        runtime = RuntimeOptions()
        return await self.replace_migration_available_numbers_with_options_async(request, runtime)

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
