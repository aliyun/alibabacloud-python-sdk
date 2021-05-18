# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiccs20191015 import models as aiccs_20191015_models
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

    def send_hotline_heart_beat_with_options(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendHotlineHeartBeatResponse(),
            self.do_rpcrequest('SendHotlineHeartBeat', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_hotline_heart_beat_with_options_async(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendHotlineHeartBeatResponse(),
            await self.do_rpcrequest_async('SendHotlineHeartBeat', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_hotline_heart_beat(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_hotline_heart_beat_with_options(request, runtime)

    async def send_hotline_heart_beat_async(
        self,
        request: aiccs_20191015_models.SendHotlineHeartBeatRequest,
    ) -> aiccs_20191015_models.SendHotlineHeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_hotline_heart_beat_with_options_async(request, runtime)

    def start_chat_work_with_options(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartChatWorkResponse(),
            self.do_rpcrequest('StartChatWork', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_chat_work_with_options_async(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartChatWorkResponse(),
            await self.do_rpcrequest_async('StartChatWork', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_chat_work(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_chat_work_with_options(request, runtime)

    async def start_chat_work_async(
        self,
        request: aiccs_20191015_models.StartChatWorkRequest,
    ) -> aiccs_20191015_models.StartChatWorkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_chat_work_with_options_async(request, runtime)

    def hang_up_double_call_with_options(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangUpDoubleCallResponse(),
            self.do_rpcrequest('HangUpDoubleCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hang_up_double_call_with_options_async(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangUpDoubleCallResponse(),
            await self.do_rpcrequest_async('HangUpDoubleCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hang_up_double_call(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hang_up_double_call_with_options(request, runtime)

    async def hang_up_double_call_async(
        self,
        request: aiccs_20191015_models.HangUpDoubleCallRequest,
    ) -> aiccs_20191015_models.HangUpDoubleCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hang_up_double_call_with_options_async(request, runtime)

    def update_agent_with_options(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAgentResponse(),
            self.do_rpcrequest('UpdateAgent', '2019-10-15', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    async def update_agent_with_options_async(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAgentResponse(),
            await self.do_rpcrequest_async('UpdateAgent', '2019-10-15', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def update_agent(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_agent_with_options(request, runtime)

    async def update_agent_async(
        self,
        request: aiccs_20191015_models.UpdateAgentRequest,
    ) -> aiccs_20191015_models.UpdateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_agent_with_options_async(request, runtime)

    def edit_quality_rule_tag_with_options(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleTagResponse(),
            self.do_rpcrequest('EditQualityRuleTag', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_quality_rule_tag_with_options_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleTagResponse(),
            await self.do_rpcrequest_async('EditQualityRuleTag', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_quality_rule_tag(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_rule_tag_with_options(request, runtime)

    async def edit_quality_rule_tag_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleTagRequest,
    ) -> aiccs_20191015_models.EditQualityRuleTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_quality_rule_tag_with_options_async(request, runtime)

    def get_online_service_volume_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineServiceVolumeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineServiceVolumeResponse(),
            self.do_rpcrequest('GetOnlineServiceVolume', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_online_service_volume_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineServiceVolumeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineServiceVolumeResponse(),
            await self.do_rpcrequest_async('GetOnlineServiceVolume', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_online_service_volume(
        self,
        request: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_online_service_volume_with_options(request, runtime)

    async def get_online_service_volume_async(
        self,
        request: aiccs_20191015_models.GetOnlineServiceVolumeRequest,
    ) -> aiccs_20191015_models.GetOnlineServiceVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_online_service_volume_with_options_async(request, runtime)

    def delete_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOutboundTaskResponse(),
            self.do_rpcrequest('DeleteOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOutboundTaskResponse(),
            await self.do_rpcrequest_async('DeleteOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_outbound_task(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_outbound_task_with_options(request, runtime)

    async def delete_outbound_task_async(
        self,
        request: aiccs_20191015_models.DeleteOutboundTaskRequest,
    ) -> aiccs_20191015_models.DeleteOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_outbound_task_with_options_async(request, runtime)

    def add_outer_account_with_options(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddOuterAccountResponse(),
            self.do_rpcrequest('AddOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_outer_account_with_options_async(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddOuterAccountResponse(),
            await self.do_rpcrequest_async('AddOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_outer_account(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_outer_account_with_options(request, runtime)

    async def add_outer_account_async(
        self,
        request: aiccs_20191015_models.AddOuterAccountRequest,
    ) -> aiccs_20191015_models.AddOuterAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_outer_account_with_options_async(request, runtime)

    def get_agent_by_id_with_options(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentByIdResponse(),
            self.do_rpcrequest('GetAgentById', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_agent_by_id_with_options_async(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentByIdResponse(),
            await self.do_rpcrequest_async('GetAgentById', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_by_id(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_by_id_with_options(request, runtime)

    async def get_agent_by_id_async(
        self,
        request: aiccs_20191015_models.GetAgentByIdRequest,
    ) -> aiccs_20191015_models.GetAgentByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_by_id_with_options_async(request, runtime)

    def get_quality_rule_detail_with_options(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleDetailResponse(),
            self.do_rpcrequest('GetQualityRuleDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_rule_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleDetailResponse(),
            await self.do_rpcrequest_async('GetQualityRuleDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule_detail(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_detail_with_options(request, runtime)

    async def get_quality_rule_detail_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleDetailRequest,
    ) -> aiccs_20191015_models.GetQualityRuleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_rule_detail_with_options_async(request, runtime)

    def get_quality_project_log_with_options(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectLogResponse(),
            self.do_rpcrequest('GetQualityProjectLog', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_project_log_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectLogResponse(),
            await self.do_rpcrequest_async('GetQualityProjectLog', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_project_log(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_log_with_options(request, runtime)

    async def get_quality_project_log_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectLogRequest,
    ) -> aiccs_20191015_models.GetQualityProjectLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_project_log_with_options_async(request, runtime)

    def list_hotline_record_detail_with_options(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordDetailResponse(),
            self.do_rpcrequest('ListHotlineRecordDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_hotline_record_detail_with_options_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordDetailResponse(),
            await self.do_rpcrequest_async('ListHotlineRecordDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_hotline_record_detail(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_record_detail_with_options(request, runtime)

    async def list_hotline_record_detail_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordDetailRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hotline_record_detail_with_options_async(request, runtime)

    def get_hotline_message_log_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineMessageLogResponse(),
            self.do_rpcrequest('GetHotlineMessageLog', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hotline_message_log_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineMessageLogResponse(),
            await self.do_rpcrequest_async('GetHotlineMessageLog', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_message_log(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_message_log_with_options(request, runtime)

    async def get_hotline_message_log_async(
        self,
        request: aiccs_20191015_models.GetHotlineMessageLogRequest,
    ) -> aiccs_20191015_models.GetHotlineMessageLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_message_log_with_options_async(request, runtime)

    def get_quality_project_list_with_options(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectListResponse(),
            self.do_rpcrequest('GetQualityProjectList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_project_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectListResponse(),
            await self.do_rpcrequest_async('GetQualityProjectList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_project_list(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_list_with_options(request, runtime)

    async def get_quality_project_list_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectListRequest,
    ) -> aiccs_20191015_models.GetQualityProjectListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_project_list_with_options_async(request, runtime)

    def create_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateOutboundTaskResponse(),
            self.do_rpcrequest('CreateOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateOutboundTaskResponse(),
            await self.do_rpcrequest_async('CreateOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_outbound_task(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_outbound_task_with_options(request, runtime)

    async def create_outbound_task_async(
        self,
        request: aiccs_20191015_models.CreateOutboundTaskRequest,
    ) -> aiccs_20191015_models.CreateOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_outbound_task_with_options_async(request, runtime)

    def get_hotline_runtime_info_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineRuntimeInfoResponse(),
            self.do_rpcrequest('GetHotlineRuntimeInfo', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hotline_runtime_info_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineRuntimeInfoResponse(),
            await self.do_rpcrequest_async('GetHotlineRuntimeInfo', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_runtime_info(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_runtime_info_with_options(request, runtime)

    async def get_hotline_runtime_info_async(
        self,
        request: aiccs_20191015_models.GetHotlineRuntimeInfoRequest,
    ) -> aiccs_20191015_models.GetHotlineRuntimeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_runtime_info_with_options_async(request, runtime)

    def make_double_call_with_options(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeDoubleCallResponse(),
            self.do_rpcrequest('MakeDoubleCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def make_double_call_with_options_async(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeDoubleCallResponse(),
            await self.do_rpcrequest_async('MakeDoubleCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def make_double_call(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.make_double_call_with_options(request, runtime)

    async def make_double_call_async(
        self,
        request: aiccs_20191015_models.MakeDoubleCallRequest,
    ) -> aiccs_20191015_models.MakeDoubleCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.make_double_call_with_options_async(request, runtime)

    def get_skill_group_agent_status_details_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAgentStatusDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse(),
            self.do_rpcrequest('GetSkillGroupAgentStatusDetails', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_skill_group_agent_status_details_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAgentStatusDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse(),
            await self.do_rpcrequest_async('GetSkillGroupAgentStatusDetails', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_agent_status_details(
        self,
        request: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_agent_status_details_with_options(request, runtime)

    async def get_skill_group_agent_status_details_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupAgentStatusDetailsRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_agent_status_details_with_options_async(request, runtime)

    def get_agent_service_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentServiceStatusResponse(),
            self.do_rpcrequest('GetAgentServiceStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_service_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentServiceStatusResponse(),
            await self.do_rpcrequest_async('GetAgentServiceStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_service_status(
        self,
        request: aiccs_20191015_models.GetAgentServiceStatusRequest,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_service_status_with_options(request, runtime)

    async def get_agent_service_status_async(
        self,
        request: aiccs_20191015_models.GetAgentServiceStatusRequest,
    ) -> aiccs_20191015_models.GetAgentServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_service_status_with_options_async(request, runtime)

    def get_num_location_with_options(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetNumLocationResponse(),
            self.do_rpcrequest('GetNumLocation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_num_location_with_options_async(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetNumLocationResponse(),
            await self.do_rpcrequest_async('GetNumLocation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_num_location(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_num_location_with_options(request, runtime)

    async def get_num_location_async(
        self,
        request: aiccs_20191015_models.GetNumLocationRequest,
    ) -> aiccs_20191015_models.GetNumLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_num_location_with_options_async(request, runtime)

    def get_quality_rule_list_with_options(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleListResponse(),
            self.do_rpcrequest('GetQualityRuleList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_rule_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleListResponse(),
            await self.do_rpcrequest_async('GetQualityRuleList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule_list(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_list_with_options(request, runtime)

    async def get_quality_rule_list_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_rule_list_with_options_async(request, runtime)

    def list_outbound_phone_number_with_options(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundPhoneNumberResponse(),
            self.do_rpcrequest('ListOutboundPhoneNumber', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_outbound_phone_number_with_options_async(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundPhoneNumberResponse(),
            await self.do_rpcrequest_async('ListOutboundPhoneNumber', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_outbound_phone_number(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_phone_number_with_options(request, runtime)

    async def list_outbound_phone_number_async(
        self,
        request: aiccs_20191015_models.ListOutboundPhoneNumberRequest,
    ) -> aiccs_20191015_models.ListOutboundPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_phone_number_with_options_async(request, runtime)

    def list_agent_by_skill_group_id_with_options(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAgentBySkillGroupIdResponse(),
            self.do_rpcrequest('ListAgentBySkillGroupId', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_agent_by_skill_group_id_with_options_async(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAgentBySkillGroupIdResponse(),
            await self.do_rpcrequest_async('ListAgentBySkillGroupId', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_agent_by_skill_group_id(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_by_skill_group_id_with_options(request, runtime)

    async def list_agent_by_skill_group_id_async(
        self,
        request: aiccs_20191015_models.ListAgentBySkillGroupIdRequest,
    ) -> aiccs_20191015_models.ListAgentBySkillGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_by_skill_group_id_with_options_async(request, runtime)

    def hangup_third_call_with_options(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupThirdCallResponse(),
            self.do_rpcrequest('HangupThirdCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hangup_third_call_with_options_async(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupThirdCallResponse(),
            await self.do_rpcrequest_async('HangupThirdCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hangup_third_call(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hangup_third_call_with_options(request, runtime)

    async def hangup_third_call_async(
        self,
        request: aiccs_20191015_models.HangupThirdCallRequest,
    ) -> aiccs_20191015_models.HangupThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hangup_third_call_with_options_async(request, runtime)

    def start_hotline_service_with_options(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartHotlineServiceResponse(),
            self.do_rpcrequest('StartHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_hotline_service_with_options_async(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartHotlineServiceResponse(),
            await self.do_rpcrequest_async('StartHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_hotline_service(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_hotline_service_with_options(request, runtime)

    async def start_hotline_service_async(
        self,
        request: aiccs_20191015_models.StartHotlineServiceRequest,
    ) -> aiccs_20191015_models.StartHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_hotline_service_with_options_async(request, runtime)

    def get_agent_with_options(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentResponse(),
            self.do_rpcrequest('GetAgent', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentResponse(),
            await self.do_rpcrequest_async('GetAgent', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
    ) -> aiccs_20191015_models.GetAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_with_options(request, runtime)

    async def get_agent_async(
        self,
        request: aiccs_20191015_models.GetAgentRequest,
    ) -> aiccs_20191015_models.GetAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_with_options_async(request, runtime)

    def get_agent_index_real_time_with_options(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentIndexRealTimeResponse(),
            self.do_rpcrequest('GetAgentIndexRealTime', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_agent_index_real_time_with_options_async(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentIndexRealTimeResponse(),
            await self.do_rpcrequest_async('GetAgentIndexRealTime', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_index_real_time(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_index_real_time_with_options(request, runtime)

    async def get_agent_index_real_time_async(
        self,
        request: aiccs_20191015_models.GetAgentIndexRealTimeRequest,
    ) -> aiccs_20191015_models.GetAgentIndexRealTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_index_real_time_with_options_async(request, runtime)

    def get_hotline_group_detail_report_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineGroupDetailReportResponse(),
            self.do_rpcrequest('GetHotlineGroupDetailReport', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotline_group_detail_report_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineGroupDetailReportResponse(),
            await self.do_rpcrequest_async('GetHotlineGroupDetailReport', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_group_detail_report(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_group_detail_report_with_options(request, runtime)

    async def get_hotline_group_detail_report_async(
        self,
        request: aiccs_20191015_models.GetHotlineGroupDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineGroupDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_group_detail_report_with_options_async(request, runtime)

    def encrypt_phone_num_with_options(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EncryptPhoneNumResponse(),
            self.do_rpcrequest('EncryptPhoneNum', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def encrypt_phone_num_with_options_async(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EncryptPhoneNumResponse(),
            await self.do_rpcrequest_async('EncryptPhoneNum', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def encrypt_phone_num(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.encrypt_phone_num_with_options(request, runtime)

    async def encrypt_phone_num_async(
        self,
        request: aiccs_20191015_models.EncryptPhoneNumRequest,
    ) -> aiccs_20191015_models.EncryptPhoneNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.encrypt_phone_num_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetInstanceListResponse(),
            self.do_rpcrequest('GetInstanceList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetInstanceListResponse(),
            await self.do_rpcrequest_async('GetInstanceList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_list(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: aiccs_20191015_models.GetInstanceListRequest,
    ) -> aiccs_20191015_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_quality_project_detail_with_options(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectDetailResponse(),
            self.do_rpcrequest('GetQualityProjectDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_project_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectDetailResponse(),
            await self.do_rpcrequest_async('GetQualityProjectDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_project_detail(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_detail_with_options(request, runtime)

    async def get_quality_project_detail_async(
        self,
        request: aiccs_20191015_models.GetQualityProjectDetailRequest,
    ) -> aiccs_20191015_models.GetQualityProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_project_detail_with_options_async(request, runtime)

    def send_cco_smart_call_operate_with_options(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallOperateResponse(),
            self.do_rpcrequest('SendCcoSmartCallOperate', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_cco_smart_call_operate_with_options_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallOperateResponse(),
            await self.do_rpcrequest_async('SendCcoSmartCallOperate', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_cco_smart_call_operate(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_cco_smart_call_operate_with_options(request, runtime)

    async def send_cco_smart_call_operate_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallOperateRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallOperateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_cco_smart_call_operate_with_options_async(request, runtime)

    def answer_call_with_options(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AnswerCallResponse(),
            self.do_rpcrequest('AnswerCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def answer_call_with_options_async(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AnswerCallResponse(),
            await self.do_rpcrequest_async('AnswerCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def answer_call(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    async def answer_call_async(
        self,
        request: aiccs_20191015_models.AnswerCallRequest,
    ) -> aiccs_20191015_models.AnswerCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.answer_call_with_options_async(request, runtime)

    def start_micro_outbound_with_options(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartMicroOutboundResponse(),
            self.do_rpcrequest('StartMicroOutbound', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_micro_outbound_with_options_async(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartMicroOutboundResponse(),
            await self.do_rpcrequest_async('StartMicroOutbound', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_micro_outbound(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_micro_outbound_with_options(request, runtime)

    async def start_micro_outbound_async(
        self,
        request: aiccs_20191015_models.StartMicroOutboundRequest,
    ) -> aiccs_20191015_models.StartMicroOutboundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_micro_outbound_with_options_async(request, runtime)

    def suspend_hotline_service_with_options(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendHotlineServiceResponse(),
            self.do_rpcrequest('SuspendHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_hotline_service_with_options_async(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendHotlineServiceResponse(),
            await self.do_rpcrequest_async('SuspendHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_hotline_service(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_hotline_service_with_options(request, runtime)

    async def suspend_hotline_service_async(
        self,
        request: aiccs_20191015_models.SuspendHotlineServiceRequest,
    ) -> aiccs_20191015_models.SuspendHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_hotline_service_with_options_async(request, runtime)

    def get_agent_statistics_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentStatisticsResponse(),
            self.do_rpcrequest('GetAgentStatistics', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_statistics_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentStatisticsResponse(),
            await self.do_rpcrequest_async('GetAgentStatistics', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_statistics(
        self,
        request: aiccs_20191015_models.GetAgentStatisticsRequest,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_statistics_with_options(request, runtime)

    async def get_agent_statistics_async(
        self,
        request: aiccs_20191015_models.GetAgentStatisticsRequest,
    ) -> aiccs_20191015_models.GetAgentStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_statistics_with_options_async(request, runtime)

    def update_outer_account_with_options(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateOuterAccountResponse(),
            self.do_rpcrequest('UpdateOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def update_outer_account_with_options_async(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateOuterAccountResponse(),
            await self.do_rpcrequest_async('UpdateOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_outer_account(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_outer_account_with_options(request, runtime)

    async def update_outer_account_async(
        self,
        request: aiccs_20191015_models.UpdateOuterAccountRequest,
    ) -> aiccs_20191015_models.UpdateOuterAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_outer_account_with_options_async(request, runtime)

    def get_hotline_waiting_number_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineWaitingNumberResponse(),
            self.do_rpcrequest('GetHotlineWaitingNumber', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hotline_waiting_number_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineWaitingNumberResponse(),
            await self.do_rpcrequest_async('GetHotlineWaitingNumber', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_waiting_number(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_waiting_number_with_options(request, runtime)

    async def get_hotline_waiting_number_async(
        self,
        request: aiccs_20191015_models.GetHotlineWaitingNumberRequest,
    ) -> aiccs_20191015_models.GetHotlineWaitingNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_waiting_number_with_options_async(request, runtime)

    def hold_call_with_options(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HoldCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HoldCallResponse(),
            self.do_rpcrequest('HoldCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hold_call_with_options_async(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HoldCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HoldCallResponse(),
            await self.do_rpcrequest_async('HoldCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hold_call(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
    ) -> aiccs_20191015_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    async def hold_call_async(
        self,
        request: aiccs_20191015_models.HoldCallRequest,
    ) -> aiccs_20191015_models.HoldCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hold_call_with_options_async(request, runtime)

    def get_seat_information_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'depIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSeatInformationResponse(),
            self.do_rpcrequest('GetSeatInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_seat_information_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'depIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSeatInformationResponse(),
            await self.do_rpcrequest_async('GetSeatInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_seat_information(
        self,
        request: aiccs_20191015_models.GetSeatInformationRequest,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_seat_information_with_options(request, runtime)

    async def get_seat_information_async(
        self,
        request: aiccs_20191015_models.GetSeatInformationRequest,
    ) -> aiccs_20191015_models.GetSeatInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_seat_information_with_options_async(request, runtime)

    def get_rtc_token_with_options(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRtcTokenResponse(),
            self.do_rpcrequest('GetRtcToken', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_rtc_token_with_options_async(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRtcTokenResponse(),
            await self.do_rpcrequest_async('GetRtcToken', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_rtc_token(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rtc_token_with_options(request, runtime)

    async def get_rtc_token_async(
        self,
        request: aiccs_20191015_models.GetRtcTokenRequest,
    ) -> aiccs_20191015_models.GetRtcTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rtc_token_with_options_async(request, runtime)

    def get_skill_group_and_agent_status_summary_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse(),
            self.do_rpcrequest('GetSkillGroupAndAgentStatusSummary', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_skill_group_and_agent_status_summary_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse(),
            await self.do_rpcrequest_async('GetSkillGroupAndAgentStatusSummary', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_and_agent_status_summary(
        self,
        request: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_and_agent_status_summary_with_options(request, runtime)

    async def get_skill_group_and_agent_status_summary_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryRequest,
    ) -> aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_and_agent_status_summary_with_options_async(request, runtime)

    def get_record_data_with_options(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRecordDataResponse(),
            self.do_rpcrequest('GetRecordData', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_record_data_with_options_async(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRecordDataResponse(),
            await self.do_rpcrequest_async('GetRecordData', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_record_data(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_record_data_with_options(request, runtime)

    async def get_record_data_async(
        self,
        request: aiccs_20191015_models.GetRecordDataRequest,
    ) -> aiccs_20191015_models.GetRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_record_data_with_options_async(request, runtime)

    def get_skill_group_latitude_state_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupLatitudeStateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupLatitudeStateResponse(),
            self.do_rpcrequest('GetSkillGroupLatitudeState', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_skill_group_latitude_state_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupLatitudeStateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupLatitudeStateResponse(),
            await self.do_rpcrequest_async('GetSkillGroupLatitudeState', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_latitude_state(
        self,
        request: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_latitude_state_with_options(request, runtime)

    async def get_skill_group_latitude_state_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupLatitudeStateRequest,
    ) -> aiccs_20191015_models.GetSkillGroupLatitudeStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_latitude_state_with_options_async(request, runtime)

    def delete_quality_rule_with_options(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityRuleResponse(),
            self.do_rpcrequest('DeleteQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_quality_rule_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityRuleResponse(),
            await self.do_rpcrequest_async('DeleteQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_rule(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    async def delete_quality_rule_async(
        self,
        request: aiccs_20191015_models.DeleteQualityRuleRequest,
    ) -> aiccs_20191015_models.DeleteQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_rule_with_options_async(request, runtime)

    def suspend_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendOutboundTaskResponse(),
            self.do_rpcrequest('SuspendOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendOutboundTaskResponse(),
            await self.do_rpcrequest_async('SuspendOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_outbound_task(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_outbound_task_with_options(request, runtime)

    async def suspend_outbound_task_async(
        self,
        request: aiccs_20191015_models.SuspendOutboundTaskRequest,
    ) -> aiccs_20191015_models.SuspendOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_outbound_task_with_options_async(request, runtime)

    def get_hotline_service_statistics_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetHotlineServiceStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineServiceStatisticsResponse(),
            self.do_rpcrequest('GetHotlineServiceStatistics', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hotline_service_statistics_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetHotlineServiceStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineServiceStatisticsResponse(),
            await self.do_rpcrequest_async('GetHotlineServiceStatistics', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_service_statistics(
        self,
        request: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_service_statistics_with_options(request, runtime)

    async def get_hotline_service_statistics_async(
        self,
        request: aiccs_20191015_models.GetHotlineServiceStatisticsRequest,
    ) -> aiccs_20191015_models.GetHotlineServiceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_service_statistics_with_options_async(request, runtime)

    def edit_quality_project_with_options(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityProjectResponse(),
            self.do_rpcrequest('EditQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_quality_project_with_options_async(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityProjectResponse(),
            await self.do_rpcrequest_async('EditQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_quality_project(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_project_with_options(request, runtime)

    async def edit_quality_project_async(
        self,
        request: aiccs_20191015_models.EditQualityProjectRequest,
    ) -> aiccs_20191015_models.EditQualityProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_quality_project_with_options_async(request, runtime)

    def list_outer_ordered_numbers_with_options(
        self,
        request: aiccs_20191015_models.ListOuterOrderedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOuterOrderedNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOuterOrderedNumbersResponse(),
            self.do_rpcrequest('ListOuterOrderedNumbers', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_outer_ordered_numbers_with_options_async(
        self,
        request: aiccs_20191015_models.ListOuterOrderedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOuterOrderedNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOuterOrderedNumbersResponse(),
            await self.do_rpcrequest_async('ListOuterOrderedNumbers', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outer_ordered_numbers(
        self,
        request: aiccs_20191015_models.ListOuterOrderedNumbersRequest,
    ) -> aiccs_20191015_models.ListOuterOrderedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outer_ordered_numbers_with_options(request, runtime)

    async def list_outer_ordered_numbers_async(
        self,
        request: aiccs_20191015_models.ListOuterOrderedNumbersRequest,
    ) -> aiccs_20191015_models.ListOuterOrderedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outer_ordered_numbers_with_options_async(request, runtime)

    def get_agent_basis_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentBasisStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentBasisStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentBasisStatusResponse(),
            self.do_rpcrequest('GetAgentBasisStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_basis_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentBasisStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentBasisStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentBasisStatusResponse(),
            await self.do_rpcrequest_async('GetAgentBasisStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_basis_status(
        self,
        request: aiccs_20191015_models.GetAgentBasisStatusRequest,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_basis_status_with_options(request, runtime)

    async def get_agent_basis_status_async(
        self,
        request: aiccs_20191015_models.GetAgentBasisStatusRequest,
    ) -> aiccs_20191015_models.GetAgentBasisStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_basis_status_with_options_async(request, runtime)

    def get_quality_result_with_options(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityResultResponse(),
            self.do_rpcrequest('GetQualityResult', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_result_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityResultResponse(),
            await self.do_rpcrequest_async('GetQualityResult', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_result(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_result_with_options(request, runtime)

    async def get_quality_result_async(
        self,
        request: aiccs_20191015_models.GetQualityResultRequest,
    ) -> aiccs_20191015_models.GetQualityResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_result_with_options_async(request, runtime)

    def get_index_current_value_with_options(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetIndexCurrentValueResponse(),
            self.do_rpcrequest('GetIndexCurrentValue', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_index_current_value_with_options_async(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetIndexCurrentValueResponse(),
            await self.do_rpcrequest_async('GetIndexCurrentValue', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_index_current_value(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_index_current_value_with_options(request, runtime)

    async def get_index_current_value_async(
        self,
        request: aiccs_20191015_models.GetIndexCurrentValueRequest,
    ) -> aiccs_20191015_models.GetIndexCurrentValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_index_current_value_with_options_async(request, runtime)

    def generate_web_socket_sign_with_options(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GenerateWebSocketSignResponse(),
            self.do_rpcrequest('GenerateWebSocketSign', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_web_socket_sign_with_options_async(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GenerateWebSocketSignResponse(),
            await self.do_rpcrequest_async('GenerateWebSocketSign', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_web_socket_sign(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_web_socket_sign_with_options(request, runtime)

    async def generate_web_socket_sign_async(
        self,
        request: aiccs_20191015_models.GenerateWebSocketSignRequest,
    ) -> aiccs_20191015_models.GenerateWebSocketSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_web_socket_sign_with_options_async(request, runtime)

    def create_agent_with_options(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAgentResponse(),
            self.do_rpcrequest('CreateAgent', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAgentResponse(),
            await self.do_rpcrequest_async('CreateAgent', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_agent(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_agent_with_options(request, runtime)

    async def create_agent_async(
        self,
        request: aiccs_20191015_models.CreateAgentRequest,
    ) -> aiccs_20191015_models.CreateAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_agent_with_options_async(request, runtime)

    def query_task_detail_with_options(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTaskDetailResponse(),
            self.do_rpcrequest('QueryTaskDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_detail_with_options_async(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTaskDetailResponse(),
            await self.do_rpcrequest_async('QueryTaskDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_task_detail(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_with_options(request, runtime)

    async def query_task_detail_async(
        self,
        request: aiccs_20191015_models.QueryTaskDetailRequest,
    ) -> aiccs_20191015_models.QueryTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_with_options_async(request, runtime)

    def edit_quality_rule_with_options(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleResponse(),
            self.do_rpcrequest('EditQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_quality_rule_with_options_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleResponse(),
            await self.do_rpcrequest_async('EditQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_quality_rule(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_rule_with_options(request, runtime)

    async def edit_quality_rule_async(
        self,
        request: aiccs_20191015_models.EditQualityRuleRequest,
    ) -> aiccs_20191015_models.EditQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_quality_rule_with_options_async(request, runtime)

    def get_mcu_lvs_ip_with_options(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetMcuLvsIpResponse(),
            self.do_rpcrequest('GetMcuLvsIp', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_mcu_lvs_ip_with_options_async(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetMcuLvsIpResponse(),
            await self.do_rpcrequest_async('GetMcuLvsIp', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_mcu_lvs_ip(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mcu_lvs_ip_with_options(request, runtime)

    async def get_mcu_lvs_ip_async(
        self,
        request: aiccs_20191015_models.GetMcuLvsIpRequest,
    ) -> aiccs_20191015_models.GetMcuLvsIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mcu_lvs_ip_with_options_async(request, runtime)

    def get_dep_group_tree_data_with_options(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepGroupTreeDataResponse(),
            self.do_rpcrequest('GetDepGroupTreeData', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_dep_group_tree_data_with_options_async(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepGroupTreeDataResponse(),
            await self.do_rpcrequest_async('GetDepGroupTreeData', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_dep_group_tree_data(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dep_group_tree_data_with_options(request, runtime)

    async def get_dep_group_tree_data_async(
        self,
        request: aiccs_20191015_models.GetDepGroupTreeDataRequest,
    ) -> aiccs_20191015_models.GetDepGroupTreeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dep_group_tree_data_with_options_async(request, runtime)

    def delete_agent_with_options(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteAgentResponse(),
            self.do_rpcrequest('DeleteAgent', '2019-10-15', 'HTTPS', 'DELETE', 'AK', 'json', req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteAgentResponse(),
            await self.do_rpcrequest_async('DeleteAgent', '2019-10-15', 'HTTPS', 'DELETE', 'AK', 'json', req, runtime)
        )

    def delete_agent(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_agent_with_options(request, runtime)

    async def delete_agent_async(
        self,
        request: aiccs_20191015_models.DeleteAgentRequest,
    ) -> aiccs_20191015_models.DeleteAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_agent_with_options_async(request, runtime)

    def get_customer_info_with_options(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCustomerInfoResponse(),
            self.do_rpcrequest('GetCustomerInfo', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_customer_info_with_options_async(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCustomerInfoResponse(),
            await self.do_rpcrequest_async('GetCustomerInfo', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_customer_info(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_customer_info_with_options(request, runtime)

    async def get_customer_info_async(
        self,
        request: aiccs_20191015_models.GetCustomerInfoRequest,
    ) -> aiccs_20191015_models.GetCustomerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_customer_info_with_options_async(request, runtime)

    def get_hotline_agent_detail_report_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailReportResponse(),
            self.do_rpcrequest('GetHotlineAgentDetailReport', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotline_agent_detail_report_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailReportResponse(),
            await self.do_rpcrequest_async('GetHotlineAgentDetailReport', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_detail_report(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_report_with_options(request, runtime)

    async def get_hotline_agent_detail_report_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_detail_report_with_options_async(request, runtime)

    def send_cco_smart_call_with_options(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallResponse(),
            self.do_rpcrequest('SendCcoSmartCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_cco_smart_call_with_options_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallResponse(),
            await self.do_rpcrequest_async('SendCcoSmartCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_cco_smart_call(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_cco_smart_call_with_options(request, runtime)

    async def send_cco_smart_call_async(
        self,
        request: aiccs_20191015_models.SendCcoSmartCallRequest,
    ) -> aiccs_20191015_models.SendCcoSmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_cco_smart_call_with_options_async(request, runtime)

    def list_chat_record_detail_with_options(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListChatRecordDetailResponse(),
            self.do_rpcrequest('ListChatRecordDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_chat_record_detail_with_options_async(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListChatRecordDetailResponse(),
            await self.do_rpcrequest_async('ListChatRecordDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_chat_record_detail(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_chat_record_detail_with_options(request, runtime)

    async def list_chat_record_detail_async(
        self,
        request: aiccs_20191015_models.ListChatRecordDetailRequest,
    ) -> aiccs_20191015_models.ListChatRecordDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_chat_record_detail_with_options_async(request, runtime)

    def add_skill_group_with_options(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddSkillGroupResponse(),
            self.do_rpcrequest('AddSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddSkillGroupResponse(),
            await self.do_rpcrequest_async('AddSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_skill_group(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_skill_group_with_options(request, runtime)

    async def add_skill_group_async(
        self,
        request: aiccs_20191015_models.AddSkillGroupRequest,
    ) -> aiccs_20191015_models.AddSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_skill_group_with_options_async(request, runtime)

    def hangup_call_with_options(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupCallResponse(),
            self.do_rpcrequest('HangupCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hangup_call_with_options_async(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HangupCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupCallResponse(),
            await self.do_rpcrequest_async('HangupCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hangup_call(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
    ) -> aiccs_20191015_models.HangupCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.hangup_call_with_options(request, runtime)

    async def hangup_call_async(
        self,
        request: aiccs_20191015_models.HangupCallRequest,
    ) -> aiccs_20191015_models.HangupCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hangup_call_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteSkillGroupResponse(),
            self.do_rpcrequest('DeleteSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteSkillGroupResponse(),
            await self.do_rpcrequest_async('DeleteSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_skill_group(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: aiccs_20191015_models.DeleteSkillGroupRequest,
    ) -> aiccs_20191015_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def create_quality_project_with_options(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityProjectResponse(),
            self.do_rpcrequest('CreateQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quality_project_with_options_async(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityProjectResponse(),
            await self.do_rpcrequest_async('CreateQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_project(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quality_project_with_options(request, runtime)

    async def create_quality_project_async(
        self,
        request: aiccs_20191015_models.CreateQualityProjectRequest,
    ) -> aiccs_20191015_models.CreateQualityProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_project_with_options_async(request, runtime)

    def query_skill_groups_with_options(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QuerySkillGroupsResponse(),
            self.do_rpcrequest('QuerySkillGroups', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_skill_groups_with_options_async(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QuerySkillGroupsResponse(),
            await self.do_rpcrequest_async('QuerySkillGroups', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_skill_groups(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_skill_groups_with_options(request, runtime)

    async def query_skill_groups_async(
        self,
        request: aiccs_20191015_models.QuerySkillGroupsRequest,
    ) -> aiccs_20191015_models.QuerySkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_skill_groups_with_options_async(request, runtime)

    def create_quality_rule_with_options(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityRuleResponse(),
            self.do_rpcrequest('CreateQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quality_rule_with_options_async(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityRuleResponse(),
            await self.do_rpcrequest_async('CreateQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_rule(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    async def create_quality_rule_async(
        self,
        request: aiccs_20191015_models.CreateQualityRuleRequest,
    ) -> aiccs_20191015_models.CreateQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_rule_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRolesResponse(),
            await self.do_rpcrequest_async('ListRoles', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_roles(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
    ) -> aiccs_20191015_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: aiccs_20191015_models.ListRolesRequest,
    ) -> aiccs_20191015_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def get_hotline_call_action_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineCallActionResponse(),
            self.do_rpcrequest('GetHotlineCallAction', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotline_call_action_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineCallActionResponse(),
            await self.do_rpcrequest_async('GetHotlineCallAction', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_call_action(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_call_action_with_options(request, runtime)

    async def get_hotline_call_action_async(
        self,
        request: aiccs_20191015_models.GetHotlineCallActionRequest,
    ) -> aiccs_20191015_models.GetHotlineCallActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_call_action_with_options_async(request, runtime)

    def list_skill_group_with_options(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListSkillGroupResponse(),
            self.do_rpcrequest('ListSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListSkillGroupResponse(),
            await self.do_rpcrequest_async('ListSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_skill_group(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_with_options(request, runtime)

    async def list_skill_group_async(
        self,
        request: aiccs_20191015_models.ListSkillGroupRequest,
    ) -> aiccs_20191015_models.ListSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_with_options_async(request, runtime)

    def get_online_seat_information_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineSeatInformationResponse(),
            self.do_rpcrequest('GetOnlineSeatInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_online_seat_information_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetOnlineSeatInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineSeatInformationResponse(),
            await self.do_rpcrequest_async('GetOnlineSeatInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_online_seat_information(
        self,
        request: aiccs_20191015_models.GetOnlineSeatInformationRequest,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_online_seat_information_with_options(request, runtime)

    async def get_online_seat_information_async(
        self,
        request: aiccs_20191015_models.GetOnlineSeatInformationRequest,
    ) -> aiccs_20191015_models.GetOnlineSeatInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_online_seat_information_with_options_async(request, runtime)

    def delete_quality_project_with_options(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityProjectResponse(),
            self.do_rpcrequest('DeleteQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_quality_project_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityProjectResponse(),
            await self.do_rpcrequest_async('DeleteQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_project(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_project_with_options(request, runtime)

    async def delete_quality_project_async(
        self,
        request: aiccs_20191015_models.DeleteQualityProjectRequest,
    ) -> aiccs_20191015_models.DeleteQualityProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_project_with_options_async(request, runtime)

    def query_touch_list_with_options(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTouchListResponse(),
            self.do_rpcrequest('QueryTouchList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_touch_list_with_options_async(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTouchListResponse(),
            await self.do_rpcrequest_async('QueryTouchList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_touch_list(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_touch_list_with_options(request, runtime)

    async def query_touch_list_async(
        self,
        request: aiccs_20191015_models.QueryTouchListRequest,
    ) -> aiccs_20191015_models.QueryTouchListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_touch_list_with_options_async(request, runtime)

    def query_hotline_in_queue_with_options(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryHotlineInQueueResponse(),
            self.do_rpcrequest('QueryHotlineInQueue', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_hotline_in_queue_with_options_async(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryHotlineInQueueResponse(),
            await self.do_rpcrequest_async('QueryHotlineInQueue', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_hotline_in_queue(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_hotline_in_queue_with_options(request, runtime)

    async def query_hotline_in_queue_async(
        self,
        request: aiccs_20191015_models.QueryHotlineInQueueRequest,
    ) -> aiccs_20191015_models.QueryHotlineInQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_hotline_in_queue_with_options_async(request, runtime)

    def finish_hotline_service_with_options(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FinishHotlineServiceResponse(),
            self.do_rpcrequest('FinishHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def finish_hotline_service_with_options_async(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FinishHotlineServiceResponse(),
            await self.do_rpcrequest_async('FinishHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def finish_hotline_service(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.finish_hotline_service_with_options(request, runtime)

    async def finish_hotline_service_async(
        self,
        request: aiccs_20191015_models.FinishHotlineServiceRequest,
    ) -> aiccs_20191015_models.FinishHotlineServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.finish_hotline_service_with_options_async(request, runtime)

    def list_outbound_strategies_with_options(
        self,
        request: aiccs_20191015_models.ListOutboundStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOutboundStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundStrategiesResponse(),
            self.do_rpcrequest('ListOutboundStrategies', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_outbound_strategies_with_options_async(
        self,
        request: aiccs_20191015_models.ListOutboundStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListOutboundStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundStrategiesResponse(),
            await self.do_rpcrequest_async('ListOutboundStrategies', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_strategies(
        self,
        request: aiccs_20191015_models.ListOutboundStrategiesRequest,
    ) -> aiccs_20191015_models.ListOutboundStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_strategies_with_options(request, runtime)

    async def list_outbound_strategies_async(
        self,
        request: aiccs_20191015_models.ListOutboundStrategiesRequest,
    ) -> aiccs_20191015_models.ListOutboundStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_strategies_with_options_async(request, runtime)

    def list_hotline_record_with_options(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordResponse(),
            self.do_rpcrequest('ListHotlineRecord', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_hotline_record_with_options_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordResponse(),
            await self.do_rpcrequest_async('ListHotlineRecord', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_hotline_record(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_record_with_options(request, runtime)

    async def list_hotline_record_async(
        self,
        request: aiccs_20191015_models.ListHotlineRecordRequest,
    ) -> aiccs_20191015_models.ListHotlineRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hotline_record_with_options_async(request, runtime)

    def change_quality_project_status_with_options(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeQualityProjectStatusResponse(),
            self.do_rpcrequest('ChangeQualityProjectStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_quality_project_status_with_options_async(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeQualityProjectStatusResponse(),
            await self.do_rpcrequest_async('ChangeQualityProjectStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_quality_project_status(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_quality_project_status_with_options(request, runtime)

    async def change_quality_project_status_async(
        self,
        request: aiccs_20191015_models.ChangeQualityProjectStatusRequest,
    ) -> aiccs_20191015_models.ChangeQualityProjectStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_quality_project_status_with_options_async(request, runtime)

    def transfer_call_to_skill_group_with_options(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.TransferCallToSkillGroupResponse(),
            self.do_rpcrequest('TransferCallToSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_call_to_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.TransferCallToSkillGroupResponse(),
            await self.do_rpcrequest_async('TransferCallToSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_call_to_skill_group(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_call_to_skill_group_with_options(request, runtime)

    async def transfer_call_to_skill_group_async(
        self,
        request: aiccs_20191015_models.TransferCallToSkillGroupRequest,
    ) -> aiccs_20191015_models.TransferCallToSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_call_to_skill_group_with_options_async(request, runtime)

    def get_skill_group_service_capability_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceCapabilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse(),
            self.do_rpcrequest('GetSkillGroupServiceCapability', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_skill_group_service_capability_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceCapabilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse(),
            await self.do_rpcrequest_async('GetSkillGroupServiceCapability', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_service_capability(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_service_capability_with_options(request, runtime)

    async def get_skill_group_service_capability_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceCapabilityRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_service_capability_with_options_async(request, runtime)

    def remove_skill_group_with_options(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RemoveSkillGroupResponse(),
            self.do_rpcrequest('RemoveSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RemoveSkillGroupResponse(),
            await self.do_rpcrequest_async('RemoveSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_skill_group(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_group_with_options(request, runtime)

    async def remove_skill_group_async(
        self,
        request: aiccs_20191015_models.RemoveSkillGroupRequest,
    ) -> aiccs_20191015_models.RemoveSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_skill_group_with_options_async(request, runtime)

    def start_call_v2with_options(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallV2Response(),
            self.do_rpcrequest('StartCallV2', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_call_v2with_options_async(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallV2Response(),
            await self.do_rpcrequest_async('StartCallV2', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_call_v2(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
    ) -> aiccs_20191015_models.StartCallV2Response:
        runtime = util_models.RuntimeOptions()
        return self.start_call_v2with_options(request, runtime)

    async def start_call_v2_async(
        self,
        request: aiccs_20191015_models.StartCallV2Request,
    ) -> aiccs_20191015_models.StartCallV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.start_call_v2with_options_async(request, runtime)

    def change_chat_agent_status_with_options(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeChatAgentStatusResponse(),
            self.do_rpcrequest('ChangeChatAgentStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_chat_agent_status_with_options_async(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeChatAgentStatusResponse(),
            await self.do_rpcrequest_async('ChangeChatAgentStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_chat_agent_status(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_chat_agent_status_with_options(request, runtime)

    async def change_chat_agent_status_async(
        self,
        request: aiccs_20191015_models.ChangeChatAgentStatusRequest,
    ) -> aiccs_20191015_models.ChangeChatAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_chat_agent_status_with_options_async(request, runtime)

    def describe_record_data_with_options(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DescribeRecordDataResponse(),
            self.do_rpcrequest('DescribeRecordData', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_data_with_options_async(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DescribeRecordDataResponse(),
            await self.do_rpcrequest_async('DescribeRecordData', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record_data(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_record_data_with_options(request, runtime)

    async def describe_record_data_async(
        self,
        request: aiccs_20191015_models.DescribeRecordDataRequest,
    ) -> aiccs_20191015_models.DescribeRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_data_with_options_async(request, runtime)

    def delete_outer_account_with_options(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOuterAccountResponse(),
            self.do_rpcrequest('DeleteOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_outer_account_with_options_async(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOuterAccountResponse(),
            await self.do_rpcrequest_async('DeleteOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_outer_account(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_outer_account_with_options(request, runtime)

    async def delete_outer_account_async(
        self,
        request: aiccs_20191015_models.DeleteOuterAccountRequest,
    ) -> aiccs_20191015_models.DeleteOuterAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_outer_account_with_options_async(request, runtime)

    def get_departmental_latitude_agent_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse(),
            self.do_rpcrequest('GetDepartmentalLatitudeAgentStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_departmental_latitude_agent_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse(),
            await self.do_rpcrequest_async('GetDepartmentalLatitudeAgentStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_departmental_latitude_agent_status(
        self,
        request: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_departmental_latitude_agent_status_with_options(request, runtime)

    async def get_departmental_latitude_agent_status_async(
        self,
        request: aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusRequest,
    ) -> aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_departmental_latitude_agent_status_with_options_async(request, runtime)

    def get_hotline_agent_detail_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailResponse(),
            self.do_rpcrequest('GetHotlineAgentDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hotline_agent_detail_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailResponse(),
            await self.do_rpcrequest_async('GetHotlineAgentDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_detail(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_with_options(request, runtime)

    async def get_hotline_agent_detail_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentDetailRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_detail_with_options_async(request, runtime)

    def make_call_with_options(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeCallResponse(),
            self.do_rpcrequest('MakeCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def make_call_with_options_async(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.MakeCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeCallResponse(),
            await self.do_rpcrequest_async('MakeCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def make_call(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
    ) -> aiccs_20191015_models.MakeCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    async def make_call_async(
        self,
        request: aiccs_20191015_models.MakeCallRequest,
    ) -> aiccs_20191015_models.MakeCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.make_call_with_options_async(request, runtime)

    def fetch_call_with_options(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FetchCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FetchCallResponse(),
            self.do_rpcrequest('FetchCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fetch_call_with_options_async(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.FetchCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FetchCallResponse(),
            await self.do_rpcrequest_async('FetchCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_call(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
    ) -> aiccs_20191015_models.FetchCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_call_with_options(request, runtime)

    async def fetch_call_async(
        self,
        request: aiccs_20191015_models.FetchCallRequest,
    ) -> aiccs_20191015_models.FetchCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_call_with_options_async(request, runtime)

    def get_hotline_agent_status_with_options(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentStatusResponse(),
            self.do_rpcrequest('GetHotlineAgentStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotline_agent_status_with_options_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentStatusResponse(),
            await self.do_rpcrequest_async('GetHotlineAgentStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_status(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_status_with_options(request, runtime)

    async def get_hotline_agent_status_async(
        self,
        request: aiccs_20191015_models.GetHotlineAgentStatusRequest,
    ) -> aiccs_20191015_models.GetHotlineAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotline_agent_status_with_options_async(request, runtime)

    def start_call_with_options(
        self,
        request: aiccs_20191015_models.StartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallResponse(),
            self.do_rpcrequest('StartCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_call_with_options_async(
        self,
        request: aiccs_20191015_models.StartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.StartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallResponse(),
            await self.do_rpcrequest_async('StartCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_call(
        self,
        request: aiccs_20191015_models.StartCallRequest,
    ) -> aiccs_20191015_models.StartCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_call_with_options(request, runtime)

    async def start_call_async(
        self,
        request: aiccs_20191015_models.StartCallRequest,
    ) -> aiccs_20191015_models.StartCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_call_with_options_async(request, runtime)

    def get_quality_rule_tag_list_with_options(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleTagListResponse(),
            self.do_rpcrequest('GetQualityRuleTagList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_rule_tag_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleTagListResponse(),
            await self.do_rpcrequest_async('GetQualityRuleTagList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule_tag_list(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_tag_list_with_options(request, runtime)

    async def get_quality_rule_tag_list_async(
        self,
        request: aiccs_20191015_models.GetQualityRuleTagListRequest,
    ) -> aiccs_20191015_models.GetQualityRuleTagListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_rule_tag_list_with_options_async(request, runtime)

    def get_outboun_num_list_with_options(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOutbounNumListResponse(),
            self.do_rpcrequest('GetOutbounNumList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_outboun_num_list_with_options_async(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOutbounNumListResponse(),
            await self.do_rpcrequest_async('GetOutbounNumList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_outboun_num_list(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_outboun_num_list_with_options(request, runtime)

    async def get_outboun_num_list_async(
        self,
        request: aiccs_20191015_models.GetOutbounNumListRequest,
    ) -> aiccs_20191015_models.GetOutbounNumListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_outboun_num_list_with_options_async(request, runtime)

    def create_third_sso_agent_with_options(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateThirdSsoAgentResponse(),
            self.do_rpcrequest('CreateThirdSsoAgent', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_third_sso_agent_with_options_async(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateThirdSsoAgentResponse(),
            await self.do_rpcrequest_async('CreateThirdSsoAgent', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_third_sso_agent(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_third_sso_agent_with_options(request, runtime)

    async def create_third_sso_agent_async(
        self,
        request: aiccs_20191015_models.CreateThirdSsoAgentRequest,
    ) -> aiccs_20191015_models.CreateThirdSsoAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_third_sso_agent_with_options_async(request, runtime)

    def get_skill_group_status_total_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupStatusTotalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupStatusTotalResponse(),
            self.do_rpcrequest('GetSkillGroupStatusTotal', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_skill_group_status_total_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupStatusTotalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupStatusTotalResponse(),
            await self.do_rpcrequest_async('GetSkillGroupStatusTotal', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_status_total(
        self,
        request: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_status_total_with_options(request, runtime)

    async def get_skill_group_status_total_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupStatusTotalRequest,
    ) -> aiccs_20191015_models.GetSkillGroupStatusTotalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_status_total_with_options_async(request, runtime)

    def batch_create_quality_projects_with_options(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.BatchCreateQualityProjectsResponse(),
            self.do_rpcrequest('BatchCreateQualityProjects', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_create_quality_projects_with_options_async(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.BatchCreateQualityProjectsResponse(),
            await self.do_rpcrequest_async('BatchCreateQualityProjects', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_create_quality_projects(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_create_quality_projects_with_options(request, runtime)

    async def batch_create_quality_projects_async(
        self,
        request: aiccs_20191015_models.BatchCreateQualityProjectsRequest,
    ) -> aiccs_20191015_models.BatchCreateQualityProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_quality_projects_with_options_async(request, runtime)

    def insert_task_detail_with_options(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.InsertTaskDetailResponse(),
            self.do_rpcrequest('InsertTaskDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_task_detail_with_options_async(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.InsertTaskDetailResponse(),
            await self.do_rpcrequest_async('InsertTaskDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_task_detail(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_task_detail_with_options(request, runtime)

    async def insert_task_detail_async(
        self,
        request: aiccs_20191015_models.InsertTaskDetailRequest,
    ) -> aiccs_20191015_models.InsertTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_task_detail_with_options_async(request, runtime)

    def update_skill_group_with_options(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateSkillGroupResponse(),
            self.do_rpcrequest('UpdateSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateSkillGroupResponse(),
            await self.do_rpcrequest_async('UpdateSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_skill_group(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_with_options(request, runtime)

    async def update_skill_group_async(
        self,
        request: aiccs_20191015_models.UpdateSkillGroupRequest,
    ) -> aiccs_20191015_models.UpdateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_skill_group_with_options_async(request, runtime)

    def hotline_session_query_with_options(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HotlineSessionQueryResponse(),
            self.do_rpcrequest('HotlineSessionQuery', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hotline_session_query_with_options_async(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HotlineSessionQueryResponse(),
            await self.do_rpcrequest_async('HotlineSessionQuery', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hotline_session_query(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.hotline_session_query_with_options(request, runtime)

    async def hotline_session_query_async(
        self,
        request: aiccs_20191015_models.HotlineSessionQueryRequest,
    ) -> aiccs_20191015_models.HotlineSessionQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hotline_session_query_with_options_async(request, runtime)

    def get_queue_information_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetQueueInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetQueueInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQueueInformationResponse(),
            self.do_rpcrequest('GetQueueInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_queue_information_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetQueueInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetQueueInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQueueInformationResponse(),
            await self.do_rpcrequest_async('GetQueueInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_queue_information(
        self,
        request: aiccs_20191015_models.GetQueueInformationRequest,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_queue_information_with_options(request, runtime)

    async def get_queue_information_async(
        self,
        request: aiccs_20191015_models.GetQueueInformationRequest,
    ) -> aiccs_20191015_models.GetQueueInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_information_with_options_async(request, runtime)

    def get_skill_group_service_status_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceStatusResponse(),
            self.do_rpcrequest('GetSkillGroupServiceStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_skill_group_service_status_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceStatusResponse(),
            await self.do_rpcrequest_async('GetSkillGroupServiceStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_service_status(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_service_status_with_options(request, runtime)

    async def get_skill_group_service_status_async(
        self,
        request: aiccs_20191015_models.GetSkillGroupServiceStatusRequest,
    ) -> aiccs_20191015_models.GetSkillGroupServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_service_status_with_options_async(request, runtime)

    def get_agent_detail_report_with_options(
        self,
        tmp_req: aiccs_20191015_models.GetAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentDetailReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentDetailReportResponse(),
            self.do_rpcrequest('GetAgentDetailReport', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_detail_report_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.GetAgentDetailReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentDetailReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentDetailReportResponse(),
            await self.do_rpcrequest_async('GetAgentDetailReport', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_detail_report(
        self,
        request: aiccs_20191015_models.GetAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_detail_report_with_options(request, runtime)

    async def get_agent_detail_report_async(
        self,
        request: aiccs_20191015_models.GetAgentDetailReportRequest,
    ) -> aiccs_20191015_models.GetAgentDetailReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_detail_report_with_options_async(request, runtime)

    def query_tickets_with_options(
        self,
        tmp_req: aiccs_20191015_models.QueryTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.QueryTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTicketsResponse(),
            self.do_rpcrequest('QueryTickets', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_tickets_with_options_async(
        self,
        tmp_req: aiccs_20191015_models.QueryTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.QueryTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTicketsResponse(),
            await self.do_rpcrequest_async('QueryTickets', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tickets(
        self,
        request: aiccs_20191015_models.QueryTicketsRequest,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tickets_with_options(request, runtime)

    async def query_tickets_async(
        self,
        request: aiccs_20191015_models.QueryTicketsRequest,
    ) -> aiccs_20191015_models.QueryTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tickets_with_options_async(request, runtime)

    def query_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryOutboundTaskResponse(),
            self.do_rpcrequest('QueryOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryOutboundTaskResponse(),
            await self.do_rpcrequest_async('QueryOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_outbound_task(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_outbound_task_with_options(request, runtime)

    async def query_outbound_task_async(
        self,
        request: aiccs_20191015_models.QueryOutboundTaskRequest,
    ) -> aiccs_20191015_models.QueryOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_outbound_task_with_options_async(request, runtime)

    def join_third_call_with_options(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.JoinThirdCallResponse(),
            self.do_rpcrequest('JoinThirdCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_third_call_with_options_async(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.JoinThirdCallResponse(),
            await self.do_rpcrequest_async('JoinThirdCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_third_call(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_third_call_with_options(request, runtime)

    async def join_third_call_async(
        self,
        request: aiccs_20191015_models.JoinThirdCallRequest,
    ) -> aiccs_20191015_models.JoinThirdCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_third_call_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateSkillGroupResponse(),
            self.do_rpcrequest('CreateSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateSkillGroupResponse(),
            await self.do_rpcrequest_async('CreateSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: aiccs_20191015_models.CreateSkillGroupRequest,
    ) -> aiccs_20191015_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def restart_outbound_task_with_options(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RestartOutboundTaskResponse(),
            self.do_rpcrequest('RestartOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_outbound_task_with_options_async(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RestartOutboundTaskResponse(),
            await self.do_rpcrequest_async('RestartOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_outbound_task(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_outbound_task_with_options(request, runtime)

    async def restart_outbound_task_async(
        self,
        request: aiccs_20191015_models.RestartOutboundTaskRequest,
    ) -> aiccs_20191015_models.RestartOutboundTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_outbound_task_with_options_async(request, runtime)
