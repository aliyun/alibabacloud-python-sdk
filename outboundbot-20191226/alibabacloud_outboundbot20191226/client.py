# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_outboundbot20191226 import models as outbound_bot_20191226_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_number_district_info_parsing_result_with_options(
        self,
        request: outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultResponse:
        """
        @summary 生效号码库解析结果
        
        @param request: ApplyNumberDistrictInfoParsingResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyNumberDistrictInfoParsingResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyNumberDistrictInfoParsingResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_number_district_info_parsing_result_with_options_async(
        self,
        request: outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultResponse:
        """
        @summary 生效号码库解析结果
        
        @param request: ApplyNumberDistrictInfoParsingResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyNumberDistrictInfoParsingResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyNumberDistrictInfoParsingResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_number_district_info_parsing_result(
        self,
        request: outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultRequest,
    ) -> outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultResponse:
        """
        @summary 生效号码库解析结果
        
        @param request: ApplyNumberDistrictInfoParsingResultRequest
        @return: ApplyNumberDistrictInfoParsingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_number_district_info_parsing_result_with_options(request, runtime)

    async def apply_number_district_info_parsing_result_async(
        self,
        request: outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultRequest,
    ) -> outbound_bot_20191226_models.ApplyNumberDistrictInfoParsingResultResponse:
        """
        @summary 生效号码库解析结果
        
        @param request: ApplyNumberDistrictInfoParsingResultRequest
        @return: ApplyNumberDistrictInfoParsingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_number_district_info_parsing_result_with_options_async(request, runtime)

    def assign_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        """
        @summary 创建外呼任务
        
        @param request: AssignJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_asynchrony):
            query['IsAsynchrony'] = request.is_asynchrony
        if not UtilClient.is_unset(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.jobs_json):
            query['JobsJson'] = request.jobs_json
        if not UtilClient.is_unset(request.roster_type):
            query['RosterType'] = request.roster_type
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.AssignJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        """
        @summary 创建外呼任务
        
        @param request: AssignJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_asynchrony):
            query['IsAsynchrony'] = request.is_asynchrony
        if not UtilClient.is_unset(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.jobs_json):
            query['JobsJson'] = request.jobs_json
        if not UtilClient.is_unset(request.roster_type):
            query['RosterType'] = request.roster_type
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.AssignJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_jobs(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        """
        @summary 创建外呼任务
        
        @param request: AssignJobsRequest
        @return: AssignJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_jobs_with_options(request, runtime)

    async def assign_jobs_async(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        """
        @summary 创建外呼任务
        
        @param request: AssignJobsRequest
        @return: AssignJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_jobs_with_options_async(request, runtime)

    def assign_jobs_async_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.AssignJobsAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.AssignJobsAsyncResponse:
        """
        @summary 异步创建外呼任务
        
        @param tmp_req: AssignJobsAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignJobsAsyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.AssignJobsAsyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.calling_number):
            request.calling_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.calling_number, 'CallingNumber', 'json')
        if not UtilClient.is_unset(tmp_req.jobs_json):
            request.jobs_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.jobs_json, 'JobsJson', 'json')
        body = {}
        if not UtilClient.is_unset(request.calling_number_shrink):
            body['CallingNumber'] = request.calling_number_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            body['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.jobs_json_shrink):
            body['JobsJson'] = request.jobs_json_shrink
        if not UtilClient.is_unset(request.strategy_json):
            body['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignJobsAsync',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.AssignJobsAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_jobs_async_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.AssignJobsAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.AssignJobsAsyncResponse:
        """
        @summary 异步创建外呼任务
        
        @param tmp_req: AssignJobsAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignJobsAsyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.AssignJobsAsyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.calling_number):
            request.calling_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.calling_number, 'CallingNumber', 'json')
        if not UtilClient.is_unset(tmp_req.jobs_json):
            request.jobs_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.jobs_json, 'JobsJson', 'json')
        body = {}
        if not UtilClient.is_unset(request.calling_number_shrink):
            body['CallingNumber'] = request.calling_number_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            body['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.jobs_json_shrink):
            body['JobsJson'] = request.jobs_json_shrink
        if not UtilClient.is_unset(request.strategy_json):
            body['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignJobsAsync',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.AssignJobsAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_jobs_async(
        self,
        request: outbound_bot_20191226_models.AssignJobsAsyncRequest,
    ) -> outbound_bot_20191226_models.AssignJobsAsyncResponse:
        """
        @summary 异步创建外呼任务
        
        @param request: AssignJobsAsyncRequest
        @return: AssignJobsAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_jobs_async_with_options(request, runtime)

    async def assign_jobs_async_async(
        self,
        request: outbound_bot_20191226_models.AssignJobsAsyncRequest,
    ) -> outbound_bot_20191226_models.AssignJobsAsyncResponse:
        """
        @summary 异步创建外呼任务
        
        @param request: AssignJobsAsyncRequest
        @return: AssignJobsAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_jobs_async_with_options_async(request, runtime)

    def cancel_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        """
        @param request: CancelJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CancelJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        """
        @param request: CancelJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CancelJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_jobs(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        """
        @param request: CancelJobsRequest
        @return: CancelJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_jobs_with_options(request, runtime)

    async def cancel_jobs_async(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        """
        @param request: CancelJobsRequest
        @return: CancelJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_jobs_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: outbound_bot_20191226_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ChangeResourceGroupResponse:
        """
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ChangeResourceGroupResponse:
        """
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: outbound_bot_20191226_models.ChangeResourceGroupRequest,
    ) -> outbound_bot_20191226_models.ChangeResourceGroupResponse:
        """
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: outbound_bot_20191226_models.ChangeResourceGroupRequest,
    ) -> outbound_bot_20191226_models.ChangeResourceGroupResponse:
        """
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_agent_profile_with_options(
        self,
        request: outbound_bot_20191226_models.CreateAgentProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateAgentProfileResponse:
        """
        @param request: CreateAgentProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentProfileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.faq_category_ids):
            body['FaqCategoryIds'] = request.faq_category_ids
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not UtilClient.is_unset(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not UtilClient.is_unset(request.scenario):
            body['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.script_id):
            body['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAgentProfile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateAgentProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_profile_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateAgentProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateAgentProfileResponse:
        """
        @param request: CreateAgentProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentProfileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.faq_category_ids):
            body['FaqCategoryIds'] = request.faq_category_ids
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not UtilClient.is_unset(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not UtilClient.is_unset(request.scenario):
            body['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.script_id):
            body['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAgentProfile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateAgentProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_profile(
        self,
        request: outbound_bot_20191226_models.CreateAgentProfileRequest,
    ) -> outbound_bot_20191226_models.CreateAgentProfileResponse:
        """
        @param request: CreateAgentProfileRequest
        @return: CreateAgentProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_agent_profile_with_options(request, runtime)

    async def create_agent_profile_async(
        self,
        request: outbound_bot_20191226_models.CreateAgentProfileRequest,
    ) -> outbound_bot_20191226_models.CreateAgentProfileResponse:
        """
        @param request: CreateAgentProfileRequest
        @return: CreateAgentProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_agent_profile_with_options_async(request, runtime)

    def create_annotation_mission_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.CreateAnnotationMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateAnnotationMissionResponse:
        """
        @param tmp_req: CreateAnnotationMissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnnotationMissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateAnnotationMissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.annotation_mission_debug_data_source_list):
            request.annotation_mission_debug_data_source_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.annotation_mission_debug_data_source_list, 'AnnotationMissionDebugDataSourceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not UtilClient.is_unset(request.annotation_mission_debug_data_source_list_shrink):
            query['AnnotationMissionDebugDataSourceList'] = request.annotation_mission_debug_data_source_list_shrink
        if not UtilClient.is_unset(request.annotation_mission_debug_data_source_list_json_string):
            query['AnnotationMissionDebugDataSourceListJsonString'] = request.annotation_mission_debug_data_source_list_json_string
        if not UtilClient.is_unset(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.conversation_time_end_filter):
            query['ConversationTimeEndFilter'] = request.conversation_time_end_filter
        if not UtilClient.is_unset(request.conversation_time_start_filter):
            query['ConversationTimeStartFilter'] = request.conversation_time_start_filter
        if not UtilClient.is_unset(request.exclude_other_session):
            query['ExcludeOtherSession'] = request.exclude_other_session
        if not UtilClient.is_unset(request.finished):
            query['Finished'] = request.finished
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sampling_count):
            query['SamplingCount'] = request.sampling_count
        if not UtilClient.is_unset(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not UtilClient.is_unset(request.sampling_type):
            query['SamplingType'] = request.sampling_type
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.session_end_reason_filter_list):
            query['SessionEndReasonFilterList'] = request.session_end_reason_filter_list
        if not UtilClient.is_unset(request.session_end_reason_filter_list_json_string):
            query['SessionEndReasonFilterListJsonString'] = request.session_end_reason_filter_list_json_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAnnotationMission',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateAnnotationMissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_annotation_mission_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.CreateAnnotationMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateAnnotationMissionResponse:
        """
        @param tmp_req: CreateAnnotationMissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnnotationMissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateAnnotationMissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.annotation_mission_debug_data_source_list):
            request.annotation_mission_debug_data_source_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.annotation_mission_debug_data_source_list, 'AnnotationMissionDebugDataSourceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not UtilClient.is_unset(request.annotation_mission_debug_data_source_list_shrink):
            query['AnnotationMissionDebugDataSourceList'] = request.annotation_mission_debug_data_source_list_shrink
        if not UtilClient.is_unset(request.annotation_mission_debug_data_source_list_json_string):
            query['AnnotationMissionDebugDataSourceListJsonString'] = request.annotation_mission_debug_data_source_list_json_string
        if not UtilClient.is_unset(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.conversation_time_end_filter):
            query['ConversationTimeEndFilter'] = request.conversation_time_end_filter
        if not UtilClient.is_unset(request.conversation_time_start_filter):
            query['ConversationTimeStartFilter'] = request.conversation_time_start_filter
        if not UtilClient.is_unset(request.exclude_other_session):
            query['ExcludeOtherSession'] = request.exclude_other_session
        if not UtilClient.is_unset(request.finished):
            query['Finished'] = request.finished
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sampling_count):
            query['SamplingCount'] = request.sampling_count
        if not UtilClient.is_unset(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not UtilClient.is_unset(request.sampling_type):
            query['SamplingType'] = request.sampling_type
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.session_end_reason_filter_list):
            query['SessionEndReasonFilterList'] = request.session_end_reason_filter_list
        if not UtilClient.is_unset(request.session_end_reason_filter_list_json_string):
            query['SessionEndReasonFilterListJsonString'] = request.session_end_reason_filter_list_json_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAnnotationMission',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateAnnotationMissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_annotation_mission(
        self,
        request: outbound_bot_20191226_models.CreateAnnotationMissionRequest,
    ) -> outbound_bot_20191226_models.CreateAnnotationMissionResponse:
        """
        @param request: CreateAnnotationMissionRequest
        @return: CreateAnnotationMissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_annotation_mission_with_options(request, runtime)

    async def create_annotation_mission_async(
        self,
        request: outbound_bot_20191226_models.CreateAnnotationMissionRequest,
    ) -> outbound_bot_20191226_models.CreateAnnotationMissionResponse:
        """
        @param request: CreateAnnotationMissionRequest
        @return: CreateAnnotationMissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_annotation_mission_with_options_async(request, runtime)

    def create_batch_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        """
        @param request: CreateBatchJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_job_description):
            query['BatchJobDescription'] = request.batch_job_description
        if not UtilClient.is_unset(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not UtilClient.is_unset(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBatchJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        """
        @param request: CreateBatchJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_job_description):
            query['BatchJobDescription'] = request.batch_job_description
        if not UtilClient.is_unset(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not UtilClient.is_unset(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBatchJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_jobs(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        """
        @param request: CreateBatchJobsRequest
        @return: CreateBatchJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_batch_jobs_with_options(request, runtime)

    async def create_batch_jobs_async(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        """
        @param request: CreateBatchJobsRequest
        @return: CreateBatchJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_jobs_with_options_async(request, runtime)

    def create_batch_repeat_job_with_options(
        self,
        request: outbound_bot_20191226_models.CreateBatchRepeatJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBatchRepeatJobResponse:
        """
        @summary CreateBatchRepeatJob
        
        @param request: CreateBatchRepeatJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchRepeatJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.filter_status):
            query['FilterStatus'] = request.filter_status
        if not UtilClient.is_unset(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not UtilClient.is_unset(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not UtilClient.is_unset(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.source_group_id):
            query['SourceGroupId'] = request.source_group_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchRepeatJob',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBatchRepeatJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_repeat_job_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateBatchRepeatJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBatchRepeatJobResponse:
        """
        @summary CreateBatchRepeatJob
        
        @param request: CreateBatchRepeatJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchRepeatJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.filter_status):
            query['FilterStatus'] = request.filter_status
        if not UtilClient.is_unset(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not UtilClient.is_unset(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not UtilClient.is_unset(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.source_group_id):
            query['SourceGroupId'] = request.source_group_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchRepeatJob',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBatchRepeatJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_repeat_job(
        self,
        request: outbound_bot_20191226_models.CreateBatchRepeatJobRequest,
    ) -> outbound_bot_20191226_models.CreateBatchRepeatJobResponse:
        """
        @summary CreateBatchRepeatJob
        
        @param request: CreateBatchRepeatJobRequest
        @return: CreateBatchRepeatJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_batch_repeat_job_with_options(request, runtime)

    async def create_batch_repeat_job_async(
        self,
        request: outbound_bot_20191226_models.CreateBatchRepeatJobRequest,
    ) -> outbound_bot_20191226_models.CreateBatchRepeatJobResponse:
        """
        @summary CreateBatchRepeatJob
        
        @param request: CreateBatchRepeatJobRequest
        @return: CreateBatchRepeatJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_repeat_job_with_options_async(request, runtime)

    def create_beebot_intent_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.CreateBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentResponse:
        """
        @summary CreateBeebotIntent
        
        @param tmp_req: CreateBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBeebotIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateBeebotIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_beebot_intent_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.CreateBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentResponse:
        """
        @summary CreateBeebotIntent
        
        @param tmp_req: CreateBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBeebotIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateBeebotIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_beebot_intent(
        self,
        request: outbound_bot_20191226_models.CreateBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentResponse:
        """
        @summary CreateBeebotIntent
        
        @param request: CreateBeebotIntentRequest
        @return: CreateBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_beebot_intent_with_options(request, runtime)

    async def create_beebot_intent_async(
        self,
        request: outbound_bot_20191226_models.CreateBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentResponse:
        """
        @summary CreateBeebotIntent
        
        @param request: CreateBeebotIntentRequest
        @return: CreateBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_beebot_intent_with_options_async(request, runtime)

    def create_beebot_intent_lgf_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.CreateBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentLgfResponse:
        """
        @summary CreateBeebotIntentLgf
        
        @param tmp_req: CreateBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBeebotIntentLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateBeebotIntentLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_beebot_intent_lgf_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.CreateBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentLgfResponse:
        """
        @summary CreateBeebotIntentLgf
        
        @param tmp_req: CreateBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBeebotIntentLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateBeebotIntentLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_beebot_intent_lgf(
        self,
        request: outbound_bot_20191226_models.CreateBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentLgfResponse:
        """
        @summary CreateBeebotIntentLgf
        
        @param request: CreateBeebotIntentLgfRequest
        @return: CreateBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_beebot_intent_lgf_with_options(request, runtime)

    async def create_beebot_intent_lgf_async(
        self,
        request: outbound_bot_20191226_models.CreateBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentLgfResponse:
        """
        @summary CreateBeebotIntentLgf
        
        @param request: CreateBeebotIntentLgfRequest
        @return: CreateBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_beebot_intent_lgf_with_options_async(request, runtime)

    def create_beebot_intent_user_say_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.CreateBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentUserSayResponse:
        """
        @summary CreateBeebotIntentUserSay
        
        @param tmp_req: CreateBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateBeebotIntentUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_beebot_intent_user_say_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.CreateBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentUserSayResponse:
        """
        @summary CreateBeebotIntentUserSay
        
        @param tmp_req: CreateBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.CreateBeebotIntentUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_beebot_intent_user_say(
        self,
        request: outbound_bot_20191226_models.CreateBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentUserSayResponse:
        """
        @summary CreateBeebotIntentUserSay
        
        @param request: CreateBeebotIntentUserSayRequest
        @return: CreateBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_beebot_intent_user_say_with_options(request, runtime)

    async def create_beebot_intent_user_say_async(
        self,
        request: outbound_bot_20191226_models.CreateBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.CreateBeebotIntentUserSayResponse:
        """
        @summary CreateBeebotIntentUserSay
        
        @param request: CreateBeebotIntentUserSayRequest
        @return: CreateBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_beebot_intent_user_say_with_options_async(request, runtime)

    def create_dialogue_flow_with_options(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        """
        @param request: CreateDialogueFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDialogueFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dialogue_flow_type):
            query['DialogueFlowType'] = request.dialogue_flow_type
        if not UtilClient.is_unset(request.dialogue_name):
            query['DialogueName'] = request.dialogue_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDialogueFlow',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateDialogueFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialogue_flow_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        """
        @param request: CreateDialogueFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDialogueFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dialogue_flow_type):
            query['DialogueFlowType'] = request.dialogue_flow_type
        if not UtilClient.is_unset(request.dialogue_name):
            query['DialogueName'] = request.dialogue_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDialogueFlow',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateDialogueFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialogue_flow(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        """
        @param request: CreateDialogueFlowRequest
        @return: CreateDialogueFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dialogue_flow_with_options(request, runtime)

    async def create_dialogue_flow_async(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        """
        @param request: CreateDialogueFlowRequest
        @return: CreateDialogueFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dialogue_flow_with_options_async(request, runtime)

    def create_download_url_with_options(
        self,
        request: outbound_bot_20191226_models.CreateDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownloadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_download_url_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownloadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_download_url(
        self,
        request: outbound_bot_20191226_models.CreateDownloadUrlRequest,
    ) -> outbound_bot_20191226_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @return: CreateDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_download_url_with_options(request, runtime)

    async def create_download_url_async(
        self,
        request: outbound_bot_20191226_models.CreateDownloadUrlRequest,
    ) -> outbound_bot_20191226_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @return: CreateDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_download_url_with_options_async(request, runtime)

    def create_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        """
        @param request: CreateGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.answers):
            query['Answers'] = request.answers
        if not UtilClient.is_unset(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not UtilClient.is_unset(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.questions):
            query['Questions'] = request.questions
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        """
        @param request: CreateGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.answers):
            query['Answers'] = request.answers
        if not UtilClient.is_unset(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not UtilClient.is_unset(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.questions):
            query['Questions'] = request.questions
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_question(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        """
        @param request: CreateGlobalQuestionRequest
        @return: CreateGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_global_question_with_options(request, runtime)

    async def create_global_question_async(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        """
        @param request: CreateGlobalQuestionRequest
        @return: CreateGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_global_question_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        if not UtilClient.is_unset(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        if not UtilClient.is_unset(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instance_bind_number_with_options(
        self,
        request: outbound_bot_20191226_models.CreateInstanceBindNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateInstanceBindNumberResponse:
        """
        @summary 创建实例绑定号码
        
        @param request: CreateInstanceBindNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceBindNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceBindNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateInstanceBindNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_bind_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateInstanceBindNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateInstanceBindNumberResponse:
        """
        @summary 创建实例绑定号码
        
        @param request: CreateInstanceBindNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceBindNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceBindNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateInstanceBindNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_bind_number(
        self,
        request: outbound_bot_20191226_models.CreateInstanceBindNumberRequest,
    ) -> outbound_bot_20191226_models.CreateInstanceBindNumberResponse:
        """
        @summary 创建实例绑定号码
        
        @param request: CreateInstanceBindNumberRequest
        @return: CreateInstanceBindNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_bind_number_with_options(request, runtime)

    async def create_instance_bind_number_async(
        self,
        request: outbound_bot_20191226_models.CreateInstanceBindNumberRequest,
    ) -> outbound_bot_20191226_models.CreateInstanceBindNumberResponse:
        """
        @summary 创建实例绑定号码
        
        @param request: CreateInstanceBindNumberRequest
        @return: CreateInstanceBindNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_bind_number_with_options_async(request, runtime)

    def create_intent_with_options(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        """
        @param request: CreateIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        """
        @param request: CreateIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intent(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        """
        @param request: CreateIntentRequest
        @return: CreateIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    async def create_intent_async(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        """
        @param request: CreateIntentRequest
        @return: CreateIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_intent_with_options_async(request, runtime)

    def create_job_data_parsing_task_with_options(
        self,
        request: outbound_bot_20191226_models.CreateJobDataParsingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobDataParsingTaskResponse:
        """
        @param request: CreateJobDataParsingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobDataParsingTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobDataParsingTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobDataParsingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_data_parsing_task_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateJobDataParsingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobDataParsingTaskResponse:
        """
        @param request: CreateJobDataParsingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobDataParsingTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobDataParsingTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobDataParsingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_data_parsing_task(
        self,
        request: outbound_bot_20191226_models.CreateJobDataParsingTaskRequest,
    ) -> outbound_bot_20191226_models.CreateJobDataParsingTaskResponse:
        """
        @param request: CreateJobDataParsingTaskRequest
        @return: CreateJobDataParsingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_data_parsing_task_with_options(request, runtime)

    async def create_job_data_parsing_task_async(
        self,
        request: outbound_bot_20191226_models.CreateJobDataParsingTaskRequest,
    ) -> outbound_bot_20191226_models.CreateJobDataParsingTaskResponse:
        """
        @param request: CreateJobDataParsingTaskRequest
        @return: CreateJobDataParsingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_data_parsing_task_with_options_async(request, runtime)

    def create_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        """
        @param request: CreateJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_description):
            query['JobGroupDescription'] = request.job_group_description
        if not UtilClient.is_unset(request.job_group_name):
            query['JobGroupName'] = request.job_group_name
        if not UtilClient.is_unset(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not UtilClient.is_unset(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not UtilClient.is_unset(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        """
        @param request: CreateJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_description):
            query['JobGroupDescription'] = request.job_group_description
        if not UtilClient.is_unset(request.job_group_name):
            query['JobGroupName'] = request.job_group_name
        if not UtilClient.is_unset(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not UtilClient.is_unset(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not UtilClient.is_unset(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_group(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        """
        @param request: CreateJobGroupRequest
        @return: CreateJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_group_with_options(request, runtime)

    async def create_job_group_async(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        """
        @param request: CreateJobGroupRequest
        @return: CreateJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_group_with_options_async(request, runtime)

    def create_job_group_export_task_with_options(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobGroupExportTaskResponse:
        """
        @param request: CreateJobGroupExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobGroupExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobGroupExportTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobGroupExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_group_export_task_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobGroupExportTaskResponse:
        """
        @param request: CreateJobGroupExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobGroupExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobGroupExportTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobGroupExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_group_export_task(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupExportTaskRequest,
    ) -> outbound_bot_20191226_models.CreateJobGroupExportTaskResponse:
        """
        @param request: CreateJobGroupExportTaskRequest
        @return: CreateJobGroupExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_group_export_task_with_options(request, runtime)

    async def create_job_group_export_task_async(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupExportTaskRequest,
    ) -> outbound_bot_20191226_models.CreateJobGroupExportTaskResponse:
        """
        @param request: CreateJobGroupExportTaskRequest
        @return: CreateJobGroupExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_group_export_task_with_options_async(request, runtime)

    def create_number_district_info_download_url_with_options(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlResponse:
        """
        @summary 创建号码库下载链接
        
        @param request: CreateNumberDistrictInfoDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNumberDistrictInfoDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNumberDistrictInfoDownloadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_number_district_info_download_url_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlResponse:
        """
        @summary 创建号码库下载链接
        
        @param request: CreateNumberDistrictInfoDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNumberDistrictInfoDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNumberDistrictInfoDownloadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_number_district_info_download_url(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlRequest,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlResponse:
        """
        @summary 创建号码库下载链接
        
        @param request: CreateNumberDistrictInfoDownloadUrlRequest
        @return: CreateNumberDistrictInfoDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_number_district_info_download_url_with_options(request, runtime)

    async def create_number_district_info_download_url_async(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlRequest,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoDownloadUrlResponse:
        """
        @summary 创建号码库下载链接
        
        @param request: CreateNumberDistrictInfoDownloadUrlRequest
        @return: CreateNumberDistrictInfoDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_number_district_info_download_url_with_options_async(request, runtime)

    def create_number_district_info_parsing_task_with_options(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskResponse:
        """
        @summary 创建号码库解析任务
        
        @param request: CreateNumberDistrictInfoParsingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNumberDistrictInfoParsingTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNumberDistrictInfoParsingTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_number_district_info_parsing_task_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskResponse:
        """
        @summary 创建号码库解析任务
        
        @param request: CreateNumberDistrictInfoParsingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNumberDistrictInfoParsingTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNumberDistrictInfoParsingTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_number_district_info_parsing_task(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskRequest,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskResponse:
        """
        @summary 创建号码库解析任务
        
        @param request: CreateNumberDistrictInfoParsingTaskRequest
        @return: CreateNumberDistrictInfoParsingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_number_district_info_parsing_task_with_options(request, runtime)

    async def create_number_district_info_parsing_task_async(
        self,
        request: outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskRequest,
    ) -> outbound_bot_20191226_models.CreateNumberDistrictInfoParsingTaskResponse:
        """
        @summary 创建号码库解析任务
        
        @param request: CreateNumberDistrictInfoParsingTaskRequest
        @return: CreateNumberDistrictInfoParsingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_number_district_info_parsing_task_with_options_async(request, runtime)

    def create_outbound_call_number_with_options(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        """
        @summary CreateOutboundCallNumber
        
        @param request: CreateOutboundCallNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOutboundCallNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.rate_limit_count):
            query['RateLimitCount'] = request.rate_limit_count
        if not UtilClient.is_unset(request.rate_limit_period):
            query['RateLimitPeriod'] = request.rate_limit_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOutboundCallNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateOutboundCallNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_outbound_call_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        """
        @summary CreateOutboundCallNumber
        
        @param request: CreateOutboundCallNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOutboundCallNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.rate_limit_count):
            query['RateLimitCount'] = request.rate_limit_count
        if not UtilClient.is_unset(request.rate_limit_period):
            query['RateLimitPeriod'] = request.rate_limit_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOutboundCallNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateOutboundCallNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_outbound_call_number(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        """
        @summary CreateOutboundCallNumber
        
        @param request: CreateOutboundCallNumberRequest
        @return: CreateOutboundCallNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_outbound_call_number_with_options(request, runtime)

    async def create_outbound_call_number_async(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        """
        @summary CreateOutboundCallNumber
        
        @param request: CreateOutboundCallNumberRequest
        @return: CreateOutboundCallNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_outbound_call_number_with_options_async(request, runtime)

    def create_script_with_options(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        """
        @summary 新建场景
        
        @param request: CreateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not UtilClient.is_unset(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not UtilClient.is_unset(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not UtilClient.is_unset(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not UtilClient.is_unset(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_nlu_profile_json_string):
            query['ScriptNluProfileJsonString'] = request.script_nlu_profile_json_string
        if not UtilClient.is_unset(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not UtilClient.is_unset(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        """
        @summary 新建场景
        
        @param request: CreateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not UtilClient.is_unset(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not UtilClient.is_unset(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not UtilClient.is_unset(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not UtilClient.is_unset(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_nlu_profile_json_string):
            query['ScriptNluProfileJsonString'] = request.script_nlu_profile_json_string
        if not UtilClient.is_unset(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not UtilClient.is_unset(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        """
        @summary 新建场景
        
        @param request: CreateScriptRequest
        @return: CreateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_script_with_options(request, runtime)

    async def create_script_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        """
        @summary 新建场景
        
        @param request: CreateScriptRequest
        @return: CreateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_script_with_options_async(request, runtime)

    def create_script_waveform_with_options(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        """
        @param request: CreateScriptWaveformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScriptWaveformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScriptWaveform',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptWaveformResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_waveform_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        """
        @param request: CreateScriptWaveformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScriptWaveformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScriptWaveform',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptWaveformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script_waveform(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        """
        @param request: CreateScriptWaveformRequest
        @return: CreateScriptWaveformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_script_waveform_with_options(request, runtime)

    async def create_script_waveform_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        """
        @param request: CreateScriptWaveformRequest
        @return: CreateScriptWaveformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_script_waveform_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        """
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.tag_group):
            query['TagGroup'] = request.tag_group
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        """
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.tag_group):
            query['TagGroup'] = request.tag_group
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        """
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        """
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_task_export_task_with_options(
        self,
        request: outbound_bot_20191226_models.CreateTaskExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateTaskExportTaskResponse:
        """
        @summary 外呼历史导出
        
        @param request: CreateTaskExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskExportTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateTaskExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_export_task_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateTaskExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateTaskExportTaskResponse:
        """
        @summary 外呼历史导出
        
        @param request: CreateTaskExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskExportTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateTaskExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_export_task(
        self,
        request: outbound_bot_20191226_models.CreateTaskExportTaskRequest,
    ) -> outbound_bot_20191226_models.CreateTaskExportTaskResponse:
        """
        @summary 外呼历史导出
        
        @param request: CreateTaskExportTaskRequest
        @return: CreateTaskExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_task_export_task_with_options(request, runtime)

    async def create_task_export_task_async(
        self,
        request: outbound_bot_20191226_models.CreateTaskExportTaskRequest,
    ) -> outbound_bot_20191226_models.CreateTaskExportTaskResponse:
        """
        @summary 外呼历史导出
        
        @param request: CreateTaskExportTaskRequest
        @return: CreateTaskExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_task_export_task_with_options_async(request, runtime)

    def delete_agent_profiles_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.DeleteAgentProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteAgentProfilesResponse:
        """
        @param tmp_req: DeleteAgentProfilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentProfilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.DeleteAgentProfilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_profile_ids):
            request.agent_profile_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_profile_ids, 'AgentProfileIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_profile_ids_shrink):
            body['AgentProfileIds'] = request.agent_profile_ids_shrink
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAgentProfiles',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteAgentProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_profiles_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.DeleteAgentProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteAgentProfilesResponse:
        """
        @param tmp_req: DeleteAgentProfilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentProfilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.DeleteAgentProfilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_profile_ids):
            request.agent_profile_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_profile_ids, 'AgentProfileIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_profile_ids_shrink):
            body['AgentProfileIds'] = request.agent_profile_ids_shrink
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAgentProfiles',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteAgentProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_profiles(
        self,
        request: outbound_bot_20191226_models.DeleteAgentProfilesRequest,
    ) -> outbound_bot_20191226_models.DeleteAgentProfilesResponse:
        """
        @param request: DeleteAgentProfilesRequest
        @return: DeleteAgentProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_agent_profiles_with_options(request, runtime)

    async def delete_agent_profiles_async(
        self,
        request: outbound_bot_20191226_models.DeleteAgentProfilesRequest,
    ) -> outbound_bot_20191226_models.DeleteAgentProfilesResponse:
        """
        @param request: DeleteAgentProfilesRequest
        @return: DeleteAgentProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_agent_profiles_with_options_async(request, runtime)

    def delete_all_number_district_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteAllNumberDistrictInfoResponse:
        """
        @summary 清空归属地号码库
        
        @param request: DeleteAllNumberDistrictInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAllNumberDistrictInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DeleteAllNumberDistrictInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteAllNumberDistrictInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_number_district_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteAllNumberDistrictInfoResponse:
        """
        @summary 清空归属地号码库
        
        @param request: DeleteAllNumberDistrictInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAllNumberDistrictInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DeleteAllNumberDistrictInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteAllNumberDistrictInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_number_district_info(self) -> outbound_bot_20191226_models.DeleteAllNumberDistrictInfoResponse:
        """
        @summary 清空归属地号码库
        
        @return: DeleteAllNumberDistrictInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_all_number_district_info_with_options(runtime)

    async def delete_all_number_district_info_async(self) -> outbound_bot_20191226_models.DeleteAllNumberDistrictInfoResponse:
        """
        @summary 清空归属地号码库
        
        @return: DeleteAllNumberDistrictInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_all_number_district_info_with_options_async(runtime)

    def delete_beebot_intent_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentResponse:
        """
        @summary DeleteBeebotIntent
        
        @param request: DeleteBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBeebotIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_beebot_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentResponse:
        """
        @summary DeleteBeebotIntent
        
        @param request: DeleteBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBeebotIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_beebot_intent(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentResponse:
        """
        @summary DeleteBeebotIntent
        
        @param request: DeleteBeebotIntentRequest
        @return: DeleteBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_beebot_intent_with_options(request, runtime)

    async def delete_beebot_intent_async(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentResponse:
        """
        @summary DeleteBeebotIntent
        
        @param request: DeleteBeebotIntentRequest
        @return: DeleteBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_beebot_intent_with_options_async(request, runtime)

    def delete_beebot_intent_lgf_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentLgfResponse:
        """
        @summary DeleteBeebotIntentLgf
        
        @param request: DeleteBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBeebotIntentLgfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_beebot_intent_lgf_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentLgfResponse:
        """
        @summary DeleteBeebotIntentLgf
        
        @param request: DeleteBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBeebotIntentLgfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_beebot_intent_lgf(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentLgfResponse:
        """
        @summary DeleteBeebotIntentLgf
        
        @param request: DeleteBeebotIntentLgfRequest
        @return: DeleteBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_beebot_intent_lgf_with_options(request, runtime)

    async def delete_beebot_intent_lgf_async(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentLgfResponse:
        """
        @summary DeleteBeebotIntentLgf
        
        @param request: DeleteBeebotIntentLgfRequest
        @return: DeleteBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_beebot_intent_lgf_with_options_async(request, runtime)

    def delete_beebot_intent_user_say_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentUserSayResponse:
        """
        @summary DeleteBeebotIntentUserSay
        
        @param request: DeleteBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_beebot_intent_user_say_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentUserSayResponse:
        """
        @summary DeleteBeebotIntentUserSay
        
        @param request: DeleteBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_beebot_intent_user_say(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentUserSayResponse:
        """
        @summary DeleteBeebotIntentUserSay
        
        @param request: DeleteBeebotIntentUserSayRequest
        @return: DeleteBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_beebot_intent_user_say_with_options(request, runtime)

    async def delete_beebot_intent_user_say_async(
        self,
        request: outbound_bot_20191226_models.DeleteBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.DeleteBeebotIntentUserSayResponse:
        """
        @summary DeleteBeebotIntentUserSay
        
        @param request: DeleteBeebotIntentUserSayRequest
        @return: DeleteBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_beebot_intent_user_say_with_options_async(request, runtime)

    def delete_contact_block_list_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteContactBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteContactBlockListResponse:
        """
        @param request: DeleteContactBlockListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactBlockListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_block_list_id):
            query['ContactBlockListId'] = request.contact_block_list_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactBlockList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteContactBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_block_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteContactBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteContactBlockListResponse:
        """
        @param request: DeleteContactBlockListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactBlockListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_block_list_id):
            query['ContactBlockListId'] = request.contact_block_list_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactBlockList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteContactBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_block_list(
        self,
        request: outbound_bot_20191226_models.DeleteContactBlockListRequest,
    ) -> outbound_bot_20191226_models.DeleteContactBlockListResponse:
        """
        @param request: DeleteContactBlockListRequest
        @return: DeleteContactBlockListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_block_list_with_options(request, runtime)

    async def delete_contact_block_list_async(
        self,
        request: outbound_bot_20191226_models.DeleteContactBlockListRequest,
    ) -> outbound_bot_20191226_models.DeleteContactBlockListResponse:
        """
        @param request: DeleteContactBlockListRequest
        @return: DeleteContactBlockListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_block_list_with_options_async(request, runtime)

    def delete_contact_white_list_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteContactWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteContactWhiteListResponse:
        """
        @param request: DeleteContactWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_white_list_id):
            query['ContactWhiteListId'] = request.contact_white_list_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactWhiteList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteContactWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_white_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteContactWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteContactWhiteListResponse:
        """
        @param request: DeleteContactWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_white_list_id):
            query['ContactWhiteListId'] = request.contact_white_list_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactWhiteList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteContactWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_white_list(
        self,
        request: outbound_bot_20191226_models.DeleteContactWhiteListRequest,
    ) -> outbound_bot_20191226_models.DeleteContactWhiteListResponse:
        """
        @param request: DeleteContactWhiteListRequest
        @return: DeleteContactWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_white_list_with_options(request, runtime)

    async def delete_contact_white_list_async(
        self,
        request: outbound_bot_20191226_models.DeleteContactWhiteListRequest,
    ) -> outbound_bot_20191226_models.DeleteContactWhiteListResponse:
        """
        @param request: DeleteContactWhiteListRequest
        @return: DeleteContactWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_white_list_with_options_async(request, runtime)

    def delete_dialogue_flow_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        """
        @param request: DeleteDialogueFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDialogueFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDialogueFlow',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteDialogueFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dialogue_flow_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        """
        @param request: DeleteDialogueFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDialogueFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDialogueFlow',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteDialogueFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dialogue_flow(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        """
        @param request: DeleteDialogueFlowRequest
        @return: DeleteDialogueFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dialogue_flow_with_options(request, runtime)

    async def delete_dialogue_flow_async(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        """
        @param request: DeleteDialogueFlowRequest
        @return: DeleteDialogueFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dialogue_flow_with_options_async(request, runtime)

    def delete_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        """
        @param request: DeleteGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        """
        @param request: DeleteGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_question(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        """
        @param request: DeleteGlobalQuestionRequest
        @return: DeleteGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_global_question_with_options(request, runtime)

    async def delete_global_question_async(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        """
        @param request: DeleteGlobalQuestionRequest
        @return: DeleteGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_question_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_intent_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        """
        @param request: DeleteIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        """
        @param request: DeleteIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_intent(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        """
        @param request: DeleteIntentRequest
        @return: DeleteIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    async def delete_intent_async(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        """
        @param request: DeleteIntentRequest
        @return: DeleteIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_intent_with_options_async(request, runtime)

    def delete_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        """
        @param request: DeleteJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        """
        @param request: DeleteJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job_group(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        """
        @param request: DeleteJobGroupRequest
        @return: DeleteJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_job_group_with_options(request, runtime)

    async def delete_job_group_async(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        """
        @param request: DeleteJobGroupRequest
        @return: DeleteJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_group_with_options_async(request, runtime)

    def delete_outbound_call_number_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        """
        @param request: DeleteOutboundCallNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOutboundCallNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOutboundCallNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteOutboundCallNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_outbound_call_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        """
        @param request: DeleteOutboundCallNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOutboundCallNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOutboundCallNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteOutboundCallNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_outbound_call_number(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        """
        @param request: DeleteOutboundCallNumberRequest
        @return: DeleteOutboundCallNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_outbound_call_number_with_options(request, runtime)

    async def delete_outbound_call_number_async(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        """
        @param request: DeleteOutboundCallNumberRequest
        @return: DeleteOutboundCallNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_outbound_call_number_with_options_async(request, runtime)

    def delete_script_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @return: DeleteScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_script_with_options(request, runtime)

    async def delete_script_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @return: DeleteScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_script_with_options_async(request, runtime)

    def delete_script_recording_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptRecordingResponse:
        """
        @param request: DeleteScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptRecordingResponse:
        """
        @param request: DeleteScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script_recording(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptRecordingResponse:
        """
        @param request: DeleteScriptRecordingRequest
        @return: DeleteScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_script_recording_with_options(request, runtime)

    async def delete_script_recording_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptRecordingResponse:
        """
        @param request: DeleteScriptRecordingRequest
        @return: DeleteScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_script_recording_with_options_async(request, runtime)

    def delete_script_waveform_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        """
        @param request: DeleteScriptWaveformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptWaveformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_waveform_id):
            query['ScriptWaveformId'] = request.script_waveform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScriptWaveform',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptWaveformResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_waveform_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        """
        @param request: DeleteScriptWaveformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptWaveformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_waveform_id):
            query['ScriptWaveformId'] = request.script_waveform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScriptWaveform',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptWaveformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script_waveform(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        """
        @param request: DeleteScriptWaveformRequest
        @return: DeleteScriptWaveformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_script_waveform_with_options(request, runtime)

    async def delete_script_waveform_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        """
        @param request: DeleteScriptWaveformRequest
        @return: DeleteScriptWaveformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_script_waveform_with_options_async(request, runtime)

    def describe_beebot_intent_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeBeebotIntentResponse:
        """
        @summary DescribeBeebotIntent
        
        @description ***\
        
        @param request: DescribeBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBeebotIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_beebot_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeBeebotIntentResponse:
        """
        @summary DescribeBeebotIntent
        
        @description ***\
        
        @param request: DescribeBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBeebotIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_beebot_intent(
        self,
        request: outbound_bot_20191226_models.DescribeBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.DescribeBeebotIntentResponse:
        """
        @summary DescribeBeebotIntent
        
        @description ***\
        
        @param request: DescribeBeebotIntentRequest
        @return: DescribeBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_beebot_intent_with_options(request, runtime)

    async def describe_beebot_intent_async(
        self,
        request: outbound_bot_20191226_models.DescribeBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.DescribeBeebotIntentResponse:
        """
        @summary DescribeBeebotIntent
        
        @description ***\
        
        @param request: DescribeBeebotIntentRequest
        @return: DescribeBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_beebot_intent_with_options_async(request, runtime)

    def describe_dialogue_node_statistics_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeDialogueNodeStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeDialogueNodeStatisticsResponse:
        """
        @param request: DescribeDialogueNodeStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDialogueNodeStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialogueNodeStatistics',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeDialogueNodeStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dialogue_node_statistics_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeDialogueNodeStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeDialogueNodeStatisticsResponse:
        """
        @param request: DescribeDialogueNodeStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDialogueNodeStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialogueNodeStatistics',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeDialogueNodeStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dialogue_node_statistics(
        self,
        request: outbound_bot_20191226_models.DescribeDialogueNodeStatisticsRequest,
    ) -> outbound_bot_20191226_models.DescribeDialogueNodeStatisticsResponse:
        """
        @param request: DescribeDialogueNodeStatisticsRequest
        @return: DescribeDialogueNodeStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dialogue_node_statistics_with_options(request, runtime)

    async def describe_dialogue_node_statistics_async(
        self,
        request: outbound_bot_20191226_models.DescribeDialogueNodeStatisticsRequest,
    ) -> outbound_bot_20191226_models.DescribeDialogueNodeStatisticsResponse:
        """
        @param request: DescribeDialogueNodeStatisticsRequest
        @return: DescribeDialogueNodeStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dialogue_node_statistics_with_options_async(request, runtime)

    def describe_ds_reports_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeDsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeDsReportsResponse:
        """
        @summary DescribeDsReports
        
        @param request: DescribeDsReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDsReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDsReports',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeDsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ds_reports_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeDsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeDsReportsResponse:
        """
        @summary DescribeDsReports
        
        @param request: DescribeDsReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDsReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDsReports',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeDsReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ds_reports(
        self,
        request: outbound_bot_20191226_models.DescribeDsReportsRequest,
    ) -> outbound_bot_20191226_models.DescribeDsReportsResponse:
        """
        @summary DescribeDsReports
        
        @param request: DescribeDsReportsRequest
        @return: DescribeDsReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ds_reports_with_options(request, runtime)

    async def describe_ds_reports_async(
        self,
        request: outbound_bot_20191226_models.DescribeDsReportsRequest,
    ) -> outbound_bot_20191226_models.DescribeDsReportsResponse:
        """
        @summary DescribeDsReports
        
        @param request: DescribeDsReportsRequest
        @return: DescribeDsReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ds_reports_with_options_async(request, runtime)

    def describe_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        """
        @param request: DescribeGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        """
        @param request: DescribeGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_question(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        """
        @param request: DescribeGlobalQuestionRequest
        @return: DescribeGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_question_with_options(request, runtime)

    async def describe_global_question_async(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        """
        @param request: DescribeGlobalQuestionRequest
        @return: DescribeGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_question_with_options_async(request, runtime)

    def describe_group_executing_info_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeGroupExecutingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeGroupExecutingInfoResponse:
        """
        @param request: DescribeGroupExecutingInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupExecutingInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupExecutingInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeGroupExecutingInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_executing_info_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeGroupExecutingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeGroupExecutingInfoResponse:
        """
        @param request: DescribeGroupExecutingInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupExecutingInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupExecutingInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeGroupExecutingInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_executing_info(
        self,
        request: outbound_bot_20191226_models.DescribeGroupExecutingInfoRequest,
    ) -> outbound_bot_20191226_models.DescribeGroupExecutingInfoResponse:
        """
        @param request: DescribeGroupExecutingInfoRequest
        @return: DescribeGroupExecutingInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_executing_info_with_options(request, runtime)

    async def describe_group_executing_info_async(
        self,
        request: outbound_bot_20191226_models.DescribeGroupExecutingInfoRequest,
    ) -> outbound_bot_20191226_models.DescribeGroupExecutingInfoResponse:
        """
        @param request: DescribeGroupExecutingInfoRequest
        @return: DescribeGroupExecutingInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_group_executing_info_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        """
        @summary DescribeInstance
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        """
        @summary DescribeInstance
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        """
        @summary DescribeInstance
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        """
        @summary DescribeInstance
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_intent_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        """
        @param request: DescribeIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        """
        @param request: DescribeIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intent(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        """
        @param request: DescribeIntentRequest
        @return: DescribeIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    async def describe_intent_async(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        """
        @param request: DescribeIntentRequest
        @return: DescribeIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_intent_with_options_async(request, runtime)

    def describe_intent_statistics_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeIntentStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeIntentStatisticsResponse:
        """
        @param request: DescribeIntentStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntentStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntentStatistics',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeIntentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intent_statistics_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeIntentStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeIntentStatisticsResponse:
        """
        @param request: DescribeIntentStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntentStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntentStatistics',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeIntentStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intent_statistics(
        self,
        request: outbound_bot_20191226_models.DescribeIntentStatisticsRequest,
    ) -> outbound_bot_20191226_models.DescribeIntentStatisticsResponse:
        """
        @param request: DescribeIntentStatisticsRequest
        @return: DescribeIntentStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_statistics_with_options(request, runtime)

    async def describe_intent_statistics_async(
        self,
        request: outbound_bot_20191226_models.DescribeIntentStatisticsRequest,
    ) -> outbound_bot_20191226_models.DescribeIntentStatisticsResponse:
        """
        @param request: DescribeIntentStatisticsRequest
        @return: DescribeIntentStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_intent_statistics_with_options_async(request, runtime)

    def describe_job_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        """
        @summary 获取job信息
        
        @param request: DescribeJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.with_script):
            query['WithScript'] = request.with_script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        """
        @summary 获取job信息
        
        @param request: DescribeJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.with_script):
            query['WithScript'] = request.with_script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        """
        @summary 获取job信息
        
        @param request: DescribeJobRequest
        @return: DescribeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    async def describe_job_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        """
        @summary 获取job信息
        
        @param request: DescribeJobRequest
        @return: DescribeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_with_options_async(request, runtime)

    def describe_job_data_parsing_task_progress_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressResponse:
        """
        @param request: DescribeJobDataParsingTaskProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobDataParsingTaskProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobDataParsingTaskProgress',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_data_parsing_task_progress_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressResponse:
        """
        @param request: DescribeJobDataParsingTaskProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobDataParsingTaskProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_data_parsing_task_id):
            query['JobDataParsingTaskId'] = request.job_data_parsing_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobDataParsingTaskProgress',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_data_parsing_task_progress(
        self,
        request: outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressRequest,
    ) -> outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressResponse:
        """
        @param request: DescribeJobDataParsingTaskProgressRequest
        @return: DescribeJobDataParsingTaskProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_data_parsing_task_progress_with_options(request, runtime)

    async def describe_job_data_parsing_task_progress_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressRequest,
    ) -> outbound_bot_20191226_models.DescribeJobDataParsingTaskProgressResponse:
        """
        @param request: DescribeJobDataParsingTaskProgressRequest
        @return: DescribeJobDataParsingTaskProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_data_parsing_task_progress_with_options_async(request, runtime)

    def describe_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        """
        @summary DescribeJobGroup
        
        @param request: DescribeJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brief_types):
            query['BriefTypes'] = request.brief_types
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        """
        @summary DescribeJobGroup
        
        @param request: DescribeJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brief_types):
            query['BriefTypes'] = request.brief_types
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_group(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        """
        @summary DescribeJobGroup
        
        @param request: DescribeJobGroupRequest
        @return: DescribeJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_group_with_options(request, runtime)

    async def describe_job_group_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        """
        @summary DescribeJobGroup
        
        @param request: DescribeJobGroupRequest
        @return: DescribeJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_group_with_options_async(request, runtime)

    def describe_job_group_export_task_progress_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressResponse:
        """
        @param request: DescribeJobGroupExportTaskProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobGroupExportTaskProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobGroupExportTaskProgress',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_group_export_task_progress_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressResponse:
        """
        @param request: DescribeJobGroupExportTaskProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobGroupExportTaskProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobGroupExportTaskProgress',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_group_export_task_progress(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressRequest,
    ) -> outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressResponse:
        """
        @param request: DescribeJobGroupExportTaskProgressRequest
        @return: DescribeJobGroupExportTaskProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_group_export_task_progress_with_options(request, runtime)

    async def describe_job_group_export_task_progress_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressRequest,
    ) -> outbound_bot_20191226_models.DescribeJobGroupExportTaskProgressResponse:
        """
        @param request: DescribeJobGroupExportTaskProgressRequest
        @return: DescribeJobGroupExportTaskProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_group_export_task_progress_with_options_async(request, runtime)

    def describe_number_district_info_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeNumberDistrictInfoStatusResponse:
        """
        @summary 查询号码库状态
        
        @param request: DescribeNumberDistrictInfoStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNumberDistrictInfoStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeNumberDistrictInfoStatus',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeNumberDistrictInfoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_number_district_info_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeNumberDistrictInfoStatusResponse:
        """
        @summary 查询号码库状态
        
        @param request: DescribeNumberDistrictInfoStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNumberDistrictInfoStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeNumberDistrictInfoStatus',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeNumberDistrictInfoStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_number_district_info_status(self) -> outbound_bot_20191226_models.DescribeNumberDistrictInfoStatusResponse:
        """
        @summary 查询号码库状态
        
        @return: DescribeNumberDistrictInfoStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_number_district_info_status_with_options(runtime)

    async def describe_number_district_info_status_async(self) -> outbound_bot_20191226_models.DescribeNumberDistrictInfoStatusResponse:
        """
        @summary 查询号码库状态
        
        @return: DescribeNumberDistrictInfoStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_number_district_info_status_with_options_async(runtime)

    def describe_script_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        """
        @summary 获取场景信息
        
        @param request: DescribeScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        """
        @summary 获取场景信息
        
        @param request: DescribeScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_script(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        """
        @summary 获取场景信息
        
        @param request: DescribeScriptRequest
        @return: DescribeScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_script_with_options(request, runtime)

    async def describe_script_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        """
        @summary 获取场景信息
        
        @param request: DescribeScriptRequest
        @return: DescribeScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_script_with_options_async(request, runtime)

    def describe_script_voice_config_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        """
        @param request: DescribeScriptVoiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScriptVoiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScriptVoiceConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_script_voice_config_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        """
        @param request: DescribeScriptVoiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScriptVoiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScriptVoiceConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_script_voice_config(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        """
        @param request: DescribeScriptVoiceConfigRequest
        @return: DescribeScriptVoiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_script_voice_config_with_options(request, runtime)

    async def describe_script_voice_config_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        """
        @param request: DescribeScriptVoiceConfigRequest
        @return: DescribeScriptVoiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_script_voice_config_with_options_async(request, runtime)

    def describe_ttsconfig_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        """
        @param request: DescribeTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTTSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTTSConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ttsconfig_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        """
        @param request: DescribeTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTTSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTTSConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ttsconfig(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        """
        @param request: DescribeTTSConfigRequest
        @return: DescribeTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ttsconfig_with_options(request, runtime)

    async def describe_ttsconfig_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        """
        @param request: DescribeTTSConfigRequest
        @return: DescribeTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ttsconfig_with_options_async(request, runtime)

    def describe_ttsdemo_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        """
        @param request: DescribeTTSDemoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTTSDemoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not UtilClient.is_unset(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTTSDemo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSDemoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ttsdemo_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        """
        @param request: DescribeTTSDemoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTTSDemoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not UtilClient.is_unset(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTTSDemo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSDemoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ttsdemo(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        """
        @param request: DescribeTTSDemoRequest
        @return: DescribeTTSDemoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ttsdemo_with_options(request, runtime)

    async def describe_ttsdemo_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        """
        @param request: DescribeTTSDemoRequest
        @return: DescribeTTSDemoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ttsdemo_with_options_async(request, runtime)

    def describe_tag_hits_summary_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        """
        @param request: DescribeTagHitsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagHitsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagHitsSummary',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTagHitsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_hits_summary_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        """
        @param request: DescribeTagHitsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagHitsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagHitsSummary',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTagHitsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_hits_summary(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        """
        @param request: DescribeTagHitsSummaryRequest
        @return: DescribeTagHitsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_hits_summary_with_options(request, runtime)

    async def describe_tag_hits_summary_async(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        """
        @param request: DescribeTagHitsSummaryRequest
        @return: DescribeTagHitsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_hits_summary_with_options_async(request, runtime)

    def describe_tenant_bind_number_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeTenantBindNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTenantBindNumberResponse:
        """
        @summary 号码绑定实例列表
        
        @param request: DescribeTenantBindNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantBindNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTenantBindNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTenantBindNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_bind_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeTenantBindNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTenantBindNumberResponse:
        """
        @summary 号码绑定实例列表
        
        @param request: DescribeTenantBindNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantBindNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTenantBindNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTenantBindNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_bind_number(
        self,
        request: outbound_bot_20191226_models.DescribeTenantBindNumberRequest,
    ) -> outbound_bot_20191226_models.DescribeTenantBindNumberResponse:
        """
        @summary 号码绑定实例列表
        
        @param request: DescribeTenantBindNumberRequest
        @return: DescribeTenantBindNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_bind_number_with_options(request, runtime)

    async def describe_tenant_bind_number_async(
        self,
        request: outbound_bot_20191226_models.DescribeTenantBindNumberRequest,
    ) -> outbound_bot_20191226_models.DescribeTenantBindNumberResponse:
        """
        @summary 号码绑定实例列表
        
        @param request: DescribeTenantBindNumberRequest
        @return: DescribeTenantBindNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_bind_number_with_options_async(request, runtime)

    def dialogue_with_options(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DialogueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_key):
            query['ActionKey'] = request.action_key
        if not UtilClient.is_unset(request.action_params):
            query['ActionParams'] = request.action_params
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_type):
            query['CallType'] = request.call_type
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Dialogue',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def dialogue_with_options_async(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DialogueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_key):
            query['ActionKey'] = request.action_key
        if not UtilClient.is_unset(request.action_params):
            query['ActionParams'] = request.action_params
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_type):
            query['CallType'] = request.call_type
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Dialogue',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dialogue(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @return: DialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    async def dialogue_async(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @return: DialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dialogue_with_options_async(request, runtime)

    def dismiss_number_district_info_parsing_result_with_options(
        self,
        request: outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultResponse:
        """
        @summary 取消号码库解析结果
        
        @param request: DismissNumberDistrictInfoParsingResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DismissNumberDistrictInfoParsingResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DismissNumberDistrictInfoParsingResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def dismiss_number_district_info_parsing_result_with_options_async(
        self,
        request: outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultResponse:
        """
        @summary 取消号码库解析结果
        
        @param request: DismissNumberDistrictInfoParsingResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DismissNumberDistrictInfoParsingResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DismissNumberDistrictInfoParsingResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dismiss_number_district_info_parsing_result(
        self,
        request: outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultRequest,
    ) -> outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultResponse:
        """
        @summary 取消号码库解析结果
        
        @param request: DismissNumberDistrictInfoParsingResultRequest
        @return: DismissNumberDistrictInfoParsingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dismiss_number_district_info_parsing_result_with_options(request, runtime)

    async def dismiss_number_district_info_parsing_result_async(
        self,
        request: outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultRequest,
    ) -> outbound_bot_20191226_models.DismissNumberDistrictInfoParsingResultResponse:
        """
        @summary 取消号码库解析结果
        
        @param request: DismissNumberDistrictInfoParsingResultRequest
        @return: DismissNumberDistrictInfoParsingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dismiss_number_district_info_parsing_result_with_options_async(request, runtime)

    def download_recording_with_options(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        """
        @summary DownloadRecording
        
        @param request: DownloadRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_voice_slice_recording):
            query['NeedVoiceSliceRecording'] = request.need_voice_slice_recording
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DownloadRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        """
        @summary DownloadRecording
        
        @param request: DownloadRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_voice_slice_recording):
            query['NeedVoiceSliceRecording'] = request.need_voice_slice_recording
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DownloadRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_recording(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        """
        @summary DownloadRecording
        
        @param request: DownloadRecordingRequest
        @return: DownloadRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_recording_with_options(request, runtime)

    async def download_recording_async(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        """
        @summary DownloadRecording
        
        @param request: DownloadRecordingRequest
        @return: DownloadRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_recording_with_options_async(request, runtime)

    def download_script_recording_with_options(
        self,
        request: outbound_bot_20191226_models.DownloadScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DownloadScriptRecordingResponse:
        """
        @param request: DownloadScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DownloadScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_script_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.DownloadScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DownloadScriptRecordingResponse:
        """
        @param request: DownloadScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DownloadScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_script_recording(
        self,
        request: outbound_bot_20191226_models.DownloadScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.DownloadScriptRecordingResponse:
        """
        @param request: DownloadScriptRecordingRequest
        @return: DownloadScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_script_recording_with_options(request, runtime)

    async def download_script_recording_async(
        self,
        request: outbound_bot_20191226_models.DownloadScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.DownloadScriptRecordingResponse:
        """
        @param request: DownloadScriptRecordingRequest
        @return: DownloadScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_script_recording_with_options_async(request, runtime)

    def duplicate_script_with_options(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        """
        @param request: DuplicateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DuplicateScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_script_id):
            query['SourceScriptId'] = request.source_script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DuplicateScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DuplicateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def duplicate_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        """
        @param request: DuplicateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DuplicateScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_script_id):
            query['SourceScriptId'] = request.source_script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DuplicateScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DuplicateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def duplicate_script(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        """
        @param request: DuplicateScriptRequest
        @return: DuplicateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.duplicate_script_with_options(request, runtime)

    async def duplicate_script_async(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        """
        @param request: DuplicateScriptRequest
        @return: DuplicateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.duplicate_script_with_options_async(request, runtime)

    def export_script_with_options(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        """
        @param request: ExportScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ExportScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        """
        @param request: ExportScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ExportScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_script(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        """
        @param request: ExportScriptRequest
        @return: ExportScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_script_with_options(request, runtime)

    async def export_script_async(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        """
        @param request: ExportScriptRequest
        @return: ExportScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_script_with_options_async(request, runtime)

    def generate_upload_url_with_options(
        self,
        request: outbound_bot_20191226_models.GenerateUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GenerateUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_url_with_options_async(
        self,
        request: outbound_bot_20191226_models.GenerateUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GenerateUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_url(
        self,
        request: outbound_bot_20191226_models.GenerateUploadUrlRequest,
    ) -> outbound_bot_20191226_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @return: GenerateUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_url_with_options(request, runtime)

    async def generate_upload_url_async(
        self,
        request: outbound_bot_20191226_models.GenerateUploadUrlRequest,
    ) -> outbound_bot_20191226_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @return: GenerateUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_url_with_options_async(request, runtime)

    def get_after_answer_delay_playback_with_options(
        self,
        request: outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackResponse:
        """
        @param request: GetAfterAnswerDelayPlaybackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAfterAnswerDelayPlaybackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAfterAnswerDelayPlayback',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_after_answer_delay_playback_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackResponse:
        """
        @param request: GetAfterAnswerDelayPlaybackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAfterAnswerDelayPlaybackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAfterAnswerDelayPlayback',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_after_answer_delay_playback(
        self,
        request: outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackRequest,
    ) -> outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackResponse:
        """
        @param request: GetAfterAnswerDelayPlaybackRequest
        @return: GetAfterAnswerDelayPlaybackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_after_answer_delay_playback_with_options(request, runtime)

    async def get_after_answer_delay_playback_async(
        self,
        request: outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackRequest,
    ) -> outbound_bot_20191226_models.GetAfterAnswerDelayPlaybackResponse:
        """
        @param request: GetAfterAnswerDelayPlaybackRequest
        @return: GetAfterAnswerDelayPlaybackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_after_answer_delay_playback_with_options_async(request, runtime)

    def get_agent_profile_with_options(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAgentProfileResponse:
        """
        @param request: GetAgentProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentProfileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAgentProfile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAgentProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_profile_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAgentProfileResponse:
        """
        @param request: GetAgentProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentProfileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAgentProfile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAgentProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_profile(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileRequest,
    ) -> outbound_bot_20191226_models.GetAgentProfileResponse:
        """
        @param request: GetAgentProfileRequest
        @return: GetAgentProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_profile_with_options(request, runtime)

    async def get_agent_profile_async(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileRequest,
    ) -> outbound_bot_20191226_models.GetAgentProfileResponse:
        """
        @param request: GetAgentProfileRequest
        @return: GetAgentProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_profile_with_options_async(request, runtime)

    def get_agent_profile_template_with_options(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAgentProfileTemplateResponse:
        """
        @param request: GetAgentProfileTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentProfileTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAgentProfileTemplate',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAgentProfileTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_profile_template_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAgentProfileTemplateResponse:
        """
        @param request: GetAgentProfileTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentProfileTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_profile_template_id):
            body['AgentProfileTemplateId'] = request.agent_profile_template_id
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAgentProfileTemplate',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAgentProfileTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_profile_template(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileTemplateRequest,
    ) -> outbound_bot_20191226_models.GetAgentProfileTemplateResponse:
        """
        @param request: GetAgentProfileTemplateRequest
        @return: GetAgentProfileTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_profile_template_with_options(request, runtime)

    async def get_agent_profile_template_async(
        self,
        request: outbound_bot_20191226_models.GetAgentProfileTemplateRequest,
    ) -> outbound_bot_20191226_models.GetAgentProfileTemplateResponse:
        """
        @param request: GetAgentProfileTemplateRequest
        @return: GetAgentProfileTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_profile_template_with_options_async(request, runtime)

    def get_annotation_mission_summary_with_options(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionSummaryResponse:
        """
        @param request: GetAnnotationMissionSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAnnotationMissionSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnnotationMissionSummary',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAnnotationMissionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_annotation_mission_summary_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionSummaryResponse:
        """
        @param request: GetAnnotationMissionSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAnnotationMissionSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnnotationMissionSummary',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAnnotationMissionSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_annotation_mission_summary(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionSummaryRequest,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionSummaryResponse:
        """
        @param request: GetAnnotationMissionSummaryRequest
        @return: GetAnnotationMissionSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_annotation_mission_summary_with_options(request, runtime)

    async def get_annotation_mission_summary_async(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionSummaryRequest,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionSummaryResponse:
        """
        @param request: GetAnnotationMissionSummaryRequest
        @return: GetAnnotationMissionSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_annotation_mission_summary_with_options_async(request, runtime)

    def get_annotation_mission_tag_info_list_with_options(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionTagInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionTagInfoListResponse:
        """
        @param request: GetAnnotationMissionTagInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAnnotationMissionTagInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnnotationMissionTagInfoList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAnnotationMissionTagInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_annotation_mission_tag_info_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionTagInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionTagInfoListResponse:
        """
        @param request: GetAnnotationMissionTagInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAnnotationMissionTagInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnnotationMissionTagInfoList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAnnotationMissionTagInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_annotation_mission_tag_info_list(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionTagInfoListRequest,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionTagInfoListResponse:
        """
        @param request: GetAnnotationMissionTagInfoListRequest
        @return: GetAnnotationMissionTagInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_annotation_mission_tag_info_list_with_options(request, runtime)

    async def get_annotation_mission_tag_info_list_async(
        self,
        request: outbound_bot_20191226_models.GetAnnotationMissionTagInfoListRequest,
    ) -> outbound_bot_20191226_models.GetAnnotationMissionTagInfoListResponse:
        """
        @param request: GetAnnotationMissionTagInfoListRequest
        @return: GetAnnotationMissionTagInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_annotation_mission_tag_info_list_with_options_async(request, runtime)

    def get_asr_server_info_with_options(
        self,
        request: outbound_bot_20191226_models.GetAsrServerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAsrServerInfoResponse:
        """
        @param request: GetAsrServerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsrServerInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrServerInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAsrServerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asr_server_info_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetAsrServerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAsrServerInfoResponse:
        """
        @param request: GetAsrServerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsrServerInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrServerInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAsrServerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asr_server_info(
        self,
        request: outbound_bot_20191226_models.GetAsrServerInfoRequest,
    ) -> outbound_bot_20191226_models.GetAsrServerInfoResponse:
        """
        @param request: GetAsrServerInfoRequest
        @return: GetAsrServerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_asr_server_info_with_options(request, runtime)

    async def get_asr_server_info_async(
        self,
        request: outbound_bot_20191226_models.GetAsrServerInfoRequest,
    ) -> outbound_bot_20191226_models.GetAsrServerInfoResponse:
        """
        @param request: GetAsrServerInfoRequest
        @return: GetAsrServerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_asr_server_info_with_options_async(request, runtime)

    def get_assign_jobs_async_result_with_options(
        self,
        request: outbound_bot_20191226_models.GetAssignJobsAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAssignJobsAsyncResultResponse:
        """
        @summary 获取异步外呼任务上传结果
        
        @param request: GetAssignJobsAsyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAssignJobsAsyncResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_task_id):
            query['AsyncTaskId'] = request.async_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAssignJobsAsyncResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAssignJobsAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_assign_jobs_async_result_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetAssignJobsAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetAssignJobsAsyncResultResponse:
        """
        @summary 获取异步外呼任务上传结果
        
        @param request: GetAssignJobsAsyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAssignJobsAsyncResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_task_id):
            query['AsyncTaskId'] = request.async_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAssignJobsAsyncResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetAssignJobsAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_assign_jobs_async_result(
        self,
        request: outbound_bot_20191226_models.GetAssignJobsAsyncResultRequest,
    ) -> outbound_bot_20191226_models.GetAssignJobsAsyncResultResponse:
        """
        @summary 获取异步外呼任务上传结果
        
        @param request: GetAssignJobsAsyncResultRequest
        @return: GetAssignJobsAsyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_assign_jobs_async_result_with_options(request, runtime)

    async def get_assign_jobs_async_result_async(
        self,
        request: outbound_bot_20191226_models.GetAssignJobsAsyncResultRequest,
    ) -> outbound_bot_20191226_models.GetAssignJobsAsyncResultResponse:
        """
        @summary 获取异步外呼任务上传结果
        
        @param request: GetAssignJobsAsyncResultRequest
        @return: GetAssignJobsAsyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_assign_jobs_async_result_with_options_async(request, runtime)

    def get_base_strategy_period_with_options(
        self,
        request: outbound_bot_20191226_models.GetBaseStrategyPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetBaseStrategyPeriodResponse:
        """
        @summary 获取系统策略配置
        
        @param request: GetBaseStrategyPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBaseStrategyPeriodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBaseStrategyPeriod',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetBaseStrategyPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_base_strategy_period_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetBaseStrategyPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetBaseStrategyPeriodResponse:
        """
        @summary 获取系统策略配置
        
        @param request: GetBaseStrategyPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBaseStrategyPeriodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBaseStrategyPeriod',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetBaseStrategyPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_base_strategy_period(
        self,
        request: outbound_bot_20191226_models.GetBaseStrategyPeriodRequest,
    ) -> outbound_bot_20191226_models.GetBaseStrategyPeriodResponse:
        """
        @summary 获取系统策略配置
        
        @param request: GetBaseStrategyPeriodRequest
        @return: GetBaseStrategyPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_base_strategy_period_with_options(request, runtime)

    async def get_base_strategy_period_async(
        self,
        request: outbound_bot_20191226_models.GetBaseStrategyPeriodRequest,
    ) -> outbound_bot_20191226_models.GetBaseStrategyPeriodResponse:
        """
        @summary 获取系统策略配置
        
        @param request: GetBaseStrategyPeriodRequest
        @return: GetBaseStrategyPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_base_strategy_period_with_options_async(request, runtime)

    def get_concurrent_conversation_quota_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetConcurrentConversationQuotaResponse:
        """
        @param request: GetConcurrentConversationQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConcurrentConversationQuotaResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConcurrentConversationQuota',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetConcurrentConversationQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_concurrent_conversation_quota_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetConcurrentConversationQuotaResponse:
        """
        @param request: GetConcurrentConversationQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConcurrentConversationQuotaResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetConcurrentConversationQuota',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetConcurrentConversationQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_concurrent_conversation_quota(self) -> outbound_bot_20191226_models.GetConcurrentConversationQuotaResponse:
        """
        @return: GetConcurrentConversationQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_concurrent_conversation_quota_with_options(runtime)

    async def get_concurrent_conversation_quota_async(self) -> outbound_bot_20191226_models.GetConcurrentConversationQuotaResponse:
        """
        @return: GetConcurrentConversationQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_concurrent_conversation_quota_with_options_async(runtime)

    def get_contact_block_list_with_options(
        self,
        request: outbound_bot_20191226_models.GetContactBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetContactBlockListResponse:
        """
        @summary GetContactBlockList
        
        @param request: GetContactBlockListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactBlockListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action='GetContactBlockList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetContactBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contact_block_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetContactBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetContactBlockListResponse:
        """
        @summary GetContactBlockList
        
        @param request: GetContactBlockListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactBlockListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action='GetContactBlockList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetContactBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contact_block_list(
        self,
        request: outbound_bot_20191226_models.GetContactBlockListRequest,
    ) -> outbound_bot_20191226_models.GetContactBlockListResponse:
        """
        @summary GetContactBlockList
        
        @param request: GetContactBlockListRequest
        @return: GetContactBlockListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_contact_block_list_with_options(request, runtime)

    async def get_contact_block_list_async(
        self,
        request: outbound_bot_20191226_models.GetContactBlockListRequest,
    ) -> outbound_bot_20191226_models.GetContactBlockListResponse:
        """
        @summary GetContactBlockList
        
        @param request: GetContactBlockListRequest
        @return: GetContactBlockListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_contact_block_list_with_options_async(request, runtime)

    def get_contact_white_list_with_options(
        self,
        request: outbound_bot_20191226_models.GetContactWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetContactWhiteListResponse:
        """
        @summary GetContactWhiteList
        
        @param request: GetContactWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action='GetContactWhiteList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetContactWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contact_white_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetContactWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetContactWhiteListResponse:
        """
        @summary GetContactWhiteList
        
        @param request: GetContactWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count_total_row):
            query['CountTotalRow'] = request.count_total_row
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
            action='GetContactWhiteList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetContactWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contact_white_list(
        self,
        request: outbound_bot_20191226_models.GetContactWhiteListRequest,
    ) -> outbound_bot_20191226_models.GetContactWhiteListResponse:
        """
        @summary GetContactWhiteList
        
        @param request: GetContactWhiteListRequest
        @return: GetContactWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_contact_white_list_with_options(request, runtime)

    async def get_contact_white_list_async(
        self,
        request: outbound_bot_20191226_models.GetContactWhiteListRequest,
    ) -> outbound_bot_20191226_models.GetContactWhiteListResponse:
        """
        @summary GetContactWhiteList
        
        @param request: GetContactWhiteListRequest
        @return: GetContactWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_contact_white_list_with_options_async(request, runtime)

    def get_current_concurrency_with_options(
        self,
        request: outbound_bot_20191226_models.GetCurrentConcurrencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetCurrentConcurrencyResponse:
        """
        @param request: GetCurrentConcurrencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCurrentConcurrencyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCurrentConcurrency',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetCurrentConcurrencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_current_concurrency_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetCurrentConcurrencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetCurrentConcurrencyResponse:
        """
        @param request: GetCurrentConcurrencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCurrentConcurrencyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCurrentConcurrency',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetCurrentConcurrencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_current_concurrency(
        self,
        request: outbound_bot_20191226_models.GetCurrentConcurrencyRequest,
    ) -> outbound_bot_20191226_models.GetCurrentConcurrencyResponse:
        """
        @param request: GetCurrentConcurrencyRequest
        @return: GetCurrentConcurrencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_current_concurrency_with_options(request, runtime)

    async def get_current_concurrency_async(
        self,
        request: outbound_bot_20191226_models.GetCurrentConcurrencyRequest,
    ) -> outbound_bot_20191226_models.GetCurrentConcurrencyResponse:
        """
        @param request: GetCurrentConcurrencyRequest
        @return: GetCurrentConcurrencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_current_concurrency_with_options_async(request, runtime)

    def get_effective_days_with_options(
        self,
        request: outbound_bot_20191226_models.GetEffectiveDaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetEffectiveDaysResponse:
        """
        @param request: GetEffectiveDaysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEffectiveDaysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEffectiveDays',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetEffectiveDaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_effective_days_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetEffectiveDaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetEffectiveDaysResponse:
        """
        @param request: GetEffectiveDaysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEffectiveDaysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEffectiveDays',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetEffectiveDaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_effective_days(
        self,
        request: outbound_bot_20191226_models.GetEffectiveDaysRequest,
    ) -> outbound_bot_20191226_models.GetEffectiveDaysResponse:
        """
        @param request: GetEffectiveDaysRequest
        @return: GetEffectiveDaysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_effective_days_with_options(request, runtime)

    async def get_effective_days_async(
        self,
        request: outbound_bot_20191226_models.GetEffectiveDaysRequest,
    ) -> outbound_bot_20191226_models.GetEffectiveDaysResponse:
        """
        @param request: GetEffectiveDaysRequest
        @return: GetEffectiveDaysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_effective_days_with_options_async(request, runtime)

    def get_empty_number_no_more_calls_info_with_options(
        self,
        request: outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoResponse:
        """
        @summary GetEmptyNumberNoMoreCallsInfo
        
        @param request: GetEmptyNumberNoMoreCallsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmptyNumberNoMoreCallsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEmptyNumberNoMoreCallsInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_empty_number_no_more_calls_info_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoResponse:
        """
        @summary GetEmptyNumberNoMoreCallsInfo
        
        @param request: GetEmptyNumberNoMoreCallsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmptyNumberNoMoreCallsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEmptyNumberNoMoreCallsInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_empty_number_no_more_calls_info(
        self,
        request: outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoRequest,
    ) -> outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoResponse:
        """
        @summary GetEmptyNumberNoMoreCallsInfo
        
        @param request: GetEmptyNumberNoMoreCallsInfoRequest
        @return: GetEmptyNumberNoMoreCallsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_empty_number_no_more_calls_info_with_options(request, runtime)

    async def get_empty_number_no_more_calls_info_async(
        self,
        request: outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoRequest,
    ) -> outbound_bot_20191226_models.GetEmptyNumberNoMoreCallsInfoResponse:
        """
        @summary GetEmptyNumberNoMoreCallsInfo
        
        @param request: GetEmptyNumberNoMoreCallsInfoRequest
        @return: GetEmptyNumberNoMoreCallsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_empty_number_no_more_calls_info_with_options_async(request, runtime)

    def get_job_data_upload_params_with_options(
        self,
        request: outbound_bot_20191226_models.GetJobDataUploadParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetJobDataUploadParamsResponse:
        """
        @summary 获取上传信息
        
        @param request: GetJobDataUploadParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobDataUploadParamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.busi_type):
            query['BusiType'] = request.busi_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobDataUploadParams',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetJobDataUploadParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_data_upload_params_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetJobDataUploadParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetJobDataUploadParamsResponse:
        """
        @summary 获取上传信息
        
        @param request: GetJobDataUploadParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobDataUploadParamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.busi_type):
            query['BusiType'] = request.busi_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobDataUploadParams',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetJobDataUploadParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_data_upload_params(
        self,
        request: outbound_bot_20191226_models.GetJobDataUploadParamsRequest,
    ) -> outbound_bot_20191226_models.GetJobDataUploadParamsResponse:
        """
        @summary 获取上传信息
        
        @param request: GetJobDataUploadParamsRequest
        @return: GetJobDataUploadParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_data_upload_params_with_options(request, runtime)

    async def get_job_data_upload_params_async(
        self,
        request: outbound_bot_20191226_models.GetJobDataUploadParamsRequest,
    ) -> outbound_bot_20191226_models.GetJobDataUploadParamsResponse:
        """
        @summary 获取上传信息
        
        @param request: GetJobDataUploadParamsRequest
        @return: GetJobDataUploadParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_data_upload_params_with_options_async(request, runtime)

    def get_max_attempts_per_day_with_options(
        self,
        request: outbound_bot_20191226_models.GetMaxAttemptsPerDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetMaxAttemptsPerDayResponse:
        """
        @summary GetMaxAttemptsPerDay
        
        @param request: GetMaxAttemptsPerDayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMaxAttemptsPerDayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMaxAttemptsPerDay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetMaxAttemptsPerDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_max_attempts_per_day_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetMaxAttemptsPerDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetMaxAttemptsPerDayResponse:
        """
        @summary GetMaxAttemptsPerDay
        
        @param request: GetMaxAttemptsPerDayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMaxAttemptsPerDayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMaxAttemptsPerDay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetMaxAttemptsPerDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_max_attempts_per_day(
        self,
        request: outbound_bot_20191226_models.GetMaxAttemptsPerDayRequest,
    ) -> outbound_bot_20191226_models.GetMaxAttemptsPerDayResponse:
        """
        @summary GetMaxAttemptsPerDay
        
        @param request: GetMaxAttemptsPerDayRequest
        @return: GetMaxAttemptsPerDayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_max_attempts_per_day_with_options(request, runtime)

    async def get_max_attempts_per_day_async(
        self,
        request: outbound_bot_20191226_models.GetMaxAttemptsPerDayRequest,
    ) -> outbound_bot_20191226_models.GetMaxAttemptsPerDayResponse:
        """
        @summary GetMaxAttemptsPerDay
        
        @param request: GetMaxAttemptsPerDayRequest
        @return: GetMaxAttemptsPerDayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_max_attempts_per_day_with_options_async(request, runtime)

    def get_number_district_info_template_download_url_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        """
        @summary 获取号码库模板下载链接
        
        @param request: GetNumberDistrictInfoTemplateDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNumberDistrictInfoTemplateDownloadUrlResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetNumberDistrictInfoTemplateDownloadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetNumberDistrictInfoTemplateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_number_district_info_template_download_url_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        """
        @summary 获取号码库模板下载链接
        
        @param request: GetNumberDistrictInfoTemplateDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNumberDistrictInfoTemplateDownloadUrlResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetNumberDistrictInfoTemplateDownloadUrl',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetNumberDistrictInfoTemplateDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_number_district_info_template_download_url(self) -> outbound_bot_20191226_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        """
        @summary 获取号码库模板下载链接
        
        @return: GetNumberDistrictInfoTemplateDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_number_district_info_template_download_url_with_options(runtime)

    async def get_number_district_info_template_download_url_async(self) -> outbound_bot_20191226_models.GetNumberDistrictInfoTemplateDownloadUrlResponse:
        """
        @summary 获取号码库模板下载链接
        
        @return: GetNumberDistrictInfoTemplateDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_number_district_info_template_download_url_with_options_async(runtime)

    def get_realtime_concurrency_report_with_options(
        self,
        request: outbound_bot_20191226_models.GetRealtimeConcurrencyReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetRealtimeConcurrencyReportResponse:
        """
        @summary GetRealtimeConcurrencyReport
        
        @param request: GetRealtimeConcurrencyReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeConcurrencyReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeConcurrencyReport',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetRealtimeConcurrencyReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_concurrency_report_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetRealtimeConcurrencyReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetRealtimeConcurrencyReportResponse:
        """
        @summary GetRealtimeConcurrencyReport
        
        @param request: GetRealtimeConcurrencyReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeConcurrencyReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeConcurrencyReport',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetRealtimeConcurrencyReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_concurrency_report(
        self,
        request: outbound_bot_20191226_models.GetRealtimeConcurrencyReportRequest,
    ) -> outbound_bot_20191226_models.GetRealtimeConcurrencyReportResponse:
        """
        @summary GetRealtimeConcurrencyReport
        
        @param request: GetRealtimeConcurrencyReportRequest
        @return: GetRealtimeConcurrencyReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_concurrency_report_with_options(request, runtime)

    async def get_realtime_concurrency_report_async(
        self,
        request: outbound_bot_20191226_models.GetRealtimeConcurrencyReportRequest,
    ) -> outbound_bot_20191226_models.GetRealtimeConcurrencyReportResponse:
        """
        @summary GetRealtimeConcurrencyReport
        
        @param request: GetRealtimeConcurrencyReportRequest
        @return: GetRealtimeConcurrencyReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_concurrency_report_with_options_async(request, runtime)

    def get_summary_info_with_options(
        self,
        request: outbound_bot_20191226_models.GetSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetSummaryInfoResponse:
        """
        @summary GetSummaryInfo
        
        @param request: GetSummaryInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSummaryInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSummaryInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_info_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetSummaryInfoResponse:
        """
        @summary GetSummaryInfo
        
        @param request: GetSummaryInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSummaryInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSummaryInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_info(
        self,
        request: outbound_bot_20191226_models.GetSummaryInfoRequest,
    ) -> outbound_bot_20191226_models.GetSummaryInfoResponse:
        """
        @summary GetSummaryInfo
        
        @param request: GetSummaryInfoRequest
        @return: GetSummaryInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_summary_info_with_options(request, runtime)

    async def get_summary_info_async(
        self,
        request: outbound_bot_20191226_models.GetSummaryInfoRequest,
    ) -> outbound_bot_20191226_models.GetSummaryInfoResponse:
        """
        @summary GetSummaryInfo
        
        @param request: GetSummaryInfoRequest
        @return: GetSummaryInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_summary_info_with_options_async(request, runtime)

    def get_task_by_uuid_with_options(
        self,
        request: outbound_bot_20191226_models.GetTaskByUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetTaskByUuidResponse:
        """
        @param request: GetTaskByUuidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskByUuidResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskByUuid',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetTaskByUuidResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_by_uuid_with_options_async(
        self,
        request: outbound_bot_20191226_models.GetTaskByUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetTaskByUuidResponse:
        """
        @param request: GetTaskByUuidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskByUuidResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskByUuid',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetTaskByUuidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_by_uuid(
        self,
        request: outbound_bot_20191226_models.GetTaskByUuidRequest,
    ) -> outbound_bot_20191226_models.GetTaskByUuidResponse:
        """
        @param request: GetTaskByUuidRequest
        @return: GetTaskByUuidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_by_uuid_with_options(request, runtime)

    async def get_task_by_uuid_async(
        self,
        request: outbound_bot_20191226_models.GetTaskByUuidRequest,
    ) -> outbound_bot_20191226_models.GetTaskByUuidResponse:
        """
        @param request: GetTaskByUuidRequest
        @return: GetTaskByUuidResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_by_uuid_with_options_async(request, runtime)

    def get_version_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetVersionResponse:
        """
        @summary GetVersion
        
        @param request: GetVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVersionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetVersion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_version_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.GetVersionResponse:
        """
        @summary GetVersion
        
        @param request: GetVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVersionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetVersion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.GetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_version(self) -> outbound_bot_20191226_models.GetVersionResponse:
        """
        @summary GetVersion
        
        @return: GetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_version_with_options(runtime)

    async def get_version_async(self) -> outbound_bot_20191226_models.GetVersionResponse:
        """
        @summary GetVersion
        
        @return: GetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_version_with_options_async(runtime)

    def import_script_with_options(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        """
        @param request: ImportScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.signature_url):
            query['SignatureUrl'] = request.signature_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ImportScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        """
        @param request: ImportScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.signature_url):
            query['SignatureUrl'] = request.signature_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ImportScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_script(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        """
        @param request: ImportScriptRequest
        @return: ImportScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_script_with_options(request, runtime)

    async def import_script_async(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        """
        @param request: ImportScriptRequest
        @return: ImportScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_script_with_options_async(request, runtime)

    def inflight_task_timeout_with_options(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        """
        @summary InflightTaskTimeout
        
        @param request: InflightTaskTimeoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InflightTaskTimeoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InflightTaskTimeout',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.InflightTaskTimeoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def inflight_task_timeout_with_options_async(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        """
        @summary InflightTaskTimeout
        
        @param request: InflightTaskTimeoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InflightTaskTimeoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InflightTaskTimeout',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.InflightTaskTimeoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inflight_task_timeout(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        """
        @summary InflightTaskTimeout
        
        @param request: InflightTaskTimeoutRequest
        @return: InflightTaskTimeoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inflight_task_timeout_with_options(request, runtime)

    async def inflight_task_timeout_async(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        """
        @summary InflightTaskTimeout
        
        @param request: InflightTaskTimeoutRequest
        @return: InflightTaskTimeoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inflight_task_timeout_with_options_async(request, runtime)

    def list_agent_profiles_with_options(
        self,
        request: outbound_bot_20191226_models.ListAgentProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAgentProfilesResponse:
        """
        @param request: ListAgentProfilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentProfilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAgentProfiles',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAgentProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_profiles_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListAgentProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAgentProfilesResponse:
        """
        @param request: ListAgentProfilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentProfilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_ip):
            body['AppIp'] = request.app_ip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            body['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAgentProfiles',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAgentProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_profiles(
        self,
        request: outbound_bot_20191226_models.ListAgentProfilesRequest,
    ) -> outbound_bot_20191226_models.ListAgentProfilesResponse:
        """
        @param request: ListAgentProfilesRequest
        @return: ListAgentProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_agent_profiles_with_options(request, runtime)

    async def list_agent_profiles_async(
        self,
        request: outbound_bot_20191226_models.ListAgentProfilesRequest,
    ) -> outbound_bot_20191226_models.ListAgentProfilesResponse:
        """
        @param request: ListAgentProfilesRequest
        @return: ListAgentProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_profiles_with_options_async(request, runtime)

    def list_all_tenant_bind_number_binding_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAllTenantBindNumberBindingResponse:
        """
        @summary 租户绑定号码列表
        
        @param request: ListAllTenantBindNumberBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllTenantBindNumberBindingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAllTenantBindNumberBinding',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAllTenantBindNumberBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_tenant_bind_number_binding_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAllTenantBindNumberBindingResponse:
        """
        @summary 租户绑定号码列表
        
        @param request: ListAllTenantBindNumberBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllTenantBindNumberBindingResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAllTenantBindNumberBinding',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAllTenantBindNumberBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_tenant_bind_number_binding(self) -> outbound_bot_20191226_models.ListAllTenantBindNumberBindingResponse:
        """
        @summary 租户绑定号码列表
        
        @return: ListAllTenantBindNumberBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_tenant_bind_number_binding_with_options(runtime)

    async def list_all_tenant_bind_number_binding_async(self) -> outbound_bot_20191226_models.ListAllTenantBindNumberBindingResponse:
        """
        @summary 租户绑定号码列表
        
        @return: ListAllTenantBindNumberBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_tenant_bind_number_binding_with_options_async(runtime)

    def list_annotation_mission_with_options(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionResponse:
        """
        @param request: ListAnnotationMissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnnotationMissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not UtilClient.is_unset(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not UtilClient.is_unset(request.annotation_status_list_filter):
            query['AnnotationStatusListFilter'] = request.annotation_status_list_filter
        if not UtilClient.is_unset(request.annotation_status_list_string_filter):
            query['AnnotationStatusListStringFilter'] = request.annotation_status_list_string_filter
        if not UtilClient.is_unset(request.create_time_end_filter):
            query['CreateTimeEndFilter'] = request.create_time_end_filter
        if not UtilClient.is_unset(request.create_time_start_filter):
            query['CreateTimeStartFilter'] = request.create_time_start_filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationMission',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAnnotationMissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_annotation_mission_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionResponse:
        """
        @param request: ListAnnotationMissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnnotationMissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not UtilClient.is_unset(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not UtilClient.is_unset(request.annotation_status_list_filter):
            query['AnnotationStatusListFilter'] = request.annotation_status_list_filter
        if not UtilClient.is_unset(request.annotation_status_list_string_filter):
            query['AnnotationStatusListStringFilter'] = request.annotation_status_list_string_filter
        if not UtilClient.is_unset(request.create_time_end_filter):
            query['CreateTimeEndFilter'] = request.create_time_end_filter
        if not UtilClient.is_unset(request.create_time_start_filter):
            query['CreateTimeStartFilter'] = request.create_time_start_filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationMission',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAnnotationMissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_annotation_mission(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionRequest,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionResponse:
        """
        @param request: ListAnnotationMissionRequest
        @return: ListAnnotationMissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_annotation_mission_with_options(request, runtime)

    async def list_annotation_mission_async(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionRequest,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionResponse:
        """
        @param request: ListAnnotationMissionRequest
        @return: ListAnnotationMissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_annotation_mission_with_options_async(request, runtime)

    def list_annotation_mission_session_with_options(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionSessionResponse:
        """
        @param request: ListAnnotationMissionSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnnotationMissionSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not UtilClient.is_unset(request.annotation_mission_session_id):
            query['AnnotationMissionSessionId'] = request.annotation_mission_session_id
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.include_status_list_json_string):
            query['IncludeStatusListJsonString'] = request.include_status_list_json_string
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationMissionSession',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAnnotationMissionSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_annotation_mission_session_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionSessionResponse:
        """
        @param request: ListAnnotationMissionSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnnotationMissionSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not UtilClient.is_unset(request.annotation_mission_session_id):
            query['AnnotationMissionSessionId'] = request.annotation_mission_session_id
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.include_status_list_json_string):
            query['IncludeStatusListJsonString'] = request.include_status_list_json_string
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationMissionSession',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListAnnotationMissionSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_annotation_mission_session(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionSessionRequest,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionSessionResponse:
        """
        @param request: ListAnnotationMissionSessionRequest
        @return: ListAnnotationMissionSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_annotation_mission_session_with_options(request, runtime)

    async def list_annotation_mission_session_async(
        self,
        request: outbound_bot_20191226_models.ListAnnotationMissionSessionRequest,
    ) -> outbound_bot_20191226_models.ListAnnotationMissionSessionResponse:
        """
        @param request: ListAnnotationMissionSessionRequest
        @return: ListAnnotationMissionSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_annotation_mission_session_with_options_async(request, runtime)

    def list_api_plugins_with_options(
        self,
        request: outbound_bot_20191226_models.ListApiPluginsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListApiPluginsResponse:
        """
        @param request: ListApiPluginsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiPluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiPlugins',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListApiPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_plugins_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListApiPluginsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListApiPluginsResponse:
        """
        @param request: ListApiPluginsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiPluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiPlugins',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListApiPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_plugins(
        self,
        request: outbound_bot_20191226_models.ListApiPluginsRequest,
    ) -> outbound_bot_20191226_models.ListApiPluginsResponse:
        """
        @param request: ListApiPluginsRequest
        @return: ListApiPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_api_plugins_with_options(request, runtime)

    async def list_api_plugins_async(
        self,
        request: outbound_bot_20191226_models.ListApiPluginsRequest,
    ) -> outbound_bot_20191226_models.ListApiPluginsResponse:
        """
        @param request: ListApiPluginsRequest
        @return: ListApiPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_api_plugins_with_options_async(request, runtime)

    def list_beebot_intent_with_options(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListBeebotIntentResponse:
        """
        @summary ListBeebotIntent
        
        @param request: ListBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBeebotIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_beebot_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListBeebotIntentResponse:
        """
        @summary ListBeebotIntent
        
        @param request: ListBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBeebotIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_beebot_intent(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.ListBeebotIntentResponse:
        """
        @summary ListBeebotIntent
        
        @param request: ListBeebotIntentRequest
        @return: ListBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_beebot_intent_with_options(request, runtime)

    async def list_beebot_intent_async(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.ListBeebotIntentResponse:
        """
        @summary ListBeebotIntent
        
        @param request: ListBeebotIntentRequest
        @return: ListBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_beebot_intent_with_options_async(request, runtime)

    def list_beebot_intent_lgf_with_options(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListBeebotIntentLgfResponse:
        """
        @summary ListBeebotIntentLgf
        
        @param request: ListBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBeebotIntentLgfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_beebot_intent_lgf_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListBeebotIntentLgfResponse:
        """
        @summary ListBeebotIntentLgf
        
        @param request: ListBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBeebotIntentLgfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_beebot_intent_lgf(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.ListBeebotIntentLgfResponse:
        """
        @summary ListBeebotIntentLgf
        
        @param request: ListBeebotIntentLgfRequest
        @return: ListBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_beebot_intent_lgf_with_options(request, runtime)

    async def list_beebot_intent_lgf_async(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.ListBeebotIntentLgfResponse:
        """
        @summary ListBeebotIntentLgf
        
        @param request: ListBeebotIntentLgfRequest
        @return: ListBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_beebot_intent_lgf_with_options_async(request, runtime)

    def list_beebot_intent_user_say_with_options(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListBeebotIntentUserSayResponse:
        """
        @summary ListBeebotIntentUserSay
        
        @param request: ListBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_beebot_intent_user_say_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListBeebotIntentUserSayResponse:
        """
        @summary ListBeebotIntentUserSay
        
        @param request: ListBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_beebot_intent_user_say(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.ListBeebotIntentUserSayResponse:
        """
        @summary ListBeebotIntentUserSay
        
        @param request: ListBeebotIntentUserSayRequest
        @return: ListBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_beebot_intent_user_say_with_options(request, runtime)

    async def list_beebot_intent_user_say_async(
        self,
        request: outbound_bot_20191226_models.ListBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.ListBeebotIntentUserSayResponse:
        """
        @summary ListBeebotIntentUserSay
        
        @param request: ListBeebotIntentUserSayRequest
        @return: ListBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_beebot_intent_user_say_with_options_async(request, runtime)

    def list_chatbot_instances_with_options(
        self,
        request: outbound_bot_20191226_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatbotInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatbotInstances',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListChatbotInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatbot_instances_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatbotInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatbotInstances',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListChatbotInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatbot_instances(
        self,
        request: outbound_bot_20191226_models.ListChatbotInstancesRequest,
    ) -> outbound_bot_20191226_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @return: ListChatbotInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chatbot_instances_with_options(request, runtime)

    async def list_chatbot_instances_async(
        self,
        request: outbound_bot_20191226_models.ListChatbotInstancesRequest,
    ) -> outbound_bot_20191226_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @return: ListChatbotInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chatbot_instances_with_options_async(request, runtime)

    def list_dialogue_flows_with_options(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        """
        @param request: ListDialogueFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialogueFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDialogueFlows',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListDialogueFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialogue_flows_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        """
        @param request: ListDialogueFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialogueFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDialogueFlows',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListDialogueFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialogue_flows(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        """
        @param request: ListDialogueFlowsRequest
        @return: ListDialogueFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dialogue_flows_with_options(request, runtime)

    async def list_dialogue_flows_async(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        """
        @param request: ListDialogueFlowsRequest
        @return: ListDialogueFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dialogue_flows_with_options_async(request, runtime)

    def list_download_tasks_with_options(
        self,
        request: outbound_bot_20191226_models.ListDownloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListDownloadTasksResponse:
        """
        @param request: ListDownloadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownloadTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownloadTasks',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListDownloadTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_download_tasks_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListDownloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListDownloadTasksResponse:
        """
        @param request: ListDownloadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownloadTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownloadTasks',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListDownloadTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_download_tasks(
        self,
        request: outbound_bot_20191226_models.ListDownloadTasksRequest,
    ) -> outbound_bot_20191226_models.ListDownloadTasksResponse:
        """
        @param request: ListDownloadTasksRequest
        @return: ListDownloadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_download_tasks_with_options(request, runtime)

    async def list_download_tasks_async(
        self,
        request: outbound_bot_20191226_models.ListDownloadTasksRequest,
    ) -> outbound_bot_20191226_models.ListDownloadTasksResponse:
        """
        @param request: ListDownloadTasksRequest
        @return: ListDownloadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_download_tasks_with_options_async(request, runtime)

    def list_flash_sms_templates_with_options(
        self,
        request: outbound_bot_20191226_models.ListFlashSmsTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListFlashSmsTemplatesResponse:
        """
        @param request: ListFlashSmsTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlashSmsTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlashSmsTemplates',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListFlashSmsTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flash_sms_templates_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListFlashSmsTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListFlashSmsTemplatesResponse:
        """
        @param request: ListFlashSmsTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlashSmsTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlashSmsTemplates',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListFlashSmsTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flash_sms_templates(
        self,
        request: outbound_bot_20191226_models.ListFlashSmsTemplatesRequest,
    ) -> outbound_bot_20191226_models.ListFlashSmsTemplatesResponse:
        """
        @param request: ListFlashSmsTemplatesRequest
        @return: ListFlashSmsTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_flash_sms_templates_with_options(request, runtime)

    async def list_flash_sms_templates_async(
        self,
        request: outbound_bot_20191226_models.ListFlashSmsTemplatesRequest,
    ) -> outbound_bot_20191226_models.ListFlashSmsTemplatesResponse:
        """
        @param request: ListFlashSmsTemplatesRequest
        @return: ListFlashSmsTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_flash_sms_templates_with_options_async(request, runtime)

    def list_global_questions_with_options(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        """
        @param request: ListGlobalQuestionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGlobalQuestionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGlobalQuestions',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListGlobalQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_global_questions_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        """
        @param request: ListGlobalQuestionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGlobalQuestionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGlobalQuestions',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListGlobalQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_global_questions(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        """
        @param request: ListGlobalQuestionsRequest
        @return: ListGlobalQuestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_global_questions_with_options(request, runtime)

    async def list_global_questions_async(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        """
        @param request: ListGlobalQuestionsRequest
        @return: ListGlobalQuestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_global_questions_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: outbound_bot_20191226_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: outbound_bot_20191226_models.ListInstancesRequest,
    ) -> outbound_bot_20191226_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: outbound_bot_20191226_models.ListInstancesRequest,
    ) -> outbound_bot_20191226_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_intentions_with_options(
        self,
        request: outbound_bot_20191226_models.ListIntentionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListIntentionsResponse:
        """
        @summary 意图列表
        
        @param request: ListIntentionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntentionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not UtilClient.is_unset(request.bot_id):
            query['BotId'] = request.bot_id
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntentions',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListIntentionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intentions_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListIntentionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListIntentionsResponse:
        """
        @summary 意图列表
        
        @param request: ListIntentionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntentionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not UtilClient.is_unset(request.bot_id):
            query['BotId'] = request.bot_id
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntentions',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListIntentionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intentions(
        self,
        request: outbound_bot_20191226_models.ListIntentionsRequest,
    ) -> outbound_bot_20191226_models.ListIntentionsResponse:
        """
        @summary 意图列表
        
        @param request: ListIntentionsRequest
        @return: ListIntentionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intentions_with_options(request, runtime)

    async def list_intentions_async(
        self,
        request: outbound_bot_20191226_models.ListIntentionsRequest,
    ) -> outbound_bot_20191226_models.ListIntentionsResponse:
        """
        @summary 意图列表
        
        @param request: ListIntentionsRequest
        @return: ListIntentionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intentions_with_options_async(request, runtime)

    def list_intents_with_options(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        """
        @param request: ListIntentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntents',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListIntentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intents_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        """
        @param request: ListIntentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntents',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListIntentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intents(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        """
        @param request: ListIntentsRequest
        @return: ListIntentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intents_with_options(request, runtime)

    async def list_intents_async(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        """
        @param request: ListIntentsRequest
        @return: ListIntentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intents_with_options_async(request, runtime)

    def list_job_groups_with_options(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        """
        @param request: ListJobGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_query):
            query['AsyncQuery'] = request.async_query
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_status_filter):
            query['JobGroupStatusFilter'] = request.job_group_status_filter
        if not UtilClient.is_unset(request.only_min_concurrency_enabled):
            query['OnlyMinConcurrencyEnabled'] = request.only_min_concurrency_enabled
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            query['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobGroups',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_groups_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        """
        @param request: ListJobGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_query):
            query['AsyncQuery'] = request.async_query
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_status_filter):
            query['JobGroupStatusFilter'] = request.job_group_status_filter
        if not UtilClient.is_unset(request.only_min_concurrency_enabled):
            query['OnlyMinConcurrencyEnabled'] = request.only_min_concurrency_enabled
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            query['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobGroups',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_groups(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        """
        @param request: ListJobGroupsRequest
        @return: ListJobGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_job_groups_with_options(request, runtime)

    async def list_job_groups_async(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        """
        @param request: ListJobGroupsRequest
        @return: ListJobGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_job_groups_with_options_async(request, runtime)

    def list_job_groups_async_with_options(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobGroupsAsyncResponse:
        """
        @param request: ListJobGroupsAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobGroupsAsyncResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobGroupsAsync',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobGroupsAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_groups_async_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobGroupsAsyncResponse:
        """
        @param request: ListJobGroupsAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobGroupsAsyncResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobGroupsAsync',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobGroupsAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_groups_async(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsAsyncRequest,
    ) -> outbound_bot_20191226_models.ListJobGroupsAsyncResponse:
        """
        @param request: ListJobGroupsAsyncRequest
        @return: ListJobGroupsAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_job_groups_async_with_options(request, runtime)

    async def list_job_groups_async_async(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsAsyncRequest,
    ) -> outbound_bot_20191226_models.ListJobGroupsAsyncResponse:
        """
        @param request: ListJobGroupsAsyncRequest
        @return: ListJobGroupsAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_job_groups_async_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        """
        @summary ListJobs
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
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
            action='ListJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        """
        @summary ListJobs
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
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
            action='ListJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        """
        @summary ListJobs
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        """
        @summary ListJobs
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_jobs_by_group_with_options(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        """
        @param request: ListJobsByGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsByGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_failure_reason):
            query['JobFailureReason'] = request.job_failure_reason
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_status):
            query['JobStatus'] = request.job_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobsByGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_by_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        """
        @param request: ListJobsByGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsByGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_failure_reason):
            query['JobFailureReason'] = request.job_failure_reason
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_status):
            query['JobStatus'] = request.job_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobsByGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsByGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs_by_group(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        """
        @param request: ListJobsByGroupRequest
        @return: ListJobsByGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_by_group_with_options(request, runtime)

    async def list_jobs_by_group_async(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        """
        @param request: ListJobsByGroupRequest
        @return: ListJobsByGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_by_group_with_options_async(request, runtime)

    def list_outbound_call_numbers_with_options(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        """
        @param request: ListOutboundCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOutboundCallNumbersResponse
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
            action='ListOutboundCallNumbers',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListOutboundCallNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_outbound_call_numbers_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        """
        @param request: ListOutboundCallNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOutboundCallNumbersResponse
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
            action='ListOutboundCallNumbers',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListOutboundCallNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_outbound_call_numbers(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        """
        @param request: ListOutboundCallNumbersRequest
        @return: ListOutboundCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_call_numbers_with_options(request, runtime)

    async def list_outbound_call_numbers_async(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        """
        @param request: ListOutboundCallNumbersRequest
        @return: ListOutboundCallNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_call_numbers_with_options_async(request, runtime)

    def list_resource_tags_with_options(
        self,
        request: outbound_bot_20191226_models.ListResourceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListResourceTagsResponse:
        """
        @param request: ListResourceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTags',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_tags_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListResourceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListResourceTagsResponse:
        """
        @param request: ListResourceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTags',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListResourceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_tags(
        self,
        request: outbound_bot_20191226_models.ListResourceTagsRequest,
    ) -> outbound_bot_20191226_models.ListResourceTagsResponse:
        """
        @param request: ListResourceTagsRequest
        @return: ListResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    async def list_resource_tags_async(
        self,
        request: outbound_bot_20191226_models.ListResourceTagsRequest,
    ) -> outbound_bot_20191226_models.ListResourceTagsResponse:
        """
        @param request: ListResourceTagsRequest
        @return: ListResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_tags_with_options_async(request, runtime)

    def list_scheduler_instances_with_options(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        """
        @param request: ListSchedulerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchedulerInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedulerInstances',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListSchedulerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduler_instances_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        """
        @param request: ListSchedulerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchedulerInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedulerInstances',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListSchedulerInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduler_instances(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        """
        @param request: ListSchedulerInstancesRequest
        @return: ListSchedulerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_scheduler_instances_with_options(request, runtime)

    async def list_scheduler_instances_async(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        """
        @param request: ListSchedulerInstancesRequest
        @return: ListSchedulerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_scheduler_instances_with_options_async(request, runtime)

    def list_script_publish_histories_with_options(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        """
        @param request: ListScriptPublishHistoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptPublishHistoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScriptPublishHistories',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptPublishHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_script_publish_histories_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        """
        @param request: ListScriptPublishHistoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptPublishHistoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScriptPublishHistories',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptPublishHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_script_publish_histories(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        """
        @param request: ListScriptPublishHistoriesRequest
        @return: ListScriptPublishHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_script_publish_histories_with_options(request, runtime)

    async def list_script_publish_histories_async(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        """
        @param request: ListScriptPublishHistoriesRequest
        @return: ListScriptPublishHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_script_publish_histories_with_options_async(request, runtime)

    def list_script_recording_with_options(
        self,
        request: outbound_bot_20191226_models.ListScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptRecordingResponse:
        """
        @param request: ListScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.ref_ids_json):
            query['RefIdsJson'] = request.ref_ids_json
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.states_json):
            query['StatesJson'] = request.states_json
        if not UtilClient.is_unset(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_script_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptRecordingResponse:
        """
        @param request: ListScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.ref_ids_json):
            query['RefIdsJson'] = request.ref_ids_json
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.states_json):
            query['StatesJson'] = request.states_json
        if not UtilClient.is_unset(request.uuids_json):
            query['UuidsJson'] = request.uuids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_script_recording(
        self,
        request: outbound_bot_20191226_models.ListScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.ListScriptRecordingResponse:
        """
        @param request: ListScriptRecordingRequest
        @return: ListScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_script_recording_with_options(request, runtime)

    async def list_script_recording_async(
        self,
        request: outbound_bot_20191226_models.ListScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.ListScriptRecordingResponse:
        """
        @param request: ListScriptRecordingRequest
        @return: ListScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_script_recording_with_options_async(request, runtime)

    def list_script_voice_configs_with_options(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        """
        @param request: ListScriptVoiceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptVoiceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScriptVoiceConfigs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptVoiceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_script_voice_configs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        """
        @param request: ListScriptVoiceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptVoiceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScriptVoiceConfigs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptVoiceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_script_voice_configs(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        """
        @param request: ListScriptVoiceConfigsRequest
        @return: ListScriptVoiceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_script_voice_configs_with_options(request, runtime)

    async def list_script_voice_configs_async(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        """
        @param request: ListScriptVoiceConfigsRequest
        @return: ListScriptVoiceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_script_voice_configs_with_options_async(request, runtime)

    def list_scripts_with_options(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        """
        @summary -\
        
        @param request: ListScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScripts',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scripts_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        """
        @summary -\
        
        @param request: ListScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScripts',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scripts(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        """
        @summary -\
        
        @param request: ListScriptsRequest
        @return: ListScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_scripts_with_options(request, runtime)

    async def list_scripts_async(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        """
        @summary -\
        
        @param request: ListScriptsRequest
        @return: ListScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_scripts_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: outbound_bot_20191226_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: outbound_bot_20191226_models.ListTagResourcesRequest,
    ) -> outbound_bot_20191226_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: outbound_bot_20191226_models.ListTagResourcesRequest,
    ) -> outbound_bot_20191226_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tags_with_options(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        """
        @param request: ListTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        """
        @param request: ListTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        """
        @param request: ListTagsRequest
        @return: ListTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        """
        @param request: ListTagsRequest
        @return: ListTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def modify_agent_profile_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyAgentProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyAgentProfileResponse:
        """
        @param tmp_req: ModifyAgentProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAgentProfileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyAgentProfileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faq_category_ids):
            request.faq_category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faq_category_ids, 'FaqCategoryIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not UtilClient.is_unset(request.api_plugin_json):
            body['ApiPluginJson'] = request.api_plugin_json
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.faq_category_ids_shrink):
            body['FaqCategoryIds'] = request.faq_category_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not UtilClient.is_unset(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not UtilClient.is_unset(request.scenario):
            body['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAgentProfile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyAgentProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_agent_profile_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyAgentProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyAgentProfileResponse:
        """
        @param tmp_req: ModifyAgentProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAgentProfileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyAgentProfileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faq_category_ids):
            request.faq_category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faq_category_ids, 'FaqCategoryIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_profile_id):
            body['AgentProfileId'] = request.agent_profile_id
        if not UtilClient.is_unset(request.api_plugin_json):
            body['ApiPluginJson'] = request.api_plugin_json
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.faq_category_ids_shrink):
            body['FaqCategoryIds'] = request.faq_category_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instruction_json):
            body['InstructionJson'] = request.instruction_json
        if not UtilClient.is_unset(request.labels_json):
            body['LabelsJson'] = request.labels_json
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.prompt_json):
            body['PromptJson'] = request.prompt_json
        if not UtilClient.is_unset(request.scenario):
            body['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.variables_json):
            body['VariablesJson'] = request.variables_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAgentProfile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyAgentProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_agent_profile(
        self,
        request: outbound_bot_20191226_models.ModifyAgentProfileRequest,
    ) -> outbound_bot_20191226_models.ModifyAgentProfileResponse:
        """
        @param request: ModifyAgentProfileRequest
        @return: ModifyAgentProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_agent_profile_with_options(request, runtime)

    async def modify_agent_profile_async(
        self,
        request: outbound_bot_20191226_models.ModifyAgentProfileRequest,
    ) -> outbound_bot_20191226_models.ModifyAgentProfileResponse:
        """
        @param request: ModifyAgentProfileRequest
        @return: ModifyAgentProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_agent_profile_with_options_async(request, runtime)

    def modify_annotation_mission_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyAnnotationMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyAnnotationMissionResponse:
        """
        @param request: ModifyAnnotationMissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnnotationMissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not UtilClient.is_unset(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not UtilClient.is_unset(request.annotation_status):
            query['AnnotationStatus'] = request.annotation_status
        if not UtilClient.is_unset(request.delete):
            query['Delete'] = request.delete
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnnotationMission',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyAnnotationMissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_annotation_mission_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyAnnotationMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyAnnotationMissionResponse:
        """
        @param request: ModifyAnnotationMissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnnotationMissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_id):
            query['AnnotationMissionId'] = request.annotation_mission_id
        if not UtilClient.is_unset(request.annotation_mission_name):
            query['AnnotationMissionName'] = request.annotation_mission_name
        if not UtilClient.is_unset(request.annotation_status):
            query['AnnotationStatus'] = request.annotation_status
        if not UtilClient.is_unset(request.delete):
            query['Delete'] = request.delete
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnnotationMission',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyAnnotationMissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_annotation_mission(
        self,
        request: outbound_bot_20191226_models.ModifyAnnotationMissionRequest,
    ) -> outbound_bot_20191226_models.ModifyAnnotationMissionResponse:
        """
        @param request: ModifyAnnotationMissionRequest
        @return: ModifyAnnotationMissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_annotation_mission_with_options(request, runtime)

    async def modify_annotation_mission_async(
        self,
        request: outbound_bot_20191226_models.ModifyAnnotationMissionRequest,
    ) -> outbound_bot_20191226_models.ModifyAnnotationMissionResponse:
        """
        @param request: ModifyAnnotationMissionRequest
        @return: ModifyAnnotationMissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_annotation_mission_with_options_async(request, runtime)

    def modify_batch_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        """
        @param request: ModifyBatchJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBatchJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not UtilClient.is_unset(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBatchJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBatchJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_batch_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        """
        @param request: ModifyBatchJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBatchJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_job_name):
            query['BatchJobName'] = request.batch_job_name
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_file_path):
            query['JobFilePath'] = request.job_file_path
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        if not UtilClient.is_unset(request.submitted):
            query['Submitted'] = request.submitted
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBatchJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBatchJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_batch_jobs(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        """
        @param request: ModifyBatchJobsRequest
        @return: ModifyBatchJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_batch_jobs_with_options(request, runtime)

    async def modify_batch_jobs_async(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        """
        @param request: ModifyBatchJobsRequest
        @return: ModifyBatchJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_batch_jobs_with_options_async(request, runtime)

    def modify_beebot_intent_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentResponse:
        """
        @summary ModifyBeebotIntent
        
        @param tmp_req: ModifyBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBeebotIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyBeebotIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBeebotIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_beebot_intent_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyBeebotIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentResponse:
        """
        @summary ModifyBeebotIntent
        
        @param tmp_req: ModifyBeebotIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBeebotIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyBeebotIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBeebotIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBeebotIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_beebot_intent(
        self,
        request: outbound_bot_20191226_models.ModifyBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentResponse:
        """
        @summary ModifyBeebotIntent
        
        @param request: ModifyBeebotIntentRequest
        @return: ModifyBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_beebot_intent_with_options(request, runtime)

    async def modify_beebot_intent_async(
        self,
        request: outbound_bot_20191226_models.ModifyBeebotIntentRequest,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentResponse:
        """
        @summary ModifyBeebotIntent
        
        @param request: ModifyBeebotIntentRequest
        @return: ModifyBeebotIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_beebot_intent_with_options_async(request, runtime)

    def modify_beebot_intent_lgf_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentLgfResponse:
        """
        @summary ModifyBeebotIntentLgf
        
        @param tmp_req: ModifyBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBeebotIntentLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyBeebotIntentLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBeebotIntentLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_beebot_intent_lgf_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyBeebotIntentLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentLgfResponse:
        """
        @summary ModifyBeebotIntentLgf
        
        @param tmp_req: ModifyBeebotIntentLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBeebotIntentLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyBeebotIntentLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBeebotIntentLgf',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBeebotIntentLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_beebot_intent_lgf(
        self,
        request: outbound_bot_20191226_models.ModifyBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentLgfResponse:
        """
        @summary ModifyBeebotIntentLgf
        
        @param request: ModifyBeebotIntentLgfRequest
        @return: ModifyBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_beebot_intent_lgf_with_options(request, runtime)

    async def modify_beebot_intent_lgf_async(
        self,
        request: outbound_bot_20191226_models.ModifyBeebotIntentLgfRequest,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentLgfResponse:
        """
        @summary ModifyBeebotIntentLgf
        
        @param request: ModifyBeebotIntentLgfRequest
        @return: ModifyBeebotIntentLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_beebot_intent_lgf_with_options_async(request, runtime)

    def modify_beebot_intent_user_say_with_options(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentUserSayResponse:
        """
        @summary ModifyBeebotIntentUserSay
        
        @param tmp_req: ModifyBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyBeebotIntentUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBeebotIntentUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_beebot_intent_user_say_with_options_async(
        self,
        tmp_req: outbound_bot_20191226_models.ModifyBeebotIntentUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentUserSayResponse:
        """
        @summary ModifyBeebotIntentUserSay
        
        @param tmp_req: ModifyBeebotIntentUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBeebotIntentUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = outbound_bot_20191226_models.ModifyBeebotIntentUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBeebotIntentUserSay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBeebotIntentUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_beebot_intent_user_say(
        self,
        request: outbound_bot_20191226_models.ModifyBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentUserSayResponse:
        """
        @summary ModifyBeebotIntentUserSay
        
        @param request: ModifyBeebotIntentUserSayRequest
        @return: ModifyBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_beebot_intent_user_say_with_options(request, runtime)

    async def modify_beebot_intent_user_say_async(
        self,
        request: outbound_bot_20191226_models.ModifyBeebotIntentUserSayRequest,
    ) -> outbound_bot_20191226_models.ModifyBeebotIntentUserSayResponse:
        """
        @summary ModifyBeebotIntentUserSay
        
        @param request: ModifyBeebotIntentUserSayRequest
        @return: ModifyBeebotIntentUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_beebot_intent_user_say_with_options_async(request, runtime)

    def modify_dialogue_flow_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        """
        @param request: ModifyDialogueFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDialogueFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dialogue_flow_definition):
            query['DialogueFlowDefinition'] = request.dialogue_flow_definition
        if not UtilClient.is_unset(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_drafted):
            query['IsDrafted'] = request.is_drafted
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDialogueFlow',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyDialogueFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dialogue_flow_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        """
        @param request: ModifyDialogueFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDialogueFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dialogue_flow_definition):
            query['DialogueFlowDefinition'] = request.dialogue_flow_definition
        if not UtilClient.is_unset(request.dialogue_flow_id):
            query['DialogueFlowId'] = request.dialogue_flow_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_drafted):
            query['IsDrafted'] = request.is_drafted
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDialogueFlow',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyDialogueFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dialogue_flow(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        """
        @param request: ModifyDialogueFlowRequest
        @return: ModifyDialogueFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dialogue_flow_with_options(request, runtime)

    async def modify_dialogue_flow_async(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        """
        @param request: ModifyDialogueFlowRequest
        @return: ModifyDialogueFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dialogue_flow_with_options_async(request, runtime)

    def modify_empty_number_no_more_calls_info_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        """
        @param request: ModifyEmptyNumberNoMoreCallsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEmptyNumberNoMoreCallsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.empty_number_no_more_calls):
            query['EmptyNumberNoMoreCalls'] = request.empty_number_no_more_calls
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEmptyNumberNoMoreCallsInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_empty_number_no_more_calls_info_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        """
        @param request: ModifyEmptyNumberNoMoreCallsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEmptyNumberNoMoreCallsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.empty_number_no_more_calls):
            query['EmptyNumberNoMoreCalls'] = request.empty_number_no_more_calls
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEmptyNumberNoMoreCallsInfo',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_empty_number_no_more_calls_info(
        self,
        request: outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
    ) -> outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        """
        @param request: ModifyEmptyNumberNoMoreCallsInfoRequest
        @return: ModifyEmptyNumberNoMoreCallsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_empty_number_no_more_calls_info_with_options(request, runtime)

    async def modify_empty_number_no_more_calls_info_async(
        self,
        request: outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoRequest,
    ) -> outbound_bot_20191226_models.ModifyEmptyNumberNoMoreCallsInfoResponse:
        """
        @param request: ModifyEmptyNumberNoMoreCallsInfoRequest
        @return: ModifyEmptyNumberNoMoreCallsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_empty_number_no_more_calls_info_with_options_async(request, runtime)

    def modify_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        """
        @param request: ModifyGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.answers):
            query['Answers'] = request.answers
        if not UtilClient.is_unset(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not UtilClient.is_unset(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not UtilClient.is_unset(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.questions):
            query['Questions'] = request.questions
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyGlobalQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        """
        @param request: ModifyGlobalQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalQuestionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.answers):
            query['Answers'] = request.answers
        if not UtilClient.is_unset(request.global_question_id):
            query['GlobalQuestionId'] = request.global_question_id
        if not UtilClient.is_unset(request.global_question_name):
            query['GlobalQuestionName'] = request.global_question_name
        if not UtilClient.is_unset(request.global_question_type):
            query['GlobalQuestionType'] = request.global_question_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.questions):
            query['Questions'] = request.questions
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalQuestion',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyGlobalQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_question(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        """
        @param request: ModifyGlobalQuestionRequest
        @return: ModifyGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_question_with_options(request, runtime)

    async def modify_global_question_async(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        """
        @param request: ModifyGlobalQuestionRequest
        @return: ModifyGlobalQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_question_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_concurrent_conversation):
            query['MaxConcurrentConversation'] = request.max_concurrent_conversation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_intent_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        """
        @param request: ModifyIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        """
        @param request: ModifyIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIntentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_description):
            query['IntentDescription'] = request.intent_description
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.utterances):
            query['Utterances'] = request.utterances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIntent',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_intent(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        """
        @param request: ModifyIntentRequest
        @return: ModifyIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_intent_with_options(request, runtime)

    async def modify_intent_async(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        """
        @param request: ModifyIntentRequest
        @return: ModifyIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_intent_with_options_async(request, runtime)

    def modify_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        """
        @param request: ModifyJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_group_status):
            query['JobGroupStatus'] = request.job_group_status
        if not UtilClient.is_unset(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not UtilClient.is_unset(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not UtilClient.is_unset(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyJobGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        """
        @param request: ModifyJobGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyJobGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flash_sms_extras):
            query['FlashSmsExtras'] = request.flash_sms_extras
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_group_status):
            query['JobGroupStatus'] = request.job_group_status
        if not UtilClient.is_unset(request.min_concurrency):
            query['MinConcurrency'] = request.min_concurrency
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.recall_calling_number):
            query['RecallCallingNumber'] = request.recall_calling_number
        if not UtilClient.is_unset(request.recall_strategy_json):
            query['RecallStrategyJson'] = request.recall_strategy_json
        if not UtilClient.is_unset(request.ringing_duration):
            query['RingingDuration'] = request.ringing_duration
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.strategy_json):
            query['StrategyJson'] = request.strategy_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyJobGroup',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyJobGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_job_group(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        """
        @param request: ModifyJobGroupRequest
        @return: ModifyJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_job_group_with_options(request, runtime)

    async def modify_job_group_async(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        """
        @param request: ModifyJobGroupRequest
        @return: ModifyJobGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_job_group_with_options_async(request, runtime)

    def modify_outbound_call_number_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        """
        @summary ModifyOutboundCallNumber
        
        @param request: ModifyOutboundCallNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOutboundCallNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        if not UtilClient.is_unset(request.rate_limit_count):
            query['RateLimitCount'] = request.rate_limit_count
        if not UtilClient.is_unset(request.rate_limit_period):
            query['RateLimitPeriod'] = request.rate_limit_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOutboundCallNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyOutboundCallNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_outbound_call_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        """
        @summary ModifyOutboundCallNumber
        
        @param request: ModifyOutboundCallNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOutboundCallNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.outbound_call_number_id):
            query['OutboundCallNumberId'] = request.outbound_call_number_id
        if not UtilClient.is_unset(request.rate_limit_count):
            query['RateLimitCount'] = request.rate_limit_count
        if not UtilClient.is_unset(request.rate_limit_period):
            query['RateLimitPeriod'] = request.rate_limit_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOutboundCallNumber',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyOutboundCallNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_outbound_call_number(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        """
        @summary ModifyOutboundCallNumber
        
        @param request: ModifyOutboundCallNumberRequest
        @return: ModifyOutboundCallNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_outbound_call_number_with_options(request, runtime)

    async def modify_outbound_call_number_async(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        """
        @summary ModifyOutboundCallNumber
        
        @param request: ModifyOutboundCallNumberRequest
        @return: ModifyOutboundCallNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_outbound_call_number_with_options_async(request, runtime)

    def modify_script_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        """
        @summary 修改场景
        
        @param request: ModifyScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not UtilClient.is_unset(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not UtilClient.is_unset(request.chat_config):
            query['ChatConfig'] = request.chat_config
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.label_config):
            query['LabelConfig'] = request.label_config
        if not UtilClient.is_unset(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not UtilClient.is_unset(request.mini_playback_config_list_json_string):
            query['MiniPlaybackConfigListJsonString'] = request.mini_playback_config_list_json_string
        if not UtilClient.is_unset(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not UtilClient.is_unset(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not UtilClient.is_unset(request.nls_config):
            query['NlsConfig'] = request.nls_config
        if not UtilClient.is_unset(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not UtilClient.is_unset(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        """
        @summary 修改场景
        
        @param request: ModifyScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.agent_llm):
            query['AgentLlm'] = request.agent_llm
        if not UtilClient.is_unset(request.asr_config):
            query['AsrConfig'] = request.asr_config
        if not UtilClient.is_unset(request.chat_config):
            query['ChatConfig'] = request.chat_config
        if not UtilClient.is_unset(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.emotion_enable):
            query['EmotionEnable'] = request.emotion_enable
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.label_config):
            query['LabelConfig'] = request.label_config
        if not UtilClient.is_unset(request.long_wait_enable):
            query['LongWaitEnable'] = request.long_wait_enable
        if not UtilClient.is_unset(request.mini_playback_config_list_json_string):
            query['MiniPlaybackConfigListJsonString'] = request.mini_playback_config_list_json_string
        if not UtilClient.is_unset(request.mini_playback_enable):
            query['MiniPlaybackEnable'] = request.mini_playback_enable
        if not UtilClient.is_unset(request.new_barge_in_enable):
            query['NewBargeInEnable'] = request.new_barge_in_enable
        if not UtilClient.is_unset(request.nls_config):
            query['NlsConfig'] = request.nls_config
        if not UtilClient.is_unset(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        if not UtilClient.is_unset(request.nlu_engine):
            query['NluEngine'] = request.nlu_engine
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_description):
            query['ScriptDescription'] = request.script_description
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_waveform):
            query['ScriptWaveform'] = request.script_waveform
        if not UtilClient.is_unset(request.tts_config):
            query['TtsConfig'] = request.tts_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_script(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        """
        @summary 修改场景
        
        @param request: ModifyScriptRequest
        @return: ModifyScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_script_with_options(request, runtime)

    async def modify_script_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        """
        @summary 修改场景
        
        @param request: ModifyScriptRequest
        @return: ModifyScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_script_with_options_async(request, runtime)

    def modify_script_voice_config_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        """
        @param request: ModifyScriptVoiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScriptVoiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        if not UtilClient.is_unset(request.script_waveform_relation):
            query['ScriptWaveformRelation'] = request.script_waveform_relation
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScriptVoiceConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_script_voice_config_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        """
        @param request: ModifyScriptVoiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScriptVoiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_voice_config_id):
            query['ScriptVoiceConfigId'] = request.script_voice_config_id
        if not UtilClient.is_unset(request.script_waveform_relation):
            query['ScriptWaveformRelation'] = request.script_waveform_relation
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScriptVoiceConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_script_voice_config(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        """
        @param request: ModifyScriptVoiceConfigRequest
        @return: ModifyScriptVoiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_script_voice_config_with_options(request, runtime)

    async def modify_script_voice_config_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        """
        @param request: ModifyScriptVoiceConfigRequest
        @return: ModifyScriptVoiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_script_voice_config_with_options_async(request, runtime)

    def modify_ttsconfig_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        """
        @param request: ModifyTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTTSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not UtilClient.is_unset(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTTSConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ttsconfig_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        """
        @param request: ModifyTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTTSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not UtilClient.is_unset(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTTSConfig',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ttsconfig(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        """
        @param request: ModifyTTSConfigRequest
        @return: ModifyTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ttsconfig_with_options(request, runtime)

    async def modify_ttsconfig_async(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        """
        @param request: ModifyTTSConfigRequest
        @return: ModifyTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_ttsconfig_with_options_async(request, runtime)

    def modify_tag_groups_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        """
        @param request: ModifyTagGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.tag_groups):
            query['TagGroups'] = request.tag_groups
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTagGroups',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTagGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tag_groups_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        """
        @param request: ModifyTagGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.tag_groups):
            query['TagGroups'] = request.tag_groups
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTagGroups',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTagGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tag_groups(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        """
        @param request: ModifyTagGroupsRequest
        @return: ModifyTagGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_groups_with_options(request, runtime)

    async def modify_tag_groups_async(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        """
        @param request: ModifyTagGroupsRequest
        @return: ModifyTagGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tag_groups_with_options_async(request, runtime)

    def publish_script_with_options(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        """
        @param request: PublishScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        """
        @param request: PublishScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_script(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        """
        @param request: PublishScriptRequest
        @return: PublishScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_script_with_options(request, runtime)

    async def publish_script_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        """
        @param request: PublishScriptRequest
        @return: PublishScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_script_with_options_async(request, runtime)

    def publish_script_for_debug_with_options(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        """
        @param request: PublishScriptForDebugRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishScriptForDebugResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScriptForDebug',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptForDebugResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_script_for_debug_with_options_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        """
        @param request: PublishScriptForDebugRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishScriptForDebugResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScriptForDebug',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptForDebugResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_script_for_debug(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        """
        @param request: PublishScriptForDebugRequest
        @return: PublishScriptForDebugResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_script_for_debug_with_options(request, runtime)

    async def publish_script_for_debug_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        """
        @param request: PublishScriptForDebugRequest
        @return: PublishScriptForDebugResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_script_for_debug_with_options_async(request, runtime)

    def query_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        """
        @summary QueryJobs
        
        @param request: QueryJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_alignment):
            query['TimeAlignment'] = request.time_alignment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        """
        @summary QueryJobs
        
        @param request: QueryJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_alignment):
            query['TimeAlignment'] = request.time_alignment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_jobs(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        """
        @summary QueryJobs
        
        @param request: QueryJobsRequest
        @return: QueryJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_jobs_with_options(request, runtime)

    async def query_jobs_async(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        """
        @summary QueryJobs
        
        @param request: QueryJobsRequest
        @return: QueryJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_jobs_with_options_async(request, runtime)

    def query_jobs_with_result_with_options(
        self,
        request: outbound_bot_20191226_models.QueryJobsWithResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryJobsWithResultResponse:
        """
        @summary 获取外呼任务结果信息
        
        @param request: QueryJobsWithResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryJobsWithResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_actual_time_filter):
            query['EndActualTimeFilter'] = request.end_actual_time_filter
        if not UtilClient.is_unset(request.has_answered_filter):
            query['HasAnsweredFilter'] = request.has_answered_filter
        if not UtilClient.is_unset(request.has_hang_up_by_rejection_filter):
            query['HasHangUpByRejectionFilter'] = request.has_hang_up_by_rejection_filter
        if not UtilClient.is_unset(request.has_reached_end_of_flow_filter):
            query['HasReachedEndOfFlowFilter'] = request.has_reached_end_of_flow_filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_failure_reasons_filter):
            query['JobFailureReasonsFilter'] = request.job_failure_reasons_filter
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_status_filter):
            query['JobStatusFilter'] = request.job_status_filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_text):
            query['QueryText'] = request.query_text
        if not UtilClient.is_unset(request.start_actual_time_filter):
            query['StartActualTimeFilter'] = request.start_actual_time_filter
        if not UtilClient.is_unset(request.task_status_filter):
            query['TaskStatusFilter'] = request.task_status_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobsWithResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryJobsWithResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_jobs_with_result_with_options_async(
        self,
        request: outbound_bot_20191226_models.QueryJobsWithResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryJobsWithResultResponse:
        """
        @summary 获取外呼任务结果信息
        
        @param request: QueryJobsWithResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryJobsWithResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_actual_time_filter):
            query['EndActualTimeFilter'] = request.end_actual_time_filter
        if not UtilClient.is_unset(request.has_answered_filter):
            query['HasAnsweredFilter'] = request.has_answered_filter
        if not UtilClient.is_unset(request.has_hang_up_by_rejection_filter):
            query['HasHangUpByRejectionFilter'] = request.has_hang_up_by_rejection_filter
        if not UtilClient.is_unset(request.has_reached_end_of_flow_filter):
            query['HasReachedEndOfFlowFilter'] = request.has_reached_end_of_flow_filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_failure_reasons_filter):
            query['JobFailureReasonsFilter'] = request.job_failure_reasons_filter
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_status_filter):
            query['JobStatusFilter'] = request.job_status_filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_text):
            query['QueryText'] = request.query_text
        if not UtilClient.is_unset(request.start_actual_time_filter):
            query['StartActualTimeFilter'] = request.start_actual_time_filter
        if not UtilClient.is_unset(request.task_status_filter):
            query['TaskStatusFilter'] = request.task_status_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobsWithResult',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryJobsWithResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_jobs_with_result(
        self,
        request: outbound_bot_20191226_models.QueryJobsWithResultRequest,
    ) -> outbound_bot_20191226_models.QueryJobsWithResultResponse:
        """
        @summary 获取外呼任务结果信息
        
        @param request: QueryJobsWithResultRequest
        @return: QueryJobsWithResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_jobs_with_result_with_options(request, runtime)

    async def query_jobs_with_result_async(
        self,
        request: outbound_bot_20191226_models.QueryJobsWithResultRequest,
    ) -> outbound_bot_20191226_models.QueryJobsWithResultResponse:
        """
        @summary 获取外呼任务结果信息
        
        @param request: QueryJobsWithResultRequest
        @return: QueryJobsWithResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_jobs_with_result_with_options_async(request, runtime)

    def query_script_waveforms_with_options(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        """
        @param request: QueryScriptWaveformsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryScriptWaveformsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScriptWaveforms',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptWaveformsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_script_waveforms_with_options_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        """
        @param request: QueryScriptWaveformsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryScriptWaveformsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScriptWaveforms',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptWaveformsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_script_waveforms(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        """
        @param request: QueryScriptWaveformsRequest
        @return: QueryScriptWaveformsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_script_waveforms_with_options(request, runtime)

    async def query_script_waveforms_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        """
        @param request: QueryScriptWaveformsRequest
        @return: QueryScriptWaveformsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_script_waveforms_with_options_async(request, runtime)

    def query_scripts_by_status_with_options(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        """
        @param request: QueryScriptsByStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryScriptsByStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScriptsByStatus',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptsByStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scripts_by_status_with_options_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        """
        @param request: QueryScriptsByStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryScriptsByStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScriptsByStatus',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptsByStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scripts_by_status(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        """
        @param request: QueryScriptsByStatusRequest
        @return: QueryScriptsByStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_scripts_by_status_with_options(request, runtime)

    async def query_scripts_by_status_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        """
        @param request: QueryScriptsByStatusRequest
        @return: QueryScriptsByStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_scripts_by_status_with_options_async(request, runtime)

    def record_failure_with_options(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        """
        @param request: RecordFailureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecordFailureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actual_time):
            query['ActualTime'] = request.actual_time
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.disposition_code):
            query['DispositionCode'] = request.disposition_code
        if not UtilClient.is_unset(request.exception_codes):
            query['ExceptionCodes'] = request.exception_codes
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordFailure',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RecordFailureResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_failure_with_options_async(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        """
        @param request: RecordFailureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecordFailureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actual_time):
            query['ActualTime'] = request.actual_time
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.disposition_code):
            query['DispositionCode'] = request.disposition_code
        if not UtilClient.is_unset(request.exception_codes):
            query['ExceptionCodes'] = request.exception_codes
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordFailure',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RecordFailureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_failure(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        """
        @param request: RecordFailureRequest
        @return: RecordFailureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.record_failure_with_options(request, runtime)

    async def record_failure_async(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        """
        @param request: RecordFailureRequest
        @return: RecordFailureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.record_failure_with_options_async(request, runtime)

    def resume_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        """
        @param request: ResumeJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ResumeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        """
        @param request: ResumeJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ResumeJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_jobs(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        """
        @param request: ResumeJobsRequest
        @return: ResumeJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_jobs_with_options(request, runtime)

    async def resume_jobs_async(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        """
        @param request: ResumeJobsRequest
        @return: ResumeJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_jobs_with_options_async(request, runtime)

    def rollback_script_with_options(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        """
        @param request: RollbackScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rollback_version):
            query['RollbackVersion'] = request.rollback_version
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RollbackScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        """
        @param request: RollbackScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rollback_version):
            query['RollbackVersion'] = request.rollback_version
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackScript',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RollbackScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_script(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        """
        @param request: RollbackScriptRequest
        @return: RollbackScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_script_with_options(request, runtime)

    async def rollback_script_async(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        """
        @param request: RollbackScriptRequest
        @return: RollbackScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_script_with_options_async(request, runtime)

    def save_after_answer_delay_playback_with_options(
        self,
        request: outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackResponse:
        """
        @param request: SaveAfterAnswerDelayPlaybackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAfterAnswerDelayPlaybackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after_answer_delay_playback):
            query['AfterAnswerDelayPlayback'] = request.after_answer_delay_playback
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAfterAnswerDelayPlayback',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_after_answer_delay_playback_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackResponse:
        """
        @param request: SaveAfterAnswerDelayPlaybackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAfterAnswerDelayPlaybackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after_answer_delay_playback):
            query['AfterAnswerDelayPlayback'] = request.after_answer_delay_playback
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAfterAnswerDelayPlayback',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_after_answer_delay_playback(
        self,
        request: outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackRequest,
    ) -> outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackResponse:
        """
        @param request: SaveAfterAnswerDelayPlaybackRequest
        @return: SaveAfterAnswerDelayPlaybackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_after_answer_delay_playback_with_options(request, runtime)

    async def save_after_answer_delay_playback_async(
        self,
        request: outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackRequest,
    ) -> outbound_bot_20191226_models.SaveAfterAnswerDelayPlaybackResponse:
        """
        @param request: SaveAfterAnswerDelayPlaybackRequest
        @return: SaveAfterAnswerDelayPlaybackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_after_answer_delay_playback_with_options_async(request, runtime)

    def save_annotation_mission_session_list_with_options(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionSessionListResponse:
        """
        @param request: SaveAnnotationMissionSessionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAnnotationMissionSessionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not UtilClient.is_unset(request.annotation_mission_session_list):
            query['AnnotationMissionSessionList'] = request.annotation_mission_session_list
        if not UtilClient.is_unset(request.annotation_mission_session_list_json_string):
            query['AnnotationMissionSessionListJsonString'] = request.annotation_mission_session_list_json_string
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAnnotationMissionSessionList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveAnnotationMissionSessionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_annotation_mission_session_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionSessionListResponse:
        """
        @param request: SaveAnnotationMissionSessionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAnnotationMissionSessionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.annotation_mission_data_source_type):
            query['AnnotationMissionDataSourceType'] = request.annotation_mission_data_source_type
        if not UtilClient.is_unset(request.annotation_mission_session_list):
            query['AnnotationMissionSessionList'] = request.annotation_mission_session_list
        if not UtilClient.is_unset(request.annotation_mission_session_list_json_string):
            query['AnnotationMissionSessionListJsonString'] = request.annotation_mission_session_list_json_string
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAnnotationMissionSessionList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveAnnotationMissionSessionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_annotation_mission_session_list(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionSessionListRequest,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionSessionListResponse:
        """
        @param request: SaveAnnotationMissionSessionListRequest
        @return: SaveAnnotationMissionSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_annotation_mission_session_list_with_options(request, runtime)

    async def save_annotation_mission_session_list_async(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionSessionListRequest,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionSessionListResponse:
        """
        @param request: SaveAnnotationMissionSessionListRequest
        @return: SaveAnnotationMissionSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_annotation_mission_session_list_with_options_async(request, runtime)

    def save_annotation_mission_tag_info_list_with_options(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListResponse:
        """
        @param request: SaveAnnotationMissionTagInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAnnotationMissionTagInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_tag_info_list):
            query['AnnotationMissionTagInfoList'] = request.annotation_mission_tag_info_list
        if not UtilClient.is_unset(request.annotation_mission_tag_info_list_json_string):
            query['AnnotationMissionTagInfoListJsonString'] = request.annotation_mission_tag_info_list_json_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reset):
            query['Reset'] = request.reset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAnnotationMissionTagInfoList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_annotation_mission_tag_info_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListResponse:
        """
        @param request: SaveAnnotationMissionTagInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAnnotationMissionTagInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotation_mission_tag_info_list):
            query['AnnotationMissionTagInfoList'] = request.annotation_mission_tag_info_list
        if not UtilClient.is_unset(request.annotation_mission_tag_info_list_json_string):
            query['AnnotationMissionTagInfoListJsonString'] = request.annotation_mission_tag_info_list_json_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reset):
            query['Reset'] = request.reset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAnnotationMissionTagInfoList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_annotation_mission_tag_info_list(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListRequest,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListResponse:
        """
        @param request: SaveAnnotationMissionTagInfoListRequest
        @return: SaveAnnotationMissionTagInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_annotation_mission_tag_info_list_with_options(request, runtime)

    async def save_annotation_mission_tag_info_list_async(
        self,
        request: outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListRequest,
    ) -> outbound_bot_20191226_models.SaveAnnotationMissionTagInfoListResponse:
        """
        @param request: SaveAnnotationMissionTagInfoListRequest
        @return: SaveAnnotationMissionTagInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_annotation_mission_tag_info_list_with_options_async(request, runtime)

    def save_base_strategy_period_with_options(
        self,
        request: outbound_bot_20191226_models.SaveBaseStrategyPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveBaseStrategyPeriodResponse:
        """
        @param request: SaveBaseStrategyPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBaseStrategyPeriodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.only_weekdays):
            query['OnlyWeekdays'] = request.only_weekdays
        if not UtilClient.is_unset(request.only_workdays):
            query['OnlyWorkdays'] = request.only_workdays
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        if not UtilClient.is_unset(request.working_time):
            query['WorkingTime'] = request.working_time
        if not UtilClient.is_unset(request.working_time_frames_json):
            query['WorkingTimeFramesJson'] = request.working_time_frames_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBaseStrategyPeriod',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveBaseStrategyPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_base_strategy_period_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveBaseStrategyPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveBaseStrategyPeriodResponse:
        """
        @param request: SaveBaseStrategyPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBaseStrategyPeriodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.only_weekdays):
            query['OnlyWeekdays'] = request.only_weekdays
        if not UtilClient.is_unset(request.only_workdays):
            query['OnlyWorkdays'] = request.only_workdays
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        if not UtilClient.is_unset(request.working_time):
            query['WorkingTime'] = request.working_time
        if not UtilClient.is_unset(request.working_time_frames_json):
            query['WorkingTimeFramesJson'] = request.working_time_frames_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBaseStrategyPeriod',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveBaseStrategyPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_base_strategy_period(
        self,
        request: outbound_bot_20191226_models.SaveBaseStrategyPeriodRequest,
    ) -> outbound_bot_20191226_models.SaveBaseStrategyPeriodResponse:
        """
        @param request: SaveBaseStrategyPeriodRequest
        @return: SaveBaseStrategyPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_base_strategy_period_with_options(request, runtime)

    async def save_base_strategy_period_async(
        self,
        request: outbound_bot_20191226_models.SaveBaseStrategyPeriodRequest,
    ) -> outbound_bot_20191226_models.SaveBaseStrategyPeriodResponse:
        """
        @param request: SaveBaseStrategyPeriodRequest
        @return: SaveBaseStrategyPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_base_strategy_period_with_options_async(request, runtime)

    def save_contact_block_list_with_options(
        self,
        request: outbound_bot_20191226_models.SaveContactBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveContactBlockListResponse:
        """
        @param request: SaveContactBlockListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveContactBlockListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_block_list_list):
            query['ContactBlockListList'] = request.contact_block_list_list
        if not UtilClient.is_unset(request.contact_block_lists_json):
            query['ContactBlockListsJson'] = request.contact_block_lists_json
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveContactBlockList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveContactBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_contact_block_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveContactBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveContactBlockListResponse:
        """
        @param request: SaveContactBlockListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveContactBlockListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_block_list_list):
            query['ContactBlockListList'] = request.contact_block_list_list
        if not UtilClient.is_unset(request.contact_block_lists_json):
            query['ContactBlockListsJson'] = request.contact_block_lists_json
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveContactBlockList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveContactBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_contact_block_list(
        self,
        request: outbound_bot_20191226_models.SaveContactBlockListRequest,
    ) -> outbound_bot_20191226_models.SaveContactBlockListResponse:
        """
        @param request: SaveContactBlockListRequest
        @return: SaveContactBlockListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_contact_block_list_with_options(request, runtime)

    async def save_contact_block_list_async(
        self,
        request: outbound_bot_20191226_models.SaveContactBlockListRequest,
    ) -> outbound_bot_20191226_models.SaveContactBlockListResponse:
        """
        @param request: SaveContactBlockListRequest
        @return: SaveContactBlockListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_contact_block_list_with_options_async(request, runtime)

    def save_contact_white_list_with_options(
        self,
        request: outbound_bot_20191226_models.SaveContactWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveContactWhiteListResponse:
        """
        @param request: SaveContactWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveContactWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_white_list_list):
            query['ContactWhiteListList'] = request.contact_white_list_list
        if not UtilClient.is_unset(request.contact_white_lists_json):
            query['ContactWhiteListsJson'] = request.contact_white_lists_json
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveContactWhiteList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveContactWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_contact_white_list_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveContactWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveContactWhiteListResponse:
        """
        @param request: SaveContactWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveContactWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_white_list_list):
            query['ContactWhiteListList'] = request.contact_white_list_list
        if not UtilClient.is_unset(request.contact_white_lists_json):
            query['ContactWhiteListsJson'] = request.contact_white_lists_json
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveContactWhiteList',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveContactWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_contact_white_list(
        self,
        request: outbound_bot_20191226_models.SaveContactWhiteListRequest,
    ) -> outbound_bot_20191226_models.SaveContactWhiteListResponse:
        """
        @param request: SaveContactWhiteListRequest
        @return: SaveContactWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_contact_white_list_with_options(request, runtime)

    async def save_contact_white_list_async(
        self,
        request: outbound_bot_20191226_models.SaveContactWhiteListRequest,
    ) -> outbound_bot_20191226_models.SaveContactWhiteListResponse:
        """
        @param request: SaveContactWhiteListRequest
        @return: SaveContactWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_contact_white_list_with_options_async(request, runtime)

    def save_effective_days_with_options(
        self,
        request: outbound_bot_20191226_models.SaveEffectiveDaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveEffectiveDaysResponse:
        """
        @param request: SaveEffectiveDaysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveEffectiveDaysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_days):
            query['EffectiveDays'] = request.effective_days
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveEffectiveDays',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveEffectiveDaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_effective_days_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveEffectiveDaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveEffectiveDaysResponse:
        """
        @param request: SaveEffectiveDaysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveEffectiveDaysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_days):
            query['EffectiveDays'] = request.effective_days
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveEffectiveDays',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveEffectiveDaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_effective_days(
        self,
        request: outbound_bot_20191226_models.SaveEffectiveDaysRequest,
    ) -> outbound_bot_20191226_models.SaveEffectiveDaysResponse:
        """
        @param request: SaveEffectiveDaysRequest
        @return: SaveEffectiveDaysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_effective_days_with_options(request, runtime)

    async def save_effective_days_async(
        self,
        request: outbound_bot_20191226_models.SaveEffectiveDaysRequest,
    ) -> outbound_bot_20191226_models.SaveEffectiveDaysResponse:
        """
        @param request: SaveEffectiveDaysRequest
        @return: SaveEffectiveDaysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_effective_days_with_options_async(request, runtime)

    def save_max_attempts_per_day_with_options(
        self,
        request: outbound_bot_20191226_models.SaveMaxAttemptsPerDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveMaxAttemptsPerDayResponse:
        """
        @param request: SaveMaxAttemptsPerDayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMaxAttemptsPerDayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.max_attempts_per_day):
            query['MaxAttemptsPerDay'] = request.max_attempts_per_day
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveMaxAttemptsPerDay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveMaxAttemptsPerDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_max_attempts_per_day_with_options_async(
        self,
        request: outbound_bot_20191226_models.SaveMaxAttemptsPerDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SaveMaxAttemptsPerDayResponse:
        """
        @param request: SaveMaxAttemptsPerDayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMaxAttemptsPerDayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        if not UtilClient.is_unset(request.max_attempts_per_day):
            query['MaxAttemptsPerDay'] = request.max_attempts_per_day
        if not UtilClient.is_unset(request.strategy_level):
            query['StrategyLevel'] = request.strategy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveMaxAttemptsPerDay',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SaveMaxAttemptsPerDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_max_attempts_per_day(
        self,
        request: outbound_bot_20191226_models.SaveMaxAttemptsPerDayRequest,
    ) -> outbound_bot_20191226_models.SaveMaxAttemptsPerDayResponse:
        """
        @param request: SaveMaxAttemptsPerDayRequest
        @return: SaveMaxAttemptsPerDayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_max_attempts_per_day_with_options(request, runtime)

    async def save_max_attempts_per_day_async(
        self,
        request: outbound_bot_20191226_models.SaveMaxAttemptsPerDayRequest,
    ) -> outbound_bot_20191226_models.SaveMaxAttemptsPerDayResponse:
        """
        @param request: SaveMaxAttemptsPerDayRequest
        @return: SaveMaxAttemptsPerDayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_max_attempts_per_day_with_options_async(request, runtime)

    def search_task_with_options(
        self,
        request: outbound_bot_20191226_models.SearchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SearchTaskResponse:
        """
        @summary 外呼历史查询
        
        @param request: SearchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_task_with_options_async(
        self,
        request: outbound_bot_20191226_models.SearchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SearchTaskResponse:
        """
        @summary 外呼历史查询
        
        @param request: SearchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTask',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SearchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_task(
        self,
        request: outbound_bot_20191226_models.SearchTaskRequest,
    ) -> outbound_bot_20191226_models.SearchTaskResponse:
        """
        @summary 外呼历史查询
        
        @param request: SearchTaskRequest
        @return: SearchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_task_with_options(request, runtime)

    async def search_task_async(
        self,
        request: outbound_bot_20191226_models.SearchTaskRequest,
    ) -> outbound_bot_20191226_models.SearchTaskResponse:
        """
        @summary 外呼历史查询
        
        @param request: SearchTaskRequest
        @return: SearchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_task_with_options_async(request, runtime)

    def start_job_with_options(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        """
        @param request: StartJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_json):
            query['JobJson'] = request.job_json
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.StartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_options_async(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        """
        @param request: StartJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_json):
            query['JobJson'] = request.job_json
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.StartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        """
        @param request: StartJobRequest
        @return: StartJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_job_with_options(request, runtime)

    async def start_job_async(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        """
        @param request: StartJobRequest
        @return: StartJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_job_with_options_async(request, runtime)

    def submit_batch_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        """
        @param request: SubmitBatchJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitBatchJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBatchJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitBatchJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_batch_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        """
        @param request: SubmitBatchJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitBatchJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBatchJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitBatchJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_batch_jobs(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        """
        @param request: SubmitBatchJobsRequest
        @return: SubmitBatchJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_batch_jobs_with_options(request, runtime)

    async def submit_batch_jobs_async(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        """
        @param request: SubmitBatchJobsRequest
        @return: SubmitBatchJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_batch_jobs_with_options_async(request, runtime)

    def submit_recording_with_options(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        """
        @param request: SubmitRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merged_recording):
            query['MergedRecording'] = request.merged_recording
        if not UtilClient.is_unset(request.resource_recording):
            query['ResourceRecording'] = request.resource_recording
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        """
        @param request: SubmitRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merged_recording):
            query['MergedRecording'] = request.merged_recording
        if not UtilClient.is_unset(request.resource_recording):
            query['ResourceRecording'] = request.resource_recording
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_recording(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        """
        @param request: SubmitRecordingRequest
        @return: SubmitRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_recording_with_options(request, runtime)

    async def submit_recording_async(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        """
        @param request: SubmitRecordingRequest
        @return: SubmitRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_recording_with_options_async(request, runtime)

    def submit_script_review_with_options(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        """
        @param request: SubmitScriptReviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitScriptReviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitScriptReview',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitScriptReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_script_review_with_options_async(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        """
        @param request: SubmitScriptReviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitScriptReviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitScriptReview',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitScriptReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_script_review(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        """
        @param request: SubmitScriptReviewRequest
        @return: SubmitScriptReviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_script_review_with_options(request, runtime)

    async def submit_script_review_async(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        """
        @param request: SubmitScriptReviewRequest
        @return: SubmitScriptReviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_script_review_with_options_async(request, runtime)

    def suspend_call_with_options(
        self,
        request: outbound_bot_20191226_models.SuspendCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendCallResponse:
        """
        @param request: SuspendCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_numbers):
            query['CalledNumbers'] = request.called_numbers
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendCall',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_call_with_options_async(
        self,
        request: outbound_bot_20191226_models.SuspendCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendCallResponse:
        """
        @param request: SuspendCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_numbers):
            query['CalledNumbers'] = request.called_numbers
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendCall',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_call(
        self,
        request: outbound_bot_20191226_models.SuspendCallRequest,
    ) -> outbound_bot_20191226_models.SuspendCallResponse:
        """
        @param request: SuspendCallRequest
        @return: SuspendCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_call_with_options(request, runtime)

    async def suspend_call_async(
        self,
        request: outbound_bot_20191226_models.SuspendCallRequest,
    ) -> outbound_bot_20191226_models.SuspendCallResponse:
        """
        @param request: SuspendCallRequest
        @return: SuspendCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_call_with_options_async(request, runtime)

    def suspend_call_with_file_with_options(
        self,
        request: outbound_bot_20191226_models.SuspendCallWithFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendCallWithFileResponse:
        """
        @param request: SuspendCallWithFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendCallWithFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendCallWithFile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendCallWithFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_call_with_file_with_options_async(
        self,
        request: outbound_bot_20191226_models.SuspendCallWithFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendCallWithFileResponse:
        """
        @param request: SuspendCallWithFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendCallWithFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendCallWithFile',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendCallWithFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_call_with_file(
        self,
        request: outbound_bot_20191226_models.SuspendCallWithFileRequest,
    ) -> outbound_bot_20191226_models.SuspendCallWithFileResponse:
        """
        @param request: SuspendCallWithFileRequest
        @return: SuspendCallWithFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_call_with_file_with_options(request, runtime)

    async def suspend_call_with_file_async(
        self,
        request: outbound_bot_20191226_models.SuspendCallWithFileRequest,
    ) -> outbound_bot_20191226_models.SuspendCallWithFileResponse:
        """
        @param request: SuspendCallWithFileRequest
        @return: SuspendCallWithFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_call_with_file_with_options_async(request, runtime)

    def suspend_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        """
        @param request: SuspendJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        """
        @param request: SuspendJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_group_id):
            query['JobGroupId'] = request.job_group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_reference_id):
            query['JobReferenceId'] = request.job_reference_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendJobs',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_jobs(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        """
        @param request: SuspendJobsRequest
        @return: SuspendJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_jobs_with_options(request, runtime)

    async def suspend_jobs_async(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        """
        @param request: SuspendJobsRequest
        @return: SuspendJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_jobs_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: outbound_bot_20191226_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TagResourcesResponse:
        """
        @description *\
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: outbound_bot_20191226_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TagResourcesResponse:
        """
        @description *\
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: outbound_bot_20191226_models.TagResourcesRequest,
    ) -> outbound_bot_20191226_models.TagResourcesResponse:
        """
        @description *\
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: outbound_bot_20191226_models.TagResourcesRequest,
    ) -> outbound_bot_20191226_models.TagResourcesResponse:
        """
        @description *\
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def task_preparing_with_options(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        """
        @summary TaskPreparing
        
        @param request: TaskPreparingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TaskPreparingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskPreparing',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TaskPreparingResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_preparing_with_options_async(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        """
        @summary TaskPreparing
        
        @param request: TaskPreparingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TaskPreparingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskPreparing',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TaskPreparingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_preparing(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        """
        @summary TaskPreparing
        
        @param request: TaskPreparingRequest
        @return: TaskPreparingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.task_preparing_with_options(request, runtime)

    async def task_preparing_async(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        """
        @summary TaskPreparing
        
        @param request: TaskPreparingRequest
        @return: TaskPreparingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.task_preparing_with_options_async(request, runtime)

    def terminate_call_with_options(
        self,
        request: outbound_bot_20191226_models.TerminateCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TerminateCallResponse:
        """
        @param request: TerminateCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateCall',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TerminateCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_call_with_options_async(
        self,
        request: outbound_bot_20191226_models.TerminateCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TerminateCallResponse:
        """
        @param request: TerminateCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateCall',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TerminateCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_call(
        self,
        request: outbound_bot_20191226_models.TerminateCallRequest,
    ) -> outbound_bot_20191226_models.TerminateCallResponse:
        """
        @param request: TerminateCallRequest
        @return: TerminateCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.terminate_call_with_options(request, runtime)

    async def terminate_call_async(
        self,
        request: outbound_bot_20191226_models.TerminateCallRequest,
    ) -> outbound_bot_20191226_models.TerminateCallResponse:
        """
        @param request: TerminateCallRequest
        @return: TerminateCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.terminate_call_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: outbound_bot_20191226_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: outbound_bot_20191226_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: outbound_bot_20191226_models.UntagResourcesRequest,
    ) -> outbound_bot_20191226_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: outbound_bot_20191226_models.UntagResourcesRequest,
    ) -> outbound_bot_20191226_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upload_script_recording_with_options(
        self,
        request: outbound_bot_20191226_models.UploadScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.UploadScriptRecordingResponse:
        """
        @param request: UploadScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.UploadScriptRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_script_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.UploadScriptRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.UploadScriptRecordingResponse:
        """
        @param request: UploadScriptRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadScriptRecordingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadScriptRecording',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.UploadScriptRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_script_recording(
        self,
        request: outbound_bot_20191226_models.UploadScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.UploadScriptRecordingResponse:
        """
        @param request: UploadScriptRecordingRequest
        @return: UploadScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_script_recording_with_options(request, runtime)

    async def upload_script_recording_async(
        self,
        request: outbound_bot_20191226_models.UploadScriptRecordingRequest,
    ) -> outbound_bot_20191226_models.UploadScriptRecordingResponse:
        """
        @param request: UploadScriptRecordingRequest
        @return: UploadScriptRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_script_recording_with_options_async(request, runtime)

    def withdraw_script_review_with_options(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        """
        @summary WithdrawScriptReview
        
        @description ***\
        
        @param request: WithdrawScriptReviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WithdrawScriptReviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawScriptReview',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.WithdrawScriptReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_script_review_with_options_async(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        """
        @summary WithdrawScriptReview
        
        @description ***\
        
        @param request: WithdrawScriptReviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WithdrawScriptReviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawScriptReview',
            version='2019-12-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.WithdrawScriptReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_script_review(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        """
        @summary WithdrawScriptReview
        
        @description ***\
        
        @param request: WithdrawScriptReviewRequest
        @return: WithdrawScriptReviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.withdraw_script_review_with_options(request, runtime)

    async def withdraw_script_review_async(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        """
        @summary WithdrawScriptReview
        
        @description ***\
        
        @param request: WithdrawScriptReviewRequest
        @return: WithdrawScriptReviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_script_review_with_options_async(request, runtime)
