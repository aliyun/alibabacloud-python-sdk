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

    def add_skill_groups_to_user_with_options(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSkillGroupsToUserResponse(),
            self.do_rpcrequest('AddSkillGroupsToUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_skill_groups_to_user_with_options_async(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSkillGroupsToUserResponse(),
            await self.do_rpcrequest_async('AddSkillGroupsToUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_skill_groups_to_user(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_skill_groups_to_user_with_options(request, runtime)

    async def add_skill_groups_to_user_async(
        self,
        request: ccc20200701_models.AddSkillGroupsToUserRequest,
    ) -> ccc20200701_models.AddSkillGroupsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_skill_groups_to_user_with_options_async(request, runtime)

    def save_web_rtcstats_with_options(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRTCStatsResponse(),
            self.do_rpcrequest('SaveWebRTCStats', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_web_rtcstats_with_options_async(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRTCStatsResponse(),
            await self.do_rpcrequest_async('SaveWebRTCStats', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_rtcstats(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtcstats_with_options(request, runtime)

    async def save_web_rtcstats_async(
        self,
        request: ccc20200701_models.SaveWebRTCStatsRequest,
    ) -> ccc20200701_models.SaveWebRTCStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_web_rtcstats_with_options_async(request, runtime)

    def get_mono_recording_with_options(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMonoRecordingResponse(),
            self.do_rpcrequest('GetMonoRecording', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_mono_recording_with_options_async(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMonoRecordingResponse(),
            await self.do_rpcrequest_async('GetMonoRecording', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mono_recording(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mono_recording_with_options(request, runtime)

    async def get_mono_recording_async(
        self,
        request: ccc20200701_models.GetMonoRecordingRequest,
    ) -> ccc20200701_models.GetMonoRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mono_recording_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ccc20200701_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ccc20200701_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUsersResponse(),
            await self.do_rpcrequest_async('ListUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: ccc20200701_models.ListUsersRequest,
    ) -> ccc20200701_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ccc20200701_models.ListUsersRequest,
    ) -> ccc20200701_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_agent_state_logs_with_options(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStateLogsResponse(),
            self.do_rpcrequest('ListAgentStateLogs', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_state_logs_with_options_async(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStateLogsResponse(),
            await self.do_rpcrequest_async('ListAgentStateLogs', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_state_logs(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_state_logs_with_options(request, runtime)

    async def list_agent_state_logs_async(
        self,
        request: ccc20200701_models.ListAgentStateLogsRequest,
    ) -> ccc20200701_models.ListAgentStateLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_state_logs_with_options_async(request, runtime)

    def remove_phone_number_from_skill_groups_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse(),
            self.do_rpcrequest('RemovePhoneNumberFromSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_phone_number_from_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse(),
            await self.do_rpcrequest_async('RemovePhoneNumberFromSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_number_from_skill_groups(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_number_from_skill_groups_with_options(request, runtime)

    async def remove_phone_number_from_skill_groups_async(
        self,
        request: ccc20200701_models.RemovePhoneNumberFromSkillGroupsRequest,
    ) -> ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_number_from_skill_groups_with_options_async(request, runtime)

    def list_phone_numbers_with_options(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersResponse(),
            self.do_rpcrequest('ListPhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersResponse(),
            await self.do_rpcrequest_async('ListPhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_numbers(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_with_options(request, runtime)

    async def list_phone_numbers_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersRequest,
    ) -> ccc20200701_models.ListPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_numbers_with_options_async(request, runtime)

    def add_numbers_to_skill_group_with_options(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddNumbersToSkillGroupResponse(),
            self.do_rpcrequest('AddNumbersToSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_numbers_to_skill_group_with_options_async(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddNumbersToSkillGroupResponse(),
            await self.do_rpcrequest_async('AddNumbersToSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_numbers_to_skill_group(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_numbers_to_skill_group_with_options(request, runtime)

    async def add_numbers_to_skill_group_async(
        self,
        request: ccc20200701_models.AddNumbersToSkillGroupRequest,
    ) -> ccc20200701_models.AddNumbersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_numbers_to_skill_group_with_options_async(request, runtime)

    def reset_agent_state_with_options(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetAgentStateResponse(),
            self.do_rpcrequest('ResetAgentState', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_agent_state_with_options_async(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetAgentStateResponse(),
            await self.do_rpcrequest_async('ResetAgentState', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_agent_state(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_agent_state_with_options(request, runtime)

    async def reset_agent_state_async(
        self,
        request: ccc20200701_models.ResetAgentStateRequest,
    ) -> ccc20200701_models.ResetAgentStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_agent_state_with_options_async(request, runtime)

    def change_work_mode_with_options(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeWorkModeResponse(),
            self.do_rpcrequest('ChangeWorkMode', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_work_mode_with_options_async(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeWorkModeResponse(),
            await self.do_rpcrequest_async('ChangeWorkMode', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_work_mode(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_work_mode_with_options(request, runtime)

    async def change_work_mode_async(
        self,
        request: ccc20200701_models.ChangeWorkModeRequest,
    ) -> ccc20200701_models.ChangeWorkModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_work_mode_with_options_async(request, runtime)

    def get_turn_credentials_with_options(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnCredentialsResponse(),
            self.do_rpcrequest('GetTurnCredentials', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_turn_credentials_with_options_async(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnCredentialsResponse(),
            await self.do_rpcrequest_async('GetTurnCredentials', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turn_credentials(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_turn_credentials_with_options(request, runtime)

    async def get_turn_credentials_async(
        self,
        request: ccc20200701_models.GetTurnCredentialsRequest,
    ) -> ccc20200701_models.GetTurnCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_turn_credentials_with_options_async(request, runtime)

    def add_phone_numbers_with_options(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumbersResponse(),
            self.do_rpcrequest('AddPhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumbersResponse(),
            await self.do_rpcrequest_async('AddPhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_numbers(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_phone_numbers_with_options(request, runtime)

    async def add_phone_numbers_async(
        self,
        request: ccc20200701_models.AddPhoneNumbersRequest,
    ) -> ccc20200701_models.AddPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_numbers_with_options_async(request, runtime)

    def save_web_rtc_info_with_options(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRtcInfoResponse(),
            self.do_rpcrequest('SaveWebRtcInfo', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_web_rtc_info_with_options_async(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRtcInfoResponse(),
            await self.do_rpcrequest_async('SaveWebRtcInfo', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_rtc_info(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtc_info_with_options(request, runtime)

    async def save_web_rtc_info_async(
        self,
        request: ccc20200701_models.SaveWebRtcInfoRequest,
    ) -> ccc20200701_models.SaveWebRtcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_web_rtc_info_with_options_async(request, runtime)

    def list_interval_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalSkillGroupReportResponse(),
            self.do_rpcrequest('ListIntervalSkillGroupReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_interval_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalSkillGroupReportResponse(),
            await self.do_rpcrequest_async('ListIntervalSkillGroupReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_interval_skill_group_report(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_interval_skill_group_report_with_options(request, runtime)

    async def list_interval_skill_group_report_async(
        self,
        request: ccc20200701_models.ListIntervalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListIntervalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_skill_group_report_with_options_async(request, runtime)

    def monitor_call_with_options(
        self,
        request: ccc20200701_models.MonitorCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MonitorCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MonitorCallResponse(),
            self.do_rpcrequest('MonitorCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def monitor_call_with_options_async(
        self,
        request: ccc20200701_models.MonitorCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MonitorCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MonitorCallResponse(),
            await self.do_rpcrequest_async('MonitorCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def monitor_call(
        self,
        request: ccc20200701_models.MonitorCallRequest,
    ) -> ccc20200701_models.MonitorCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.monitor_call_with_options(request, runtime)

    async def monitor_call_async(
        self,
        request: ccc20200701_models.MonitorCallRequest,
    ) -> ccc20200701_models.MonitorCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.monitor_call_with_options_async(request, runtime)

    def remove_users_from_skill_group_with_options(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersFromSkillGroupResponse(),
            self.do_rpcrequest('RemoveUsersFromSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_users_from_skill_group_with_options_async(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersFromSkillGroupResponse(),
            await self.do_rpcrequest_async('RemoveUsersFromSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users_from_skill_group(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_skill_group_with_options(request, runtime)

    async def remove_users_from_skill_group_async(
        self,
        request: ccc20200701_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemoveUsersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_from_skill_group_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSkillGroupResponse(),
            self.do_rpcrequest('DeleteSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSkillGroupResponse(),
            await self.do_rpcrequest_async('DeleteSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_skill_group(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: ccc20200701_models.DeleteSkillGroupRequest,
    ) -> ccc20200701_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def blind_transfer_with_options(
        self,
        request: ccc20200701_models.BlindTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BlindTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.BlindTransferResponse(),
            self.do_rpcrequest('BlindTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def blind_transfer_with_options_async(
        self,
        request: ccc20200701_models.BlindTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BlindTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.BlindTransferResponse(),
            await self.do_rpcrequest_async('BlindTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def blind_transfer(
        self,
        request: ccc20200701_models.BlindTransferRequest,
    ) -> ccc20200701_models.BlindTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.blind_transfer_with_options(request, runtime)

    async def blind_transfer_async(
        self,
        request: ccc20200701_models.BlindTransferRequest,
    ) -> ccc20200701_models.BlindTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.blind_transfer_with_options_async(request, runtime)

    def list_skill_levels_of_user_with_options(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillLevelsOfUserResponse(),
            self.do_rpcrequest('ListSkillLevelsOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_levels_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillLevelsOfUserResponse(),
            await self.do_rpcrequest_async('ListSkillLevelsOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_levels_of_user(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_levels_of_user_with_options(request, runtime)

    async def list_skill_levels_of_user_async(
        self,
        request: ccc20200701_models.ListSkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ListSkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_levels_of_user_with_options_async(request, runtime)

    def list_unassigned_numbers_with_options(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUnassignedNumbersResponse(),
            self.do_rpcrequest('ListUnassignedNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_unassigned_numbers_with_options_async(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUnassignedNumbersResponse(),
            await self.do_rpcrequest_async('ListUnassignedNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_unassigned_numbers(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_unassigned_numbers_with_options(request, runtime)

    async def list_unassigned_numbers_async(
        self,
        request: ccc20200701_models.ListUnassignedNumbersRequest,
    ) -> ccc20200701_models.ListUnassignedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_unassigned_numbers_with_options_async(request, runtime)

    def get_instance_trending_report_with_options(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceTrendingReportResponse(),
            self.do_rpcrequest('GetInstanceTrendingReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_trending_report_with_options_async(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceTrendingReportResponse(),
            await self.do_rpcrequest_async('GetInstanceTrendingReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_trending_report(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_trending_report_with_options(request, runtime)

    async def get_instance_trending_report_async(
        self,
        request: ccc20200701_models.GetInstanceTrendingReportRequest,
    ) -> ccc20200701_models.GetInstanceTrendingReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_trending_report_with_options_async(request, runtime)

    def list_instances_of_user_with_options(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesOfUserResponse(),
            self.do_rpcrequest('ListInstancesOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesOfUserResponse(),
            await self.do_rpcrequest_async('ListInstancesOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances_of_user(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_of_user_with_options(request, runtime)

    async def list_instances_of_user_async(
        self,
        request: ccc20200701_models.ListInstancesOfUserRequest,
    ) -> ccc20200701_models.ListInstancesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_of_user_with_options_async(request, runtime)

    def launch_survey_with_options(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchSurveyResponse(),
            self.do_rpcrequest('LaunchSurvey', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def launch_survey_with_options_async(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchSurveyResponse(),
            await self.do_rpcrequest_async('LaunchSurvey', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_survey(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_survey_with_options(request, runtime)

    async def launch_survey_async(
        self,
        request: ccc20200701_models.LaunchSurveyRequest,
    ) -> ccc20200701_models.LaunchSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_survey_with_options_async(request, runtime)

    def list_ivr_tracking_details_with_options(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIvrTrackingDetailsResponse(),
            self.do_rpcrequest('ListIvrTrackingDetails', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ivr_tracking_details_with_options_async(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIvrTrackingDetailsResponse(),
            await self.do_rpcrequest_async('ListIvrTrackingDetails', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ivr_tracking_details(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ivr_tracking_details_with_options(request, runtime)

    async def list_ivr_tracking_details_async(
        self,
        request: ccc20200701_models.ListIvrTrackingDetailsRequest,
    ) -> ccc20200701_models.ListIvrTrackingDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ivr_tracking_details_with_options_async(request, runtime)

    def list_brief_skill_groups_with_options(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBriefSkillGroupsResponse(),
            self.do_rpcrequest('ListBriefSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_brief_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBriefSkillGroupsResponse(),
            await self.do_rpcrequest_async('ListBriefSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_brief_skill_groups(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_brief_skill_groups_with_options(request, runtime)

    async def list_brief_skill_groups_async(
        self,
        request: ccc20200701_models.ListBriefSkillGroupsRequest,
    ) -> ccc20200701_models.ListBriefSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_brief_skill_groups_with_options_async(request, runtime)

    def unmute_call_with_options(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnmuteCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.UnmuteCallResponse(),
            self.do_rpcrequest('UnmuteCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unmute_call_with_options_async(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UnmuteCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.UnmuteCallResponse(),
            await self.do_rpcrequest_async('UnmuteCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unmute_call(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
    ) -> ccc20200701_models.UnmuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.unmute_call_with_options(request, runtime)

    async def unmute_call_async(
        self,
        request: ccc20200701_models.UnmuteCallRequest,
    ) -> ccc20200701_models.UnmuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unmute_call_with_options_async(request, runtime)

    def modify_skill_levels_of_user_with_options(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillLevelsOfUserResponse(),
            self.do_rpcrequest('ModifySkillLevelsOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_skill_levels_of_user_with_options_async(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillLevelsOfUserResponse(),
            await self.do_rpcrequest_async('ModifySkillLevelsOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_levels_of_user(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_levels_of_user_with_options(request, runtime)

    async def modify_skill_levels_of_user_async(
        self,
        request: ccc20200701_models.ModifySkillLevelsOfUserRequest,
    ) -> ccc20200701_models.ModifySkillLevelsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_levels_of_user_with_options_async(request, runtime)

    def assign_users_with_options(
        self,
        request: ccc20200701_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AssignUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AssignUsersResponse(),
            self.do_rpcrequest('AssignUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_users_with_options_async(
        self,
        request: ccc20200701_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AssignUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AssignUsersResponse(),
            await self.do_rpcrequest_async('AssignUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_users(
        self,
        request: ccc20200701_models.AssignUsersRequest,
    ) -> ccc20200701_models.AssignUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_users_with_options(request, runtime)

    async def assign_users_async(
        self,
        request: ccc20200701_models.AssignUsersRequest,
    ) -> ccc20200701_models.AssignUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_users_with_options_async(request, runtime)

    def list_user_levels_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUserLevelsOfSkillGroupResponse(),
            self.do_rpcrequest('ListUserLevelsOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_levels_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUserLevelsOfSkillGroupResponse(),
            await self.do_rpcrequest_async('ListUserLevelsOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_levels_of_skill_group(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_levels_of_skill_group_with_options(request, runtime)

    async def list_user_levels_of_skill_group_async(
        self,
        request: ccc20200701_models.ListUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ListUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_levels_of_skill_group_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: ccc20200701_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: ccc20200701_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRolesResponse(),
            await self.do_rpcrequest_async('ListRoles', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(
        self,
        request: ccc20200701_models.ListRolesRequest,
    ) -> ccc20200701_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: ccc20200701_models.ListRolesRequest,
    ) -> ccc20200701_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def update_config_items_with_options(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateConfigItemsResponse(),
            self.do_rpcrequest('UpdateConfigItems', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_config_items_with_options_async(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateConfigItemsResponse(),
            await self.do_rpcrequest_async('UpdateConfigItems', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_config_items(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_config_items_with_options(request, runtime)

    async def update_config_items_async(
        self,
        request: ccc20200701_models.UpdateConfigItemsRequest,
    ) -> ccc20200701_models.UpdateConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_config_items_with_options_async(request, runtime)

    def get_call_detail_record_with_options(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCallDetailRecordResponse(),
            self.do_rpcrequest('GetCallDetailRecord', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_call_detail_record_with_options_async(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCallDetailRecordResponse(),
            await self.do_rpcrequest_async('GetCallDetailRecord', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_call_detail_record(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_call_detail_record_with_options(request, runtime)

    async def get_call_detail_record_async(
        self,
        request: ccc20200701_models.GetCallDetailRecordRequest,
    ) -> ccc20200701_models.GetCallDetailRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_call_detail_record_with_options_async(request, runtime)

    def modify_phone_number_with_options(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyPhoneNumberResponse(),
            self.do_rpcrequest('ModifyPhoneNumber', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_phone_number_with_options_async(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyPhoneNumberResponse(),
            await self.do_rpcrequest_async('ModifyPhoneNumber', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_phone_number(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_number_with_options(request, runtime)

    async def modify_phone_number_async(
        self,
        request: ccc20200701_models.ModifyPhoneNumberRequest,
    ) -> ccc20200701_models.ModifyPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_phone_number_with_options_async(request, runtime)

    def coach_call_with_options(
        self,
        request: ccc20200701_models.CoachCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CoachCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CoachCallResponse(),
            self.do_rpcrequest('CoachCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def coach_call_with_options_async(
        self,
        request: ccc20200701_models.CoachCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CoachCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CoachCallResponse(),
            await self.do_rpcrequest_async('CoachCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def coach_call(
        self,
        request: ccc20200701_models.CoachCallRequest,
    ) -> ccc20200701_models.CoachCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.coach_call_with_options(request, runtime)

    async def coach_call_async(
        self,
        request: ccc20200701_models.CoachCallRequest,
    ) -> ccc20200701_models.CoachCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.coach_call_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ccc20200701_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateUserResponse(),
            self.do_rpcrequest('CreateUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ccc20200701_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateUserResponse(),
            await self.do_rpcrequest_async('CreateUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(
        self,
        request: ccc20200701_models.CreateUserRequest,
    ) -> ccc20200701_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ccc20200701_models.CreateUserRequest,
    ) -> ccc20200701_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def list_privileges_of_user_with_options(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPrivilegesOfUserResponse(),
            self.do_rpcrequest('ListPrivilegesOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_privileges_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPrivilegesOfUserResponse(),
            await self.do_rpcrequest_async('ListPrivilegesOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_privileges_of_user(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_privileges_of_user_with_options(request, runtime)

    async def list_privileges_of_user_async(
        self,
        request: ccc20200701_models.ListPrivilegesOfUserRequest,
    ) -> ccc20200701_models.ListPrivilegesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_privileges_of_user_with_options_async(request, runtime)

    def add_personal_numbers_to_user_with_options(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPersonalNumbersToUserResponse(),
            self.do_rpcrequest('AddPersonalNumbersToUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_personal_numbers_to_user_with_options_async(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPersonalNumbersToUserResponse(),
            await self.do_rpcrequest_async('AddPersonalNumbersToUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_personal_numbers_to_user(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_personal_numbers_to_user_with_options(request, runtime)

    async def add_personal_numbers_to_user_async(
        self,
        request: ccc20200701_models.AddPersonalNumbersToUserRequest,
    ) -> ccc20200701_models.AddPersonalNumbersToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_personal_numbers_to_user_with_options_async(request, runtime)

    def list_historical_agent_report_with_options(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentReportResponse(),
            self.do_rpcrequest('ListHistoricalAgentReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_historical_agent_report_with_options_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentReportResponse(),
            await self.do_rpcrequest_async('ListHistoricalAgentReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_historical_agent_report(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_historical_agent_report_with_options(request, runtime)

    async def list_historical_agent_report_async(
        self,
        request: ccc20200701_models.ListHistoricalAgentReportRequest,
    ) -> ccc20200701_models.ListHistoricalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_historical_agent_report_with_options_async(request, runtime)

    def intercept_call_with_options(
        self,
        request: ccc20200701_models.InterceptCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InterceptCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.InterceptCallResponse(),
            self.do_rpcrequest('InterceptCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def intercept_call_with_options_async(
        self,
        request: ccc20200701_models.InterceptCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InterceptCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.InterceptCallResponse(),
            await self.do_rpcrequest_async('InterceptCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def intercept_call(
        self,
        request: ccc20200701_models.InterceptCallRequest,
    ) -> ccc20200701_models.InterceptCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.intercept_call_with_options(request, runtime)

    async def intercept_call_async(
        self,
        request: ccc20200701_models.InterceptCallRequest,
    ) -> ccc20200701_models.InterceptCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.intercept_call_with_options_async(request, runtime)

    def list_contact_flows_with_options(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListContactFlowsResponse(),
            self.do_rpcrequest('ListContactFlows', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_contact_flows_with_options_async(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListContactFlowsResponse(),
            await self.do_rpcrequest_async('ListContactFlows', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_contact_flows(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_contact_flows_with_options(request, runtime)

    async def list_contact_flows_async(
        self,
        request: ccc20200701_models.ListContactFlowsRequest,
    ) -> ccc20200701_models.ListContactFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_contact_flows_with_options_async(request, runtime)

    def list_personal_numbers_of_user_with_options(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPersonalNumbersOfUserResponse(),
            self.do_rpcrequest('ListPersonalNumbersOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_personal_numbers_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPersonalNumbersOfUserResponse(),
            await self.do_rpcrequest_async('ListPersonalNumbersOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_personal_numbers_of_user(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_personal_numbers_of_user_with_options(request, runtime)

    async def list_personal_numbers_of_user_async(
        self,
        request: ccc20200701_models.ListPersonalNumbersOfUserRequest,
    ) -> ccc20200701_models.ListPersonalNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_personal_numbers_of_user_with_options_async(request, runtime)

    def start_predictive_call_with_options(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPredictiveCallResponse(),
            self.do_rpcrequest('StartPredictiveCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_predictive_call_with_options_async(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPredictiveCallResponse(),
            await self.do_rpcrequest_async('StartPredictiveCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_predictive_call(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_predictive_call_with_options(request, runtime)

    async def start_predictive_call_async(
        self,
        request: ccc20200701_models.StartPredictiveCallRequest,
    ) -> ccc20200701_models.StartPredictiveCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_predictive_call_with_options_async(request, runtime)

    def list_interval_instance_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalInstanceReportResponse(),
            self.do_rpcrequest('ListIntervalInstanceReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_interval_instance_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalInstanceReportResponse(),
            await self.do_rpcrequest_async('ListIntervalInstanceReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_interval_instance_report(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_interval_instance_report_with_options(request, runtime)

    async def list_interval_instance_report_async(
        self,
        request: ccc20200701_models.ListIntervalInstanceReportRequest,
    ) -> ccc20200701_models.ListIntervalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_instance_report_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateInstanceResponse(),
            await self.do_rpcrequest_async('CreateInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
    ) -> ccc20200701_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ccc20200701_models.CreateInstanceRequest,
    ) -> ccc20200701_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def remove_skill_groups_from_user_with_options(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveSkillGroupsFromUserResponse(),
            self.do_rpcrequest('RemoveSkillGroupsFromUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_skill_groups_from_user_with_options_async(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveSkillGroupsFromUserResponse(),
            await self.do_rpcrequest_async('RemoveSkillGroupsFromUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_skill_groups_from_user(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_groups_from_user_with_options(request, runtime)

    async def remove_skill_groups_from_user_async(
        self,
        request: ccc20200701_models.RemoveSkillGroupsFromUserRequest,
    ) -> ccc20200701_models.RemoveSkillGroupsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_skill_groups_from_user_with_options_async(request, runtime)

    def list_realtime_agent_states_with_options(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeAgentStatesResponse(),
            self.do_rpcrequest('ListRealtimeAgentStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_realtime_agent_states_with_options_async(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeAgentStatesResponse(),
            await self.do_rpcrequest_async('ListRealtimeAgentStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_realtime_agent_states(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_agent_states_with_options(request, runtime)

    async def list_realtime_agent_states_async(
        self,
        request: ccc20200701_models.ListRealtimeAgentStatesRequest,
    ) -> ccc20200701_models.ListRealtimeAgentStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_agent_states_with_options_async(request, runtime)

    def launch_authentication_with_options(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchAuthenticationResponse(),
            self.do_rpcrequest('LaunchAuthentication', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def launch_authentication_with_options_async(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchAuthenticationResponse(),
            await self.do_rpcrequest_async('LaunchAuthentication', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_authentication(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_authentication_with_options(request, runtime)

    async def launch_authentication_async(
        self,
        request: ccc20200701_models.LaunchAuthenticationRequest,
    ) -> ccc20200701_models.LaunchAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_authentication_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: ccc20200701_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: ccc20200701_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesResponse(),
            await self.do_rpcrequest_async('ListInstances', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(
        self,
        request: ccc20200701_models.ListInstancesRequest,
    ) -> ccc20200701_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: ccc20200701_models.ListInstancesRequest,
    ) -> ccc20200701_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def get_historical_instance_report_with_options(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalInstanceReportResponse(),
            self.do_rpcrequest('GetHistoricalInstanceReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_historical_instance_report_with_options_async(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalInstanceReportResponse(),
            await self.do_rpcrequest_async('GetHistoricalInstanceReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_historical_instance_report(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_historical_instance_report_with_options(request, runtime)

    async def get_historical_instance_report_async(
        self,
        request: ccc20200701_models.GetHistoricalInstanceReportRequest,
    ) -> ccc20200701_models.GetHistoricalInstanceReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_historical_instance_report_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersResponse(),
            self.do_rpcrequest('RemoveUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemoveUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersResponse(),
            await self.do_rpcrequest_async('RemoveUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
    ) -> ccc20200701_models.RemoveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: ccc20200701_models.RemoveUsersRequest,
    ) -> ccc20200701_models.RemoveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def start_back_2back_call_with_options(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.StartBack2BackCallResponse(),
            self.do_rpcrequest('StartBack2BackCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_back_2back_call_with_options_async(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.StartBack2BackCallResponse(),
            await self.do_rpcrequest_async('StartBack2BackCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_back_2back_call(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_back_2back_call_with_options(request, runtime)

    async def start_back_2back_call_async(
        self,
        request: ccc20200701_models.StartBack2BackCallRequest,
    ) -> ccc20200701_models.StartBack2BackCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_back_2back_call_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: ccc20200701_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUserResponse(),
            self.do_rpcrequest('GetUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ccc20200701_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUserResponse(),
            await self.do_rpcrequest_async('GetUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(
        self,
        request: ccc20200701_models.GetUserRequest,
    ) -> ccc20200701_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ccc20200701_models.GetUserRequest,
    ) -> ccc20200701_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def remove_phone_numbers_from_skill_group_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse(),
            self.do_rpcrequest('RemovePhoneNumbersFromSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_phone_numbers_from_skill_group_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse(),
            await self.do_rpcrequest_async('RemovePhoneNumbersFromSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_numbers_from_skill_group(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_from_skill_group_with_options(request, runtime)

    async def remove_phone_numbers_from_skill_group_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersFromSkillGroupRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_numbers_from_skill_group_with_options_async(request, runtime)

    def complete_attended_transfer_with_options(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CompleteAttendedTransferResponse(),
            self.do_rpcrequest('CompleteAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def complete_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CompleteAttendedTransferResponse(),
            await self.do_rpcrequest_async('CompleteAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_attended_transfer(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_attended_transfer_with_options(request, runtime)

    async def complete_attended_transfer_async(
        self,
        request: ccc20200701_models.CompleteAttendedTransferRequest,
    ) -> ccc20200701_models.CompleteAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_attended_transfer_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetUserPasswordResponse(),
            self.do_rpcrequest('ResetUserPassword', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetUserPasswordResponse(),
            await self.do_rpcrequest_async('ResetUserPassword', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_user_password(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: ccc20200701_models.ResetUserPasswordRequest,
    ) -> ccc20200701_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def get_turn_server_list_with_options(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnServerListResponse(),
            self.do_rpcrequest('GetTurnServerList', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_turn_server_list_with_options_async(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnServerListResponse(),
            await self.do_rpcrequest_async('GetTurnServerList', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turn_server_list(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_turn_server_list_with_options(request, runtime)

    async def get_turn_server_list_async(
        self,
        request: ccc20200701_models.GetTurnServerListRequest,
    ) -> ccc20200701_models.GetTurnServerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_turn_server_list_with_options_async(request, runtime)

    def get_number_location_with_options(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetNumberLocationResponse(),
            self.do_rpcrequest('GetNumberLocation', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_number_location_with_options_async(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetNumberLocationResponse(),
            await self.do_rpcrequest_async('GetNumberLocation', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_number_location(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_number_location_with_options(request, runtime)

    async def get_number_location_async(
        self,
        request: ccc20200701_models.GetNumberLocationRequest,
    ) -> ccc20200701_models.GetNumberLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_number_location_with_options_async(request, runtime)

    def list_ram_users_with_options(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRamUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRamUsersResponse(),
            self.do_rpcrequest('ListRamUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ram_users_with_options_async(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRamUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRamUsersResponse(),
            await self.do_rpcrequest_async('ListRamUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ram_users(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
    ) -> ccc20200701_models.ListRamUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ram_users_with_options(request, runtime)

    async def list_ram_users_async(
        self,
        request: ccc20200701_models.ListRamUsersRequest,
    ) -> ccc20200701_models.ListRamUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ram_users_with_options_async(request, runtime)

    def mute_call_with_options(
        self,
        request: ccc20200701_models.MuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MuteCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MuteCallResponse(),
            self.do_rpcrequest('MuteCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mute_call_with_options_async(
        self,
        request: ccc20200701_models.MuteCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MuteCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MuteCallResponse(),
            await self.do_rpcrequest_async('MuteCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mute_call(
        self,
        request: ccc20200701_models.MuteCallRequest,
    ) -> ccc20200701_models.MuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.mute_call_with_options(request, runtime)

    async def mute_call_async(
        self,
        request: ccc20200701_models.MuteCallRequest,
    ) -> ccc20200701_models.MuteCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mute_call_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: ccc20200701_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AnswerCallResponse(),
            self.do_rpcrequest('AnswerCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: ccc20200701_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AnswerCallResponse(),
            await self.do_rpcrequest_async('AnswerCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def answer_call(
        self,
        request: ccc20200701_models.AnswerCallRequest,
    ) -> ccc20200701_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: ccc20200701_models.AnswerCallRequest,
    ) -> ccc20200701_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def list_interval_agent_report_with_options(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentReportResponse(),
            self.do_rpcrequest('ListIntervalAgentReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_interval_agent_report_with_options_async(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentReportResponse(),
            await self.do_rpcrequest_async('ListIntervalAgentReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_interval_agent_report(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_interval_agent_report_with_options(request, runtime)

    async def list_interval_agent_report_async(
        self,
        request: ccc20200701_models.ListIntervalAgentReportRequest,
    ) -> ccc20200701_models.ListIntervalAgentReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_interval_agent_report_with_options_async(request, runtime)

    def list_call_detail_records_with_options(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallDetailRecordsResponse(),
            self.do_rpcrequest('ListCallDetailRecords', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_call_detail_records_with_options_async(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallDetailRecordsResponse(),
            await self.do_rpcrequest_async('ListCallDetailRecords', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_detail_records(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    async def list_call_detail_records_async(
        self,
        request: ccc20200701_models.ListCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_detail_records_with_options_async(request, runtime)

    def remove_phone_numbers_with_options(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersResponse(),
            self.do_rpcrequest('RemovePhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_phone_numbers_with_options_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersResponse(),
            await self.do_rpcrequest_async('RemovePhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_numbers(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_with_options(request, runtime)

    async def remove_phone_numbers_async(
        self,
        request: ccc20200701_models.RemovePhoneNumbersRequest,
    ) -> ccc20200701_models.RemovePhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_numbers_with_options_async(request, runtime)

    def cancel_attended_transfer_with_options(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CancelAttendedTransferResponse(),
            self.do_rpcrequest('CancelAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CancelAttendedTransferResponse(),
            await self.do_rpcrequest_async('CancelAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_attended_transfer(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_attended_transfer_with_options(request, runtime)

    async def cancel_attended_transfer_async(
        self,
        request: ccc20200701_models.CancelAttendedTransferRequest,
    ) -> ccc20200701_models.CancelAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_attended_transfer_with_options_async(request, runtime)

    def take_break_with_options(
        self,
        request: ccc20200701_models.TakeBreakRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.TakeBreakResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.TakeBreakResponse(),
            self.do_rpcrequest('TakeBreak', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def take_break_with_options_async(
        self,
        request: ccc20200701_models.TakeBreakRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.TakeBreakResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.TakeBreakResponse(),
            await self.do_rpcrequest_async('TakeBreak', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def take_break(
        self,
        request: ccc20200701_models.TakeBreakRequest,
    ) -> ccc20200701_models.TakeBreakResponse:
        runtime = util_models.RuntimeOptions()
        return self.take_break_with_options(request, runtime)

    async def take_break_async(
        self,
        request: ccc20200701_models.TakeBreakRequest,
    ) -> ccc20200701_models.TakeBreakResponse:
        runtime = util_models.RuntimeOptions()
        return await self.take_break_with_options_async(request, runtime)

    def list_historical_skill_group_report_with_options(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalSkillGroupReportResponse(),
            self.do_rpcrequest('ListHistoricalSkillGroupReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_historical_skill_group_report_with_options_async(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalSkillGroupReportResponse(),
            await self.do_rpcrequest_async('ListHistoricalSkillGroupReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_historical_skill_group_report(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_historical_skill_group_report_with_options(request, runtime)

    async def list_historical_skill_group_report_async(
        self,
        request: ccc20200701_models.ListHistoricalSkillGroupReportRequest,
    ) -> ccc20200701_models.ListHistoricalSkillGroupReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_historical_skill_group_report_with_options_async(request, runtime)

    def send_dtmf_signaling_with_options(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SendDtmfSignalingResponse(),
            self.do_rpcrequest('SendDtmfSignaling', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_dtmf_signaling_with_options_async(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SendDtmfSignalingResponse(),
            await self.do_rpcrequest_async('SendDtmfSignaling', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_dtmf_signaling(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_dtmf_signaling_with_options(request, runtime)

    async def send_dtmf_signaling_async(
        self,
        request: ccc20200701_models.SendDtmfSignalingRequest,
    ) -> ccc20200701_models.SendDtmfSignalingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_dtmf_signaling_with_options_async(request, runtime)

    def list_recent_call_detail_records_with_options(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRecentCallDetailRecordsResponse(),
            self.do_rpcrequest('ListRecentCallDetailRecords', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_recent_call_detail_records_with_options_async(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRecentCallDetailRecordsResponse(),
            await self.do_rpcrequest_async('ListRecentCallDetailRecords', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recent_call_detail_records(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recent_call_detail_records_with_options(request, runtime)

    async def list_recent_call_detail_records_async(
        self,
        request: ccc20200701_models.ListRecentCallDetailRecordsRequest,
    ) -> ccc20200701_models.ListRecentCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recent_call_detail_records_with_options_async(request, runtime)

    def initiate_attended_transfer_with_options(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.InitiateAttendedTransferResponse(),
            self.do_rpcrequest('InitiateAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def initiate_attended_transfer_with_options_async(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.InitiateAttendedTransferResponse(),
            await self.do_rpcrequest_async('InitiateAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def initiate_attended_transfer(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.initiate_attended_transfer_with_options(request, runtime)

    async def initiate_attended_transfer_async(
        self,
        request: ccc20200701_models.InitiateAttendedTransferRequest,
    ) -> ccc20200701_models.InitiateAttendedTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initiate_attended_transfer_with_options_async(request, runtime)

    def make_call_with_options(
        self,
        request: ccc20200701_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MakeCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MakeCallResponse(),
            self.do_rpcrequest('MakeCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def make_call_with_options_async(
        self,
        request: ccc20200701_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.MakeCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MakeCallResponse(),
            await self.do_rpcrequest_async('MakeCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def make_call(
        self,
        request: ccc20200701_models.MakeCallRequest,
    ) -> ccc20200701_models.MakeCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    async def make_call_async(
        self,
        request: ccc20200701_models.MakeCallRequest,
    ) -> ccc20200701_models.MakeCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.make_call_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: ccc20200701_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceResponse(),
            self.do_rpcrequest('GetInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: ccc20200701_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceResponse(),
            await self.do_rpcrequest_async('GetInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(
        self,
        request: ccc20200701_models.GetInstanceRequest,
    ) -> ccc20200701_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: ccc20200701_models.GetInstanceRequest,
    ) -> ccc20200701_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def add_users_to_skill_group_with_options(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddUsersToSkillGroupResponse(),
            self.do_rpcrequest('AddUsersToSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_users_to_skill_group_with_options_async(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddUsersToSkillGroupResponse(),
            await self.do_rpcrequest_async('AddUsersToSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_users_to_skill_group(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_skill_group_with_options(request, runtime)

    async def add_users_to_skill_group_async(
        self,
        request: ccc20200701_models.AddUsersToSkillGroupRequest,
    ) -> ccc20200701_models.AddUsersToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_users_to_skill_group_with_options_async(request, runtime)

    def list_config_items_with_options(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListConfigItemsResponse(),
            self.do_rpcrequest('ListConfigItems', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_config_items_with_options_async(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListConfigItemsResponse(),
            await self.do_rpcrequest_async('ListConfigItems', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_config_items(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_items_with_options(request, runtime)

    async def list_config_items_async(
        self,
        request: ccc20200701_models.ListConfigItemsRequest,
    ) -> ccc20200701_models.ListConfigItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_items_with_options_async(request, runtime)

    def sign_in_group_with_options(
        self,
        request: ccc20200701_models.SignInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignInGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SignInGroupResponse(),
            self.do_rpcrequest('SignInGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sign_in_group_with_options_async(
        self,
        request: ccc20200701_models.SignInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignInGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SignInGroupResponse(),
            await self.do_rpcrequest_async('SignInGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sign_in_group(
        self,
        request: ccc20200701_models.SignInGroupRequest,
    ) -> ccc20200701_models.SignInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.sign_in_group_with_options(request, runtime)

    async def sign_in_group_async(
        self,
        request: ccc20200701_models.SignInGroupRequest,
    ) -> ccc20200701_models.SignInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sign_in_group_with_options_async(request, runtime)

    def get_realtime_instance_states_with_options(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeInstanceStatesResponse(),
            self.do_rpcrequest('GetRealtimeInstanceStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_realtime_instance_states_with_options_async(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeInstanceStatesResponse(),
            await self.do_rpcrequest_async('GetRealtimeInstanceStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_realtime_instance_states(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_instance_states_with_options(request, runtime)

    async def get_realtime_instance_states_async(
        self,
        request: ccc20200701_models.GetRealtimeInstanceStatesRequest,
    ) -> ccc20200701_models.GetRealtimeInstanceStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_instance_states_with_options_async(request, runtime)

    def modify_skill_group_with_options(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillGroupResponse(),
            self.do_rpcrequest('ModifySkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillGroupResponse(),
            await self.do_rpcrequest_async('ModifySkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_with_options(request, runtime)

    async def modify_skill_group_async(
        self,
        request: ccc20200701_models.ModifySkillGroupRequest,
    ) -> ccc20200701_models.ModifySkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_group_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: ccc20200701_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserResponse(),
            self.do_rpcrequest('ModifyUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: ccc20200701_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserResponse(),
            await self.do_rpcrequest_async('ModifyUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user(
        self,
        request: ccc20200701_models.ModifyUserRequest,
    ) -> ccc20200701_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: ccc20200701_models.ModifyUserRequest,
    ) -> ccc20200701_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def add_phone_number_to_skill_groups_with_options(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumberToSkillGroupsResponse(),
            self.do_rpcrequest('AddPhoneNumberToSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_phone_number_to_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumberToSkillGroupsResponse(),
            await self.do_rpcrequest_async('AddPhoneNumberToSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_number_to_skill_groups(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_phone_number_to_skill_groups_with_options(request, runtime)

    async def add_phone_number_to_skill_groups_async(
        self,
        request: ccc20200701_models.AddPhoneNumberToSkillGroupsRequest,
    ) -> ccc20200701_models.AddPhoneNumberToSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_number_to_skill_groups_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: ccc20200701_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDevicesResponse(),
            self.do_rpcrequest('ListDevices', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: ccc20200701_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDevicesResponse(),
            await self.do_rpcrequest_async('ListDevices', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devices(
        self,
        request: ccc20200701_models.ListDevicesRequest,
    ) -> ccc20200701_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: ccc20200701_models.ListDevicesRequest,
    ) -> ccc20200701_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def retrieve_call_with_options(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RetrieveCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RetrieveCallResponse(),
            self.do_rpcrequest('RetrieveCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retrieve_call_with_options_async(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RetrieveCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RetrieveCallResponse(),
            await self.do_rpcrequest_async('RetrieveCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retrieve_call(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
    ) -> ccc20200701_models.RetrieveCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.retrieve_call_with_options(request, runtime)

    async def retrieve_call_async(
        self,
        request: ccc20200701_models.RetrieveCallRequest,
    ) -> ccc20200701_models.RetrieveCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retrieve_call_with_options_async(request, runtime)

    def list_skill_groups_with_options(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupsResponse(),
            self.do_rpcrequest('ListSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_groups_with_options_async(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupsResponse(),
            await self.do_rpcrequest_async('ListSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_groups(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_with_options(request, runtime)

    async def list_skill_groups_async(
        self,
        request: ccc20200701_models.ListSkillGroupsRequest,
    ) -> ccc20200701_models.ListSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_groups_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: ccc20200701_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.HoldCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.HoldCallResponse(),
            self.do_rpcrequest('HoldCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: ccc20200701_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.HoldCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.HoldCallResponse(),
            await self.do_rpcrequest_async('HoldCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hold_call(
        self,
        request: ccc20200701_models.HoldCallRequest,
    ) -> ccc20200701_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: ccc20200701_models.HoldCallRequest,
    ) -> ccc20200701_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def register_device_with_options(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDeviceResponse(),
            self.do_rpcrequest('RegisterDevice', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDeviceResponse(),
            await self.do_rpcrequest_async('RegisterDevice', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_device(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: ccc20200701_models.RegisterDeviceRequest,
    ) -> ccc20200701_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)

    def remove_personal_numbers_from_user_with_options(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePersonalNumbersFromUserResponse(),
            self.do_rpcrequest('RemovePersonalNumbersFromUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_personal_numbers_from_user_with_options_async(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePersonalNumbersFromUserResponse(),
            await self.do_rpcrequest_async('RemovePersonalNumbersFromUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_personal_numbers_from_user(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_personal_numbers_from_user_with_options(request, runtime)

    async def remove_personal_numbers_from_user_async(
        self,
        request: ccc20200701_models.RemovePersonalNumbersFromUserRequest,
    ) -> ccc20200701_models.RemovePersonalNumbersFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_personal_numbers_from_user_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyInstanceResponse(),
            self.do_rpcrequest('ModifyInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyInstanceResponse(),
            await self.do_rpcrequest_async('ModifyInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: ccc20200701_models.ModifyInstanceRequest,
    ) -> ccc20200701_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def list_outbound_numbers_of_user_with_options(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListOutboundNumbersOfUserResponse(),
            self.do_rpcrequest('ListOutboundNumbersOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_outbound_numbers_of_user_with_options_async(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListOutboundNumbersOfUserResponse(),
            await self.do_rpcrequest_async('ListOutboundNumbersOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_numbers_of_user(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_numbers_of_user_with_options(request, runtime)

    async def list_outbound_numbers_of_user_async(
        self,
        request: ccc20200701_models.ListOutboundNumbersOfUserRequest,
    ) -> ccc20200701_models.ListOutboundNumbersOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_numbers_of_user_with_options_async(request, runtime)

    def poll_user_status_with_options(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PollUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.PollUserStatusResponse(),
            self.do_rpcrequest('PollUserStatus', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def poll_user_status_with_options_async(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PollUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.PollUserStatusResponse(),
            await self.do_rpcrequest_async('PollUserStatus', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def poll_user_status(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
    ) -> ccc20200701_models.PollUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.poll_user_status_with_options(request, runtime)

    async def poll_user_status_async(
        self,
        request: ccc20200701_models.PollUserStatusRequest,
    ) -> ccc20200701_models.PollUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.poll_user_status_with_options_async(request, runtime)

    def ready_for_service_with_options(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ReadyForServiceResponse(),
            self.do_rpcrequest('ReadyForService', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ready_for_service_with_options_async(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ReadyForServiceResponse(),
            await self.do_rpcrequest_async('ReadyForService', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ready_for_service(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.ready_for_service_with_options(request, runtime)

    async def ready_for_service_async(
        self,
        request: ccc20200701_models.ReadyForServiceRequest,
    ) -> ccc20200701_models.ReadyForServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ready_for_service_with_options_async(request, runtime)

    def get_multi_channel_recording_with_options(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMultiChannelRecordingResponse(),
            self.do_rpcrequest('GetMultiChannelRecording', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_multi_channel_recording_with_options_async(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMultiChannelRecordingResponse(),
            await self.do_rpcrequest_async('GetMultiChannelRecording', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_multi_channel_recording(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multi_channel_recording_with_options(request, runtime)

    async def get_multi_channel_recording_async(
        self,
        request: ccc20200701_models.GetMultiChannelRecordingRequest,
    ) -> ccc20200701_models.GetMultiChannelRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_channel_recording_with_options_async(request, runtime)

    def barge_in_call_with_options(
        self,
        request: ccc20200701_models.BargeInCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BargeInCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.BargeInCallResponse(),
            self.do_rpcrequest('BargeInCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def barge_in_call_with_options_async(
        self,
        request: ccc20200701_models.BargeInCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.BargeInCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.BargeInCallResponse(),
            await self.do_rpcrequest_async('BargeInCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def barge_in_call(
        self,
        request: ccc20200701_models.BargeInCallRequest,
    ) -> ccc20200701_models.BargeInCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.barge_in_call_with_options(request, runtime)

    async def barge_in_call_async(
        self,
        request: ccc20200701_models.BargeInCallRequest,
    ) -> ccc20200701_models.BargeInCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.barge_in_call_with_options_async(request, runtime)

    def list_phone_numbers_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse(),
            self.do_rpcrequest('ListPhoneNumbersOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_phone_numbers_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse(),
            await self.do_rpcrequest_async('ListPhoneNumbersOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_numbers_of_skill_group(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_of_skill_group_with_options(request, runtime)

    async def list_phone_numbers_of_skill_group_async(
        self,
        request: ccc20200701_models.ListPhoneNumbersOfSkillGroupRequest,
    ) -> ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_numbers_of_skill_group_with_options_async(request, runtime)

    def sign_out_group_with_options(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignOutGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SignOutGroupResponse(),
            self.do_rpcrequest('SignOutGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sign_out_group_with_options_async(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SignOutGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SignOutGroupResponse(),
            await self.do_rpcrequest_async('SignOutGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sign_out_group(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
    ) -> ccc20200701_models.SignOutGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.sign_out_group_with_options(request, runtime)

    async def sign_out_group_async(
        self,
        request: ccc20200701_models.SignOutGroupRequest,
    ) -> ccc20200701_models.SignOutGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sign_out_group_with_options_async(request, runtime)

    def save_rtcstats_v2with_options(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveRTCStatsV2Response(),
            self.do_rpcrequest('SaveRTCStatsV2', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_rtcstats_v2with_options_async(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveRTCStatsV2Response(),
            await self.do_rpcrequest_async('SaveRTCStatsV2', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_rtcstats_v2(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.save_rtcstats_v2with_options(request, runtime)

    async def save_rtcstats_v2_async(
        self,
        request: ccc20200701_models.SaveRTCStatsV2Request,
    ) -> ccc20200701_models.SaveRTCStatsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.save_rtcstats_v2with_options_async(request, runtime)

    def get_historical_caller_report_with_options(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCallerReportResponse(),
            self.do_rpcrequest('GetHistoricalCallerReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_historical_caller_report_with_options_async(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCallerReportResponse(),
            await self.do_rpcrequest_async('GetHistoricalCallerReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_historical_caller_report(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_historical_caller_report_with_options(request, runtime)

    async def get_historical_caller_report_async(
        self,
        request: ccc20200701_models.GetHistoricalCallerReportRequest,
    ) -> ccc20200701_models.GetHistoricalCallerReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_historical_caller_report_with_options_async(request, runtime)

    def modify_user_levels_of_skill_group_with_options(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse(),
            self.do_rpcrequest('ModifyUserLevelsOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_levels_of_skill_group_with_options_async(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse(),
            await self.do_rpcrequest_async('ModifyUserLevelsOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_levels_of_skill_group(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_levels_of_skill_group_with_options(request, runtime)

    async def modify_user_levels_of_skill_group_async(
        self,
        request: ccc20200701_models.ModifyUserLevelsOfSkillGroupRequest,
    ) -> ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_levels_of_skill_group_with_options_async(request, runtime)

    def save_terminal_log_with_options(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveTerminalLogResponse(),
            self.do_rpcrequest('SaveTerminalLog', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_terminal_log_with_options_async(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveTerminalLogResponse(),
            await self.do_rpcrequest_async('SaveTerminalLog', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_terminal_log(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_terminal_log_with_options(request, runtime)

    async def save_terminal_log_async(
        self,
        request: ccc20200701_models.SaveTerminalLogRequest,
    ) -> ccc20200701_models.SaveTerminalLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_terminal_log_with_options_async(request, runtime)

    def list_realtime_skill_group_states_with_options(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeSkillGroupStatesResponse(),
            self.do_rpcrequest('ListRealtimeSkillGroupStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_realtime_skill_group_states_with_options_async(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeSkillGroupStatesResponse(),
            await self.do_rpcrequest_async('ListRealtimeSkillGroupStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_realtime_skill_group_states(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_skill_group_states_with_options(request, runtime)

    async def list_realtime_skill_group_states_async(
        self,
        request: ccc20200701_models.ListRealtimeSkillGroupStatesRequest,
    ) -> ccc20200701_models.ListRealtimeSkillGroupStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_skill_group_states_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSkillGroupResponse(),
            self.do_rpcrequest('CreateSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSkillGroupResponse(),
            await self.do_rpcrequest_async('CreateSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: ccc20200701_models.CreateSkillGroupRequest,
    ) -> ccc20200701_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def pick_outbound_numbers_with_options(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.PickOutboundNumbersResponse(),
            self.do_rpcrequest('PickOutboundNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pick_outbound_numbers_with_options_async(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.PickOutboundNumbersResponse(),
            await self.do_rpcrequest_async('PickOutboundNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_outbound_numbers(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.pick_outbound_numbers_with_options(request, runtime)

    async def pick_outbound_numbers_async(
        self,
        request: ccc20200701_models.PickOutboundNumbersRequest,
    ) -> ccc20200701_models.PickOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pick_outbound_numbers_with_options_async(request, runtime)

    def release_call_with_options(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReleaseCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ReleaseCallResponse(),
            self.do_rpcrequest('ReleaseCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_call_with_options_async(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.ReleaseCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ReleaseCallResponse(),
            await self.do_rpcrequest_async('ReleaseCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_call(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
    ) -> ccc20200701_models.ReleaseCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_call_with_options(request, runtime)

    async def release_call_async(
        self,
        request: ccc20200701_models.ReleaseCallRequest,
    ) -> ccc20200701_models.ReleaseCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_call_with_options_async(request, runtime)

    def get_login_details_with_options(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetLoginDetailsResponse(),
            self.do_rpcrequest('GetLoginDetails', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_login_details_with_options_async(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetLoginDetailsResponse(),
            await self.do_rpcrequest_async('GetLoginDetails', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_details(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_details_with_options(request, runtime)

    async def get_login_details_async(
        self,
        request: ccc20200701_models.GetLoginDetailsRequest,
    ) -> ccc20200701_models.GetLoginDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_details_with_options_async(request, runtime)
