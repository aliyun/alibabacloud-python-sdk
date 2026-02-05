# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_outboundbot20191226 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('outboundbot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assign_jobs_with_options(
        self,
        request: main_models.AssignJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_asynchrony):
            query['IsAsynchrony'] = request.is_asynchrony
        if not DaraCore.is_null(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.jobs_json):
            query['JobsJson'] = request.jobs_json
        if not DaraCore.is_null(request.roster_type):
            query['RosterType'] = request.roster_type
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_jobs_with_options_async(
        self,
        request: main_models.AssignJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_asynchrony):
            query['IsAsynchrony'] = request.is_asynchrony
        if not DaraCore.is_null(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.jobs_json):
            query['JobsJson'] = request.jobs_json
        if not DaraCore.is_null(request.roster_type):
            query['RosterType'] = request.roster_type
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_jobs(
        self,
        request: main_models.AssignJobsRequest,
    ) -> main_models.AssignJobsResponse:
        runtime = RuntimeOptions()
        return self.assign_jobs_with_options(request, runtime)

    async def assign_jobs_async(
        self,
        request: main_models.AssignJobsRequest,
    ) -> main_models.AssignJobsResponse:
        runtime = RuntimeOptions()
        return await self.assign_jobs_with_options_async(request, runtime)

    def assign_jobs_async_with_options(
        self,
        tmp_req: main_models.AssignJobsAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignJobsAsyncResponse:
        tmp_req.validate()
        request = main_models.AssignJobsAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.calling_number):
            request.calling_number_shrink = Utils.array_to_string_with_specified_style(tmp_req.calling_number, 'CallingNumber', 'json')
        if not DaraCore.is_null(tmp_req.jobs_json):
            request.jobs_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.jobs_json, 'JobsJson', 'json')
        body = {}
        if not DaraCore.is_null(request.calling_number_shrink):
            body['CallingNumber'] = request.calling_number_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            body['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.jobs_json_shrink):
            body['JobsJson'] = request.jobs_json_shrink
        if not DaraCore.is_null(request.strategy_json):
            body['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignJobsAsync',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignJobsAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_jobs_async_with_options_async(
        self,
        tmp_req: main_models.AssignJobsAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignJobsAsyncResponse:
        tmp_req.validate()
        request = main_models.AssignJobsAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.calling_number):
            request.calling_number_shrink = Utils.array_to_string_with_specified_style(tmp_req.calling_number, 'CallingNumber', 'json')
        if not DaraCore.is_null(tmp_req.jobs_json):
            request.jobs_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.jobs_json, 'JobsJson', 'json')
        body = {}
        if not DaraCore.is_null(request.calling_number_shrink):
            body['CallingNumber'] = request.calling_number_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            body['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.jobs_json_shrink):
            body['JobsJson'] = request.jobs_json_shrink
        if not DaraCore.is_null(request.strategy_json):
            body['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignJobsAsync',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignJobsAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_jobs_async(
        self,
        request: main_models.AssignJobsAsyncRequest,
    ) -> main_models.AssignJobsAsyncResponse:
        runtime = RuntimeOptions()
        return self.assign_jobs_async_with_options(request, runtime)

    async def assign_jobs_async_async(
        self,
        request: main_models.AssignJobsAsyncRequest,
    ) -> main_models.AssignJobsAsyncResponse:
        runtime = RuntimeOptions()
        return await self.assign_jobs_async_with_options_async(request, runtime)

    def cancel_jobs_with_options(
        self,
        request: main_models.CancelJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_jobs_with_options_async(
        self,
        request: main_models.CancelJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_jobs(
        self,
        request: main_models.CancelJobsRequest,
    ) -> main_models.CancelJobsResponse:
        runtime = RuntimeOptions()
        return self.cancel_jobs_with_options(request, runtime)

    async def cancel_jobs_async(
        self,
        request: main_models.CancelJobsRequest,
    ) -> main_models.CancelJobsResponse:
        runtime = RuntimeOptions()
        return await self.cancel_jobs_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_agent_profile_with_options(
        self,
        request: main_models.CreateAgentProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.faq_category_ids):
            body['FaqCategoryIds'] = request.faq_category_ids
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not DaraCore.is_null(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.model_config):
            body['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not DaraCore.is_null(request.scenario):
            body['Scenario'] = request.scenario
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentProfile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_profile_with_options_async(
        self,
        request: main_models.CreateAgentProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.faq_category_ids):
            body['FaqCategoryIds'] = request.faq_category_ids
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not DaraCore.is_null(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.model_config):
            body['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not DaraCore.is_null(request.scenario):
            body['Scenario'] = request.scenario
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentProfile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_profile(
        self,
        request: main_models.CreateAgentProfileRequest,
    ) -> main_models.CreateAgentProfileResponse:
        runtime = RuntimeOptions()
        return self.create_agent_profile_with_options(request, runtime)

    async def create_agent_profile_async(
        self,
        request: main_models.CreateAgentProfileRequest,
    ) -> main_models.CreateAgentProfileResponse:
        runtime = RuntimeOptions()
        return await self.create_agent_profile_with_options_async(request, runtime)

    def create_annotation_mission_with_options(
        self,
        tmp_req: main_models.CreateAnnotationMissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationMissionResponse:
        tmp_req.validate()
        request = main_models.CreateAnnotationMissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.annotation_mission_debug_data_source_list):
            request.annotation_mission_debug_data_source_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.annotation_mission_debug_data_source_list, 'AnnotationMissionDebugDataSourceList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not DaraCore.is_null(request.annotation_mission_debug_data_source_list_shrink):
            query['AnnotationMissionDebugDataSourceList'] = request.annotation_mission_debug_data_source_list_shrink
        if not DaraCore.is_null(request.annotation_mission_debug_data_source_list_json_string):
            query['AnnotationMissionDebugDataSourceListJsonString'] = request.annotation_mission_debug_data_source_list_json_string
        if not DaraCore.is_null(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.conversation_time_end_filter):
            query['ConversationTimeEndFilter'] = request.conversation_time_end_filter
        if not DaraCore.is_null(request.conversation_time_start_filter):
            query['ConversationTimeStartFilter'] = request.conversation_time_start_filter
        if not DaraCore.is_null(request.exclude_other_session):
            query['ExcludeOtherSession'] = request.exclude_other_session
        if not DaraCore.is_null(request.finished):
            query['Finished'] = request.finished
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sampling_count):
            query['SamplingCount'] = request.sampling_count
        if not DaraCore.is_null(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not DaraCore.is_null(request.sampling_type):
            query['SamplingType'] = request.sampling_type
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.session_end_reason_filter_list):
            query['SessionEndReasonFilterList'] = request.session_end_reason_filter_list
        if not DaraCore.is_null(request.session_end_reason_filter_list_json_string):
            query['SessionEndReasonFilterListJsonString'] = request.session_end_reason_filter_list_json_string
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationMission',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationMissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_annotation_mission_with_options_async(
        self,
        tmp_req: main_models.CreateAnnotationMissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationMissionResponse:
        tmp_req.validate()
        request = main_models.CreateAnnotationMissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.annotation_mission_debug_data_source_list):
            request.annotation_mission_debug_data_source_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.annotation_mission_debug_data_source_list, 'AnnotationMissionDebugDataSourceList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not DaraCore.is_null(request.annotation_mission_debug_data_source_list_shrink):
            query['AnnotationMissionDebugDataSourceList'] = request.annotation_mission_debug_data_source_list_shrink
        if not DaraCore.is_null(request.annotation_mission_debug_data_source_list_json_string):
            query['AnnotationMissionDebugDataSourceListJsonString'] = request.annotation_mission_debug_data_source_list_json_string
        if not DaraCore.is_null(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.conversation_time_end_filter):
            query['ConversationTimeEndFilter'] = request.conversation_time_end_filter
        if not DaraCore.is_null(request.conversation_time_start_filter):
            query['ConversationTimeStartFilter'] = request.conversation_time_start_filter
        if not DaraCore.is_null(request.exclude_other_session):
            query['ExcludeOtherSession'] = request.exclude_other_session
        if not DaraCore.is_null(request.finished):
            query['Finished'] = request.finished
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sampling_count):
            query['SamplingCount'] = request.sampling_count
        if not DaraCore.is_null(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not DaraCore.is_null(request.sampling_type):
            query['SamplingType'] = request.sampling_type
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.session_end_reason_filter_list):
            query['SessionEndReasonFilterList'] = request.session_end_reason_filter_list
        if not DaraCore.is_null(request.session_end_reason_filter_list_json_string):
            query['SessionEndReasonFilterListJsonString'] = request.session_end_reason_filter_list_json_string
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationMission',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationMissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_annotation_mission(
        self,
        request: main_models.CreateAnnotationMissionRequest,
    ) -> main_models.CreateAnnotationMissionResponse:
        runtime = RuntimeOptions()
        return self.create_annotation_mission_with_options(request, runtime)

    async def create_annotation_mission_async(
        self,
        request: main_models.CreateAnnotationMissionRequest,
    ) -> main_models.CreateAnnotationMissionResponse:
        runtime = RuntimeOptions()
        return await self.create_annotation_mission_with_options_async(request, runtime)

    def create_batch_jobs_with_options(
        self,
        request: main_models.CreateBatchJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_job_description):
            query['BatchJobDescription'] = request.batch_job_description
        if not DaraCore.is_null(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not DaraCore.is_null(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatchJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_jobs_with_options_async(
        self,
        request: main_models.CreateBatchJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_job_description):
            query['BatchJobDescription'] = request.batch_job_description
        if not DaraCore.is_null(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not DaraCore.is_null(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatchJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_jobs(
        self,
        request: main_models.CreateBatchJobsRequest,
    ) -> main_models.CreateBatchJobsResponse:
        runtime = RuntimeOptions()
        return self.create_batch_jobs_with_options(request, runtime)

    async def create_batch_jobs_async(
        self,
        request: main_models.CreateBatchJobsRequest,
    ) -> main_models.CreateBatchJobsResponse:
        runtime = RuntimeOptions()
        return await self.create_batch_jobs_with_options_async(request, runtime)

    def create_batch_repeat_job_with_options(
        self,
        request: main_models.CreateBatchRepeatJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchRepeatJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.filter_status):
            query['FilterStatus'] = request.filter_status
        if not DaraCore.is_null(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not DaraCore.is_null(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not DaraCore.is_null(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.source_group_id):
            query['SourceGroupId'] = request.source_group_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatchRepeatJob',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchRepeatJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_repeat_job_with_options_async(
        self,
        request: main_models.CreateBatchRepeatJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchRepeatJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.filter_status):
            query['FilterStatus'] = request.filter_status
        if not DaraCore.is_null(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not DaraCore.is_null(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not DaraCore.is_null(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.source_group_id):
            query['SourceGroupId'] = request.source_group_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatchRepeatJob',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchRepeatJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_repeat_job(
        self,
        request: main_models.CreateBatchRepeatJobRequest,
    ) -> main_models.CreateBatchRepeatJobResponse:
        runtime = RuntimeOptions()
        return self.create_batch_repeat_job_with_options(request, runtime)

    async def create_batch_repeat_job_async(
        self,
        request: main_models.CreateBatchRepeatJobRequest,
    ) -> main_models.CreateBatchRepeatJobResponse:
        runtime = RuntimeOptions()
        return await self.create_batch_repeat_job_with_options_async(request, runtime)

    def create_beebot_intent_with_options(
        self,
        tmp_req: main_models.CreateBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBeebotIntentResponse:
        tmp_req.validate()
        request = main_models.CreateBeebotIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_beebot_intent_with_options_async(
        self,
        tmp_req: main_models.CreateBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBeebotIntentResponse:
        tmp_req.validate()
        request = main_models.CreateBeebotIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_beebot_intent(
        self,
        request: main_models.CreateBeebotIntentRequest,
    ) -> main_models.CreateBeebotIntentResponse:
        runtime = RuntimeOptions()
        return self.create_beebot_intent_with_options(request, runtime)

    async def create_beebot_intent_async(
        self,
        request: main_models.CreateBeebotIntentRequest,
    ) -> main_models.CreateBeebotIntentResponse:
        runtime = RuntimeOptions()
        return await self.create_beebot_intent_with_options_async(request, runtime)

    def create_beebot_intent_lgf_with_options(
        self,
        tmp_req: main_models.CreateBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBeebotIntentLgfResponse:
        tmp_req.validate()
        request = main_models.CreateBeebotIntentLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_beebot_intent_lgf_with_options_async(
        self,
        tmp_req: main_models.CreateBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBeebotIntentLgfResponse:
        tmp_req.validate()
        request = main_models.CreateBeebotIntentLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_beebot_intent_lgf(
        self,
        request: main_models.CreateBeebotIntentLgfRequest,
    ) -> main_models.CreateBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return self.create_beebot_intent_lgf_with_options(request, runtime)

    async def create_beebot_intent_lgf_async(
        self,
        request: main_models.CreateBeebotIntentLgfRequest,
    ) -> main_models.CreateBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return await self.create_beebot_intent_lgf_with_options_async(request, runtime)

    def create_beebot_intent_user_say_with_options(
        self,
        tmp_req: main_models.CreateBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBeebotIntentUserSayResponse:
        tmp_req.validate()
        request = main_models.CreateBeebotIntentUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_beebot_intent_user_say_with_options_async(
        self,
        tmp_req: main_models.CreateBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBeebotIntentUserSayResponse:
        tmp_req.validate()
        request = main_models.CreateBeebotIntentUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_beebot_intent_user_say(
        self,
        request: main_models.CreateBeebotIntentUserSayRequest,
    ) -> main_models.CreateBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return self.create_beebot_intent_user_say_with_options(request, runtime)

    async def create_beebot_intent_user_say_async(
        self,
        request: main_models.CreateBeebotIntentUserSayRequest,
    ) -> main_models.CreateBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return await self.create_beebot_intent_user_say_with_options_async(request, runtime)

    def create_dialogue_flow_with_options(
        self,
        request: main_models.CreateDialogueFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDialogueFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dialogue_flow_type):
            query['DialogueFlowType'] = request.dialogue_flow_type
        if not DaraCore.is_null(request.dialogue_name):
            query['DialogueName'] = request.dialogue_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDialogueFlow',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDialogueFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialogue_flow_with_options_async(
        self,
        request: main_models.CreateDialogueFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDialogueFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dialogue_flow_type):
            query['DialogueFlowType'] = request.dialogue_flow_type
        if not DaraCore.is_null(request.dialogue_name):
            query['DialogueName'] = request.dialogue_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDialogueFlow',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDialogueFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialogue_flow(
        self,
        request: main_models.CreateDialogueFlowRequest,
    ) -> main_models.CreateDialogueFlowResponse:
        runtime = RuntimeOptions()
        return self.create_dialogue_flow_with_options(request, runtime)

    async def create_dialogue_flow_async(
        self,
        request: main_models.CreateDialogueFlowRequest,
    ) -> main_models.CreateDialogueFlowResponse:
        runtime = RuntimeOptions()
        return await self.create_dialogue_flow_with_options_async(request, runtime)

    def create_download_url_with_options(
        self,
        request: main_models.CreateDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadUrl',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_download_url_with_options_async(
        self,
        request: main_models.CreateDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadUrl',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_download_url(
        self,
        request: main_models.CreateDownloadUrlRequest,
    ) -> main_models.CreateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.create_download_url_with_options(request, runtime)

    async def create_download_url_async(
        self,
        request: main_models.CreateDownloadUrlRequest,
    ) -> main_models.CreateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.create_download_url_with_options_async(request, runtime)

    def create_global_question_with_options(
        self,
        request: main_models.CreateGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.answers):
            query['Answers'] = request.answers
        if not DaraCore.is_null(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not DaraCore.is_null(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.questions):
            query['Questions'] = request.questions
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_question_with_options_async(
        self,
        request: main_models.CreateGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.answers):
            query['Answers'] = request.answers
        if not DaraCore.is_null(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not DaraCore.is_null(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.questions):
            query['Questions'] = request.questions
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_question(
        self,
        request: main_models.CreateGlobalQuestionRequest,
    ) -> main_models.CreateGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return self.create_global_question_with_options(request, runtime)

    async def create_global_question_async(
        self,
        request: main_models.CreateGlobalQuestionRequest,
    ) -> main_models.CreateGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return await self.create_global_question_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        if not DaraCore.is_null(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2019-12-26',
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
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        if not DaraCore.is_null(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2019-12-26',
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

    def create_instance_bind_number_with_options(
        self,
        request: main_models.CreateInstanceBindNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceBindNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceBindNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceBindNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_bind_number_with_options_async(
        self,
        request: main_models.CreateInstanceBindNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceBindNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceBindNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceBindNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_bind_number(
        self,
        request: main_models.CreateInstanceBindNumberRequest,
    ) -> main_models.CreateInstanceBindNumberResponse:
        runtime = RuntimeOptions()
        return self.create_instance_bind_number_with_options(request, runtime)

    async def create_instance_bind_number_async(
        self,
        request: main_models.CreateInstanceBindNumberRequest,
    ) -> main_models.CreateInstanceBindNumberResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_bind_number_with_options_async(request, runtime)

    def create_intent_with_options(
        self,
        request: main_models.CreateIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intent_with_options_async(
        self,
        request: main_models.CreateIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intent(
        self,
        request: main_models.CreateIntentRequest,
    ) -> main_models.CreateIntentResponse:
        runtime = RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    async def create_intent_async(
        self,
        request: main_models.CreateIntentRequest,
    ) -> main_models.CreateIntentResponse:
        runtime = RuntimeOptions()
        return await self.create_intent_with_options_async(request, runtime)

    def create_job_data_parsing_task_with_options(
        self,
        request: main_models.CreateJobDataParsingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobDataParsingTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobDataParsingTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobDataParsingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_data_parsing_task_with_options_async(
        self,
        request: main_models.CreateJobDataParsingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobDataParsingTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobDataParsingTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobDataParsingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_data_parsing_task(
        self,
        request: main_models.CreateJobDataParsingTaskRequest,
    ) -> main_models.CreateJobDataParsingTaskResponse:
        runtime = RuntimeOptions()
        return self.create_job_data_parsing_task_with_options(request, runtime)

    async def create_job_data_parsing_task_async(
        self,
        request: main_models.CreateJobDataParsingTaskRequest,
    ) -> main_models.CreateJobDataParsingTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_job_data_parsing_task_with_options_async(request, runtime)

    def create_job_group_with_options(
        self,
        request: main_models.CreateJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_description):
            query['JobGroupDescription'] = request.job_group_description
        if not DaraCore.is_null(request.job_group_name):
            query['JobGroupName'] = request.job_group_name
        if not DaraCore.is_null(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not DaraCore.is_null(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not DaraCore.is_null(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_group_with_options_async(
        self,
        request: main_models.CreateJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_description):
            query['JobGroupDescription'] = request.job_group_description
        if not DaraCore.is_null(request.job_group_name):
            query['JobGroupName'] = request.job_group_name
        if not DaraCore.is_null(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not DaraCore.is_null(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not DaraCore.is_null(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_group(
        self,
        request: main_models.CreateJobGroupRequest,
    ) -> main_models.CreateJobGroupResponse:
        runtime = RuntimeOptions()
        return self.create_job_group_with_options(request, runtime)

    async def create_job_group_async(
        self,
        request: main_models.CreateJobGroupRequest,
    ) -> main_models.CreateJobGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_job_group_with_options_async(request, runtime)

    def create_job_group_export_task_with_options(
        self,
        request: main_models.CreateJobGroupExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobGroupExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobGroupExportTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobGroupExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_group_export_task_with_options_async(
        self,
        request: main_models.CreateJobGroupExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobGroupExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobGroupExportTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobGroupExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_group_export_task(
        self,
        request: main_models.CreateJobGroupExportTaskRequest,
    ) -> main_models.CreateJobGroupExportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_job_group_export_task_with_options(request, runtime)

    async def create_job_group_export_task_async(
        self,
        request: main_models.CreateJobGroupExportTaskRequest,
    ) -> main_models.CreateJobGroupExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_job_group_export_task_with_options_async(request, runtime)

    def create_script_with_options(
        self,
        request: main_models.CreateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not DaraCore.is_null(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not DaraCore.is_null(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not DaraCore.is_null(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not DaraCore.is_null(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        if not DaraCore.is_null(request.script_nlu_profile_json_string):
            query['ScriptNluProfileJsonString'] = request.script_nlu_profile_json_string
        if not DaraCore.is_null(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not DaraCore.is_null(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_with_options_async(
        self,
        request: main_models.CreateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not DaraCore.is_null(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not DaraCore.is_null(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not DaraCore.is_null(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not DaraCore.is_null(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        if not DaraCore.is_null(request.script_nlu_profile_json_string):
            query['ScriptNluProfileJsonString'] = request.script_nlu_profile_json_string
        if not DaraCore.is_null(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not DaraCore.is_null(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script(
        self,
        request: main_models.CreateScriptRequest,
    ) -> main_models.CreateScriptResponse:
        runtime = RuntimeOptions()
        return self.create_script_with_options(request, runtime)

    async def create_script_async(
        self,
        request: main_models.CreateScriptRequest,
    ) -> main_models.CreateScriptResponse:
        runtime = RuntimeOptions()
        return await self.create_script_with_options_async(request, runtime)

    def create_script_waveform_with_options(
        self,
        request: main_models.CreateScriptWaveformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptWaveformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScriptWaveform',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptWaveformResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_waveform_with_options_async(
        self,
        request: main_models.CreateScriptWaveformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptWaveformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScriptWaveform',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptWaveformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script_waveform(
        self,
        request: main_models.CreateScriptWaveformRequest,
    ) -> main_models.CreateScriptWaveformResponse:
        runtime = RuntimeOptions()
        return self.create_script_waveform_with_options(request, runtime)

    async def create_script_waveform_async(
        self,
        request: main_models.CreateScriptWaveformRequest,
    ) -> main_models.CreateScriptWaveformResponse:
        runtime = RuntimeOptions()
        return await self.create_script_waveform_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: main_models.CreateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.tag_group):
            query['TagGroup'] = request.tag_group
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: main_models.CreateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.tag_group):
            query['TagGroup'] = request.tag_group
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_task_export_task_with_options(
        self,
        request: main_models.CreateTaskExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskExportTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTaskExportTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_export_task_with_options_async(
        self,
        request: main_models.CreateTaskExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskExportTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTaskExportTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_export_task(
        self,
        request: main_models.CreateTaskExportTaskRequest,
    ) -> main_models.CreateTaskExportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_task_export_task_with_options(request, runtime)

    async def create_task_export_task_async(
        self,
        request: main_models.CreateTaskExportTaskRequest,
    ) -> main_models.CreateTaskExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_task_export_task_with_options_async(request, runtime)

    def delete_agent_profiles_with_options(
        self,
        tmp_req: main_models.DeleteAgentProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentProfilesResponse:
        tmp_req.validate()
        request = main_models.DeleteAgentProfilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_profile_ids):
            request.agent_profile_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_profile_ids, 'AgentProfileIds', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_profile_ids_shrink):
            body['AgentProfileIds'] = request.agent_profile_ids_shrink
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentProfiles',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_profiles_with_options_async(
        self,
        tmp_req: main_models.DeleteAgentProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentProfilesResponse:
        tmp_req.validate()
        request = main_models.DeleteAgentProfilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_profile_ids):
            request.agent_profile_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_profile_ids, 'AgentProfileIds', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_profile_ids_shrink):
            body['AgentProfileIds'] = request.agent_profile_ids_shrink
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentProfiles',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_profiles(
        self,
        request: main_models.DeleteAgentProfilesRequest,
    ) -> main_models.DeleteAgentProfilesResponse:
        runtime = RuntimeOptions()
        return self.delete_agent_profiles_with_options(request, runtime)

    async def delete_agent_profiles_async(
        self,
        request: main_models.DeleteAgentProfilesRequest,
    ) -> main_models.DeleteAgentProfilesResponse:
        runtime = RuntimeOptions()
        return await self.delete_agent_profiles_with_options_async(request, runtime)

    def delete_all_number_district_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllNumberDistrictInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DeleteAllNumberDistrictInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllNumberDistrictInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_number_district_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllNumberDistrictInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DeleteAllNumberDistrictInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllNumberDistrictInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_number_district_info(self) -> main_models.DeleteAllNumberDistrictInfoResponse:
        runtime = RuntimeOptions()
        return self.delete_all_number_district_info_with_options(runtime)

    async def delete_all_number_district_info_async(self) -> main_models.DeleteAllNumberDistrictInfoResponse:
        runtime = RuntimeOptions()
        return await self.delete_all_number_district_info_with_options_async(runtime)

    def delete_beebot_intent_with_options(
        self,
        request: main_models.DeleteBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBeebotIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_beebot_intent_with_options_async(
        self,
        request: main_models.DeleteBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBeebotIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_beebot_intent(
        self,
        request: main_models.DeleteBeebotIntentRequest,
    ) -> main_models.DeleteBeebotIntentResponse:
        runtime = RuntimeOptions()
        return self.delete_beebot_intent_with_options(request, runtime)

    async def delete_beebot_intent_async(
        self,
        request: main_models.DeleteBeebotIntentRequest,
    ) -> main_models.DeleteBeebotIntentResponse:
        runtime = RuntimeOptions()
        return await self.delete_beebot_intent_with_options_async(request, runtime)

    def delete_beebot_intent_lgf_with_options(
        self,
        request: main_models.DeleteBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBeebotIntentLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_beebot_intent_lgf_with_options_async(
        self,
        request: main_models.DeleteBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBeebotIntentLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_beebot_intent_lgf(
        self,
        request: main_models.DeleteBeebotIntentLgfRequest,
    ) -> main_models.DeleteBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return self.delete_beebot_intent_lgf_with_options(request, runtime)

    async def delete_beebot_intent_lgf_async(
        self,
        request: main_models.DeleteBeebotIntentLgfRequest,
    ) -> main_models.DeleteBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return await self.delete_beebot_intent_lgf_with_options_async(request, runtime)

    def delete_beebot_intent_user_say_with_options(
        self,
        request: main_models.DeleteBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBeebotIntentUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_beebot_intent_user_say_with_options_async(
        self,
        request: main_models.DeleteBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBeebotIntentUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_beebot_intent_user_say(
        self,
        request: main_models.DeleteBeebotIntentUserSayRequest,
    ) -> main_models.DeleteBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return self.delete_beebot_intent_user_say_with_options(request, runtime)

    async def delete_beebot_intent_user_say_async(
        self,
        request: main_models.DeleteBeebotIntentUserSayRequest,
    ) -> main_models.DeleteBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return await self.delete_beebot_intent_user_say_with_options_async(request, runtime)

    def delete_contact_block_list_with_options(
        self,
        request: main_models.DeleteContactBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_block_list_id):
            query['ContactBlockListId'] = request.contact_block_list_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactBlockList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_block_list_with_options_async(
        self,
        request: main_models.DeleteContactBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_block_list_id):
            query['ContactBlockListId'] = request.contact_block_list_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactBlockList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_block_list(
        self,
        request: main_models.DeleteContactBlockListRequest,
    ) -> main_models.DeleteContactBlockListResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_block_list_with_options(request, runtime)

    async def delete_contact_block_list_async(
        self,
        request: main_models.DeleteContactBlockListRequest,
    ) -> main_models.DeleteContactBlockListResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_block_list_with_options_async(request, runtime)

    def delete_contact_white_list_with_options(
        self,
        request: main_models.DeleteContactWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_white_list_id):
            query['ContactWhiteListId'] = request.contact_white_list_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactWhiteList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_white_list_with_options_async(
        self,
        request: main_models.DeleteContactWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_white_list_id):
            query['ContactWhiteListId'] = request.contact_white_list_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactWhiteList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_white_list(
        self,
        request: main_models.DeleteContactWhiteListRequest,
    ) -> main_models.DeleteContactWhiteListResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_white_list_with_options(request, runtime)

    async def delete_contact_white_list_async(
        self,
        request: main_models.DeleteContactWhiteListRequest,
    ) -> main_models.DeleteContactWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_white_list_with_options_async(request, runtime)

    def delete_dialogue_flow_with_options(
        self,
        request: main_models.DeleteDialogueFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDialogueFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDialogueFlow',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDialogueFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dialogue_flow_with_options_async(
        self,
        request: main_models.DeleteDialogueFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDialogueFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDialogueFlow',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDialogueFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dialogue_flow(
        self,
        request: main_models.DeleteDialogueFlowRequest,
    ) -> main_models.DeleteDialogueFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_dialogue_flow_with_options(request, runtime)

    async def delete_dialogue_flow_async(
        self,
        request: main_models.DeleteDialogueFlowRequest,
    ) -> main_models.DeleteDialogueFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_dialogue_flow_with_options_async(request, runtime)

    def delete_global_question_with_options(
        self,
        request: main_models.DeleteGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_question_with_options_async(
        self,
        request: main_models.DeleteGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_question(
        self,
        request: main_models.DeleteGlobalQuestionRequest,
    ) -> main_models.DeleteGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return self.delete_global_question_with_options(request, runtime)

    async def delete_global_question_async(
        self,
        request: main_models.DeleteGlobalQuestionRequest,
    ) -> main_models.DeleteGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return await self.delete_global_question_with_options_async(request, runtime)

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
            version = '2019-12-26',
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
            version = '2019-12-26',
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

    def delete_intent_with_options(
        self,
        request: main_models.DeleteIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intent_with_options_async(
        self,
        request: main_models.DeleteIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_intent(
        self,
        request: main_models.DeleteIntentRequest,
    ) -> main_models.DeleteIntentResponse:
        runtime = RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    async def delete_intent_async(
        self,
        request: main_models.DeleteIntentRequest,
    ) -> main_models.DeleteIntentResponse:
        runtime = RuntimeOptions()
        return await self.delete_intent_with_options_async(request, runtime)

    def delete_job_group_with_options(
        self,
        request: main_models.DeleteJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_group_with_options_async(
        self,
        request: main_models.DeleteJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job_group(
        self,
        request: main_models.DeleteJobGroupRequest,
    ) -> main_models.DeleteJobGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_job_group_with_options(request, runtime)

    async def delete_job_group_async(
        self,
        request: main_models.DeleteJobGroupRequest,
    ) -> main_models.DeleteJobGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_job_group_with_options_async(request, runtime)

    def delete_outbound_call_number_with_options(
        self,
        request: main_models.DeleteOutboundCallNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOutboundCallNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOutboundCallNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOutboundCallNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_outbound_call_number_with_options_async(
        self,
        request: main_models.DeleteOutboundCallNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOutboundCallNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOutboundCallNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOutboundCallNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_outbound_call_number(
        self,
        request: main_models.DeleteOutboundCallNumberRequest,
    ) -> main_models.DeleteOutboundCallNumberResponse:
        runtime = RuntimeOptions()
        return self.delete_outbound_call_number_with_options(request, runtime)

    async def delete_outbound_call_number_async(
        self,
        request: main_models.DeleteOutboundCallNumberRequest,
    ) -> main_models.DeleteOutboundCallNumberResponse:
        runtime = RuntimeOptions()
        return await self.delete_outbound_call_number_with_options_async(request, runtime)

    def delete_script_with_options(
        self,
        request: main_models.DeleteScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_with_options_async(
        self,
        request: main_models.DeleteScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script(
        self,
        request: main_models.DeleteScriptRequest,
    ) -> main_models.DeleteScriptResponse:
        runtime = RuntimeOptions()
        return self.delete_script_with_options(request, runtime)

    async def delete_script_async(
        self,
        request: main_models.DeleteScriptRequest,
    ) -> main_models.DeleteScriptResponse:
        runtime = RuntimeOptions()
        return await self.delete_script_with_options_async(request, runtime)

    def delete_script_recording_with_options(
        self,
        request: main_models.DeleteScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_recording_with_options_async(
        self,
        request: main_models.DeleteScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script_recording(
        self,
        request: main_models.DeleteScriptRecordingRequest,
    ) -> main_models.DeleteScriptRecordingResponse:
        runtime = RuntimeOptions()
        return self.delete_script_recording_with_options(request, runtime)

    async def delete_script_recording_async(
        self,
        request: main_models.DeleteScriptRecordingRequest,
    ) -> main_models.DeleteScriptRecordingResponse:
        runtime = RuntimeOptions()
        return await self.delete_script_recording_with_options_async(request, runtime)

    def delete_script_waveform_with_options(
        self,
        request: main_models.DeleteScriptWaveformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptWaveformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_waveform_id):
            query['ScriptWaveformId'] = request.script_waveform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScriptWaveform',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptWaveformResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_waveform_with_options_async(
        self,
        request: main_models.DeleteScriptWaveformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptWaveformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_waveform_id):
            query['ScriptWaveformId'] = request.script_waveform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScriptWaveform',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptWaveformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script_waveform(
        self,
        request: main_models.DeleteScriptWaveformRequest,
    ) -> main_models.DeleteScriptWaveformResponse:
        runtime = RuntimeOptions()
        return self.delete_script_waveform_with_options(request, runtime)

    async def delete_script_waveform_async(
        self,
        request: main_models.DeleteScriptWaveformRequest,
    ) -> main_models.DeleteScriptWaveformResponse:
        runtime = RuntimeOptions()
        return await self.delete_script_waveform_with_options_async(request, runtime)

    def describe_beebot_intent_with_options(
        self,
        request: main_models.DescribeBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBeebotIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_beebot_intent_with_options_async(
        self,
        request: main_models.DescribeBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBeebotIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_beebot_intent(
        self,
        request: main_models.DescribeBeebotIntentRequest,
    ) -> main_models.DescribeBeebotIntentResponse:
        runtime = RuntimeOptions()
        return self.describe_beebot_intent_with_options(request, runtime)

    async def describe_beebot_intent_async(
        self,
        request: main_models.DescribeBeebotIntentRequest,
    ) -> main_models.DescribeBeebotIntentResponse:
        runtime = RuntimeOptions()
        return await self.describe_beebot_intent_with_options_async(request, runtime)

    def describe_dialogue_node_statistics_with_options(
        self,
        request: main_models.DescribeDialogueNodeStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDialogueNodeStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDialogueNodeStatistics',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDialogueNodeStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dialogue_node_statistics_with_options_async(
        self,
        request: main_models.DescribeDialogueNodeStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDialogueNodeStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDialogueNodeStatistics',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDialogueNodeStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dialogue_node_statistics(
        self,
        request: main_models.DescribeDialogueNodeStatisticsRequest,
    ) -> main_models.DescribeDialogueNodeStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_dialogue_node_statistics_with_options(request, runtime)

    async def describe_dialogue_node_statistics_async(
        self,
        request: main_models.DescribeDialogueNodeStatisticsRequest,
    ) -> main_models.DescribeDialogueNodeStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dialogue_node_statistics_with_options_async(request, runtime)

    def describe_ds_reports_with_options(
        self,
        request: main_models.DescribeDsReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDsReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDsReports',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ds_reports_with_options_async(
        self,
        request: main_models.DescribeDsReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDsReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDsReports',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDsReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ds_reports(
        self,
        request: main_models.DescribeDsReportsRequest,
    ) -> main_models.DescribeDsReportsResponse:
        runtime = RuntimeOptions()
        return self.describe_ds_reports_with_options(request, runtime)

    async def describe_ds_reports_async(
        self,
        request: main_models.DescribeDsReportsRequest,
    ) -> main_models.DescribeDsReportsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ds_reports_with_options_async(request, runtime)

    def describe_global_question_with_options(
        self,
        request: main_models.DescribeGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_question_with_options_async(
        self,
        request: main_models.DescribeGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_question(
        self,
        request: main_models.DescribeGlobalQuestionRequest,
    ) -> main_models.DescribeGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return self.describe_global_question_with_options(request, runtime)

    async def describe_global_question_async(
        self,
        request: main_models.DescribeGlobalQuestionRequest,
    ) -> main_models.DescribeGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return await self.describe_global_question_with_options_async(request, runtime)

    def describe_group_executing_info_with_options(
        self,
        request: main_models.DescribeGroupExecutingInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupExecutingInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupExecutingInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupExecutingInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_executing_info_with_options_async(
        self,
        request: main_models.DescribeGroupExecutingInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupExecutingInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupExecutingInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupExecutingInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_executing_info(
        self,
        request: main_models.DescribeGroupExecutingInfoRequest,
    ) -> main_models.DescribeGroupExecutingInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_group_executing_info_with_options(request, runtime)

    async def describe_group_executing_info_async(
        self,
        request: main_models.DescribeGroupExecutingInfoRequest,
    ) -> main_models.DescribeGroupExecutingInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_executing_info_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_intent_with_options(
        self,
        request: main_models.DescribeIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intent_with_options_async(
        self,
        request: main_models.DescribeIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intent(
        self,
        request: main_models.DescribeIntentRequest,
    ) -> main_models.DescribeIntentResponse:
        runtime = RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    async def describe_intent_async(
        self,
        request: main_models.DescribeIntentRequest,
    ) -> main_models.DescribeIntentResponse:
        runtime = RuntimeOptions()
        return await self.describe_intent_with_options_async(request, runtime)

    def describe_intent_statistics_with_options(
        self,
        request: main_models.DescribeIntentStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntentStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntentStatistics',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intent_statistics_with_options_async(
        self,
        request: main_models.DescribeIntentStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntentStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntentStatistics',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntentStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intent_statistics(
        self,
        request: main_models.DescribeIntentStatisticsRequest,
    ) -> main_models.DescribeIntentStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_intent_statistics_with_options(request, runtime)

    async def describe_intent_statistics_async(
        self,
        request: main_models.DescribeIntentStatisticsRequest,
    ) -> main_models.DescribeIntentStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_intent_statistics_with_options_async(request, runtime)

    def describe_job_with_options(
        self,
        request: main_models.DescribeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.with_script):
            query['WithScript'] = request.with_script
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJob',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: main_models.DescribeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.with_script):
            query['WithScript'] = request.with_script
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJob',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job(
        self,
        request: main_models.DescribeJobRequest,
    ) -> main_models.DescribeJobResponse:
        runtime = RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    async def describe_job_async(
        self,
        request: main_models.DescribeJobRequest,
    ) -> main_models.DescribeJobResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_with_options_async(request, runtime)

    def describe_job_data_parsing_task_progress_with_options(
        self,
        request: main_models.DescribeJobDataParsingTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobDataParsingTaskProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobDataParsingTaskProgress',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobDataParsingTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_data_parsing_task_progress_with_options_async(
        self,
        request: main_models.DescribeJobDataParsingTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobDataParsingTaskProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobDataParsingTaskProgress',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobDataParsingTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_data_parsing_task_progress(
        self,
        request: main_models.DescribeJobDataParsingTaskProgressRequest,
    ) -> main_models.DescribeJobDataParsingTaskProgressResponse:
        runtime = RuntimeOptions()
        return self.describe_job_data_parsing_task_progress_with_options(request, runtime)

    async def describe_job_data_parsing_task_progress_async(
        self,
        request: main_models.DescribeJobDataParsingTaskProgressRequest,
    ) -> main_models.DescribeJobDataParsingTaskProgressResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_data_parsing_task_progress_with_options_async(request, runtime)

    def describe_job_group_with_options(
        self,
        request: main_models.DescribeJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brief_types):
            query['BriefTypes'] = request.brief_types
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_group_with_options_async(
        self,
        request: main_models.DescribeJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brief_types):
            query['BriefTypes'] = request.brief_types
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_group(
        self,
        request: main_models.DescribeJobGroupRequest,
    ) -> main_models.DescribeJobGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_job_group_with_options(request, runtime)

    async def describe_job_group_async(
        self,
        request: main_models.DescribeJobGroupRequest,
    ) -> main_models.DescribeJobGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_group_with_options_async(request, runtime)

    def describe_job_group_export_task_progress_with_options(
        self,
        request: main_models.DescribeJobGroupExportTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobGroupExportTaskProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobGroupExportTaskProgress',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobGroupExportTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_group_export_task_progress_with_options_async(
        self,
        request: main_models.DescribeJobGroupExportTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobGroupExportTaskProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobGroupExportTaskProgress',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobGroupExportTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_group_export_task_progress(
        self,
        request: main_models.DescribeJobGroupExportTaskProgressRequest,
    ) -> main_models.DescribeJobGroupExportTaskProgressResponse:
        runtime = RuntimeOptions()
        return self.describe_job_group_export_task_progress_with_options(request, runtime)

    async def describe_job_group_export_task_progress_async(
        self,
        request: main_models.DescribeJobGroupExportTaskProgressRequest,
    ) -> main_models.DescribeJobGroupExportTaskProgressResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_group_export_task_progress_with_options_async(request, runtime)

    def describe_script_with_options(
        self,
        request: main_models.DescribeScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_script_with_options_async(
        self,
        request: main_models.DescribeScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_script(
        self,
        request: main_models.DescribeScriptRequest,
    ) -> main_models.DescribeScriptResponse:
        runtime = RuntimeOptions()
        return self.describe_script_with_options(request, runtime)

    async def describe_script_async(
        self,
        request: main_models.DescribeScriptRequest,
    ) -> main_models.DescribeScriptResponse:
        runtime = RuntimeOptions()
        return await self.describe_script_with_options_async(request, runtime)

    def describe_script_voice_config_with_options(
        self,
        request: main_models.DescribeScriptVoiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScriptVoiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScriptVoiceConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScriptVoiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_script_voice_config_with_options_async(
        self,
        request: main_models.DescribeScriptVoiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScriptVoiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScriptVoiceConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScriptVoiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_script_voice_config(
        self,
        request: main_models.DescribeScriptVoiceConfigRequest,
    ) -> main_models.DescribeScriptVoiceConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_script_voice_config_with_options(request, runtime)

    async def describe_script_voice_config_async(
        self,
        request: main_models.DescribeScriptVoiceConfigRequest,
    ) -> main_models.DescribeScriptVoiceConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_script_voice_config_with_options_async(request, runtime)

    def describe_ttsconfig_with_options(
        self,
        request: main_models.DescribeTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTTSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTTSConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ttsconfig_with_options_async(
        self,
        request: main_models.DescribeTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTTSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTTSConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ttsconfig(
        self,
        request: main_models.DescribeTTSConfigRequest,
    ) -> main_models.DescribeTTSConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_ttsconfig_with_options(request, runtime)

    async def describe_ttsconfig_async(
        self,
        request: main_models.DescribeTTSConfigRequest,
    ) -> main_models.DescribeTTSConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_ttsconfig_with_options_async(request, runtime)

    def describe_ttsdemo_with_options(
        self,
        request: main_models.DescribeTTSDemoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTTSDemoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTTSDemo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTTSDemoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ttsdemo_with_options_async(
        self,
        request: main_models.DescribeTTSDemoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTTSDemoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTTSDemo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTTSDemoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ttsdemo(
        self,
        request: main_models.DescribeTTSDemoRequest,
    ) -> main_models.DescribeTTSDemoResponse:
        runtime = RuntimeOptions()
        return self.describe_ttsdemo_with_options(request, runtime)

    async def describe_ttsdemo_async(
        self,
        request: main_models.DescribeTTSDemoRequest,
    ) -> main_models.DescribeTTSDemoResponse:
        runtime = RuntimeOptions()
        return await self.describe_ttsdemo_with_options_async(request, runtime)

    def describe_tag_hits_summary_with_options(
        self,
        request: main_models.DescribeTagHitsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagHitsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagHitsSummary',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagHitsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_hits_summary_with_options_async(
        self,
        request: main_models.DescribeTagHitsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagHitsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagHitsSummary',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagHitsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_hits_summary(
        self,
        request: main_models.DescribeTagHitsSummaryRequest,
    ) -> main_models.DescribeTagHitsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_hits_summary_with_options(request, runtime)

    async def describe_tag_hits_summary_async(
        self,
        request: main_models.DescribeTagHitsSummaryRequest,
    ) -> main_models.DescribeTagHitsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_hits_summary_with_options_async(request, runtime)

    def describe_tenant_bind_number_with_options(
        self,
        request: main_models.DescribeTenantBindNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTenantBindNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTenantBindNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTenantBindNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_bind_number_with_options_async(
        self,
        request: main_models.DescribeTenantBindNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTenantBindNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTenantBindNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTenantBindNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_bind_number(
        self,
        request: main_models.DescribeTenantBindNumberRequest,
    ) -> main_models.DescribeTenantBindNumberResponse:
        runtime = RuntimeOptions()
        return self.describe_tenant_bind_number_with_options(request, runtime)

    async def describe_tenant_bind_number_async(
        self,
        request: main_models.DescribeTenantBindNumberRequest,
    ) -> main_models.DescribeTenantBindNumberResponse:
        runtime = RuntimeOptions()
        return await self.describe_tenant_bind_number_with_options_async(request, runtime)

    def dialogue_with_options(
        self,
        request: main_models.DialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_key):
            query['ActionKey'] = request.action_key
        if not DaraCore.is_null(request.action_params):
            query['ActionParams'] = request.action_params
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_type):
            query['CallType'] = request.call_type
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Dialogue',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def dialogue_with_options_async(
        self,
        request: main_models.DialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_key):
            query['ActionKey'] = request.action_key
        if not DaraCore.is_null(request.action_params):
            query['ActionParams'] = request.action_params
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_type):
            query['CallType'] = request.call_type
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Dialogue',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dialogue(
        self,
        request: main_models.DialogueRequest,
    ) -> main_models.DialogueResponse:
        runtime = RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    async def dialogue_async(
        self,
        request: main_models.DialogueRequest,
    ) -> main_models.DialogueResponse:
        runtime = RuntimeOptions()
        return await self.dialogue_with_options_async(request, runtime)

    def download_recording_with_options(
        self,
        request: main_models.DownloadRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_voice_slice_recording):
            query['NeedVoiceSliceRecording'] = request.need_voice_slice_recording
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_recording_with_options_async(
        self,
        request: main_models.DownloadRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_voice_slice_recording):
            query['NeedVoiceSliceRecording'] = request.need_voice_slice_recording
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_recording(
        self,
        request: main_models.DownloadRecordingRequest,
    ) -> main_models.DownloadRecordingResponse:
        runtime = RuntimeOptions()
        return self.download_recording_with_options(request, runtime)

    async def download_recording_async(
        self,
        request: main_models.DownloadRecordingRequest,
    ) -> main_models.DownloadRecordingResponse:
        runtime = RuntimeOptions()
        return await self.download_recording_with_options_async(request, runtime)

    def download_script_recording_with_options(
        self,
        request: main_models.DownloadScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_script_recording_with_options_async(
        self,
        request: main_models.DownloadScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_script_recording(
        self,
        request: main_models.DownloadScriptRecordingRequest,
    ) -> main_models.DownloadScriptRecordingResponse:
        runtime = RuntimeOptions()
        return self.download_script_recording_with_options(request, runtime)

    async def download_script_recording_async(
        self,
        request: main_models.DownloadScriptRecordingRequest,
    ) -> main_models.DownloadScriptRecordingResponse:
        runtime = RuntimeOptions()
        return await self.download_script_recording_with_options_async(request, runtime)

    def duplicate_script_with_options(
        self,
        request: main_models.DuplicateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DuplicateScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.source_script_id):
            query['SourceScriptId'] = request.source_script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DuplicateScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DuplicateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def duplicate_script_with_options_async(
        self,
        request: main_models.DuplicateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DuplicateScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.source_script_id):
            query['SourceScriptId'] = request.source_script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DuplicateScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DuplicateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def duplicate_script(
        self,
        request: main_models.DuplicateScriptRequest,
    ) -> main_models.DuplicateScriptResponse:
        runtime = RuntimeOptions()
        return self.duplicate_script_with_options(request, runtime)

    async def duplicate_script_async(
        self,
        request: main_models.DuplicateScriptRequest,
    ) -> main_models.DuplicateScriptResponse:
        runtime = RuntimeOptions()
        return await self.duplicate_script_with_options_async(request, runtime)

    def export_script_with_options(
        self,
        request: main_models.ExportScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_script_with_options_async(
        self,
        request: main_models.ExportScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_script(
        self,
        request: main_models.ExportScriptRequest,
    ) -> main_models.ExportScriptResponse:
        runtime = RuntimeOptions()
        return self.export_script_with_options(request, runtime)

    async def export_script_async(
        self,
        request: main_models.ExportScriptRequest,
    ) -> main_models.ExportScriptResponse:
        runtime = RuntimeOptions()
        return await self.export_script_with_options_async(request, runtime)

    def generate_upload_url_with_options(
        self,
        request: main_models.GenerateUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadUrl',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_url_with_options_async(
        self,
        request: main_models.GenerateUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadUrl',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_url(
        self,
        request: main_models.GenerateUploadUrlRequest,
    ) -> main_models.GenerateUploadUrlResponse:
        runtime = RuntimeOptions()
        return self.generate_upload_url_with_options(request, runtime)

    async def generate_upload_url_async(
        self,
        request: main_models.GenerateUploadUrlRequest,
    ) -> main_models.GenerateUploadUrlResponse:
        runtime = RuntimeOptions()
        return await self.generate_upload_url_with_options_async(request, runtime)

    def get_after_answer_delay_playback_with_options(
        self,
        request: main_models.GetAfterAnswerDelayPlaybackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAfterAnswerDelayPlaybackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAfterAnswerDelayPlayback',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAfterAnswerDelayPlaybackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_after_answer_delay_playback_with_options_async(
        self,
        request: main_models.GetAfterAnswerDelayPlaybackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAfterAnswerDelayPlaybackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAfterAnswerDelayPlayback',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAfterAnswerDelayPlaybackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_after_answer_delay_playback(
        self,
        request: main_models.GetAfterAnswerDelayPlaybackRequest,
    ) -> main_models.GetAfterAnswerDelayPlaybackResponse:
        runtime = RuntimeOptions()
        return self.get_after_answer_delay_playback_with_options(request, runtime)

    async def get_after_answer_delay_playback_async(
        self,
        request: main_models.GetAfterAnswerDelayPlaybackRequest,
    ) -> main_models.GetAfterAnswerDelayPlaybackResponse:
        runtime = RuntimeOptions()
        return await self.get_after_answer_delay_playback_with_options_async(request, runtime)

    def get_agent_profile_with_options(
        self,
        request: main_models.GetAgentProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentProfile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_profile_with_options_async(
        self,
        request: main_models.GetAgentProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentProfileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentProfile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_profile(
        self,
        request: main_models.GetAgentProfileRequest,
    ) -> main_models.GetAgentProfileResponse:
        runtime = RuntimeOptions()
        return self.get_agent_profile_with_options(request, runtime)

    async def get_agent_profile_async(
        self,
        request: main_models.GetAgentProfileRequest,
    ) -> main_models.GetAgentProfileResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_profile_with_options_async(request, runtime)

    def get_agent_profile_template_with_options(
        self,
        request: main_models.GetAgentProfileTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentProfileTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentProfileTemplate',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentProfileTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_profile_template_with_options_async(
        self,
        request: main_models.GetAgentProfileTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentProfileTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentProfileTemplate',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentProfileTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_profile_template(
        self,
        request: main_models.GetAgentProfileTemplateRequest,
    ) -> main_models.GetAgentProfileTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_agent_profile_template_with_options(request, runtime)

    async def get_agent_profile_template_async(
        self,
        request: main_models.GetAgentProfileTemplateRequest,
    ) -> main_models.GetAgentProfileTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_profile_template_with_options_async(request, runtime)

    def get_annotation_mission_summary_with_options(
        self,
        request: main_models.GetAnnotationMissionSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationMissionSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationMissionSummary',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationMissionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_annotation_mission_summary_with_options_async(
        self,
        request: main_models.GetAnnotationMissionSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationMissionSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationMissionSummary',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationMissionSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_annotation_mission_summary(
        self,
        request: main_models.GetAnnotationMissionSummaryRequest,
    ) -> main_models.GetAnnotationMissionSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_annotation_mission_summary_with_options(request, runtime)

    async def get_annotation_mission_summary_async(
        self,
        request: main_models.GetAnnotationMissionSummaryRequest,
    ) -> main_models.GetAnnotationMissionSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_annotation_mission_summary_with_options_async(request, runtime)

    def get_annotation_mission_tag_info_list_with_options(
        self,
        request: main_models.GetAnnotationMissionTagInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationMissionTagInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationMissionTagInfoList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationMissionTagInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_annotation_mission_tag_info_list_with_options_async(
        self,
        request: main_models.GetAnnotationMissionTagInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationMissionTagInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationMissionTagInfoList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationMissionTagInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_annotation_mission_tag_info_list(
        self,
        request: main_models.GetAnnotationMissionTagInfoListRequest,
    ) -> main_models.GetAnnotationMissionTagInfoListResponse:
        runtime = RuntimeOptions()
        return self.get_annotation_mission_tag_info_list_with_options(request, runtime)

    async def get_annotation_mission_tag_info_list_async(
        self,
        request: main_models.GetAnnotationMissionTagInfoListRequest,
    ) -> main_models.GetAnnotationMissionTagInfoListResponse:
        runtime = RuntimeOptions()
        return await self.get_annotation_mission_tag_info_list_with_options_async(request, runtime)

    def get_asr_server_info_with_options(
        self,
        request: main_models.GetAsrServerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsrServerInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsrServerInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsrServerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asr_server_info_with_options_async(
        self,
        request: main_models.GetAsrServerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsrServerInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsrServerInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsrServerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asr_server_info(
        self,
        request: main_models.GetAsrServerInfoRequest,
    ) -> main_models.GetAsrServerInfoResponse:
        runtime = RuntimeOptions()
        return self.get_asr_server_info_with_options(request, runtime)

    async def get_asr_server_info_async(
        self,
        request: main_models.GetAsrServerInfoRequest,
    ) -> main_models.GetAsrServerInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_asr_server_info_with_options_async(request, runtime)

    def get_assign_jobs_async_result_with_options(
        self,
        request: main_models.GetAssignJobsAsyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAssignJobsAsyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_task_id):
            query['AsyncTaskId'] = request.async_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAssignJobsAsyncResult',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAssignJobsAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_assign_jobs_async_result_with_options_async(
        self,
        request: main_models.GetAssignJobsAsyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAssignJobsAsyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_task_id):
            query['AsyncTaskId'] = request.async_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAssignJobsAsyncResult',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAssignJobsAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_assign_jobs_async_result(
        self,
        request: main_models.GetAssignJobsAsyncResultRequest,
    ) -> main_models.GetAssignJobsAsyncResultResponse:
        runtime = RuntimeOptions()
        return self.get_assign_jobs_async_result_with_options(request, runtime)

    async def get_assign_jobs_async_result_async(
        self,
        request: main_models.GetAssignJobsAsyncResultRequest,
    ) -> main_models.GetAssignJobsAsyncResultResponse:
        runtime = RuntimeOptions()
        return await self.get_assign_jobs_async_result_with_options_async(request, runtime)

    def get_base_strategy_period_with_options(
        self,
        request: main_models.GetBaseStrategyPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBaseStrategyPeriodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBaseStrategyPeriod',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBaseStrategyPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_base_strategy_period_with_options_async(
        self,
        request: main_models.GetBaseStrategyPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBaseStrategyPeriodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBaseStrategyPeriod',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBaseStrategyPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_base_strategy_period(
        self,
        request: main_models.GetBaseStrategyPeriodRequest,
    ) -> main_models.GetBaseStrategyPeriodResponse:
        runtime = RuntimeOptions()
        return self.get_base_strategy_period_with_options(request, runtime)

    async def get_base_strategy_period_async(
        self,
        request: main_models.GetBaseStrategyPeriodRequest,
    ) -> main_models.GetBaseStrategyPeriodResponse:
        runtime = RuntimeOptions()
        return await self.get_base_strategy_period_with_options_async(request, runtime)

    def get_concurrent_conversation_quota_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetConcurrentConversationQuotaResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetConcurrentConversationQuota',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConcurrentConversationQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_concurrent_conversation_quota_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetConcurrentConversationQuotaResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetConcurrentConversationQuota',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConcurrentConversationQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_concurrent_conversation_quota(self) -> main_models.GetConcurrentConversationQuotaResponse:
        runtime = RuntimeOptions()
        return self.get_concurrent_conversation_quota_with_options(runtime)

    async def get_concurrent_conversation_quota_async(self) -> main_models.GetConcurrentConversationQuotaResponse:
        runtime = RuntimeOptions()
        return await self.get_concurrent_conversation_quota_with_options_async(runtime)

    def get_contact_block_list_with_options(
        self,
        request: main_models.GetContactBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetContactBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action = 'GetContactBlockList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContactBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contact_block_list_with_options_async(
        self,
        request: main_models.GetContactBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetContactBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action = 'GetContactBlockList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContactBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contact_block_list(
        self,
        request: main_models.GetContactBlockListRequest,
    ) -> main_models.GetContactBlockListResponse:
        runtime = RuntimeOptions()
        return self.get_contact_block_list_with_options(request, runtime)

    async def get_contact_block_list_async(
        self,
        request: main_models.GetContactBlockListRequest,
    ) -> main_models.GetContactBlockListResponse:
        runtime = RuntimeOptions()
        return await self.get_contact_block_list_with_options_async(request, runtime)

    def get_contact_white_list_with_options(
        self,
        request: main_models.GetContactWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetContactWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action = 'GetContactWhiteList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContactWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contact_white_list_with_options_async(
        self,
        request: main_models.GetContactWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetContactWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action = 'GetContactWhiteList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContactWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contact_white_list(
        self,
        request: main_models.GetContactWhiteListRequest,
    ) -> main_models.GetContactWhiteListResponse:
        runtime = RuntimeOptions()
        return self.get_contact_white_list_with_options(request, runtime)

    async def get_contact_white_list_async(
        self,
        request: main_models.GetContactWhiteListRequest,
    ) -> main_models.GetContactWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.get_contact_white_list_with_options_async(request, runtime)

    def get_current_concurrency_with_options(
        self,
        request: main_models.GetCurrentConcurrencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCurrentConcurrencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCurrentConcurrency',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCurrentConcurrencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_current_concurrency_with_options_async(
        self,
        request: main_models.GetCurrentConcurrencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCurrentConcurrencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCurrentConcurrency',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCurrentConcurrencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_current_concurrency(
        self,
        request: main_models.GetCurrentConcurrencyRequest,
    ) -> main_models.GetCurrentConcurrencyResponse:
        runtime = RuntimeOptions()
        return self.get_current_concurrency_with_options(request, runtime)

    async def get_current_concurrency_async(
        self,
        request: main_models.GetCurrentConcurrencyRequest,
    ) -> main_models.GetCurrentConcurrencyResponse:
        runtime = RuntimeOptions()
        return await self.get_current_concurrency_with_options_async(request, runtime)

    def get_empty_number_no_more_calls_info_with_options(
        self,
        request: main_models.GetEmptyNumberNoMoreCallsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEmptyNumberNoMoreCallsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmptyNumberNoMoreCallsInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmptyNumberNoMoreCallsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_empty_number_no_more_calls_info_with_options_async(
        self,
        request: main_models.GetEmptyNumberNoMoreCallsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEmptyNumberNoMoreCallsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmptyNumberNoMoreCallsInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmptyNumberNoMoreCallsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_empty_number_no_more_calls_info(
        self,
        request: main_models.GetEmptyNumberNoMoreCallsInfoRequest,
    ) -> main_models.GetEmptyNumberNoMoreCallsInfoResponse:
        runtime = RuntimeOptions()
        return self.get_empty_number_no_more_calls_info_with_options(request, runtime)

    async def get_empty_number_no_more_calls_info_async(
        self,
        request: main_models.GetEmptyNumberNoMoreCallsInfoRequest,
    ) -> main_models.GetEmptyNumberNoMoreCallsInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_empty_number_no_more_calls_info_with_options_async(request, runtime)

    def get_job_data_upload_params_with_options(
        self,
        request: main_models.GetJobDataUploadParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDataUploadParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.busi_type):
            query['BusiType'] = request.busi_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobDataUploadParams',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDataUploadParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_data_upload_params_with_options_async(
        self,
        request: main_models.GetJobDataUploadParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDataUploadParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.busi_type):
            query['BusiType'] = request.busi_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobDataUploadParams',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDataUploadParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_data_upload_params(
        self,
        request: main_models.GetJobDataUploadParamsRequest,
    ) -> main_models.GetJobDataUploadParamsResponse:
        runtime = RuntimeOptions()
        return self.get_job_data_upload_params_with_options(request, runtime)

    async def get_job_data_upload_params_async(
        self,
        request: main_models.GetJobDataUploadParamsRequest,
    ) -> main_models.GetJobDataUploadParamsResponse:
        runtime = RuntimeOptions()
        return await self.get_job_data_upload_params_with_options_async(request, runtime)

    def get_max_attempts_per_day_with_options(
        self,
        request: main_models.GetMaxAttemptsPerDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMaxAttemptsPerDayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMaxAttemptsPerDay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaxAttemptsPerDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_max_attempts_per_day_with_options_async(
        self,
        request: main_models.GetMaxAttemptsPerDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMaxAttemptsPerDayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMaxAttemptsPerDay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaxAttemptsPerDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_max_attempts_per_day(
        self,
        request: main_models.GetMaxAttemptsPerDayRequest,
    ) -> main_models.GetMaxAttemptsPerDayResponse:
        runtime = RuntimeOptions()
        return self.get_max_attempts_per_day_with_options(request, runtime)

    async def get_max_attempts_per_day_async(
        self,
        request: main_models.GetMaxAttemptsPerDayRequest,
    ) -> main_models.GetMaxAttemptsPerDayResponse:
        runtime = RuntimeOptions()
        return await self.get_max_attempts_per_day_with_options_async(request, runtime)

    def get_number_district_info_template_download_url_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNumberDistrictInfoTemplateDownloadUrl',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNumberDistrictInfoTemplateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_number_district_info_template_download_url_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetNumberDistrictInfoTemplateDownloadUrl',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNumberDistrictInfoTemplateDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_number_district_info_template_download_url(self) -> main_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.get_number_district_info_template_download_url_with_options(runtime)

    async def get_number_district_info_template_download_url_async(self) -> main_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_number_district_info_template_download_url_with_options_async(runtime)

    def get_realtime_concurrency_report_with_options(
        self,
        request: main_models.GetRealtimeConcurrencyReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeConcurrencyReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeConcurrencyReport',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealtimeConcurrencyReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_concurrency_report_with_options_async(
        self,
        request: main_models.GetRealtimeConcurrencyReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealtimeConcurrencyReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealtimeConcurrencyReport',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealtimeConcurrencyReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_concurrency_report(
        self,
        request: main_models.GetRealtimeConcurrencyReportRequest,
    ) -> main_models.GetRealtimeConcurrencyReportResponse:
        runtime = RuntimeOptions()
        return self.get_realtime_concurrency_report_with_options(request, runtime)

    async def get_realtime_concurrency_report_async(
        self,
        request: main_models.GetRealtimeConcurrencyReportRequest,
    ) -> main_models.GetRealtimeConcurrencyReportResponse:
        runtime = RuntimeOptions()
        return await self.get_realtime_concurrency_report_with_options_async(request, runtime)

    def get_summary_info_with_options(
        self,
        request: main_models.GetSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSummaryInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSummaryInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_info_with_options_async(
        self,
        request: main_models.GetSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSummaryInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSummaryInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_info(
        self,
        request: main_models.GetSummaryInfoRequest,
    ) -> main_models.GetSummaryInfoResponse:
        runtime = RuntimeOptions()
        return self.get_summary_info_with_options(request, runtime)

    async def get_summary_info_async(
        self,
        request: main_models.GetSummaryInfoRequest,
    ) -> main_models.GetSummaryInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_summary_info_with_options_async(request, runtime)

    def get_task_by_uuid_with_options(
        self,
        request: main_models.GetTaskByUuidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskByUuidResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskByUuid',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskByUuidResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_by_uuid_with_options_async(
        self,
        request: main_models.GetTaskByUuidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskByUuidResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskByUuid',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskByUuidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_by_uuid(
        self,
        request: main_models.GetTaskByUuidRequest,
    ) -> main_models.GetTaskByUuidResponse:
        runtime = RuntimeOptions()
        return self.get_task_by_uuid_with_options(request, runtime)

    async def get_task_by_uuid_async(
        self,
        request: main_models.GetTaskByUuidRequest,
    ) -> main_models.GetTaskByUuidResponse:
        runtime = RuntimeOptions()
        return await self.get_task_by_uuid_with_options_async(request, runtime)

    def get_version_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetVersionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetVersion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_version_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetVersionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetVersion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_version(self) -> main_models.GetVersionResponse:
        runtime = RuntimeOptions()
        return self.get_version_with_options(runtime)

    async def get_version_async(self) -> main_models.GetVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_version_with_options_async(runtime)

    def import_script_with_options(
        self,
        request: main_models.ImportScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.signature_url):
            query['SignatureUrl'] = request.signature_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_script_with_options_async(
        self,
        request: main_models.ImportScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.signature_url):
            query['SignatureUrl'] = request.signature_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_script(
        self,
        request: main_models.ImportScriptRequest,
    ) -> main_models.ImportScriptResponse:
        runtime = RuntimeOptions()
        return self.import_script_with_options(request, runtime)

    async def import_script_async(
        self,
        request: main_models.ImportScriptRequest,
    ) -> main_models.ImportScriptResponse:
        runtime = RuntimeOptions()
        return await self.import_script_with_options_async(request, runtime)

    def inflight_task_timeout_with_options(
        self,
        request: main_models.InflightTaskTimeoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InflightTaskTimeoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InflightTaskTimeout',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InflightTaskTimeoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def inflight_task_timeout_with_options_async(
        self,
        request: main_models.InflightTaskTimeoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InflightTaskTimeoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InflightTaskTimeout',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InflightTaskTimeoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inflight_task_timeout(
        self,
        request: main_models.InflightTaskTimeoutRequest,
    ) -> main_models.InflightTaskTimeoutResponse:
        runtime = RuntimeOptions()
        return self.inflight_task_timeout_with_options(request, runtime)

    async def inflight_task_timeout_async(
        self,
        request: main_models.InflightTaskTimeoutRequest,
    ) -> main_models.InflightTaskTimeoutResponse:
        runtime = RuntimeOptions()
        return await self.inflight_task_timeout_with_options_async(request, runtime)

    def list_agent_profiles_with_options(
        self,
        request: main_models.ListAgentProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentProfilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentProfiles',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_profiles_with_options_async(
        self,
        request: main_models.ListAgentProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentProfilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_ip):
            body['AppIp'] = request.app_ip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentProfiles',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_profiles(
        self,
        request: main_models.ListAgentProfilesRequest,
    ) -> main_models.ListAgentProfilesResponse:
        runtime = RuntimeOptions()
        return self.list_agent_profiles_with_options(request, runtime)

    async def list_agent_profiles_async(
        self,
        request: main_models.ListAgentProfilesRequest,
    ) -> main_models.ListAgentProfilesResponse:
        runtime = RuntimeOptions()
        return await self.list_agent_profiles_with_options_async(request, runtime)

    def list_all_tenant_bind_number_binding_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllTenantBindNumberBindingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAllTenantBindNumberBinding',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllTenantBindNumberBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_tenant_bind_number_binding_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllTenantBindNumberBindingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAllTenantBindNumberBinding',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllTenantBindNumberBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_tenant_bind_number_binding(self) -> main_models.ListAllTenantBindNumberBindingResponse:
        runtime = RuntimeOptions()
        return self.list_all_tenant_bind_number_binding_with_options(runtime)

    async def list_all_tenant_bind_number_binding_async(self) -> main_models.ListAllTenantBindNumberBindingResponse:
        runtime = RuntimeOptions()
        return await self.list_all_tenant_bind_number_binding_with_options_async(runtime)

    def list_annotation_mission_with_options(
        self,
        request: main_models.ListAnnotationMissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationMissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not DaraCore.is_null(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not DaraCore.is_null(request.annotation_status_list_filter):
            query['AnnotationStatusListFilter'] = request.annotation_status_list_filter
        if not DaraCore.is_null(request.annotation_status_list_string_filter):
            query['AnnotationStatusListStringFilter'] = request.annotation_status_list_string_filter
        if not DaraCore.is_null(request.create_time_end_filter):
            query['CreateTimeEndFilter'] = request.create_time_end_filter
        if not DaraCore.is_null(request.create_time_start_filter):
            query['CreateTimeStartFilter'] = request.create_time_start_filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationMission',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationMissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_annotation_mission_with_options_async(
        self,
        request: main_models.ListAnnotationMissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationMissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not DaraCore.is_null(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not DaraCore.is_null(request.annotation_status_list_filter):
            query['AnnotationStatusListFilter'] = request.annotation_status_list_filter
        if not DaraCore.is_null(request.annotation_status_list_string_filter):
            query['AnnotationStatusListStringFilter'] = request.annotation_status_list_string_filter
        if not DaraCore.is_null(request.create_time_end_filter):
            query['CreateTimeEndFilter'] = request.create_time_end_filter
        if not DaraCore.is_null(request.create_time_start_filter):
            query['CreateTimeStartFilter'] = request.create_time_start_filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationMission',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationMissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_annotation_mission(
        self,
        request: main_models.ListAnnotationMissionRequest,
    ) -> main_models.ListAnnotationMissionResponse:
        runtime = RuntimeOptions()
        return self.list_annotation_mission_with_options(request, runtime)

    async def list_annotation_mission_async(
        self,
        request: main_models.ListAnnotationMissionRequest,
    ) -> main_models.ListAnnotationMissionResponse:
        runtime = RuntimeOptions()
        return await self.list_annotation_mission_with_options_async(request, runtime)

    def list_annotation_mission_session_with_options(
        self,
        request: main_models.ListAnnotationMissionSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationMissionSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not DaraCore.is_null(request.annotation_mission_session_id):
            query['AnnotationMissionSessionId'] = request.annotation_mission_session_id
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.include_status_list_json_string):
            query['IncludeStatusListJsonString'] = request.include_status_list_json_string
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationMissionSession',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationMissionSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_annotation_mission_session_with_options_async(
        self,
        request: main_models.ListAnnotationMissionSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationMissionSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not DaraCore.is_null(request.annotation_mission_session_id):
            query['AnnotationMissionSessionId'] = request.annotation_mission_session_id
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.include_status_list_json_string):
            query['IncludeStatusListJsonString'] = request.include_status_list_json_string
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationMissionSession',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationMissionSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_annotation_mission_session(
        self,
        request: main_models.ListAnnotationMissionSessionRequest,
    ) -> main_models.ListAnnotationMissionSessionResponse:
        runtime = RuntimeOptions()
        return self.list_annotation_mission_session_with_options(request, runtime)

    async def list_annotation_mission_session_async(
        self,
        request: main_models.ListAnnotationMissionSessionRequest,
    ) -> main_models.ListAnnotationMissionSessionResponse:
        runtime = RuntimeOptions()
        return await self.list_annotation_mission_session_with_options_async(request, runtime)

    def list_api_plugins_with_options(
        self,
        request: main_models.ListApiPluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiPlugins',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_plugins_with_options_async(
        self,
        request: main_models.ListApiPluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiPlugins',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_plugins(
        self,
        request: main_models.ListApiPluginsRequest,
    ) -> main_models.ListApiPluginsResponse:
        runtime = RuntimeOptions()
        return self.list_api_plugins_with_options(request, runtime)

    async def list_api_plugins_async(
        self,
        request: main_models.ListApiPluginsRequest,
    ) -> main_models.ListApiPluginsResponse:
        runtime = RuntimeOptions()
        return await self.list_api_plugins_with_options_async(request, runtime)

    def list_beebot_intent_with_options(
        self,
        request: main_models.ListBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBeebotIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_beebot_intent_with_options_async(
        self,
        request: main_models.ListBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBeebotIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_beebot_intent(
        self,
        request: main_models.ListBeebotIntentRequest,
    ) -> main_models.ListBeebotIntentResponse:
        runtime = RuntimeOptions()
        return self.list_beebot_intent_with_options(request, runtime)

    async def list_beebot_intent_async(
        self,
        request: main_models.ListBeebotIntentRequest,
    ) -> main_models.ListBeebotIntentResponse:
        runtime = RuntimeOptions()
        return await self.list_beebot_intent_with_options_async(request, runtime)

    def list_beebot_intent_lgf_with_options(
        self,
        request: main_models.ListBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBeebotIntentLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_beebot_intent_lgf_with_options_async(
        self,
        request: main_models.ListBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBeebotIntentLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_beebot_intent_lgf(
        self,
        request: main_models.ListBeebotIntentLgfRequest,
    ) -> main_models.ListBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return self.list_beebot_intent_lgf_with_options(request, runtime)

    async def list_beebot_intent_lgf_async(
        self,
        request: main_models.ListBeebotIntentLgfRequest,
    ) -> main_models.ListBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return await self.list_beebot_intent_lgf_with_options_async(request, runtime)

    def list_beebot_intent_user_say_with_options(
        self,
        request: main_models.ListBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBeebotIntentUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_beebot_intent_user_say_with_options_async(
        self,
        request: main_models.ListBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBeebotIntentUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_beebot_intent_user_say(
        self,
        request: main_models.ListBeebotIntentUserSayRequest,
    ) -> main_models.ListBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return self.list_beebot_intent_user_say_with_options(request, runtime)

    async def list_beebot_intent_user_say_async(
        self,
        request: main_models.ListBeebotIntentUserSayRequest,
    ) -> main_models.ListBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return await self.list_beebot_intent_user_say_with_options_async(request, runtime)

    def list_chatbot_instances_with_options(
        self,
        request: main_models.ListChatbotInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatbotInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatbotInstances',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatbotInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatbot_instances_with_options_async(
        self,
        request: main_models.ListChatbotInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatbotInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatbotInstances',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatbotInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatbot_instances(
        self,
        request: main_models.ListChatbotInstancesRequest,
    ) -> main_models.ListChatbotInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_chatbot_instances_with_options(request, runtime)

    async def list_chatbot_instances_async(
        self,
        request: main_models.ListChatbotInstancesRequest,
    ) -> main_models.ListChatbotInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_chatbot_instances_with_options_async(request, runtime)

    def list_dialogue_flows_with_options(
        self,
        request: main_models.ListDialogueFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialogueFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDialogueFlows',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialogueFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialogue_flows_with_options_async(
        self,
        request: main_models.ListDialogueFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialogueFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDialogueFlows',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialogueFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialogue_flows(
        self,
        request: main_models.ListDialogueFlowsRequest,
    ) -> main_models.ListDialogueFlowsResponse:
        runtime = RuntimeOptions()
        return self.list_dialogue_flows_with_options(request, runtime)

    async def list_dialogue_flows_async(
        self,
        request: main_models.ListDialogueFlowsRequest,
    ) -> main_models.ListDialogueFlowsResponse:
        runtime = RuntimeOptions()
        return await self.list_dialogue_flows_with_options_async(request, runtime)

    def list_download_tasks_with_options(
        self,
        request: main_models.ListDownloadTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownloadTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownloadTasks',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownloadTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_download_tasks_with_options_async(
        self,
        request: main_models.ListDownloadTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownloadTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownloadTasks',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownloadTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_download_tasks(
        self,
        request: main_models.ListDownloadTasksRequest,
    ) -> main_models.ListDownloadTasksResponse:
        runtime = RuntimeOptions()
        return self.list_download_tasks_with_options(request, runtime)

    async def list_download_tasks_async(
        self,
        request: main_models.ListDownloadTasksRequest,
    ) -> main_models.ListDownloadTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_download_tasks_with_options_async(request, runtime)

    def list_flash_sms_templates_with_options(
        self,
        request: main_models.ListFlashSmsTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlashSmsTemplatesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsTemplates',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlashSmsTemplates',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def list_global_questions_with_options(
        self,
        request: main_models.ListGlobalQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGlobalQuestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGlobalQuestions',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGlobalQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_global_questions_with_options_async(
        self,
        request: main_models.ListGlobalQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGlobalQuestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGlobalQuestions',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGlobalQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_global_questions(
        self,
        request: main_models.ListGlobalQuestionsRequest,
    ) -> main_models.ListGlobalQuestionsResponse:
        runtime = RuntimeOptions()
        return self.list_global_questions_with_options(request, runtime)

    async def list_global_questions_async(
        self,
        request: main_models.ListGlobalQuestionsRequest,
    ) -> main_models.ListGlobalQuestionsResponse:
        runtime = RuntimeOptions()
        return await self.list_global_questions_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2019-12-26',
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
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2019-12-26',
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

    def list_intentions_with_options(
        self,
        request: main_models.ListIntentionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntentions',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intentions_with_options_async(
        self,
        request: main_models.ListIntentionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntentions',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intentions(
        self,
        request: main_models.ListIntentionsRequest,
    ) -> main_models.ListIntentionsResponse:
        runtime = RuntimeOptions()
        return self.list_intentions_with_options(request, runtime)

    async def list_intentions_async(
        self,
        request: main_models.ListIntentionsRequest,
    ) -> main_models.ListIntentionsResponse:
        runtime = RuntimeOptions()
        return await self.list_intentions_with_options_async(request, runtime)

    def list_intents_with_options(
        self,
        request: main_models.ListIntentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntents',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intents_with_options_async(
        self,
        request: main_models.ListIntentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntents',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intents(
        self,
        request: main_models.ListIntentsRequest,
    ) -> main_models.ListIntentsResponse:
        runtime = RuntimeOptions()
        return self.list_intents_with_options(request, runtime)

    async def list_intents_async(
        self,
        request: main_models.ListIntentsRequest,
    ) -> main_models.ListIntentsResponse:
        runtime = RuntimeOptions()
        return await self.list_intents_with_options_async(request, runtime)

    def list_job_groups_with_options(
        self,
        request: main_models.ListJobGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_query):
            query['AsyncQuery'] = request.async_query
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_status_filter):
            query['JobGroupStatusFilter'] = request.job_group_status_filter
        if not DaraCore.is_null(request.only_min_concurrency_enabled):
            query['OnlyMinConcurrencyEnabled'] = request.only_min_concurrency_enabled
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_text):
            query['SearchText'] = request.search_text
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobGroups',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_groups_with_options_async(
        self,
        request: main_models.ListJobGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_query):
            query['AsyncQuery'] = request.async_query
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_status_filter):
            query['JobGroupStatusFilter'] = request.job_group_status_filter
        if not DaraCore.is_null(request.only_min_concurrency_enabled):
            query['OnlyMinConcurrencyEnabled'] = request.only_min_concurrency_enabled
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_text):
            query['SearchText'] = request.search_text
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobGroups',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_groups(
        self,
        request: main_models.ListJobGroupsRequest,
    ) -> main_models.ListJobGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_job_groups_with_options(request, runtime)

    async def list_job_groups_async(
        self,
        request: main_models.ListJobGroupsRequest,
    ) -> main_models.ListJobGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_job_groups_with_options_async(request, runtime)

    def list_job_groups_async_with_options(
        self,
        request: main_models.ListJobGroupsAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobGroupsAsyncResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobGroupsAsync',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobGroupsAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_groups_async_with_options_async(
        self,
        request: main_models.ListJobGroupsAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobGroupsAsyncResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobGroupsAsync',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobGroupsAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_groups_async(
        self,
        request: main_models.ListJobGroupsAsyncRequest,
    ) -> main_models.ListJobGroupsAsyncResponse:
        runtime = RuntimeOptions()
        return self.list_job_groups_async_with_options(request, runtime)

    async def list_job_groups_async_async(
        self,
        request: main_models.ListJobGroupsAsyncRequest,
    ) -> main_models.ListJobGroupsAsyncResponse:
        runtime = RuntimeOptions()
        return await self.list_job_groups_async_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
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
            action = 'ListJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
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
            action = 'ListJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_jobs_by_group_with_options(
        self,
        request: main_models.ListJobsByGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsByGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_failure_reason):
            query['JobFailureReason'] = request.job_failure_reason
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_status):
            query['JobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobsByGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_by_group_with_options_async(
        self,
        request: main_models.ListJobsByGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsByGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_failure_reason):
            query['JobFailureReason'] = request.job_failure_reason
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_status):
            query['JobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobsByGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsByGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs_by_group(
        self,
        request: main_models.ListJobsByGroupRequest,
    ) -> main_models.ListJobsByGroupResponse:
        runtime = RuntimeOptions()
        return self.list_jobs_by_group_with_options(request, runtime)

    async def list_jobs_by_group_async(
        self,
        request: main_models.ListJobsByGroupRequest,
    ) -> main_models.ListJobsByGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_jobs_by_group_with_options_async(request, runtime)

    def list_outbound_call_numbers_with_options(
        self,
        request: main_models.ListOutboundCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundCallNumbersResponse:
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
            action = 'ListOutboundCallNumbers',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_call_numbers_with_options_async(
        self,
        request: main_models.ListOutboundCallNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOutboundCallNumbersResponse:
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
            action = 'ListOutboundCallNumbers',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutboundCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_call_numbers(
        self,
        request: main_models.ListOutboundCallNumbersRequest,
    ) -> main_models.ListOutboundCallNumbersResponse:
        runtime = RuntimeOptions()
        return self.list_outbound_call_numbers_with_options(request, runtime)

    async def list_outbound_call_numbers_async(
        self,
        request: main_models.ListOutboundCallNumbersRequest,
    ) -> main_models.ListOutboundCallNumbersResponse:
        runtime = RuntimeOptions()
        return await self.list_outbound_call_numbers_with_options_async(request, runtime)

    def list_resource_tags_with_options(
        self,
        request: main_models.ListResourceTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTags',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_tags_with_options_async(
        self,
        request: main_models.ListResourceTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTags',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_tags(
        self,
        request: main_models.ListResourceTagsRequest,
    ) -> main_models.ListResourceTagsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    async def list_resource_tags_async(
        self,
        request: main_models.ListResourceTagsRequest,
    ) -> main_models.ListResourceTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_tags_with_options_async(request, runtime)

    def list_script_publish_histories_with_options(
        self,
        request: main_models.ListScriptPublishHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptPublishHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptPublishHistories',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptPublishHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_script_publish_histories_with_options_async(
        self,
        request: main_models.ListScriptPublishHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptPublishHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptPublishHistories',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptPublishHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_script_publish_histories(
        self,
        request: main_models.ListScriptPublishHistoriesRequest,
    ) -> main_models.ListScriptPublishHistoriesResponse:
        runtime = RuntimeOptions()
        return self.list_script_publish_histories_with_options(request, runtime)

    async def list_script_publish_histories_async(
        self,
        request: main_models.ListScriptPublishHistoriesRequest,
    ) -> main_models.ListScriptPublishHistoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_script_publish_histories_with_options_async(request, runtime)

    def list_script_recording_with_options(
        self,
        request: main_models.ListScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ref_ids_json):
            query['RefIdsJson'] = request.ref_ids_json
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.states_json):
            query['StatesJson'] = request.states_json
        if not DaraCore.is_null(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_script_recording_with_options_async(
        self,
        request: main_models.ListScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ref_ids_json):
            query['RefIdsJson'] = request.ref_ids_json
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.states_json):
            query['StatesJson'] = request.states_json
        if not DaraCore.is_null(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_script_recording(
        self,
        request: main_models.ListScriptRecordingRequest,
    ) -> main_models.ListScriptRecordingResponse:
        runtime = RuntimeOptions()
        return self.list_script_recording_with_options(request, runtime)

    async def list_script_recording_async(
        self,
        request: main_models.ListScriptRecordingRequest,
    ) -> main_models.ListScriptRecordingResponse:
        runtime = RuntimeOptions()
        return await self.list_script_recording_with_options_async(request, runtime)

    def list_script_voice_configs_with_options(
        self,
        request: main_models.ListScriptVoiceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptVoiceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptVoiceConfigs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptVoiceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_script_voice_configs_with_options_async(
        self,
        request: main_models.ListScriptVoiceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptVoiceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScriptVoiceConfigs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptVoiceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_script_voice_configs(
        self,
        request: main_models.ListScriptVoiceConfigsRequest,
    ) -> main_models.ListScriptVoiceConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_script_voice_configs_with_options(request, runtime)

    async def list_script_voice_configs_async(
        self,
        request: main_models.ListScriptVoiceConfigsRequest,
    ) -> main_models.ListScriptVoiceConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_script_voice_configs_with_options_async(request, runtime)

    def list_scripts_with_options(
        self,
        request: main_models.ListScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScripts',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scripts_with_options_async(
        self,
        request: main_models.ListScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScripts',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scripts(
        self,
        request: main_models.ListScriptsRequest,
    ) -> main_models.ListScriptsResponse:
        runtime = RuntimeOptions()
        return self.list_scripts_with_options(request, runtime)

    async def list_scripts_async(
        self,
        request: main_models.ListScriptsRequest,
    ) -> main_models.ListScriptsResponse:
        runtime = RuntimeOptions()
        return await self.list_scripts_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tags_with_options(
        self,
        request: main_models.ListTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: main_models.ListTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def modify_agent_profile_with_options(
        self,
        tmp_req: main_models.ModifyAgentProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAgentProfileResponse:
        tmp_req.validate()
        request = main_models.ModifyAgentProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.faq_category_ids):
            request.faq_category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.faq_category_ids, 'FaqCategoryIds', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not DaraCore.is_null(request.api_plugin_json):
            body['ApiPluginJson'] = request.api_plugin_json
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.faq_category_ids_shrink):
            body['FaqCategoryIds'] = request.faq_category_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not DaraCore.is_null(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.model_config):
            body['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not DaraCore.is_null(request.scenario):
            body['Scenario'] = request.scenario
        if not DaraCore.is_null(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAgentProfile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAgentProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_agent_profile_with_options_async(
        self,
        tmp_req: main_models.ModifyAgentProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAgentProfileResponse:
        tmp_req.validate()
        request = main_models.ModifyAgentProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.faq_category_ids):
            request.faq_category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.faq_category_ids, 'FaqCategoryIds', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not DaraCore.is_null(request.api_plugin_json):
            body['ApiPluginJson'] = request.api_plugin_json
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.faq_category_ids_shrink):
            body['FaqCategoryIds'] = request.faq_category_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not DaraCore.is_null(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.model_config):
            body['ModelConfig'] = request.model_config
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not DaraCore.is_null(request.scenario):
            body['Scenario'] = request.scenario
        if not DaraCore.is_null(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAgentProfile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAgentProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_agent_profile(
        self,
        request: main_models.ModifyAgentProfileRequest,
    ) -> main_models.ModifyAgentProfileResponse:
        runtime = RuntimeOptions()
        return self.modify_agent_profile_with_options(request, runtime)

    async def modify_agent_profile_async(
        self,
        request: main_models.ModifyAgentProfileRequest,
    ) -> main_models.ModifyAgentProfileResponse:
        runtime = RuntimeOptions()
        return await self.modify_agent_profile_with_options_async(request, runtime)

    def modify_annotation_mission_with_options(
        self,
        request: main_models.ModifyAnnotationMissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAnnotationMissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not DaraCore.is_null(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not DaraCore.is_null(request.annotation_status):
            query['AnnotationStatus'] = request.annotation_status
        if not DaraCore.is_null(request.delete):
            query['Delete'] = request.delete
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAnnotationMission',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAnnotationMissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_annotation_mission_with_options_async(
        self,
        request: main_models.ModifyAnnotationMissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAnnotationMissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not DaraCore.is_null(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not DaraCore.is_null(request.annotation_status):
            query['AnnotationStatus'] = request.annotation_status
        if not DaraCore.is_null(request.delete):
            query['Delete'] = request.delete
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAnnotationMission',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAnnotationMissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_annotation_mission(
        self,
        request: main_models.ModifyAnnotationMissionRequest,
    ) -> main_models.ModifyAnnotationMissionResponse:
        runtime = RuntimeOptions()
        return self.modify_annotation_mission_with_options(request, runtime)

    async def modify_annotation_mission_async(
        self,
        request: main_models.ModifyAnnotationMissionRequest,
    ) -> main_models.ModifyAnnotationMissionResponse:
        runtime = RuntimeOptions()
        return await self.modify_annotation_mission_with_options_async(request, runtime)

    def modify_batch_jobs_with_options(
        self,
        request: main_models.ModifyBatchJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBatchJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not DaraCore.is_null(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBatchJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBatchJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_batch_jobs_with_options_async(
        self,
        request: main_models.ModifyBatchJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBatchJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not DaraCore.is_null(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBatchJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBatchJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_batch_jobs(
        self,
        request: main_models.ModifyBatchJobsRequest,
    ) -> main_models.ModifyBatchJobsResponse:
        runtime = RuntimeOptions()
        return self.modify_batch_jobs_with_options(request, runtime)

    async def modify_batch_jobs_async(
        self,
        request: main_models.ModifyBatchJobsRequest,
    ) -> main_models.ModifyBatchJobsResponse:
        runtime = RuntimeOptions()
        return await self.modify_batch_jobs_with_options_async(request, runtime)

    def modify_beebot_intent_with_options(
        self,
        tmp_req: main_models.ModifyBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBeebotIntentResponse:
        tmp_req.validate()
        request = main_models.ModifyBeebotIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_beebot_intent_with_options_async(
        self,
        tmp_req: main_models.ModifyBeebotIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBeebotIntentResponse:
        tmp_req.validate()
        request = main_models.ModifyBeebotIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBeebotIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_beebot_intent(
        self,
        request: main_models.ModifyBeebotIntentRequest,
    ) -> main_models.ModifyBeebotIntentResponse:
        runtime = RuntimeOptions()
        return self.modify_beebot_intent_with_options(request, runtime)

    async def modify_beebot_intent_async(
        self,
        request: main_models.ModifyBeebotIntentRequest,
    ) -> main_models.ModifyBeebotIntentResponse:
        runtime = RuntimeOptions()
        return await self.modify_beebot_intent_with_options_async(request, runtime)

    def modify_beebot_intent_lgf_with_options(
        self,
        tmp_req: main_models.ModifyBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBeebotIntentLgfResponse:
        tmp_req.validate()
        request = main_models.ModifyBeebotIntentLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_beebot_intent_lgf_with_options_async(
        self,
        tmp_req: main_models.ModifyBeebotIntentLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBeebotIntentLgfResponse:
        tmp_req.validate()
        request = main_models.ModifyBeebotIntentLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBeebotIntentLgf',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_beebot_intent_lgf(
        self,
        request: main_models.ModifyBeebotIntentLgfRequest,
    ) -> main_models.ModifyBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return self.modify_beebot_intent_lgf_with_options(request, runtime)

    async def modify_beebot_intent_lgf_async(
        self,
        request: main_models.ModifyBeebotIntentLgfRequest,
    ) -> main_models.ModifyBeebotIntentLgfResponse:
        runtime = RuntimeOptions()
        return await self.modify_beebot_intent_lgf_with_options_async(request, runtime)

    def modify_beebot_intent_user_say_with_options(
        self,
        tmp_req: main_models.ModifyBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBeebotIntentUserSayResponse:
        tmp_req.validate()
        request = main_models.ModifyBeebotIntentUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_beebot_intent_user_say_with_options_async(
        self,
        tmp_req: main_models.ModifyBeebotIntentUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBeebotIntentUserSayResponse:
        tmp_req.validate()
        request = main_models.ModifyBeebotIntentUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBeebotIntentUserSay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_beebot_intent_user_say(
        self,
        request: main_models.ModifyBeebotIntentUserSayRequest,
    ) -> main_models.ModifyBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return self.modify_beebot_intent_user_say_with_options(request, runtime)

    async def modify_beebot_intent_user_say_async(
        self,
        request: main_models.ModifyBeebotIntentUserSayRequest,
    ) -> main_models.ModifyBeebotIntentUserSayResponse:
        runtime = RuntimeOptions()
        return await self.modify_beebot_intent_user_say_with_options_async(request, runtime)

    def modify_dialogue_flow_with_options(
        self,
        request: main_models.ModifyDialogueFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDialogueFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dialogue_flow_definition):
            query['DialogueFlowDefinition'] = request.dialogue_flow_definition
        if not DaraCore.is_null(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_drafted):
            query['IsDrafted'] = request.is_drafted
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDialogueFlow',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDialogueFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dialogue_flow_with_options_async(
        self,
        request: main_models.ModifyDialogueFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDialogueFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dialogue_flow_definition):
            query['DialogueFlowDefinition'] = request.dialogue_flow_definition
        if not DaraCore.is_null(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_drafted):
            query['IsDrafted'] = request.is_drafted
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDialogueFlow',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDialogueFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dialogue_flow(
        self,
        request: main_models.ModifyDialogueFlowRequest,
    ) -> main_models.ModifyDialogueFlowResponse:
        runtime = RuntimeOptions()
        return self.modify_dialogue_flow_with_options(request, runtime)

    async def modify_dialogue_flow_async(
        self,
        request: main_models.ModifyDialogueFlowRequest,
    ) -> main_models.ModifyDialogueFlowResponse:
        runtime = RuntimeOptions()
        return await self.modify_dialogue_flow_with_options_async(request, runtime)

    def modify_empty_number_no_more_calls_info_with_options(
        self,
        request: main_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.empty_number_no_more_calls):
            query['EmptyNumberNoMoreCalls'] = request.empty_number_no_more_calls
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEmptyNumberNoMoreCallsInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEmptyNumberNoMoreCallsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_empty_number_no_more_calls_info_with_options_async(
        self,
        request: main_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.empty_number_no_more_calls):
            query['EmptyNumberNoMoreCalls'] = request.empty_number_no_more_calls
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEmptyNumberNoMoreCallsInfo',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEmptyNumberNoMoreCallsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_empty_number_no_more_calls_info(
        self,
        request: main_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
    ) -> main_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        runtime = RuntimeOptions()
        return self.modify_empty_number_no_more_calls_info_with_options(request, runtime)

    async def modify_empty_number_no_more_calls_info_async(
        self,
        request: main_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
    ) -> main_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        runtime = RuntimeOptions()
        return await self.modify_empty_number_no_more_calls_info_with_options_async(request, runtime)

    def modify_global_question_with_options(
        self,
        request: main_models.ModifyGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.answers):
            query['Answers'] = request.answers
        if not DaraCore.is_null(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not DaraCore.is_null(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not DaraCore.is_null(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.questions):
            query['Questions'] = request.questions
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_question_with_options_async(
        self,
        request: main_models.ModifyGlobalQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.answers):
            query['Answers'] = request.answers
        if not DaraCore.is_null(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not DaraCore.is_null(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not DaraCore.is_null(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.questions):
            query['Questions'] = request.questions
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGlobalQuestion',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_question(
        self,
        request: main_models.ModifyGlobalQuestionRequest,
    ) -> main_models.ModifyGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return self.modify_global_question_with_options(request, runtime)

    async def modify_global_question_async(
        self,
        request: main_models.ModifyGlobalQuestionRequest,
    ) -> main_models.ModifyGlobalQuestionResponse:
        runtime = RuntimeOptions()
        return await self.modify_global_question_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2019-12-26',
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
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2019-12-26',
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

    def modify_intent_with_options(
        self,
        request: main_models.ModifyIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_intent_with_options_async(
        self,
        request: main_models.ModifyIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIntent',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_intent(
        self,
        request: main_models.ModifyIntentRequest,
    ) -> main_models.ModifyIntentResponse:
        runtime = RuntimeOptions()
        return self.modify_intent_with_options(request, runtime)

    async def modify_intent_async(
        self,
        request: main_models.ModifyIntentRequest,
    ) -> main_models.ModifyIntentResponse:
        runtime = RuntimeOptions()
        return await self.modify_intent_with_options_async(request, runtime)

    def modify_job_group_with_options(
        self,
        request: main_models.ModifyJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_group_status):
            query['JobGroupStatus'] = request.job_group_status
        if not DaraCore.is_null(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not DaraCore.is_null(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not DaraCore.is_null(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_job_group_with_options_async(
        self,
        request: main_models.ModifyJobGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyJobGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_group_status):
            query['JobGroupStatus'] = request.job_group_status
        if not DaraCore.is_null(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not DaraCore.is_null(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not DaraCore.is_null(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyJobGroup',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_job_group(
        self,
        request: main_models.ModifyJobGroupRequest,
    ) -> main_models.ModifyJobGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_job_group_with_options(request, runtime)

    async def modify_job_group_async(
        self,
        request: main_models.ModifyJobGroupRequest,
    ) -> main_models.ModifyJobGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_job_group_with_options_async(request, runtime)

    def modify_outbound_call_number_with_options(
        self,
        request: main_models.ModifyOutboundCallNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOutboundCallNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        if not DaraCore.is_null(request.rate_limit_count):
            query['RateLimitCount'] = request.rate_limit_count
        if not DaraCore.is_null(request.rate_limit_period):
            query['RateLimitPeriod'] = request.rate_limit_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOutboundCallNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOutboundCallNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_outbound_call_number_with_options_async(
        self,
        request: main_models.ModifyOutboundCallNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOutboundCallNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        if not DaraCore.is_null(request.rate_limit_count):
            query['RateLimitCount'] = request.rate_limit_count
        if not DaraCore.is_null(request.rate_limit_period):
            query['RateLimitPeriod'] = request.rate_limit_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOutboundCallNumber',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOutboundCallNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_outbound_call_number(
        self,
        request: main_models.ModifyOutboundCallNumberRequest,
    ) -> main_models.ModifyOutboundCallNumberResponse:
        runtime = RuntimeOptions()
        return self.modify_outbound_call_number_with_options(request, runtime)

    async def modify_outbound_call_number_async(
        self,
        request: main_models.ModifyOutboundCallNumberRequest,
    ) -> main_models.ModifyOutboundCallNumberResponse:
        runtime = RuntimeOptions()
        return await self.modify_outbound_call_number_with_options_async(request, runtime)

    def modify_script_with_options(
        self,
        request: main_models.ModifyScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not DaraCore.is_null(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not DaraCore.is_null(request.chat_config):
            query['ChatConfig'] = request.chat_config
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.label_config):
            query['LabelConfig'] = request.label_config
        if not DaraCore.is_null(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not DaraCore.is_null(request.mini_playback_config_list_json_string):
            query['MiniPlaybackConfigListJsonString'] = request.mini_playback_config_list_json_string
        if not DaraCore.is_null(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not DaraCore.is_null(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not DaraCore.is_null(request.nls_config):
            query['NlsConfig'] = request.nls_config
        if not DaraCore.is_null(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        if not DaraCore.is_null(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not DaraCore.is_null(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_script_with_options_async(
        self,
        request: main_models.ModifyScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not DaraCore.is_null(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not DaraCore.is_null(request.chat_config):
            query['ChatConfig'] = request.chat_config
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.label_config):
            query['LabelConfig'] = request.label_config
        if not DaraCore.is_null(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not DaraCore.is_null(request.mini_playback_config_list_json_string):
            query['MiniPlaybackConfigListJsonString'] = request.mini_playback_config_list_json_string
        if not DaraCore.is_null(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not DaraCore.is_null(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not DaraCore.is_null(request.nls_config):
            query['NlsConfig'] = request.nls_config
        if not DaraCore.is_null(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not DaraCore.is_null(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        if not DaraCore.is_null(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not DaraCore.is_null(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_script(
        self,
        request: main_models.ModifyScriptRequest,
    ) -> main_models.ModifyScriptResponse:
        runtime = RuntimeOptions()
        return self.modify_script_with_options(request, runtime)

    async def modify_script_async(
        self,
        request: main_models.ModifyScriptRequest,
    ) -> main_models.ModifyScriptResponse:
        runtime = RuntimeOptions()
        return await self.modify_script_with_options_async(request, runtime)

    def modify_script_voice_config_with_options(
        self,
        request: main_models.ModifyScriptVoiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScriptVoiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        if not DaraCore.is_null(request.script_waveform_relation):
            query['ScriptWaveformRelation'] = request.script_waveform_relation
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScriptVoiceConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScriptVoiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_script_voice_config_with_options_async(
        self,
        request: main_models.ModifyScriptVoiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScriptVoiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        if not DaraCore.is_null(request.script_waveform_relation):
            query['ScriptWaveformRelation'] = request.script_waveform_relation
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScriptVoiceConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScriptVoiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_script_voice_config(
        self,
        request: main_models.ModifyScriptVoiceConfigRequest,
    ) -> main_models.ModifyScriptVoiceConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_script_voice_config_with_options(request, runtime)

    async def modify_script_voice_config_async(
        self,
        request: main_models.ModifyScriptVoiceConfigRequest,
    ) -> main_models.ModifyScriptVoiceConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_script_voice_config_with_options_async(request, runtime)

    def modify_ttsconfig_with_options(
        self,
        request: main_models.ModifyTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTTSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTTSConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ttsconfig_with_options_async(
        self,
        request: main_models.ModifyTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTTSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTTSConfig',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ttsconfig(
        self,
        request: main_models.ModifyTTSConfigRequest,
    ) -> main_models.ModifyTTSConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_ttsconfig_with_options(request, runtime)

    async def modify_ttsconfig_async(
        self,
        request: main_models.ModifyTTSConfigRequest,
    ) -> main_models.ModifyTTSConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_ttsconfig_with_options_async(request, runtime)

    def modify_tag_groups_with_options(
        self,
        request: main_models.ModifyTagGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTagGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.tag_groups):
            query['TagGroups'] = request.tag_groups
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTagGroups',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTagGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tag_groups_with_options_async(
        self,
        request: main_models.ModifyTagGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTagGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.tag_groups):
            query['TagGroups'] = request.tag_groups
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTagGroups',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTagGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tag_groups(
        self,
        request: main_models.ModifyTagGroupsRequest,
    ) -> main_models.ModifyTagGroupsResponse:
        runtime = RuntimeOptions()
        return self.modify_tag_groups_with_options(request, runtime)

    async def modify_tag_groups_async(
        self,
        request: main_models.ModifyTagGroupsRequest,
    ) -> main_models.ModifyTagGroupsResponse:
        runtime = RuntimeOptions()
        return await self.modify_tag_groups_with_options_async(request, runtime)

    def publish_script_with_options(
        self,
        request: main_models.PublishScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_script_with_options_async(
        self,
        request: main_models.PublishScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_script(
        self,
        request: main_models.PublishScriptRequest,
    ) -> main_models.PublishScriptResponse:
        runtime = RuntimeOptions()
        return self.publish_script_with_options(request, runtime)

    async def publish_script_async(
        self,
        request: main_models.PublishScriptRequest,
    ) -> main_models.PublishScriptResponse:
        runtime = RuntimeOptions()
        return await self.publish_script_with_options_async(request, runtime)

    def publish_script_for_debug_with_options(
        self,
        request: main_models.PublishScriptForDebugRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishScriptForDebugResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishScriptForDebug',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishScriptForDebugResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_script_for_debug_with_options_async(
        self,
        request: main_models.PublishScriptForDebugRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishScriptForDebugResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishScriptForDebug',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishScriptForDebugResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_script_for_debug(
        self,
        request: main_models.PublishScriptForDebugRequest,
    ) -> main_models.PublishScriptForDebugResponse:
        runtime = RuntimeOptions()
        return self.publish_script_for_debug_with_options(request, runtime)

    async def publish_script_for_debug_async(
        self,
        request: main_models.PublishScriptForDebugRequest,
    ) -> main_models.PublishScriptForDebugResponse:
        runtime = RuntimeOptions()
        return await self.publish_script_for_debug_with_options_async(request, runtime)

    def query_jobs_with_options(
        self,
        request: main_models.QueryJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_alignment):
            query['TimeAlignment'] = request.time_alignment
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_jobs_with_options_async(
        self,
        request: main_models.QueryJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_alignment):
            query['TimeAlignment'] = request.time_alignment
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_jobs(
        self,
        request: main_models.QueryJobsRequest,
    ) -> main_models.QueryJobsResponse:
        runtime = RuntimeOptions()
        return self.query_jobs_with_options(request, runtime)

    async def query_jobs_async(
        self,
        request: main_models.QueryJobsRequest,
    ) -> main_models.QueryJobsResponse:
        runtime = RuntimeOptions()
        return await self.query_jobs_with_options_async(request, runtime)

    def query_jobs_with_result_with_options(
        self,
        request: main_models.QueryJobsWithResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobsWithResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_actual_time_filter):
            query['EndActualTimeFilter'] = request.end_actual_time_filter
        if not DaraCore.is_null(request.has_answered_filter):
            query['HasAnsweredFilter'] = request.has_answered_filter
        if not DaraCore.is_null(request.has_hang_up_by_rejection_filter):
            query['HasHangUpByRejectionFilter'] = request.has_hang_up_by_rejection_filter
        if not DaraCore.is_null(request.has_reached_end_of_flow_filter):
            query['HasReachedEndOfFlowFilter'] = request.has_reached_end_of_flow_filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_failure_reasons_filter):
            query['JobFailureReasonsFilter'] = request.job_failure_reasons_filter
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_status_filter):
            query['JobStatusFilter'] = request.job_status_filter
        if not DaraCore.is_null(request.labels_json):
            query['LabelsJson'] = request.labels_json
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_text):
            query['QueryText'] = request.query_text
        if not DaraCore.is_null(request.start_actual_time_filter):
            query['StartActualTimeFilter'] = request.start_actual_time_filter
        if not DaraCore.is_null(request.task_status_filter):
            query['TaskStatusFilter'] = request.task_status_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobsWithResult',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobsWithResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_jobs_with_result_with_options_async(
        self,
        request: main_models.QueryJobsWithResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobsWithResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_actual_time_filter):
            query['EndActualTimeFilter'] = request.end_actual_time_filter
        if not DaraCore.is_null(request.has_answered_filter):
            query['HasAnsweredFilter'] = request.has_answered_filter
        if not DaraCore.is_null(request.has_hang_up_by_rejection_filter):
            query['HasHangUpByRejectionFilter'] = request.has_hang_up_by_rejection_filter
        if not DaraCore.is_null(request.has_reached_end_of_flow_filter):
            query['HasReachedEndOfFlowFilter'] = request.has_reached_end_of_flow_filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_failure_reasons_filter):
            query['JobFailureReasonsFilter'] = request.job_failure_reasons_filter
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_status_filter):
            query['JobStatusFilter'] = request.job_status_filter
        if not DaraCore.is_null(request.labels_json):
            query['LabelsJson'] = request.labels_json
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_text):
            query['QueryText'] = request.query_text
        if not DaraCore.is_null(request.start_actual_time_filter):
            query['StartActualTimeFilter'] = request.start_actual_time_filter
        if not DaraCore.is_null(request.task_status_filter):
            query['TaskStatusFilter'] = request.task_status_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobsWithResult',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobsWithResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_jobs_with_result(
        self,
        request: main_models.QueryJobsWithResultRequest,
    ) -> main_models.QueryJobsWithResultResponse:
        runtime = RuntimeOptions()
        return self.query_jobs_with_result_with_options(request, runtime)

    async def query_jobs_with_result_async(
        self,
        request: main_models.QueryJobsWithResultRequest,
    ) -> main_models.QueryJobsWithResultResponse:
        runtime = RuntimeOptions()
        return await self.query_jobs_with_result_with_options_async(request, runtime)

    def query_script_waveforms_with_options(
        self,
        request: main_models.QueryScriptWaveformsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryScriptWaveformsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryScriptWaveforms',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryScriptWaveformsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_script_waveforms_with_options_async(
        self,
        request: main_models.QueryScriptWaveformsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryScriptWaveformsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_content):
            query['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryScriptWaveforms',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryScriptWaveformsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_script_waveforms(
        self,
        request: main_models.QueryScriptWaveformsRequest,
    ) -> main_models.QueryScriptWaveformsResponse:
        runtime = RuntimeOptions()
        return self.query_script_waveforms_with_options(request, runtime)

    async def query_script_waveforms_async(
        self,
        request: main_models.QueryScriptWaveformsRequest,
    ) -> main_models.QueryScriptWaveformsResponse:
        runtime = RuntimeOptions()
        return await self.query_script_waveforms_with_options_async(request, runtime)

    def query_scripts_by_status_with_options(
        self,
        request: main_models.QueryScriptsByStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryScriptsByStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryScriptsByStatus',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryScriptsByStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scripts_by_status_with_options_async(
        self,
        request: main_models.QueryScriptsByStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryScriptsByStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryScriptsByStatus',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryScriptsByStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scripts_by_status(
        self,
        request: main_models.QueryScriptsByStatusRequest,
    ) -> main_models.QueryScriptsByStatusResponse:
        runtime = RuntimeOptions()
        return self.query_scripts_by_status_with_options(request, runtime)

    async def query_scripts_by_status_async(
        self,
        request: main_models.QueryScriptsByStatusRequest,
    ) -> main_models.QueryScriptsByStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_scripts_by_status_with_options_async(request, runtime)

    def record_failure_with_options(
        self,
        request: main_models.RecordFailureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordFailureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.actual_time):
            query['ActualTime'] = request.actual_time
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.disposition_code):
            query['DispositionCode'] = request.disposition_code
        if not DaraCore.is_null(request.exception_codes):
            query['ExceptionCodes'] = request.exception_codes
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordFailure',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordFailureResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_failure_with_options_async(
        self,
        request: main_models.RecordFailureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordFailureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.actual_time):
            query['ActualTime'] = request.actual_time
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.disposition_code):
            query['DispositionCode'] = request.disposition_code
        if not DaraCore.is_null(request.exception_codes):
            query['ExceptionCodes'] = request.exception_codes
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordFailure',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordFailureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_failure(
        self,
        request: main_models.RecordFailureRequest,
    ) -> main_models.RecordFailureResponse:
        runtime = RuntimeOptions()
        return self.record_failure_with_options(request, runtime)

    async def record_failure_async(
        self,
        request: main_models.RecordFailureRequest,
    ) -> main_models.RecordFailureResponse:
        runtime = RuntimeOptions()
        return await self.record_failure_with_options_async(request, runtime)

    def resume_jobs_with_options(
        self,
        request: main_models.ResumeJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_jobs_with_options_async(
        self,
        request: main_models.ResumeJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_jobs(
        self,
        request: main_models.ResumeJobsRequest,
    ) -> main_models.ResumeJobsResponse:
        runtime = RuntimeOptions()
        return self.resume_jobs_with_options(request, runtime)

    async def resume_jobs_async(
        self,
        request: main_models.ResumeJobsRequest,
    ) -> main_models.ResumeJobsResponse:
        runtime = RuntimeOptions()
        return await self.resume_jobs_with_options_async(request, runtime)

    def rollback_script_with_options(
        self,
        request: main_models.RollbackScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rollback_version):
            query['RollbackVersion'] = request.rollback_version
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_script_with_options_async(
        self,
        request: main_models.RollbackScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rollback_version):
            query['RollbackVersion'] = request.rollback_version
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackScript',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_script(
        self,
        request: main_models.RollbackScriptRequest,
    ) -> main_models.RollbackScriptResponse:
        runtime = RuntimeOptions()
        return self.rollback_script_with_options(request, runtime)

    async def rollback_script_async(
        self,
        request: main_models.RollbackScriptRequest,
    ) -> main_models.RollbackScriptResponse:
        runtime = RuntimeOptions()
        return await self.rollback_script_with_options_async(request, runtime)

    def save_after_answer_delay_playback_with_options(
        self,
        request: main_models.SaveAfterAnswerDelayPlaybackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAfterAnswerDelayPlaybackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_answer_delay_playback):
            query['AfterAnswerDelayPlayback'] = request.after_answer_delay_playback
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAfterAnswerDelayPlayback',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAfterAnswerDelayPlaybackResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_after_answer_delay_playback_with_options_async(
        self,
        request: main_models.SaveAfterAnswerDelayPlaybackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAfterAnswerDelayPlaybackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_answer_delay_playback):
            query['AfterAnswerDelayPlayback'] = request.after_answer_delay_playback
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAfterAnswerDelayPlayback',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAfterAnswerDelayPlaybackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_after_answer_delay_playback(
        self,
        request: main_models.SaveAfterAnswerDelayPlaybackRequest,
    ) -> main_models.SaveAfterAnswerDelayPlaybackResponse:
        runtime = RuntimeOptions()
        return self.save_after_answer_delay_playback_with_options(request, runtime)

    async def save_after_answer_delay_playback_async(
        self,
        request: main_models.SaveAfterAnswerDelayPlaybackRequest,
    ) -> main_models.SaveAfterAnswerDelayPlaybackResponse:
        runtime = RuntimeOptions()
        return await self.save_after_answer_delay_playback_with_options_async(request, runtime)

    def save_annotation_mission_session_list_with_options(
        self,
        request: main_models.SaveAnnotationMissionSessionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnnotationMissionSessionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not DaraCore.is_null(request.annotation_mission_session_list):
            query['AnnotationMissionSessionList'] = request.annotation_mission_session_list
        if not DaraCore.is_null(request.annotation_mission_session_list_json_string):
            query['AnnotationMissionSessionListJsonString'] = request.annotation_mission_session_list_json_string
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnnotationMissionSessionList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnnotationMissionSessionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_annotation_mission_session_list_with_options_async(
        self,
        request: main_models.SaveAnnotationMissionSessionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnnotationMissionSessionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not DaraCore.is_null(request.annotation_mission_session_list):
            query['AnnotationMissionSessionList'] = request.annotation_mission_session_list
        if not DaraCore.is_null(request.annotation_mission_session_list_json_string):
            query['AnnotationMissionSessionListJsonString'] = request.annotation_mission_session_list_json_string
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnnotationMissionSessionList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnnotationMissionSessionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_annotation_mission_session_list(
        self,
        request: main_models.SaveAnnotationMissionSessionListRequest,
    ) -> main_models.SaveAnnotationMissionSessionListResponse:
        runtime = RuntimeOptions()
        return self.save_annotation_mission_session_list_with_options(request, runtime)

    async def save_annotation_mission_session_list_async(
        self,
        request: main_models.SaveAnnotationMissionSessionListRequest,
    ) -> main_models.SaveAnnotationMissionSessionListResponse:
        runtime = RuntimeOptions()
        return await self.save_annotation_mission_session_list_with_options_async(request, runtime)

    def save_annotation_mission_tag_info_list_with_options(
        self,
        request: main_models.SaveAnnotationMissionTagInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnnotationMissionTagInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_tag_info_list):
            query['AnnotationMissionTagInfoList'] = request.annotation_mission_tag_info_list
        if not DaraCore.is_null(request.annotation_mission_tag_info_list_json_string):
            query['AnnotationMissionTagInfoListJsonString'] = request.annotation_mission_tag_info_list_json_string
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reset):
            query['Reset'] = request.reset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnnotationMissionTagInfoList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnnotationMissionTagInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_annotation_mission_tag_info_list_with_options_async(
        self,
        request: main_models.SaveAnnotationMissionTagInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnnotationMissionTagInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotation_mission_tag_info_list):
            query['AnnotationMissionTagInfoList'] = request.annotation_mission_tag_info_list
        if not DaraCore.is_null(request.annotation_mission_tag_info_list_json_string):
            query['AnnotationMissionTagInfoListJsonString'] = request.annotation_mission_tag_info_list_json_string
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reset):
            query['Reset'] = request.reset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnnotationMissionTagInfoList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnnotationMissionTagInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_annotation_mission_tag_info_list(
        self,
        request: main_models.SaveAnnotationMissionTagInfoListRequest,
    ) -> main_models.SaveAnnotationMissionTagInfoListResponse:
        runtime = RuntimeOptions()
        return self.save_annotation_mission_tag_info_list_with_options(request, runtime)

    async def save_annotation_mission_tag_info_list_async(
        self,
        request: main_models.SaveAnnotationMissionTagInfoListRequest,
    ) -> main_models.SaveAnnotationMissionTagInfoListResponse:
        runtime = RuntimeOptions()
        return await self.save_annotation_mission_tag_info_list_with_options_async(request, runtime)

    def save_base_strategy_period_with_options(
        self,
        request: main_models.SaveBaseStrategyPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBaseStrategyPeriodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.only_weekdays):
            query['OnlyWeekdays'] = request.only_weekdays
        if not DaraCore.is_null(request.only_workdays):
            query['OnlyWorkdays'] = request.only_workdays
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        if not DaraCore.is_null(request.working_time):
            query['WorkingTime'] = request.working_time
        if not DaraCore.is_null(request.working_time_frames_json):
            query['WorkingTimeFramesJson'] = request.working_time_frames_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBaseStrategyPeriod',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBaseStrategyPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_base_strategy_period_with_options_async(
        self,
        request: main_models.SaveBaseStrategyPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBaseStrategyPeriodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.only_weekdays):
            query['OnlyWeekdays'] = request.only_weekdays
        if not DaraCore.is_null(request.only_workdays):
            query['OnlyWorkdays'] = request.only_workdays
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        if not DaraCore.is_null(request.working_time):
            query['WorkingTime'] = request.working_time
        if not DaraCore.is_null(request.working_time_frames_json):
            query['WorkingTimeFramesJson'] = request.working_time_frames_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBaseStrategyPeriod',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBaseStrategyPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_base_strategy_period(
        self,
        request: main_models.SaveBaseStrategyPeriodRequest,
    ) -> main_models.SaveBaseStrategyPeriodResponse:
        runtime = RuntimeOptions()
        return self.save_base_strategy_period_with_options(request, runtime)

    async def save_base_strategy_period_async(
        self,
        request: main_models.SaveBaseStrategyPeriodRequest,
    ) -> main_models.SaveBaseStrategyPeriodResponse:
        runtime = RuntimeOptions()
        return await self.save_base_strategy_period_with_options_async(request, runtime)

    def save_contact_block_list_with_options(
        self,
        request: main_models.SaveContactBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_block_list_list):
            query['ContactBlockListList'] = request.contact_block_list_list
        if not DaraCore.is_null(request.contact_block_lists_json):
            query['ContactBlockListsJson'] = request.contact_block_lists_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactBlockList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_contact_block_list_with_options_async(
        self,
        request: main_models.SaveContactBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_block_list_list):
            query['ContactBlockListList'] = request.contact_block_list_list
        if not DaraCore.is_null(request.contact_block_lists_json):
            query['ContactBlockListsJson'] = request.contact_block_lists_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactBlockList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_contact_block_list(
        self,
        request: main_models.SaveContactBlockListRequest,
    ) -> main_models.SaveContactBlockListResponse:
        runtime = RuntimeOptions()
        return self.save_contact_block_list_with_options(request, runtime)

    async def save_contact_block_list_async(
        self,
        request: main_models.SaveContactBlockListRequest,
    ) -> main_models.SaveContactBlockListResponse:
        runtime = RuntimeOptions()
        return await self.save_contact_block_list_with_options_async(request, runtime)

    def save_contact_white_list_with_options(
        self,
        request: main_models.SaveContactWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_white_list_list):
            query['ContactWhiteListList'] = request.contact_white_list_list
        if not DaraCore.is_null(request.contact_white_lists_json):
            query['ContactWhiteListsJson'] = request.contact_white_lists_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactWhiteList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_contact_white_list_with_options_async(
        self,
        request: main_models.SaveContactWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_white_list_list):
            query['ContactWhiteListList'] = request.contact_white_list_list
        if not DaraCore.is_null(request.contact_white_lists_json):
            query['ContactWhiteListsJson'] = request.contact_white_lists_json
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactWhiteList',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_contact_white_list(
        self,
        request: main_models.SaveContactWhiteListRequest,
    ) -> main_models.SaveContactWhiteListResponse:
        runtime = RuntimeOptions()
        return self.save_contact_white_list_with_options(request, runtime)

    async def save_contact_white_list_async(
        self,
        request: main_models.SaveContactWhiteListRequest,
    ) -> main_models.SaveContactWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.save_contact_white_list_with_options_async(request, runtime)

    def save_effective_days_with_options(
        self,
        request: main_models.SaveEffectiveDaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveEffectiveDaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_days):
            query['EffectiveDays'] = request.effective_days
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveEffectiveDays',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveEffectiveDaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_effective_days_with_options_async(
        self,
        request: main_models.SaveEffectiveDaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveEffectiveDaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_days):
            query['EffectiveDays'] = request.effective_days
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveEffectiveDays',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveEffectiveDaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_effective_days(
        self,
        request: main_models.SaveEffectiveDaysRequest,
    ) -> main_models.SaveEffectiveDaysResponse:
        runtime = RuntimeOptions()
        return self.save_effective_days_with_options(request, runtime)

    async def save_effective_days_async(
        self,
        request: main_models.SaveEffectiveDaysRequest,
    ) -> main_models.SaveEffectiveDaysResponse:
        runtime = RuntimeOptions()
        return await self.save_effective_days_with_options_async(request, runtime)

    def save_max_attempts_per_day_with_options(
        self,
        request: main_models.SaveMaxAttemptsPerDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMaxAttemptsPerDayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.max_attempts_per_day):
            query['MaxAttemptsPerDay'] = request.max_attempts_per_day
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveMaxAttemptsPerDay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMaxAttemptsPerDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_max_attempts_per_day_with_options_async(
        self,
        request: main_models.SaveMaxAttemptsPerDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMaxAttemptsPerDayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.max_attempts_per_day):
            query['MaxAttemptsPerDay'] = request.max_attempts_per_day
        if not DaraCore.is_null(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveMaxAttemptsPerDay',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMaxAttemptsPerDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_max_attempts_per_day(
        self,
        request: main_models.SaveMaxAttemptsPerDayRequest,
    ) -> main_models.SaveMaxAttemptsPerDayResponse:
        runtime = RuntimeOptions()
        return self.save_max_attempts_per_day_with_options(request, runtime)

    async def save_max_attempts_per_day_async(
        self,
        request: main_models.SaveMaxAttemptsPerDayRequest,
    ) -> main_models.SaveMaxAttemptsPerDayResponse:
        runtime = RuntimeOptions()
        return await self.save_max_attempts_per_day_with_options_async(request, runtime)

    def search_task_with_options(
        self,
        request: main_models.SearchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_task_with_options_async(
        self,
        request: main_models.SearchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTask',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_task(
        self,
        request: main_models.SearchTaskRequest,
    ) -> main_models.SearchTaskResponse:
        runtime = RuntimeOptions()
        return self.search_task_with_options(request, runtime)

    async def search_task_async(
        self,
        request: main_models.SearchTaskRequest,
    ) -> main_models.SearchTaskResponse:
        runtime = RuntimeOptions()
        return await self.search_task_with_options_async(request, runtime)

    def start_job_with_options(
        self,
        request: main_models.StartJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_json):
            query['JobJson'] = request.job_json
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartJob',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_options_async(
        self,
        request: main_models.StartJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_json):
            query['JobJson'] = request.job_json
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartJob',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job(
        self,
        request: main_models.StartJobRequest,
    ) -> main_models.StartJobResponse:
        runtime = RuntimeOptions()
        return self.start_job_with_options(request, runtime)

    async def start_job_async(
        self,
        request: main_models.StartJobRequest,
    ) -> main_models.StartJobResponse:
        runtime = RuntimeOptions()
        return await self.start_job_with_options_async(request, runtime)

    def submit_batch_jobs_with_options(
        self,
        request: main_models.SubmitBatchJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitBatchJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitBatchJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitBatchJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_batch_jobs_with_options_async(
        self,
        request: main_models.SubmitBatchJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitBatchJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitBatchJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitBatchJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_batch_jobs(
        self,
        request: main_models.SubmitBatchJobsRequest,
    ) -> main_models.SubmitBatchJobsResponse:
        runtime = RuntimeOptions()
        return self.submit_batch_jobs_with_options(request, runtime)

    async def submit_batch_jobs_async(
        self,
        request: main_models.SubmitBatchJobsRequest,
    ) -> main_models.SubmitBatchJobsResponse:
        runtime = RuntimeOptions()
        return await self.submit_batch_jobs_with_options_async(request, runtime)

    def submit_recording_with_options(
        self,
        request: main_models.SubmitRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.merged_recording):
            query['MergedRecording'] = request.merged_recording
        if not DaraCore.is_null(request.resource_recording):
            query['ResourceRecording'] = request.resource_recording
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_recording_with_options_async(
        self,
        request: main_models.SubmitRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.merged_recording):
            query['MergedRecording'] = request.merged_recording
        if not DaraCore.is_null(request.resource_recording):
            query['ResourceRecording'] = request.resource_recording
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_recording(
        self,
        request: main_models.SubmitRecordingRequest,
    ) -> main_models.SubmitRecordingResponse:
        runtime = RuntimeOptions()
        return self.submit_recording_with_options(request, runtime)

    async def submit_recording_async(
        self,
        request: main_models.SubmitRecordingRequest,
    ) -> main_models.SubmitRecordingResponse:
        runtime = RuntimeOptions()
        return await self.submit_recording_with_options_async(request, runtime)

    def submit_script_review_with_options(
        self,
        request: main_models.SubmitScriptReviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitScriptReviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitScriptReview',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitScriptReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_script_review_with_options_async(
        self,
        request: main_models.SubmitScriptReviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitScriptReviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitScriptReview',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitScriptReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_script_review(
        self,
        request: main_models.SubmitScriptReviewRequest,
    ) -> main_models.SubmitScriptReviewResponse:
        runtime = RuntimeOptions()
        return self.submit_script_review_with_options(request, runtime)

    async def submit_script_review_async(
        self,
        request: main_models.SubmitScriptReviewRequest,
    ) -> main_models.SubmitScriptReviewResponse:
        runtime = RuntimeOptions()
        return await self.submit_script_review_with_options_async(request, runtime)

    def suspend_call_with_options(
        self,
        request: main_models.SuspendCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_numbers):
            query['CalledNumbers'] = request.called_numbers
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendCall',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_call_with_options_async(
        self,
        request: main_models.SuspendCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_numbers):
            query['CalledNumbers'] = request.called_numbers
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendCall',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_call(
        self,
        request: main_models.SuspendCallRequest,
    ) -> main_models.SuspendCallResponse:
        runtime = RuntimeOptions()
        return self.suspend_call_with_options(request, runtime)

    async def suspend_call_async(
        self,
        request: main_models.SuspendCallRequest,
    ) -> main_models.SuspendCallResponse:
        runtime = RuntimeOptions()
        return await self.suspend_call_with_options_async(request, runtime)

    def suspend_call_with_file_with_options(
        self,
        request: main_models.SuspendCallWithFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendCallWithFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendCallWithFile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendCallWithFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_call_with_file_with_options_async(
        self,
        request: main_models.SuspendCallWithFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendCallWithFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendCallWithFile',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendCallWithFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_call_with_file(
        self,
        request: main_models.SuspendCallWithFileRequest,
    ) -> main_models.SuspendCallWithFileResponse:
        runtime = RuntimeOptions()
        return self.suspend_call_with_file_with_options(request, runtime)

    async def suspend_call_with_file_async(
        self,
        request: main_models.SuspendCallWithFileRequest,
    ) -> main_models.SuspendCallWithFileResponse:
        runtime = RuntimeOptions()
        return await self.suspend_call_with_file_with_options_async(request, runtime)

    def suspend_jobs_with_options(
        self,
        request: main_models.SuspendJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_jobs_with_options_async(
        self,
        request: main_models.SuspendJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendJobs',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_jobs(
        self,
        request: main_models.SuspendJobsRequest,
    ) -> main_models.SuspendJobsResponse:
        runtime = RuntimeOptions()
        return self.suspend_jobs_with_options(request, runtime)

    async def suspend_jobs_async(
        self,
        request: main_models.SuspendJobsRequest,
    ) -> main_models.SuspendJobsResponse:
        runtime = RuntimeOptions()
        return await self.suspend_jobs_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def task_preparing_with_options(
        self,
        request: main_models.TaskPreparingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskPreparingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskPreparing',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskPreparingResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_preparing_with_options_async(
        self,
        request: main_models.TaskPreparingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskPreparingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskPreparing',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskPreparingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_preparing(
        self,
        request: main_models.TaskPreparingRequest,
    ) -> main_models.TaskPreparingResponse:
        runtime = RuntimeOptions()
        return self.task_preparing_with_options(request, runtime)

    async def task_preparing_async(
        self,
        request: main_models.TaskPreparingRequest,
    ) -> main_models.TaskPreparingResponse:
        runtime = RuntimeOptions()
        return await self.task_preparing_with_options_async(request, runtime)

    def terminate_call_with_options(
        self,
        request: main_models.TerminateCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateCall',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_call_with_options_async(
        self,
        request: main_models.TerminateCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateCall',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_call(
        self,
        request: main_models.TerminateCallRequest,
    ) -> main_models.TerminateCallResponse:
        runtime = RuntimeOptions()
        return self.terminate_call_with_options(request, runtime)

    async def terminate_call_async(
        self,
        request: main_models.TerminateCallRequest,
    ) -> main_models.TerminateCallResponse:
        runtime = RuntimeOptions()
        return await self.terminate_call_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upload_script_recording_with_options(
        self,
        request: main_models.UploadScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_script_recording_with_options_async(
        self,
        request: main_models.UploadScriptRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadScriptRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadScriptRecording',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_script_recording(
        self,
        request: main_models.UploadScriptRecordingRequest,
    ) -> main_models.UploadScriptRecordingResponse:
        runtime = RuntimeOptions()
        return self.upload_script_recording_with_options(request, runtime)

    async def upload_script_recording_async(
        self,
        request: main_models.UploadScriptRecordingRequest,
    ) -> main_models.UploadScriptRecordingResponse:
        runtime = RuntimeOptions()
        return await self.upload_script_recording_with_options_async(request, runtime)

    def withdraw_script_review_with_options(
        self,
        request: main_models.WithdrawScriptReviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawScriptReviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawScriptReview',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawScriptReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_script_review_with_options_async(
        self,
        request: main_models.WithdrawScriptReviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawScriptReviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawScriptReview',
            version = '2019-12-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawScriptReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_script_review(
        self,
        request: main_models.WithdrawScriptReviewRequest,
    ) -> main_models.WithdrawScriptReviewResponse:
        runtime = RuntimeOptions()
        return self.withdraw_script_review_with_options(request, runtime)

    async def withdraw_script_review_async(
        self,
        request: main_models.WithdrawScriptReviewRequest,
    ) -> main_models.WithdrawScriptReviewResponse:
        runtime = RuntimeOptions()
        return await self.withdraw_script_review_with_options_async(request, runtime)
