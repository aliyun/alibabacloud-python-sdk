# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_scsp20200702 import models as scsp_20200702_models
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
        self._endpoint_map = {
            'cn-shanghai': 'scsp-vpc.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('scsp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_user_token_with_options(
        self,
        request: scsp_20200702_models.GetUserTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetUserTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetUserTokenResponse(),
            self.do_rpcrequest('GetUserToken', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_token_with_options_async(
        self,
        request: scsp_20200702_models.GetUserTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetUserTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetUserTokenResponse(),
            await self.do_rpcrequest_async('GetUserToken', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_token(
        self,
        request: scsp_20200702_models.GetUserTokenRequest,
    ) -> scsp_20200702_models.GetUserTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_token_with_options(request, runtime)

    async def get_user_token_async(
        self,
        request: scsp_20200702_models.GetUserTokenRequest,
    ) -> scsp_20200702_models.GetUserTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_token_with_options_async(request, runtime)

    def search_ticket_list_with_options(
        self,
        request: scsp_20200702_models.SearchTicketListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SearchTicketListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.SearchTicketListResponse(),
            self.do_rpcrequest('SearchTicketList', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def search_ticket_list_with_options_async(
        self,
        request: scsp_20200702_models.SearchTicketListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SearchTicketListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.SearchTicketListResponse(),
            await self.do_rpcrequest_async('SearchTicketList', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def search_ticket_list(
        self,
        request: scsp_20200702_models.SearchTicketListRequest,
    ) -> scsp_20200702_models.SearchTicketListResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_ticket_list_with_options(request, runtime)

    async def search_ticket_list_async(
        self,
        request: scsp_20200702_models.SearchTicketListRequest,
    ) -> scsp_20200702_models.SearchTicketListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_ticket_list_with_options_async(request, runtime)

    def send_hotline_heart_beat_with_options(
        self,
        request: scsp_20200702_models.SendHotlineHeartBeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SendHotlineHeartBeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.SendHotlineHeartBeatResponse(),
            self.do_rpcrequest('SendHotlineHeartBeat', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_hotline_heart_beat_with_options_async(
        self,
        request: scsp_20200702_models.SendHotlineHeartBeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SendHotlineHeartBeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.SendHotlineHeartBeatResponse(),
            await self.do_rpcrequest_async('SendHotlineHeartBeat', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_hotline_heart_beat(
        self,
        request: scsp_20200702_models.SendHotlineHeartBeatRequest,
    ) -> scsp_20200702_models.SendHotlineHeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_hotline_heart_beat_with_options(request, runtime)

    async def send_hotline_heart_beat_async(
        self,
        request: scsp_20200702_models.SendHotlineHeartBeatRequest,
    ) -> scsp_20200702_models.SendHotlineHeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_hotline_heart_beat_with_options_async(request, runtime)

    def transfer_call_to_skill_group_with_options(
        self,
        request: scsp_20200702_models.TransferCallToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferCallToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferCallToSkillGroupResponse(),
            self.do_rpcrequest('TransferCallToSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_call_to_skill_group_with_options_async(
        self,
        request: scsp_20200702_models.TransferCallToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferCallToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferCallToSkillGroupResponse(),
            await self.do_rpcrequest_async('TransferCallToSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_call_to_skill_group(
        self,
        request: scsp_20200702_models.TransferCallToSkillGroupRequest,
    ) -> scsp_20200702_models.TransferCallToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_call_to_skill_group_with_options(request, runtime)

    async def transfer_call_to_skill_group_async(
        self,
        request: scsp_20200702_models.TransferCallToSkillGroupRequest,
    ) -> scsp_20200702_models.TransferCallToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_call_to_skill_group_with_options_async(request, runtime)

    def edit_entity_route_with_options(
        self,
        request: scsp_20200702_models.EditEntityRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.EditEntityRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.EditEntityRouteResponse(),
            self.do_rpcrequest('EditEntityRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_entity_route_with_options_async(
        self,
        request: scsp_20200702_models.EditEntityRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.EditEntityRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.EditEntityRouteResponse(),
            await self.do_rpcrequest_async('EditEntityRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_entity_route(
        self,
        request: scsp_20200702_models.EditEntityRouteRequest,
    ) -> scsp_20200702_models.EditEntityRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_entity_route_with_options(request, runtime)

    async def edit_entity_route_async(
        self,
        request: scsp_20200702_models.EditEntityRouteRequest,
    ) -> scsp_20200702_models.EditEntityRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_entity_route_with_options_async(request, runtime)

    def get_tag_list_with_options(
        self,
        request: scsp_20200702_models.GetTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetTagListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetTagListResponse(),
            self.do_rpcrequest('GetTagList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_tag_list_with_options_async(
        self,
        request: scsp_20200702_models.GetTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetTagListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetTagListResponse(),
            await self.do_rpcrequest_async('GetTagList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_tag_list(
        self,
        request: scsp_20200702_models.GetTagListRequest,
    ) -> scsp_20200702_models.GetTagListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tag_list_with_options(request, runtime)

    async def get_tag_list_async(
        self,
        request: scsp_20200702_models.GetTagListRequest,
    ) -> scsp_20200702_models.GetTagListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_list_with_options_async(request, runtime)

    def update_ticket_with_options(
        self,
        request: scsp_20200702_models.UpdateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateTicketResponse(),
            self.do_rpcrequest('UpdateTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ticket_with_options_async(
        self,
        request: scsp_20200702_models.UpdateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateTicketResponse(),
            await self.do_rpcrequest_async('UpdateTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ticket(
        self,
        request: scsp_20200702_models.UpdateTicketRequest,
    ) -> scsp_20200702_models.UpdateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ticket_with_options(request, runtime)

    async def update_ticket_async(
        self,
        request: scsp_20200702_models.UpdateTicketRequest,
    ) -> scsp_20200702_models.UpdateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ticket_with_options_async(request, runtime)

    def list_outbound_phone_number_with_options(
        self,
        request: scsp_20200702_models.ListOutboundPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListOutboundPhoneNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListOutboundPhoneNumberResponse(),
            self.do_rpcrequest('ListOutboundPhoneNumber', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_outbound_phone_number_with_options_async(
        self,
        request: scsp_20200702_models.ListOutboundPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListOutboundPhoneNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListOutboundPhoneNumberResponse(),
            await self.do_rpcrequest_async('ListOutboundPhoneNumber', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_outbound_phone_number(
        self,
        request: scsp_20200702_models.ListOutboundPhoneNumberRequest,
    ) -> scsp_20200702_models.ListOutboundPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_phone_number_with_options(request, runtime)

    async def list_outbound_phone_number_async(
        self,
        request: scsp_20200702_models.ListOutboundPhoneNumberRequest,
    ) -> scsp_20200702_models.ListOutboundPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_phone_number_with_options_async(request, runtime)

    def remove_skill_group_with_options(
        self,
        request: scsp_20200702_models.RemoveSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.RemoveSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.RemoveSkillGroupResponse(),
            self.do_rpcrequest('RemoveSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_skill_group_with_options_async(
        self,
        request: scsp_20200702_models.RemoveSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.RemoveSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.RemoveSkillGroupResponse(),
            await self.do_rpcrequest_async('RemoveSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_skill_group(
        self,
        request: scsp_20200702_models.RemoveSkillGroupRequest,
    ) -> scsp_20200702_models.RemoveSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_group_with_options(request, runtime)

    async def remove_skill_group_async(
        self,
        request: scsp_20200702_models.RemoveSkillGroupRequest,
    ) -> scsp_20200702_models.RemoveSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_skill_group_with_options_async(request, runtime)

    def list_agent_by_skill_group_id_with_options(
        self,
        request: scsp_20200702_models.ListAgentBySkillGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListAgentBySkillGroupIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListAgentBySkillGroupIdResponse(),
            self.do_rpcrequest('ListAgentBySkillGroupId', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_agent_by_skill_group_id_with_options_async(
        self,
        request: scsp_20200702_models.ListAgentBySkillGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListAgentBySkillGroupIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListAgentBySkillGroupIdResponse(),
            await self.do_rpcrequest_async('ListAgentBySkillGroupId', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_agent_by_skill_group_id(
        self,
        request: scsp_20200702_models.ListAgentBySkillGroupIdRequest,
    ) -> scsp_20200702_models.ListAgentBySkillGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_by_skill_group_id_with_options(request, runtime)

    async def list_agent_by_skill_group_id_async(
        self,
        request: scsp_20200702_models.ListAgentBySkillGroupIdRequest,
    ) -> scsp_20200702_models.ListAgentBySkillGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_by_skill_group_id_with_options_async(request, runtime)

    def query_hotline_session_with_options(
        self,
        request: scsp_20200702_models.QueryHotlineSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryHotlineSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryHotlineSessionResponse(),
            self.do_rpcrequest('QueryHotlineSession', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_hotline_session_with_options_async(
        self,
        request: scsp_20200702_models.QueryHotlineSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryHotlineSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryHotlineSessionResponse(),
            await self.do_rpcrequest_async('QueryHotlineSession', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_hotline_session(
        self,
        request: scsp_20200702_models.QueryHotlineSessionRequest,
    ) -> scsp_20200702_models.QueryHotlineSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_hotline_session_with_options(request, runtime)

    async def query_hotline_session_async(
        self,
        request: scsp_20200702_models.QueryHotlineSessionRequest,
    ) -> scsp_20200702_models.QueryHotlineSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_hotline_session_with_options_async(request, runtime)

    def start_chat_work_with_options(
        self,
        request: scsp_20200702_models.StartChatWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartChatWorkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartChatWorkResponse(),
            self.do_rpcrequest('StartChatWork', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_chat_work_with_options_async(
        self,
        request: scsp_20200702_models.StartChatWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartChatWorkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartChatWorkResponse(),
            await self.do_rpcrequest_async('StartChatWork', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_chat_work(
        self,
        request: scsp_20200702_models.StartChatWorkRequest,
    ) -> scsp_20200702_models.StartChatWorkResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_chat_work_with_options(request, runtime)

    async def start_chat_work_async(
        self,
        request: scsp_20200702_models.StartChatWorkRequest,
    ) -> scsp_20200702_models.StartChatWorkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_chat_work_with_options_async(request, runtime)

    def hangup_third_call_with_options(
        self,
        request: scsp_20200702_models.HangupThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.HangupThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.HangupThirdCallResponse(),
            self.do_rpcrequest('HangupThirdCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hangup_third_call_with_options_async(
        self,
        request: scsp_20200702_models.HangupThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.HangupThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.HangupThirdCallResponse(),
            await self.do_rpcrequest_async('HangupThirdCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hangup_third_call(
        self,
        request: scsp_20200702_models.HangupThirdCallRequest,
    ) -> scsp_20200702_models.HangupThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hangup_third_call_with_options(request, runtime)

    async def hangup_third_call_async(
        self,
        request: scsp_20200702_models.HangupThirdCallRequest,
    ) -> scsp_20200702_models.HangupThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hangup_third_call_with_options_async(request, runtime)

    def start_hotline_service_with_options(
        self,
        request: scsp_20200702_models.StartHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartHotlineServiceResponse(),
            self.do_rpcrequest('StartHotlineService', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_hotline_service_with_options_async(
        self,
        request: scsp_20200702_models.StartHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartHotlineServiceResponse(),
            await self.do_rpcrequest_async('StartHotlineService', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_hotline_service(
        self,
        request: scsp_20200702_models.StartHotlineServiceRequest,
    ) -> scsp_20200702_models.StartHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_hotline_service_with_options(request, runtime)

    async def start_hotline_service_async(
        self,
        request: scsp_20200702_models.StartHotlineServiceRequest,
    ) -> scsp_20200702_models.StartHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_hotline_service_with_options_async(request, runtime)

    def start_call_v2with_options(
        self,
        request: scsp_20200702_models.StartCallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartCallV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartCallV2Response(),
            self.do_rpcrequest('StartCallV2', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_call_v2with_options_async(
        self,
        request: scsp_20200702_models.StartCallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartCallV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartCallV2Response(),
            await self.do_rpcrequest_async('StartCallV2', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_call_v2(
        self,
        request: scsp_20200702_models.StartCallV2Request,
    ) -> scsp_20200702_models.StartCallV2Response:
        runtime = util_models.RuntimeOptions()
        return self.start_call_v2with_options(request, runtime)

    async def start_call_v2_async(
        self,
        request: scsp_20200702_models.StartCallV2Request,
    ) -> scsp_20200702_models.StartCallV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.start_call_v2with_options_async(request, runtime)

    def enable_role_with_options(
        self,
        request: scsp_20200702_models.EnableRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.EnableRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.EnableRoleResponse(),
            self.do_rpcrequest('EnableRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_role_with_options_async(
        self,
        request: scsp_20200702_models.EnableRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.EnableRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.EnableRoleResponse(),
            await self.do_rpcrequest_async('EnableRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_role(
        self,
        request: scsp_20200702_models.EnableRoleRequest,
    ) -> scsp_20200702_models.EnableRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_role_with_options(request, runtime)

    async def enable_role_async(
        self,
        request: scsp_20200702_models.EnableRoleRequest,
    ) -> scsp_20200702_models.EnableRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_role_with_options_async(request, runtime)

    def get_agent_with_options(
        self,
        request: scsp_20200702_models.GetAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetAgentResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetAgentResponse(),
            self.do_rpcrequest('GetAgent', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: scsp_20200702_models.GetAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetAgentResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetAgentResponse(),
            await self.do_rpcrequest_async('GetAgent', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent(
        self,
        request: scsp_20200702_models.GetAgentRequest,
    ) -> scsp_20200702_models.GetAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_with_options(request, runtime)

    async def get_agent_async(
        self,
        request: scsp_20200702_models.GetAgentRequest,
    ) -> scsp_20200702_models.GetAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_with_options_async(request, runtime)

    def get_cmsid_by_foreign_id_with_options(
        self,
        request: scsp_20200702_models.GetCMSIdByForeignIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetCMSIdByForeignIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetCMSIdByForeignIdResponse(),
            self.do_rpcrequest('GetCMSIdByForeignId', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_cmsid_by_foreign_id_with_options_async(
        self,
        request: scsp_20200702_models.GetCMSIdByForeignIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetCMSIdByForeignIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetCMSIdByForeignIdResponse(),
            await self.do_rpcrequest_async('GetCMSIdByForeignId', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cmsid_by_foreign_id(
        self,
        request: scsp_20200702_models.GetCMSIdByForeignIdRequest,
    ) -> scsp_20200702_models.GetCMSIdByForeignIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cmsid_by_foreign_id_with_options(request, runtime)

    async def get_cmsid_by_foreign_id_async(
        self,
        request: scsp_20200702_models.GetCMSIdByForeignIdRequest,
    ) -> scsp_20200702_models.GetCMSIdByForeignIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cmsid_by_foreign_id_with_options_async(request, runtime)

    def transfer_to_third_call_with_options(
        self,
        request: scsp_20200702_models.TransferToThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferToThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferToThirdCallResponse(),
            self.do_rpcrequest('TransferToThirdCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_to_third_call_with_options_async(
        self,
        request: scsp_20200702_models.TransferToThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferToThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferToThirdCallResponse(),
            await self.do_rpcrequest_async('TransferToThirdCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_to_third_call(
        self,
        request: scsp_20200702_models.TransferToThirdCallRequest,
    ) -> scsp_20200702_models.TransferToThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_to_third_call_with_options(request, runtime)

    async def transfer_to_third_call_async(
        self,
        request: scsp_20200702_models.TransferToThirdCallRequest,
    ) -> scsp_20200702_models.TransferToThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_to_third_call_with_options_async(request, runtime)

    def update_agent_with_options(
        self,
        request: scsp_20200702_models.UpdateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateAgentResponse(),
            self.do_rpcrequest('UpdateAgent', '2020-07-02', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    async def update_agent_with_options_async(
        self,
        request: scsp_20200702_models.UpdateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateAgentResponse(),
            await self.do_rpcrequest_async('UpdateAgent', '2020-07-02', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def update_agent(
        self,
        request: scsp_20200702_models.UpdateAgentRequest,
    ) -> scsp_20200702_models.UpdateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_agent_with_options(request, runtime)

    async def update_agent_async(
        self,
        request: scsp_20200702_models.UpdateAgentRequest,
    ) -> scsp_20200702_models.UpdateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_agent_with_options_async(request, runtime)

    def change_chat_agent_status_with_options(
        self,
        request: scsp_20200702_models.ChangeChatAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ChangeChatAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.ChangeChatAgentStatusResponse(),
            self.do_rpcrequest('ChangeChatAgentStatus', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_chat_agent_status_with_options_async(
        self,
        request: scsp_20200702_models.ChangeChatAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ChangeChatAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.ChangeChatAgentStatusResponse(),
            await self.do_rpcrequest_async('ChangeChatAgentStatus', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_chat_agent_status(
        self,
        request: scsp_20200702_models.ChangeChatAgentStatusRequest,
    ) -> scsp_20200702_models.ChangeChatAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_chat_agent_status_with_options(request, runtime)

    async def change_chat_agent_status_async(
        self,
        request: scsp_20200702_models.ChangeChatAgentStatusRequest,
    ) -> scsp_20200702_models.ChangeChatAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_chat_agent_status_with_options_async(request, runtime)

    def generate_web_socket_sign_with_options(
        self,
        request: scsp_20200702_models.GenerateWebSocketSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GenerateWebSocketSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GenerateWebSocketSignResponse(),
            self.do_rpcrequest('GenerateWebSocketSign', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_web_socket_sign_with_options_async(
        self,
        request: scsp_20200702_models.GenerateWebSocketSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GenerateWebSocketSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GenerateWebSocketSignResponse(),
            await self.do_rpcrequest_async('GenerateWebSocketSign', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_web_socket_sign(
        self,
        request: scsp_20200702_models.GenerateWebSocketSignRequest,
    ) -> scsp_20200702_models.GenerateWebSocketSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_web_socket_sign_with_options(request, runtime)

    async def generate_web_socket_sign_async(
        self,
        request: scsp_20200702_models.GenerateWebSocketSignRequest,
    ) -> scsp_20200702_models.GenerateWebSocketSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_web_socket_sign_with_options_async(request, runtime)

    def update_ring_status_with_options(
        self,
        request: scsp_20200702_models.UpdateRingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateRingStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateRingStatusResponse(),
            self.do_rpcrequest('UpdateRingStatus', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ring_status_with_options_async(
        self,
        request: scsp_20200702_models.UpdateRingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateRingStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateRingStatusResponse(),
            await self.do_rpcrequest_async('UpdateRingStatus', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ring_status(
        self,
        request: scsp_20200702_models.UpdateRingStatusRequest,
    ) -> scsp_20200702_models.UpdateRingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ring_status_with_options(request, runtime)

    async def update_ring_status_async(
        self,
        request: scsp_20200702_models.UpdateRingStatusRequest,
    ) -> scsp_20200702_models.UpdateRingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ring_status_with_options_async(request, runtime)

    def create_agent_with_options(
        self,
        request: scsp_20200702_models.CreateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateAgentResponse(),
            self.do_rpcrequest('CreateAgent', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        request: scsp_20200702_models.CreateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateAgentResponse(),
            await self.do_rpcrequest_async('CreateAgent', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_agent(
        self,
        request: scsp_20200702_models.CreateAgentRequest,
    ) -> scsp_20200702_models.CreateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_agent_with_options(request, runtime)

    async def create_agent_async(
        self,
        request: scsp_20200702_models.CreateAgentRequest,
    ) -> scsp_20200702_models.CreateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_agent_with_options_async(request, runtime)

    def delete_entity_route_with_options(
        self,
        request: scsp_20200702_models.DeleteEntityRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.DeleteEntityRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.DeleteEntityRouteResponse(),
            self.do_rpcrequest('DeleteEntityRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_entity_route_with_options_async(
        self,
        request: scsp_20200702_models.DeleteEntityRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.DeleteEntityRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.DeleteEntityRouteResponse(),
            await self.do_rpcrequest_async('DeleteEntityRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_entity_route(
        self,
        request: scsp_20200702_models.DeleteEntityRouteRequest,
    ) -> scsp_20200702_models.DeleteEntityRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_route_with_options(request, runtime)

    async def delete_entity_route_async(
        self,
        request: scsp_20200702_models.DeleteEntityRouteRequest,
    ) -> scsp_20200702_models.DeleteEntityRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_entity_route_with_options_async(request, runtime)

    def get_hotline_group_detail_report_with_options(
        self,
        request: scsp_20200702_models.GetHotlineGroupDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineGroupDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineGroupDetailReportResponse(),
            self.do_rpcrequest('GetHotlineGroupDetailReport', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotline_group_detail_report_with_options_async(
        self,
        request: scsp_20200702_models.GetHotlineGroupDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineGroupDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineGroupDetailReportResponse(),
            await self.do_rpcrequest_async('GetHotlineGroupDetailReport', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_group_detail_report(
        self,
        request: scsp_20200702_models.GetHotlineGroupDetailReportRequest,
    ) -> scsp_20200702_models.GetHotlineGroupDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_group_detail_report_with_options(request, runtime)

    async def get_hotline_group_detail_report_async(
        self,
        request: scsp_20200702_models.GetHotlineGroupDetailReportRequest,
    ) -> scsp_20200702_models.GetHotlineGroupDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_group_detail_report_with_options_async(request, runtime)

    def create_ticket_with_options(
        self,
        request: scsp_20200702_models.CreateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateTicketResponse(),
            self.do_rpcrequest('CreateTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: scsp_20200702_models.CreateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateTicketResponse(),
            await self.do_rpcrequest_async('CreateTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ticket(
        self,
        request: scsp_20200702_models.CreateTicketRequest,
    ) -> scsp_20200702_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    async def create_ticket_async(
        self,
        request: scsp_20200702_models.CreateTicketRequest,
    ) -> scsp_20200702_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ticket_with_options_async(request, runtime)

    def update_customer_with_options(
        self,
        request: scsp_20200702_models.UpdateCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateCustomerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateCustomerResponse(),
            self.do_rpcrequest('UpdateCustomer', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_customer_with_options_async(
        self,
        request: scsp_20200702_models.UpdateCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateCustomerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateCustomerResponse(),
            await self.do_rpcrequest_async('UpdateCustomer', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_customer(
        self,
        request: scsp_20200702_models.UpdateCustomerRequest,
    ) -> scsp_20200702_models.UpdateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_customer_with_options(request, runtime)

    async def update_customer_async(
        self,
        request: scsp_20200702_models.UpdateCustomerRequest,
    ) -> scsp_20200702_models.UpdateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_customer_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: scsp_20200702_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.AnswerCallResponse(),
            self.do_rpcrequest('AnswerCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: scsp_20200702_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.AnswerCallResponse(),
            await self.do_rpcrequest_async('AnswerCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def answer_call(
        self,
        request: scsp_20200702_models.AnswerCallRequest,
    ) -> scsp_20200702_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: scsp_20200702_models.AnswerCallRequest,
    ) -> scsp_20200702_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def delete_agent_with_options(
        self,
        request: scsp_20200702_models.DeleteAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.DeleteAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.DeleteAgentResponse(),
            self.do_rpcrequest('DeleteAgent', '2020-07-02', 'HTTPS', 'DELETE', 'AK', 'json', req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        request: scsp_20200702_models.DeleteAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.DeleteAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.DeleteAgentResponse(),
            await self.do_rpcrequest_async('DeleteAgent', '2020-07-02', 'HTTPS', 'DELETE', 'AK', 'json', req, runtime)
        )

    def delete_agent(
        self,
        request: scsp_20200702_models.DeleteAgentRequest,
    ) -> scsp_20200702_models.DeleteAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_agent_with_options(request, runtime)

    async def delete_agent_async(
        self,
        request: scsp_20200702_models.DeleteAgentRequest,
    ) -> scsp_20200702_models.DeleteAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_agent_with_options_async(request, runtime)

    def get_entity_tag_relation_with_options(
        self,
        request: scsp_20200702_models.GetEntityTagRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetEntityTagRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetEntityTagRelationResponse(),
            self.do_rpcrequest('GetEntityTagRelation', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_entity_tag_relation_with_options_async(
        self,
        request: scsp_20200702_models.GetEntityTagRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetEntityTagRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetEntityTagRelationResponse(),
            await self.do_rpcrequest_async('GetEntityTagRelation', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_entity_tag_relation(
        self,
        request: scsp_20200702_models.GetEntityTagRelationRequest,
    ) -> scsp_20200702_models.GetEntityTagRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_entity_tag_relation_with_options(request, runtime)

    async def get_entity_tag_relation_async(
        self,
        request: scsp_20200702_models.GetEntityTagRelationRequest,
    ) -> scsp_20200702_models.GetEntityTagRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_entity_tag_relation_with_options_async(request, runtime)

    def get_hotline_agent_detail_with_options(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineAgentDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineAgentDetailResponse(),
            self.do_rpcrequest('GetHotlineAgentDetail', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hotline_agent_detail_with_options_async(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineAgentDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineAgentDetailResponse(),
            await self.do_rpcrequest_async('GetHotlineAgentDetail', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_detail(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailRequest,
    ) -> scsp_20200702_models.GetHotlineAgentDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_with_options(request, runtime)

    async def get_hotline_agent_detail_async(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailRequest,
    ) -> scsp_20200702_models.GetHotlineAgentDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_detail_with_options_async(request, runtime)

    def suspend_hotline_service_with_options(
        self,
        request: scsp_20200702_models.SuspendHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SuspendHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.SuspendHotlineServiceResponse(),
            self.do_rpcrequest('SuspendHotlineService', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_hotline_service_with_options_async(
        self,
        request: scsp_20200702_models.SuspendHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SuspendHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.SuspendHotlineServiceResponse(),
            await self.do_rpcrequest_async('SuspendHotlineService', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_hotline_service(
        self,
        request: scsp_20200702_models.SuspendHotlineServiceRequest,
    ) -> scsp_20200702_models.SuspendHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_hotline_service_with_options(request, runtime)

    async def suspend_hotline_service_async(
        self,
        request: scsp_20200702_models.SuspendHotlineServiceRequest,
    ) -> scsp_20200702_models.SuspendHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_hotline_service_with_options_async(request, runtime)

    def get_calls_per_day_with_options(
        self,
        request: scsp_20200702_models.GetCallsPerDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetCallsPerDayResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetCallsPerDayResponse(),
            self.do_rpcrequest('GetCallsPerDay', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_calls_per_day_with_options_async(
        self,
        request: scsp_20200702_models.GetCallsPerDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetCallsPerDayResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetCallsPerDayResponse(),
            await self.do_rpcrequest_async('GetCallsPerDay', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_calls_per_day(
        self,
        request: scsp_20200702_models.GetCallsPerDayRequest,
    ) -> scsp_20200702_models.GetCallsPerDayResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_calls_per_day_with_options(request, runtime)

    async def get_calls_per_day_async(
        self,
        request: scsp_20200702_models.GetCallsPerDayRequest,
    ) -> scsp_20200702_models.GetCallsPerDayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_calls_per_day_with_options_async(request, runtime)

    def fetch_call_with_options(
        self,
        request: scsp_20200702_models.FetchCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.FetchCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.FetchCallResponse(),
            self.do_rpcrequest('FetchCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fetch_call_with_options_async(
        self,
        request: scsp_20200702_models.FetchCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.FetchCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.FetchCallResponse(),
            await self.do_rpcrequest_async('FetchCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_call(
        self,
        request: scsp_20200702_models.FetchCallRequest,
    ) -> scsp_20200702_models.FetchCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_call_with_options(request, runtime)

    async def fetch_call_async(
        self,
        request: scsp_20200702_models.FetchCallRequest,
    ) -> scsp_20200702_models.FetchCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_call_with_options_async(request, runtime)

    def get_hotline_agent_detail_report_with_options(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineAgentDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineAgentDetailReportResponse(),
            self.do_rpcrequest('GetHotlineAgentDetailReport', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotline_agent_detail_report_with_options_async(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineAgentDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineAgentDetailReportResponse(),
            await self.do_rpcrequest_async('GetHotlineAgentDetailReport', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_detail_report(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailReportRequest,
    ) -> scsp_20200702_models.GetHotlineAgentDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_report_with_options(request, runtime)

    async def get_hotline_agent_detail_report_async(
        self,
        request: scsp_20200702_models.GetHotlineAgentDetailReportRequest,
    ) -> scsp_20200702_models.GetHotlineAgentDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_detail_report_with_options_async(request, runtime)

    def query_ticket_count_with_options(
        self,
        request: scsp_20200702_models.QueryTicketCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryTicketCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryTicketCountResponse(),
            self.do_rpcrequest('QueryTicketCount', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_ticket_count_with_options_async(
        self,
        request: scsp_20200702_models.QueryTicketCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryTicketCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryTicketCountResponse(),
            await self.do_rpcrequest_async('QueryTicketCount', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ticket_count(
        self,
        request: scsp_20200702_models.QueryTicketCountRequest,
    ) -> scsp_20200702_models.QueryTicketCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ticket_count_with_options(request, runtime)

    async def query_ticket_count_async(
        self,
        request: scsp_20200702_models.QueryTicketCountRequest,
    ) -> scsp_20200702_models.QueryTicketCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ticket_count_with_options_async(request, runtime)

    def app_message_push_with_options(
        self,
        request: scsp_20200702_models.AppMessagePushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.AppMessagePushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.AppMessagePushResponse(),
            self.do_rpcrequest('AppMessagePush', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def app_message_push_with_options_async(
        self,
        request: scsp_20200702_models.AppMessagePushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.AppMessagePushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.AppMessagePushResponse(),
            await self.do_rpcrequest_async('AppMessagePush', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def app_message_push(
        self,
        request: scsp_20200702_models.AppMessagePushRequest,
    ) -> scsp_20200702_models.AppMessagePushResponse:
        runtime = util_models.RuntimeOptions()
        return self.app_message_push_with_options(request, runtime)

    async def app_message_push_async(
        self,
        request: scsp_20200702_models.AppMessagePushRequest,
    ) -> scsp_20200702_models.AppMessagePushResponse:
        runtime = util_models.RuntimeOptions()
        return await self.app_message_push_with_options_async(request, runtime)

    def get_hotline_agent_status_with_options(
        self,
        request: scsp_20200702_models.GetHotlineAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineAgentStatusResponse(),
            self.do_rpcrequest('GetHotlineAgentStatus', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotline_agent_status_with_options_async(
        self,
        request: scsp_20200702_models.GetHotlineAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineAgentStatusResponse(),
            await self.do_rpcrequest_async('GetHotlineAgentStatus', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_status(
        self,
        request: scsp_20200702_models.GetHotlineAgentStatusRequest,
    ) -> scsp_20200702_models.GetHotlineAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_status_with_options(request, runtime)

    async def get_hotline_agent_status_async(
        self,
        request: scsp_20200702_models.GetHotlineAgentStatusRequest,
    ) -> scsp_20200702_models.GetHotlineAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_status_with_options_async(request, runtime)

    def get_hotline_waiting_number_with_options(
        self,
        request: scsp_20200702_models.GetHotlineWaitingNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineWaitingNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineWaitingNumberResponse(),
            self.do_rpcrequest('GetHotlineWaitingNumber', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hotline_waiting_number_with_options_async(
        self,
        request: scsp_20200702_models.GetHotlineWaitingNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetHotlineWaitingNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetHotlineWaitingNumberResponse(),
            await self.do_rpcrequest_async('GetHotlineWaitingNumber', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_waiting_number(
        self,
        request: scsp_20200702_models.GetHotlineWaitingNumberRequest,
    ) -> scsp_20200702_models.GetHotlineWaitingNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_waiting_number_with_options(request, runtime)

    async def get_hotline_waiting_number_async(
        self,
        request: scsp_20200702_models.GetHotlineWaitingNumberRequest,
    ) -> scsp_20200702_models.GetHotlineWaitingNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_waiting_number_with_options_async(request, runtime)

    def start_call_with_options(
        self,
        request: scsp_20200702_models.StartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartCallResponse(),
            self.do_rpcrequest('StartCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_call_with_options_async(
        self,
        request: scsp_20200702_models.StartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.StartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.StartCallResponse(),
            await self.do_rpcrequest_async('StartCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_call(
        self,
        request: scsp_20200702_models.StartCallRequest,
    ) -> scsp_20200702_models.StartCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_call_with_options(request, runtime)

    async def start_call_async(
        self,
        request: scsp_20200702_models.StartCallRequest,
    ) -> scsp_20200702_models.StartCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_call_with_options_async(request, runtime)

    def assign_ticket_with_options(
        self,
        request: scsp_20200702_models.AssignTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.AssignTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.AssignTicketResponse(),
            self.do_rpcrequest('AssignTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_ticket_with_options_async(
        self,
        request: scsp_20200702_models.AssignTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.AssignTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.AssignTicketResponse(),
            await self.do_rpcrequest_async('AssignTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_ticket(
        self,
        request: scsp_20200702_models.AssignTicketRequest,
    ) -> scsp_20200702_models.AssignTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_ticket_with_options(request, runtime)

    async def assign_ticket_async(
        self,
        request: scsp_20200702_models.AssignTicketRequest,
    ) -> scsp_20200702_models.AssignTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_ticket_with_options_async(request, runtime)

    def hangup_call_with_options(
        self,
        request: scsp_20200702_models.HangupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.HangupCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.HangupCallResponse(),
            self.do_rpcrequest('HangupCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hangup_call_with_options_async(
        self,
        request: scsp_20200702_models.HangupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.HangupCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.HangupCallResponse(),
            await self.do_rpcrequest_async('HangupCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hangup_call(
        self,
        request: scsp_20200702_models.HangupCallRequest,
    ) -> scsp_20200702_models.HangupCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hangup_call_with_options(request, runtime)

    async def hangup_call_async(
        self,
        request: scsp_20200702_models.HangupCallRequest,
    ) -> scsp_20200702_models.HangupCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hangup_call_with_options_async(request, runtime)

    def get_outboun_num_list_with_options(
        self,
        request: scsp_20200702_models.GetOutbounNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetOutbounNumListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetOutbounNumListResponse(),
            self.do_rpcrequest('GetOutbounNumList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_outboun_num_list_with_options_async(
        self,
        request: scsp_20200702_models.GetOutbounNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetOutbounNumListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetOutbounNumListResponse(),
            await self.do_rpcrequest_async('GetOutbounNumList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_outboun_num_list(
        self,
        request: scsp_20200702_models.GetOutbounNumListRequest,
    ) -> scsp_20200702_models.GetOutbounNumListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_outboun_num_list_with_options(request, runtime)

    async def get_outboun_num_list_async(
        self,
        request: scsp_20200702_models.GetOutbounNumListRequest,
    ) -> scsp_20200702_models.GetOutbounNumListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_outboun_num_list_with_options_async(request, runtime)

    def create_ticket_with_biz_data_with_options(
        self,
        request: scsp_20200702_models.CreateTicketWithBizDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateTicketWithBizDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateTicketWithBizDataResponse(),
            self.do_rpcrequest('createTicketWithBizData', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ticket_with_biz_data_with_options_async(
        self,
        request: scsp_20200702_models.CreateTicketWithBizDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateTicketWithBizDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateTicketWithBizDataResponse(),
            await self.do_rpcrequest_async('createTicketWithBizData', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ticket_with_biz_data(
        self,
        request: scsp_20200702_models.CreateTicketWithBizDataRequest,
    ) -> scsp_20200702_models.CreateTicketWithBizDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_with_biz_data_with_options(request, runtime)

    async def create_ticket_with_biz_data_async(
        self,
        request: scsp_20200702_models.CreateTicketWithBizDataRequest,
    ) -> scsp_20200702_models.CreateTicketWithBizDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ticket_with_biz_data_with_options_async(request, runtime)

    def search_ticket_by_phone_with_options(
        self,
        request: scsp_20200702_models.SearchTicketByPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SearchTicketByPhoneResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.SearchTicketByPhoneResponse(),
            self.do_rpcrequest('SearchTicketByPhone', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def search_ticket_by_phone_with_options_async(
        self,
        request: scsp_20200702_models.SearchTicketByPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SearchTicketByPhoneResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.SearchTicketByPhoneResponse(),
            await self.do_rpcrequest_async('SearchTicketByPhone', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def search_ticket_by_phone(
        self,
        request: scsp_20200702_models.SearchTicketByPhoneRequest,
    ) -> scsp_20200702_models.SearchTicketByPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_ticket_by_phone_with_options(request, runtime)

    async def search_ticket_by_phone_async(
        self,
        request: scsp_20200702_models.SearchTicketByPhoneRequest,
    ) -> scsp_20200702_models.SearchTicketByPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_ticket_by_phone_with_options_async(request, runtime)

    def create_third_sso_agent_with_options(
        self,
        request: scsp_20200702_models.CreateThirdSsoAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateThirdSsoAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateThirdSsoAgentResponse(),
            self.do_rpcrequest('CreateThirdSsoAgent', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_third_sso_agent_with_options_async(
        self,
        request: scsp_20200702_models.CreateThirdSsoAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateThirdSsoAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateThirdSsoAgentResponse(),
            await self.do_rpcrequest_async('CreateThirdSsoAgent', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_third_sso_agent(
        self,
        request: scsp_20200702_models.CreateThirdSsoAgentRequest,
    ) -> scsp_20200702_models.CreateThirdSsoAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_third_sso_agent_with_options(request, runtime)

    async def create_third_sso_agent_async(
        self,
        request: scsp_20200702_models.CreateThirdSsoAgentRequest,
    ) -> scsp_20200702_models.CreateThirdSsoAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_third_sso_agent_with_options_async(request, runtime)

    def create_entity_ivr_route_with_options(
        self,
        request: scsp_20200702_models.CreateEntityIvrRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateEntityIvrRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateEntityIvrRouteResponse(),
            self.do_rpcrequest('CreateEntityIvrRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_entity_ivr_route_with_options_async(
        self,
        request: scsp_20200702_models.CreateEntityIvrRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateEntityIvrRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateEntityIvrRouteResponse(),
            await self.do_rpcrequest_async('CreateEntityIvrRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_entity_ivr_route(
        self,
        request: scsp_20200702_models.CreateEntityIvrRouteRequest,
    ) -> scsp_20200702_models.CreateEntityIvrRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_entity_ivr_route_with_options(request, runtime)

    async def create_entity_ivr_route_async(
        self,
        request: scsp_20200702_models.CreateEntityIvrRouteRequest,
    ) -> scsp_20200702_models.CreateEntityIvrRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_entity_ivr_route_with_options_async(request, runtime)

    def close_ticket_with_options(
        self,
        request: scsp_20200702_models.CloseTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CloseTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CloseTicketResponse(),
            self.do_rpcrequest('CloseTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_ticket_with_options_async(
        self,
        request: scsp_20200702_models.CloseTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CloseTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CloseTicketResponse(),
            await self.do_rpcrequest_async('CloseTicket', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_ticket(
        self,
        request: scsp_20200702_models.CloseTicketRequest,
    ) -> scsp_20200702_models.CloseTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_ticket_with_options(request, runtime)

    async def close_ticket_async(
        self,
        request: scsp_20200702_models.CloseTicketRequest,
    ) -> scsp_20200702_models.CloseTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_ticket_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: scsp_20200702_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.HoldCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.HoldCallResponse(),
            self.do_rpcrequest('HoldCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: scsp_20200702_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.HoldCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.HoldCallResponse(),
            await self.do_rpcrequest_async('HoldCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hold_call(
        self,
        request: scsp_20200702_models.HoldCallRequest,
    ) -> scsp_20200702_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: scsp_20200702_models.HoldCallRequest,
    ) -> scsp_20200702_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def query_ring_detail_list_with_options(
        self,
        tmp_req: scsp_20200702_models.QueryRingDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryRingDetailListResponse:
        UtilClient.validate_model(tmp_req)
        request = scsp_20200702_models.QueryRingDetailListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.from_phone_num_list):
            request.from_phone_num_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.from_phone_num_list, 'FromPhoneNumList', 'json')
        if not UtilClient.is_unset(tmp_req.to_phone_num_list):
            request.to_phone_num_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_phone_num_list, 'ToPhoneNumList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryRingDetailListResponse(),
            self.do_rpcrequest('QueryRingDetailList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_ring_detail_list_with_options_async(
        self,
        tmp_req: scsp_20200702_models.QueryRingDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryRingDetailListResponse:
        UtilClient.validate_model(tmp_req)
        request = scsp_20200702_models.QueryRingDetailListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.from_phone_num_list):
            request.from_phone_num_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.from_phone_num_list, 'FromPhoneNumList', 'json')
        if not UtilClient.is_unset(tmp_req.to_phone_num_list):
            request.to_phone_num_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_phone_num_list, 'ToPhoneNumList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryRingDetailListResponse(),
            await self.do_rpcrequest_async('QueryRingDetailList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ring_detail_list(
        self,
        request: scsp_20200702_models.QueryRingDetailListRequest,
    ) -> scsp_20200702_models.QueryRingDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ring_detail_list_with_options(request, runtime)

    async def query_ring_detail_list_async(
        self,
        request: scsp_20200702_models.QueryRingDetailListRequest,
    ) -> scsp_20200702_models.QueryRingDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ring_detail_list_with_options_async(request, runtime)

    def search_ticket_by_id_with_options(
        self,
        request: scsp_20200702_models.SearchTicketByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SearchTicketByIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.SearchTicketByIdResponse(),
            self.do_rpcrequest('SearchTicketById', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def search_ticket_by_id_with_options_async(
        self,
        request: scsp_20200702_models.SearchTicketByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SearchTicketByIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.SearchTicketByIdResponse(),
            await self.do_rpcrequest_async('SearchTicketById', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def search_ticket_by_id(
        self,
        request: scsp_20200702_models.SearchTicketByIdRequest,
    ) -> scsp_20200702_models.SearchTicketByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_ticket_by_id_with_options(request, runtime)

    async def search_ticket_by_id_async(
        self,
        request: scsp_20200702_models.SearchTicketByIdRequest,
    ) -> scsp_20200702_models.SearchTicketByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_ticket_by_id_with_options_async(request, runtime)

    def update_skill_group_with_options(
        self,
        request: scsp_20200702_models.UpdateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateSkillGroupResponse(),
            self.do_rpcrequest('UpdateSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_skill_group_with_options_async(
        self,
        request: scsp_20200702_models.UpdateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateSkillGroupResponse(),
            await self.do_rpcrequest_async('UpdateSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_skill_group(
        self,
        request: scsp_20200702_models.UpdateSkillGroupRequest,
    ) -> scsp_20200702_models.UpdateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_with_options(request, runtime)

    async def update_skill_group_async(
        self,
        request: scsp_20200702_models.UpdateSkillGroupRequest,
    ) -> scsp_20200702_models.UpdateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_skill_group_with_options_async(request, runtime)

    def query_service_config_with_options(
        self,
        request: scsp_20200702_models.QueryServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryServiceConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryServiceConfigResponse(),
            self.do_rpcrequest('QueryServiceConfig', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_service_config_with_options_async(
        self,
        request: scsp_20200702_models.QueryServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryServiceConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryServiceConfigResponse(),
            await self.do_rpcrequest_async('QueryServiceConfig', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_service_config(
        self,
        request: scsp_20200702_models.QueryServiceConfigRequest,
    ) -> scsp_20200702_models.QueryServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_service_config_with_options(request, runtime)

    async def query_service_config_async(
        self,
        request: scsp_20200702_models.QueryServiceConfigRequest,
    ) -> scsp_20200702_models.QueryServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_service_config_with_options_async(request, runtime)

    def disable_role_with_options(
        self,
        request: scsp_20200702_models.DisableRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.DisableRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.DisableRoleResponse(),
            self.do_rpcrequest('DisableRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_role_with_options_async(
        self,
        request: scsp_20200702_models.DisableRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.DisableRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.DisableRoleResponse(),
            await self.do_rpcrequest_async('DisableRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_role(
        self,
        request: scsp_20200702_models.DisableRoleRequest,
    ) -> scsp_20200702_models.DisableRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_role_with_options(request, runtime)

    async def disable_role_async(
        self,
        request: scsp_20200702_models.DisableRoleRequest,
    ) -> scsp_20200702_models.DisableRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_role_with_options_async(request, runtime)

    def get_entity_route_list_with_options(
        self,
        request: scsp_20200702_models.GetEntityRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetEntityRouteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetEntityRouteListResponse(),
            self.do_rpcrequest('GetEntityRouteList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_entity_route_list_with_options_async(
        self,
        request: scsp_20200702_models.GetEntityRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetEntityRouteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetEntityRouteListResponse(),
            await self.do_rpcrequest_async('GetEntityRouteList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_entity_route_list(
        self,
        request: scsp_20200702_models.GetEntityRouteListRequest,
    ) -> scsp_20200702_models.GetEntityRouteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_entity_route_list_with_options(request, runtime)

    async def get_entity_route_list_async(
        self,
        request: scsp_20200702_models.GetEntityRouteListRequest,
    ) -> scsp_20200702_models.GetEntityRouteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_entity_route_list_with_options_async(request, runtime)

    def get_auth_info_with_options(
        self,
        request: scsp_20200702_models.GetAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetAuthInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetAuthInfoResponse(),
            self.do_rpcrequest('GetAuthInfo', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_auth_info_with_options_async(
        self,
        request: scsp_20200702_models.GetAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetAuthInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetAuthInfoResponse(),
            await self.do_rpcrequest_async('GetAuthInfo', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auth_info(
        self,
        request: scsp_20200702_models.GetAuthInfoRequest,
    ) -> scsp_20200702_models.GetAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auth_info_with_options(request, runtime)

    async def get_auth_info_async(
        self,
        request: scsp_20200702_models.GetAuthInfoRequest,
    ) -> scsp_20200702_models.GetAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auth_info_with_options_async(request, runtime)

    def update_role_with_options(
        self,
        request: scsp_20200702_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateRoleResponse(),
            self.do_rpcrequest('UpdateRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: scsp_20200702_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateRoleResponse(),
            await self.do_rpcrequest_async('UpdateRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_role(
        self,
        request: scsp_20200702_models.UpdateRoleRequest,
    ) -> scsp_20200702_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)

    async def update_role_async(
        self,
        request: scsp_20200702_models.UpdateRoleRequest,
    ) -> scsp_20200702_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_role_with_options_async(request, runtime)

    def get_ticket_template_schema_with_options(
        self,
        request: scsp_20200702_models.GetTicketTemplateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetTicketTemplateSchemaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetTicketTemplateSchemaResponse(),
            self.do_rpcrequest('GetTicketTemplateSchema', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_ticket_template_schema_with_options_async(
        self,
        request: scsp_20200702_models.GetTicketTemplateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetTicketTemplateSchemaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetTicketTemplateSchemaResponse(),
            await self.do_rpcrequest_async('GetTicketTemplateSchema', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ticket_template_schema(
        self,
        request: scsp_20200702_models.GetTicketTemplateSchemaRequest,
    ) -> scsp_20200702_models.GetTicketTemplateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ticket_template_schema_with_options(request, runtime)

    async def get_ticket_template_schema_async(
        self,
        request: scsp_20200702_models.GetTicketTemplateSchemaRequest,
    ) -> scsp_20200702_models.GetTicketTemplateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ticket_template_schema_with_options_async(request, runtime)

    def transfer_call_to_phone_with_options(
        self,
        request: scsp_20200702_models.TransferCallToPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferCallToPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferCallToPhoneResponse(),
            self.do_rpcrequest('TransferCallToPhone', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_call_to_phone_with_options_async(
        self,
        request: scsp_20200702_models.TransferCallToPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferCallToPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferCallToPhoneResponse(),
            await self.do_rpcrequest_async('TransferCallToPhone', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_call_to_phone(
        self,
        request: scsp_20200702_models.TransferCallToPhoneRequest,
    ) -> scsp_20200702_models.TransferCallToPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_call_to_phone_with_options(request, runtime)

    async def transfer_call_to_phone_async(
        self,
        request: scsp_20200702_models.TransferCallToPhoneRequest,
    ) -> scsp_20200702_models.TransferCallToPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_call_to_phone_with_options_async(request, runtime)

    def query_skill_groups_with_options(
        self,
        request: scsp_20200702_models.QuerySkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QuerySkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QuerySkillGroupsResponse(),
            self.do_rpcrequest('QuerySkillGroups', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_skill_groups_with_options_async(
        self,
        request: scsp_20200702_models.QuerySkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QuerySkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QuerySkillGroupsResponse(),
            await self.do_rpcrequest_async('QuerySkillGroups', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_skill_groups(
        self,
        request: scsp_20200702_models.QuerySkillGroupsRequest,
    ) -> scsp_20200702_models.QuerySkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_skill_groups_with_options(request, runtime)

    async def query_skill_groups_async(
        self,
        request: scsp_20200702_models.QuerySkillGroupsRequest,
    ) -> scsp_20200702_models.QuerySkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_skill_groups_with_options_async(request, runtime)

    def get_entity_route_with_options(
        self,
        request: scsp_20200702_models.GetEntityRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetEntityRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetEntityRouteResponse(),
            self.do_rpcrequest('GetEntityRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_entity_route_with_options_async(
        self,
        request: scsp_20200702_models.GetEntityRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetEntityRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetEntityRouteResponse(),
            await self.do_rpcrequest_async('GetEntityRoute', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_entity_route(
        self,
        request: scsp_20200702_models.GetEntityRouteRequest,
    ) -> scsp_20200702_models.GetEntityRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_entity_route_with_options(request, runtime)

    async def get_entity_route_async(
        self,
        request: scsp_20200702_models.GetEntityRouteRequest,
    ) -> scsp_20200702_models.GetEntityRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_entity_route_with_options_async(request, runtime)

    def update_entity_tag_relation_with_options(
        self,
        request: scsp_20200702_models.UpdateEntityTagRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateEntityTagRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateEntityTagRelationResponse(),
            self.do_rpcrequest('UpdateEntityTagRelation', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_entity_tag_relation_with_options_async(
        self,
        request: scsp_20200702_models.UpdateEntityTagRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.UpdateEntityTagRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.UpdateEntityTagRelationResponse(),
            await self.do_rpcrequest_async('UpdateEntityTagRelation', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_entity_tag_relation(
        self,
        request: scsp_20200702_models.UpdateEntityTagRelationRequest,
    ) -> scsp_20200702_models.UpdateEntityTagRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_entity_tag_relation_with_options(request, runtime)

    async def update_entity_tag_relation_async(
        self,
        request: scsp_20200702_models.UpdateEntityTagRelationRequest,
    ) -> scsp_20200702_models.UpdateEntityTagRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_entity_tag_relation_with_options_async(request, runtime)

    def create_outer_call_center_data_with_options(
        self,
        request: scsp_20200702_models.CreateOuterCallCenterDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateOuterCallCenterDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateOuterCallCenterDataResponse(),
            self.do_rpcrequest('CreateOuterCallCenterData', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_outer_call_center_data_with_options_async(
        self,
        request: scsp_20200702_models.CreateOuterCallCenterDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateOuterCallCenterDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateOuterCallCenterDataResponse(),
            await self.do_rpcrequest_async('CreateOuterCallCenterData', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_outer_call_center_data(
        self,
        request: scsp_20200702_models.CreateOuterCallCenterDataRequest,
    ) -> scsp_20200702_models.CreateOuterCallCenterDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_outer_call_center_data_with_options(request, runtime)

    async def create_outer_call_center_data_async(
        self,
        request: scsp_20200702_models.CreateOuterCallCenterDataRequest,
    ) -> scsp_20200702_models.CreateOuterCallCenterDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_outer_call_center_data_with_options_async(request, runtime)

    def send_outbound_command_with_options(
        self,
        request: scsp_20200702_models.SendOutboundCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SendOutboundCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.SendOutboundCommandResponse(),
            self.do_rpcrequest('SendOutboundCommand', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_outbound_command_with_options_async(
        self,
        request: scsp_20200702_models.SendOutboundCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.SendOutboundCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.SendOutboundCommandResponse(),
            await self.do_rpcrequest_async('SendOutboundCommand', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_outbound_command(
        self,
        request: scsp_20200702_models.SendOutboundCommandRequest,
    ) -> scsp_20200702_models.SendOutboundCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_outbound_command_with_options(request, runtime)

    async def send_outbound_command_async(
        self,
        request: scsp_20200702_models.SendOutboundCommandRequest,
    ) -> scsp_20200702_models.SendOutboundCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_outbound_command_with_options_async(request, runtime)

    def create_role_with_options(
        self,
        request: scsp_20200702_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateRoleResponse(),
            self.do_rpcrequest('CreateRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: scsp_20200702_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateRoleResponse(),
            await self.do_rpcrequest_async('CreateRole', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_role(
        self,
        request: scsp_20200702_models.CreateRoleRequest,
    ) -> scsp_20200702_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    async def create_role_async(
        self,
        request: scsp_20200702_models.CreateRoleRequest,
    ) -> scsp_20200702_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_role_with_options_async(request, runtime)

    def list_skill_group_with_options(
        self,
        request: scsp_20200702_models.ListSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListSkillGroupResponse(),
            self.do_rpcrequest('ListSkillGroup', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_skill_group_with_options_async(
        self,
        request: scsp_20200702_models.ListSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListSkillGroupResponse(),
            await self.do_rpcrequest_async('ListSkillGroup', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_skill_group(
        self,
        request: scsp_20200702_models.ListSkillGroupRequest,
    ) -> scsp_20200702_models.ListSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_with_options(request, runtime)

    async def list_skill_group_async(
        self,
        request: scsp_20200702_models.ListSkillGroupRequest,
    ) -> scsp_20200702_models.ListSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_with_options_async(request, runtime)

    def grant_roles_with_options(
        self,
        request: scsp_20200702_models.GrantRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GrantRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GrantRolesResponse(),
            self.do_rpcrequest('GrantRoles', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_roles_with_options_async(
        self,
        request: scsp_20200702_models.GrantRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GrantRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GrantRolesResponse(),
            await self.do_rpcrequest_async('GrantRoles', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_roles(
        self,
        request: scsp_20200702_models.GrantRolesRequest,
    ) -> scsp_20200702_models.GrantRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_roles_with_options(request, runtime)

    async def grant_roles_async(
        self,
        request: scsp_20200702_models.GrantRolesRequest,
    ) -> scsp_20200702_models.GrantRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_roles_with_options_async(request, runtime)

    def get_outer_call_center_data_list_with_options(
        self,
        request: scsp_20200702_models.GetOuterCallCenterDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetOuterCallCenterDataListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetOuterCallCenterDataListResponse(),
            self.do_rpcrequest('GetOuterCallCenterDataList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_outer_call_center_data_list_with_options_async(
        self,
        request: scsp_20200702_models.GetOuterCallCenterDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetOuterCallCenterDataListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetOuterCallCenterDataListResponse(),
            await self.do_rpcrequest_async('GetOuterCallCenterDataList', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_outer_call_center_data_list(
        self,
        request: scsp_20200702_models.GetOuterCallCenterDataListRequest,
    ) -> scsp_20200702_models.GetOuterCallCenterDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_outer_call_center_data_list_with_options(request, runtime)

    async def get_outer_call_center_data_list_async(
        self,
        request: scsp_20200702_models.GetOuterCallCenterDataListRequest,
    ) -> scsp_20200702_models.GetOuterCallCenterDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_outer_call_center_data_list_with_options_async(request, runtime)

    def query_tickets_with_options(
        self,
        tmp_req: scsp_20200702_models.QueryTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryTicketsResponse:
        UtilClient.validate_model(tmp_req)
        request = scsp_20200702_models.QueryTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryTicketsResponse(),
            self.do_rpcrequest('QueryTickets', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_tickets_with_options_async(
        self,
        tmp_req: scsp_20200702_models.QueryTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryTicketsResponse:
        UtilClient.validate_model(tmp_req)
        request = scsp_20200702_models.QueryTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryTicketsResponse(),
            await self.do_rpcrequest_async('QueryTickets', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tickets(
        self,
        request: scsp_20200702_models.QueryTicketsRequest,
    ) -> scsp_20200702_models.QueryTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tickets_with_options(request, runtime)

    async def query_tickets_async(
        self,
        request: scsp_20200702_models.QueryTicketsRequest,
    ) -> scsp_20200702_models.QueryTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tickets_with_options_async(request, runtime)

    def query_ticket_actions_with_options(
        self,
        request: scsp_20200702_models.QueryTicketActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryTicketActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryTicketActionsResponse(),
            self.do_rpcrequest('QueryTicketActions', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_ticket_actions_with_options_async(
        self,
        request: scsp_20200702_models.QueryTicketActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.QueryTicketActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.QueryTicketActionsResponse(),
            await self.do_rpcrequest_async('QueryTicketActions', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ticket_actions(
        self,
        request: scsp_20200702_models.QueryTicketActionsRequest,
    ) -> scsp_20200702_models.QueryTicketActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ticket_actions_with_options(request, runtime)

    async def query_ticket_actions_async(
        self,
        request: scsp_20200702_models.QueryTicketActionsRequest,
    ) -> scsp_20200702_models.QueryTicketActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ticket_actions_with_options_async(request, runtime)

    def transfer_call_to_agent_with_options(
        self,
        request: scsp_20200702_models.TransferCallToAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferCallToAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferCallToAgentResponse(),
            self.do_rpcrequest('TransferCallToAgent', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_call_to_agent_with_options_async(
        self,
        request: scsp_20200702_models.TransferCallToAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.TransferCallToAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.TransferCallToAgentResponse(),
            await self.do_rpcrequest_async('TransferCallToAgent', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_call_to_agent(
        self,
        request: scsp_20200702_models.TransferCallToAgentRequest,
    ) -> scsp_20200702_models.TransferCallToAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_call_to_agent_with_options(request, runtime)

    async def transfer_call_to_agent_async(
        self,
        request: scsp_20200702_models.TransferCallToAgentRequest,
    ) -> scsp_20200702_models.TransferCallToAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_call_to_agent_with_options_async(request, runtime)

    def finish_hotline_service_with_options(
        self,
        request: scsp_20200702_models.FinishHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.FinishHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.FinishHotlineServiceResponse(),
            self.do_rpcrequest('FinishHotlineService', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def finish_hotline_service_with_options_async(
        self,
        request: scsp_20200702_models.FinishHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.FinishHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.FinishHotlineServiceResponse(),
            await self.do_rpcrequest_async('FinishHotlineService', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def finish_hotline_service(
        self,
        request: scsp_20200702_models.FinishHotlineServiceRequest,
    ) -> scsp_20200702_models.FinishHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.finish_hotline_service_with_options(request, runtime)

    async def finish_hotline_service_async(
        self,
        request: scsp_20200702_models.FinishHotlineServiceRequest,
    ) -> scsp_20200702_models.FinishHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.finish_hotline_service_with_options_async(request, runtime)

    def join_third_call_with_options(
        self,
        request: scsp_20200702_models.JoinThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.JoinThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.JoinThirdCallResponse(),
            self.do_rpcrequest('JoinThirdCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_third_call_with_options_async(
        self,
        request: scsp_20200702_models.JoinThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.JoinThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.JoinThirdCallResponse(),
            await self.do_rpcrequest_async('JoinThirdCall', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_third_call(
        self,
        request: scsp_20200702_models.JoinThirdCallRequest,
    ) -> scsp_20200702_models.JoinThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_third_call_with_options(request, runtime)

    async def join_third_call_async(
        self,
        request: scsp_20200702_models.JoinThirdCallRequest,
    ) -> scsp_20200702_models.JoinThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_third_call_with_options_async(request, runtime)

    def execute_activity_with_options(
        self,
        request: scsp_20200702_models.ExecuteActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ExecuteActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.ExecuteActivityResponse(),
            self.do_rpcrequest('ExecuteActivity', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_activity_with_options_async(
        self,
        request: scsp_20200702_models.ExecuteActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ExecuteActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.ExecuteActivityResponse(),
            await self.do_rpcrequest_async('ExecuteActivity', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_activity(
        self,
        request: scsp_20200702_models.ExecuteActivityRequest,
    ) -> scsp_20200702_models.ExecuteActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_activity_with_options(request, runtime)

    async def execute_activity_async(
        self,
        request: scsp_20200702_models.ExecuteActivityRequest,
    ) -> scsp_20200702_models.ExecuteActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_activity_with_options_async(request, runtime)

    def get_granted_role_ids_with_options(
        self,
        request: scsp_20200702_models.GetGrantedRoleIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetGrantedRoleIdsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetGrantedRoleIdsResponse(),
            self.do_rpcrequest('GetGrantedRoleIds', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_granted_role_ids_with_options_async(
        self,
        request: scsp_20200702_models.GetGrantedRoleIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetGrantedRoleIdsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetGrantedRoleIdsResponse(),
            await self.do_rpcrequest_async('GetGrantedRoleIds', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_granted_role_ids(
        self,
        request: scsp_20200702_models.GetGrantedRoleIdsRequest,
    ) -> scsp_20200702_models.GetGrantedRoleIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_granted_role_ids_with_options(request, runtime)

    async def get_granted_role_ids_async(
        self,
        request: scsp_20200702_models.GetGrantedRoleIdsRequest,
    ) -> scsp_20200702_models.GetGrantedRoleIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_granted_role_ids_with_options_async(request, runtime)

    def list_hotline_record_with_options(
        self,
        request: scsp_20200702_models.ListHotlineRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListHotlineRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListHotlineRecordResponse(),
            self.do_rpcrequest('ListHotlineRecord', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_hotline_record_with_options_async(
        self,
        request: scsp_20200702_models.ListHotlineRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.ListHotlineRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.ListHotlineRecordResponse(),
            await self.do_rpcrequest_async('ListHotlineRecord', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_hotline_record(
        self,
        request: scsp_20200702_models.ListHotlineRecordRequest,
    ) -> scsp_20200702_models.ListHotlineRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_record_with_options(request, runtime)

    async def list_hotline_record_async(
        self,
        request: scsp_20200702_models.ListHotlineRecordRequest,
    ) -> scsp_20200702_models.ListHotlineRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hotline_record_with_options_async(request, runtime)

    def get_num_location_with_options(
        self,
        request: scsp_20200702_models.GetNumLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetNumLocationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetNumLocationResponse(),
            self.do_rpcrequest('GetNumLocation', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_num_location_with_options_async(
        self,
        request: scsp_20200702_models.GetNumLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.GetNumLocationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            scsp_20200702_models.GetNumLocationResponse(),
            await self.do_rpcrequest_async('GetNumLocation', '2020-07-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_num_location(
        self,
        request: scsp_20200702_models.GetNumLocationRequest,
    ) -> scsp_20200702_models.GetNumLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_num_location_with_options(request, runtime)

    async def get_num_location_async(
        self,
        request: scsp_20200702_models.GetNumLocationRequest,
    ) -> scsp_20200702_models.GetNumLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_num_location_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: scsp_20200702_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateSkillGroupResponse(),
            self.do_rpcrequest('CreateSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: scsp_20200702_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateSkillGroupResponse(),
            await self.do_rpcrequest_async('CreateSkillGroup', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group(
        self,
        request: scsp_20200702_models.CreateSkillGroupRequest,
    ) -> scsp_20200702_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: scsp_20200702_models.CreateSkillGroupRequest,
    ) -> scsp_20200702_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def create_customer_with_options(
        self,
        request: scsp_20200702_models.CreateCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateCustomerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateCustomerResponse(),
            self.do_rpcrequest('CreateCustomer', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_customer_with_options_async(
        self,
        request: scsp_20200702_models.CreateCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scsp_20200702_models.CreateCustomerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            scsp_20200702_models.CreateCustomerResponse(),
            await self.do_rpcrequest_async('CreateCustomer', '2020-07-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_customer(
        self,
        request: scsp_20200702_models.CreateCustomerRequest,
    ) -> scsp_20200702_models.CreateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_customer_with_options(request, runtime)

    async def create_customer_async(
        self,
        request: scsp_20200702_models.CreateCustomerRequest,
    ) -> scsp_20200702_models.CreateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_customer_with_options_async(request, runtime)
