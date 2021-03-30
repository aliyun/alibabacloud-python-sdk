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

    def assign_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.AssignJobsResponse(),
            self.do_rpcrequest('AssignJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.AssignJobsResponse(),
            await self.do_rpcrequest_async('AssignJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_jobs(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_jobs_with_options(request, runtime)

    async def assign_jobs_async(
        self,
        request: outbound_bot_20191226_models.AssignJobsRequest,
    ) -> outbound_bot_20191226_models.AssignJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_jobs_with_options_async(request, runtime)

    def cancel_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CancelJobsResponse(),
            self.do_rpcrequest('CancelJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CancelJobsResponse(),
            await self.do_rpcrequest_async('CancelJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_jobs(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_jobs_with_options(request, runtime)

    async def cancel_jobs_async(
        self,
        request: outbound_bot_20191226_models.CancelJobsRequest,
    ) -> outbound_bot_20191226_models.CancelJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_jobs_with_options_async(request, runtime)

    def create_batch_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBatchJobsResponse(),
            self.do_rpcrequest('CreateBatchJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_batch_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateBatchJobsResponse(),
            await self.do_rpcrequest_async('CreateBatchJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_batch_jobs(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_batch_jobs_with_options(request, runtime)

    async def create_batch_jobs_async(
        self,
        request: outbound_bot_20191226_models.CreateBatchJobsRequest,
    ) -> outbound_bot_20191226_models.CreateBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_jobs_with_options_async(request, runtime)

    def create_dialogue_flow_with_options(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateDialogueFlowResponse(),
            self.do_rpcrequest('CreateDialogueFlow', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dialogue_flow_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateDialogueFlowResponse(),
            await self.do_rpcrequest_async('CreateDialogueFlow', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dialogue_flow(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dialogue_flow_with_options(request, runtime)

    async def create_dialogue_flow_async(
        self,
        request: outbound_bot_20191226_models.CreateDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.CreateDialogueFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dialogue_flow_with_options_async(request, runtime)

    def create_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateGlobalQuestionResponse(),
            self.do_rpcrequest('CreateGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateGlobalQuestionResponse(),
            await self.do_rpcrequest_async('CreateGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_global_question(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_global_question_with_options(request, runtime)

    async def create_global_question_async(
        self,
        request: outbound_bot_20191226_models.CreateGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.CreateGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_global_question_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateInstanceResponse(),
            await self.do_rpcrequest_async('CreateInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: outbound_bot_20191226_models.CreateInstanceRequest,
    ) -> outbound_bot_20191226_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_intent_with_options(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateIntentResponse(),
            self.do_rpcrequest('CreateIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateIntentResponse(),
            await self.do_rpcrequest_async('CreateIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intent(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    async def create_intent_async(
        self,
        request: outbound_bot_20191226_models.CreateIntentRequest,
    ) -> outbound_bot_20191226_models.CreateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_intent_with_options_async(request, runtime)

    def create_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobGroupResponse(),
            self.do_rpcrequest('CreateJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateJobGroupResponse(),
            await self.do_rpcrequest_async('CreateJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job_group(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_group_with_options(request, runtime)

    async def create_job_group_async(
        self,
        request: outbound_bot_20191226_models.CreateJobGroupRequest,
    ) -> outbound_bot_20191226_models.CreateJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_group_with_options_async(request, runtime)

    def create_outbound_call_number_with_options(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateOutboundCallNumberResponse(),
            self.do_rpcrequest('CreateOutboundCallNumber', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_outbound_call_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateOutboundCallNumberResponse(),
            await self.do_rpcrequest_async('CreateOutboundCallNumber', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_outbound_call_number(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_outbound_call_number_with_options(request, runtime)

    async def create_outbound_call_number_async(
        self,
        request: outbound_bot_20191226_models.CreateOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.CreateOutboundCallNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_outbound_call_number_with_options_async(request, runtime)

    def create_script_with_options(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptResponse(),
            self.do_rpcrequest('CreateScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptResponse(),
            await self.do_rpcrequest_async('CreateScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_script(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_script_with_options(request, runtime)

    async def create_script_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptRequest,
    ) -> outbound_bot_20191226_models.CreateScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_script_with_options_async(request, runtime)

    def create_script_waveform_with_options(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptWaveformResponse(),
            self.do_rpcrequest('CreateScriptWaveform', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_script_waveform_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateScriptWaveformResponse(),
            await self.do_rpcrequest_async('CreateScriptWaveform', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_script_waveform(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_script_waveform_with_options(request, runtime)

    async def create_script_waveform_async(
        self,
        request: outbound_bot_20191226_models.CreateScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.CreateScriptWaveformResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_script_waveform_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateTagResponse(),
            self.do_rpcrequest('CreateTag', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.CreateTagResponse(),
            await self.do_rpcrequest_async('CreateTag', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tag(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: outbound_bot_20191226_models.CreateTagRequest,
    ) -> outbound_bot_20191226_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def delete_dialogue_flow_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteDialogueFlowResponse(),
            self.do_rpcrequest('DeleteDialogueFlow', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dialogue_flow_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteDialogueFlowResponse(),
            await self.do_rpcrequest_async('DeleteDialogueFlow', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dialogue_flow(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dialogue_flow_with_options(request, runtime)

    async def delete_dialogue_flow_async(
        self,
        request: outbound_bot_20191226_models.DeleteDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.DeleteDialogueFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dialogue_flow_with_options_async(request, runtime)

    def delete_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteGlobalQuestionResponse(),
            self.do_rpcrequest('DeleteGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteGlobalQuestionResponse(),
            await self.do_rpcrequest_async('DeleteGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_global_question(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_global_question_with_options(request, runtime)

    async def delete_global_question_async(
        self,
        request: outbound_bot_20191226_models.DeleteGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DeleteGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_question_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteInstanceResponse(),
            await self.do_rpcrequest_async('DeleteInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: outbound_bot_20191226_models.DeleteInstanceRequest,
    ) -> outbound_bot_20191226_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_intent_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteIntentResponse(),
            self.do_rpcrequest('DeleteIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteIntentResponse(),
            await self.do_rpcrequest_async('DeleteIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_intent(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    async def delete_intent_async(
        self,
        request: outbound_bot_20191226_models.DeleteIntentRequest,
    ) -> outbound_bot_20191226_models.DeleteIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_intent_with_options_async(request, runtime)

    def delete_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteJobGroupResponse(),
            self.do_rpcrequest('DeleteJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteJobGroupResponse(),
            await self.do_rpcrequest_async('DeleteJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job_group(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_group_with_options(request, runtime)

    async def delete_job_group_async(
        self,
        request: outbound_bot_20191226_models.DeleteJobGroupRequest,
    ) -> outbound_bot_20191226_models.DeleteJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_group_with_options_async(request, runtime)

    def delete_outbound_call_number_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteOutboundCallNumberResponse(),
            self.do_rpcrequest('DeleteOutboundCallNumber', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_outbound_call_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteOutboundCallNumberResponse(),
            await self.do_rpcrequest_async('DeleteOutboundCallNumber', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_outbound_call_number(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_outbound_call_number_with_options(request, runtime)

    async def delete_outbound_call_number_async(
        self,
        request: outbound_bot_20191226_models.DeleteOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.DeleteOutboundCallNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_outbound_call_number_with_options_async(request, runtime)

    def delete_script_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptResponse(),
            self.do_rpcrequest('DeleteScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptResponse(),
            await self.do_rpcrequest_async('DeleteScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_script(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_script_with_options(request, runtime)

    async def delete_script_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_script_with_options_async(request, runtime)

    def delete_script_waveform_with_options(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptWaveformResponse(),
            self.do_rpcrequest('DeleteScriptWaveform', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_script_waveform_with_options_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DeleteScriptWaveformResponse(),
            await self.do_rpcrequest_async('DeleteScriptWaveform', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_script_waveform(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_script_waveform_with_options(request, runtime)

    async def delete_script_waveform_async(
        self,
        request: outbound_bot_20191226_models.DeleteScriptWaveformRequest,
    ) -> outbound_bot_20191226_models.DeleteScriptWaveformResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_script_waveform_with_options_async(request, runtime)

    def describe_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeGlobalQuestionResponse(),
            self.do_rpcrequest('DescribeGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeGlobalQuestionResponse(),
            await self.do_rpcrequest_async('DescribeGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_global_question(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_global_question_with_options(request, runtime)

    async def describe_global_question_async(
        self,
        request: outbound_bot_20191226_models.DescribeGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.DescribeGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_question_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeInstanceResponse(),
            self.do_rpcrequest('DescribeInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeInstanceResponse(),
            await self.do_rpcrequest_async('DescribeInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: outbound_bot_20191226_models.DescribeInstanceRequest,
    ) -> outbound_bot_20191226_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_intent_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeIntentResponse(),
            self.do_rpcrequest('DescribeIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeIntentResponse(),
            await self.do_rpcrequest_async('DescribeIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_intent(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    async def describe_intent_async(
        self,
        request: outbound_bot_20191226_models.DescribeIntentRequest,
    ) -> outbound_bot_20191226_models.DescribeIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_intent_with_options_async(request, runtime)

    def describe_job_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobResponse(),
            self.do_rpcrequest('DescribeJob', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobResponse(),
            await self.do_rpcrequest_async('DescribeJob', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_job(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    async def describe_job_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobRequest,
    ) -> outbound_bot_20191226_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_with_options_async(request, runtime)

    def describe_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobGroupResponse(),
            self.do_rpcrequest('DescribeJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeJobGroupResponse(),
            await self.do_rpcrequest_async('DescribeJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_job_group(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_group_with_options(request, runtime)

    async def describe_job_group_async(
        self,
        request: outbound_bot_20191226_models.DescribeJobGroupRequest,
    ) -> outbound_bot_20191226_models.DescribeJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_group_with_options_async(request, runtime)

    def describe_script_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptResponse(),
            self.do_rpcrequest('DescribeScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptResponse(),
            await self.do_rpcrequest_async('DescribeScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_script(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_script_with_options(request, runtime)

    async def describe_script_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_script_with_options_async(request, runtime)

    def describe_script_voice_config_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse(),
            self.do_rpcrequest('DescribeScriptVoiceConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_script_voice_config_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse(),
            await self.do_rpcrequest_async('DescribeScriptVoiceConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_script_voice_config(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_script_voice_config_with_options(request, runtime)

    async def describe_script_voice_config_async(
        self,
        request: outbound_bot_20191226_models.DescribeScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeScriptVoiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_script_voice_config_with_options_async(request, runtime)

    def describe_tag_hits_summary_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTagHitsSummaryResponse(),
            self.do_rpcrequest('DescribeTagHitsSummary', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tag_hits_summary_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTagHitsSummaryResponse(),
            await self.do_rpcrequest_async('DescribeTagHitsSummary', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tag_hits_summary(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_hits_summary_with_options(request, runtime)

    async def describe_tag_hits_summary_async(
        self,
        request: outbound_bot_20191226_models.DescribeTagHitsSummaryRequest,
    ) -> outbound_bot_20191226_models.DescribeTagHitsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_hits_summary_with_options_async(request, runtime)

    def describe_ttsconfig_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSConfigResponse(),
            self.do_rpcrequest('DescribeTTSConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ttsconfig_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSConfigResponse(),
            await self.do_rpcrequest_async('DescribeTTSConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ttsconfig(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ttsconfig_with_options(request, runtime)

    async def describe_ttsconfig_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSConfigRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ttsconfig_with_options_async(request, runtime)

    def describe_ttsdemo_with_options(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSDemoResponse(),
            self.do_rpcrequest('DescribeTTSDemo', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ttsdemo_with_options_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DescribeTTSDemoResponse(),
            await self.do_rpcrequest_async('DescribeTTSDemo', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ttsdemo(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ttsdemo_with_options(request, runtime)

    async def describe_ttsdemo_async(
        self,
        request: outbound_bot_20191226_models.DescribeTTSDemoRequest,
    ) -> outbound_bot_20191226_models.DescribeTTSDemoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ttsdemo_with_options_async(request, runtime)

    def dialogue_with_options(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DialogueResponse(),
            self.do_rpcrequest('Dialogue', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dialogue_with_options_async(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DialogueResponse(),
            await self.do_rpcrequest_async('Dialogue', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dialogue(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    async def dialogue_async(
        self,
        request: outbound_bot_20191226_models.DialogueRequest,
    ) -> outbound_bot_20191226_models.DialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dialogue_with_options_async(request, runtime)

    def download_recording_with_options(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DownloadRecordingResponse(),
            self.do_rpcrequest('DownloadRecording', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DownloadRecordingResponse(),
            await self.do_rpcrequest_async('DownloadRecording', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_recording(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_recording_with_options(request, runtime)

    async def download_recording_async(
        self,
        request: outbound_bot_20191226_models.DownloadRecordingRequest,
    ) -> outbound_bot_20191226_models.DownloadRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_recording_with_options_async(request, runtime)

    def duplicate_script_with_options(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DuplicateScriptResponse(),
            self.do_rpcrequest('DuplicateScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def duplicate_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.DuplicateScriptResponse(),
            await self.do_rpcrequest_async('DuplicateScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def duplicate_script(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.duplicate_script_with_options(request, runtime)

    async def duplicate_script_async(
        self,
        request: outbound_bot_20191226_models.DuplicateScriptRequest,
    ) -> outbound_bot_20191226_models.DuplicateScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.duplicate_script_with_options_async(request, runtime)

    def export_script_with_options(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ExportScriptResponse(),
            self.do_rpcrequest('ExportScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ExportScriptResponse(),
            await self.do_rpcrequest_async('ExportScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_script(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_script_with_options(request, runtime)

    async def export_script_async(
        self,
        request: outbound_bot_20191226_models.ExportScriptRequest,
    ) -> outbound_bot_20191226_models.ExportScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_script_with_options_async(request, runtime)

    def import_script_with_options(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ImportScriptResponse(),
            self.do_rpcrequest('ImportScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ImportScriptResponse(),
            await self.do_rpcrequest_async('ImportScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_script(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_script_with_options(request, runtime)

    async def import_script_async(
        self,
        request: outbound_bot_20191226_models.ImportScriptRequest,
    ) -> outbound_bot_20191226_models.ImportScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_script_with_options_async(request, runtime)

    def inflight_task_timeout_with_options(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.InflightTaskTimeoutResponse(),
            self.do_rpcrequest('InflightTaskTimeout', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def inflight_task_timeout_with_options_async(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.InflightTaskTimeoutResponse(),
            await self.do_rpcrequest_async('InflightTaskTimeout', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def inflight_task_timeout(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.inflight_task_timeout_with_options(request, runtime)

    async def inflight_task_timeout_async(
        self,
        request: outbound_bot_20191226_models.InflightTaskTimeoutRequest,
    ) -> outbound_bot_20191226_models.InflightTaskTimeoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inflight_task_timeout_with_options_async(request, runtime)

    def list_dialogue_flows_with_options(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListDialogueFlowsResponse(),
            self.do_rpcrequest('ListDialogueFlows', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dialogue_flows_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListDialogueFlowsResponse(),
            await self.do_rpcrequest_async('ListDialogueFlows', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dialogue_flows(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dialogue_flows_with_options(request, runtime)

    async def list_dialogue_flows_async(
        self,
        request: outbound_bot_20191226_models.ListDialogueFlowsRequest,
    ) -> outbound_bot_20191226_models.ListDialogueFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dialogue_flows_with_options_async(request, runtime)

    def list_global_questions_with_options(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListGlobalQuestionsResponse(),
            self.do_rpcrequest('ListGlobalQuestions', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_global_questions_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListGlobalQuestionsResponse(),
            await self.do_rpcrequest_async('ListGlobalQuestions', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_global_questions(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_global_questions_with_options(request, runtime)

    async def list_global_questions_async(
        self,
        request: outbound_bot_20191226_models.ListGlobalQuestionsRequest,
    ) -> outbound_bot_20191226_models.ListGlobalQuestionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_global_questions_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListInstancesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListInstancesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListInstancesResponse(),
            await self.do_rpcrequest_async('ListInstances', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(self) -> outbound_bot_20191226_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(runtime)

    async def list_instances_async(self) -> outbound_bot_20191226_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(runtime)

    def list_intents_with_options(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListIntentsResponse(),
            self.do_rpcrequest('ListIntents', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_intents_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListIntentsResponse(),
            await self.do_rpcrequest_async('ListIntents', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_intents(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_intents_with_options(request, runtime)

    async def list_intents_async(
        self,
        request: outbound_bot_20191226_models.ListIntentsRequest,
    ) -> outbound_bot_20191226_models.ListIntentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_intents_with_options_async(request, runtime)

    def list_job_groups_with_options(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobGroupsResponse(),
            self.do_rpcrequest('ListJobGroups', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_groups_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobGroupsResponse(),
            await self.do_rpcrequest_async('ListJobGroups', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_groups(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_groups_with_options(request, runtime)

    async def list_job_groups_async(
        self,
        request: outbound_bot_20191226_models.ListJobGroupsRequest,
    ) -> outbound_bot_20191226_models.ListJobGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_groups_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsResponse(),
            self.do_rpcrequest('ListJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsResponse(),
            await self.do_rpcrequest_async('ListJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jobs(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: outbound_bot_20191226_models.ListJobsRequest,
    ) -> outbound_bot_20191226_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_jobs_by_group_with_options(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsByGroupResponse(),
            self.do_rpcrequest('ListJobsByGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_jobs_by_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListJobsByGroupResponse(),
            await self.do_rpcrequest_async('ListJobsByGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jobs_by_group(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_by_group_with_options(request, runtime)

    async def list_jobs_by_group_async(
        self,
        request: outbound_bot_20191226_models.ListJobsByGroupRequest,
    ) -> outbound_bot_20191226_models.ListJobsByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_by_group_with_options_async(request, runtime)

    def list_media_with_options(
        self,
        request: outbound_bot_20191226_models.ListMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListMediaResponse(),
            self.do_rpcrequest('ListMedia', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_media_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListMediaResponse(),
            await self.do_rpcrequest_async('ListMedia', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media(
        self,
        request: outbound_bot_20191226_models.ListMediaRequest,
    ) -> outbound_bot_20191226_models.ListMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_with_options(request, runtime)

    async def list_media_async(
        self,
        request: outbound_bot_20191226_models.ListMediaRequest,
    ) -> outbound_bot_20191226_models.ListMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_with_options_async(request, runtime)

    def list_outbound_call_numbers_with_options(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListOutboundCallNumbersResponse(),
            self.do_rpcrequest('ListOutboundCallNumbers', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_outbound_call_numbers_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListOutboundCallNumbersResponse(),
            await self.do_rpcrequest_async('ListOutboundCallNumbers', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_call_numbers(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_call_numbers_with_options(request, runtime)

    async def list_outbound_call_numbers_async(
        self,
        request: outbound_bot_20191226_models.ListOutboundCallNumbersRequest,
    ) -> outbound_bot_20191226_models.ListOutboundCallNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_call_numbers_with_options_async(request, runtime)

    def list_scheduler_instances_with_options(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListSchedulerInstancesResponse(),
            self.do_rpcrequest('ListSchedulerInstances', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scheduler_instances_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListSchedulerInstancesResponse(),
            await self.do_rpcrequest_async('ListSchedulerInstances', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scheduler_instances(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scheduler_instances_with_options(request, runtime)

    async def list_scheduler_instances_async(
        self,
        request: outbound_bot_20191226_models.ListSchedulerInstancesRequest,
    ) -> outbound_bot_20191226_models.ListSchedulerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scheduler_instances_with_options_async(request, runtime)

    def list_script_publish_histories_with_options(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptPublishHistoriesResponse(),
            self.do_rpcrequest('ListScriptPublishHistories', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_script_publish_histories_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptPublishHistoriesResponse(),
            await self.do_rpcrequest_async('ListScriptPublishHistories', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_script_publish_histories(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_script_publish_histories_with_options(request, runtime)

    async def list_script_publish_histories_async(
        self,
        request: outbound_bot_20191226_models.ListScriptPublishHistoriesRequest,
    ) -> outbound_bot_20191226_models.ListScriptPublishHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_script_publish_histories_with_options_async(request, runtime)

    def list_scripts_with_options(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptsResponse(),
            self.do_rpcrequest('ListScripts', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scripts_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptsResponse(),
            await self.do_rpcrequest_async('ListScripts', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scripts(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scripts_with_options(request, runtime)

    async def list_scripts_async(
        self,
        request: outbound_bot_20191226_models.ListScriptsRequest,
    ) -> outbound_bot_20191226_models.ListScriptsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scripts_with_options_async(request, runtime)

    def list_script_voice_configs_with_options(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptVoiceConfigsResponse(),
            self.do_rpcrequest('ListScriptVoiceConfigs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_script_voice_configs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListScriptVoiceConfigsResponse(),
            await self.do_rpcrequest_async('ListScriptVoiceConfigs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_script_voice_configs(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_script_voice_configs_with_options(request, runtime)

    async def list_script_voice_configs_async(
        self,
        request: outbound_bot_20191226_models.ListScriptVoiceConfigsRequest,
    ) -> outbound_bot_20191226_models.ListScriptVoiceConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_script_voice_configs_with_options_async(request, runtime)

    def list_tags_with_options(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListTagsResponse(),
            self.do_rpcrequest('ListTags', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ListTagsResponse(),
            await self.do_rpcrequest_async('ListTags', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tags(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: outbound_bot_20191226_models.ListTagsRequest,
    ) -> outbound_bot_20191226_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def modify_batch_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBatchJobsResponse(),
            self.do_rpcrequest('ModifyBatchJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_batch_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyBatchJobsResponse(),
            await self.do_rpcrequest_async('ModifyBatchJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_batch_jobs(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_batch_jobs_with_options(request, runtime)

    async def modify_batch_jobs_async(
        self,
        request: outbound_bot_20191226_models.ModifyBatchJobsRequest,
    ) -> outbound_bot_20191226_models.ModifyBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_batch_jobs_with_options_async(request, runtime)

    def modify_dialogue_flow_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyDialogueFlowResponse(),
            self.do_rpcrequest('ModifyDialogueFlow', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dialogue_flow_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyDialogueFlowResponse(),
            await self.do_rpcrequest_async('ModifyDialogueFlow', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dialogue_flow(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dialogue_flow_with_options(request, runtime)

    async def modify_dialogue_flow_async(
        self,
        request: outbound_bot_20191226_models.ModifyDialogueFlowRequest,
    ) -> outbound_bot_20191226_models.ModifyDialogueFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dialogue_flow_with_options_async(request, runtime)

    def modify_global_question_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyGlobalQuestionResponse(),
            self.do_rpcrequest('ModifyGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_global_question_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyGlobalQuestionResponse(),
            await self.do_rpcrequest_async('ModifyGlobalQuestion', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_global_question(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_global_question_with_options(request, runtime)

    async def modify_global_question_async(
        self,
        request: outbound_bot_20191226_models.ModifyGlobalQuestionRequest,
    ) -> outbound_bot_20191226_models.ModifyGlobalQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_question_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyInstanceResponse(),
            self.do_rpcrequest('ModifyInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyInstanceResponse(),
            await self.do_rpcrequest_async('ModifyInstance', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: outbound_bot_20191226_models.ModifyInstanceRequest,
    ) -> outbound_bot_20191226_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_intent_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyIntentResponse(),
            self.do_rpcrequest('ModifyIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_intent_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyIntentResponse(),
            await self.do_rpcrequest_async('ModifyIntent', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_intent(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_intent_with_options(request, runtime)

    async def modify_intent_async(
        self,
        request: outbound_bot_20191226_models.ModifyIntentRequest,
    ) -> outbound_bot_20191226_models.ModifyIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_intent_with_options_async(request, runtime)

    def modify_job_group_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyJobGroupResponse(),
            self.do_rpcrequest('ModifyJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_job_group_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyJobGroupResponse(),
            await self.do_rpcrequest_async('ModifyJobGroup', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_job_group(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_job_group_with_options(request, runtime)

    async def modify_job_group_async(
        self,
        request: outbound_bot_20191226_models.ModifyJobGroupRequest,
    ) -> outbound_bot_20191226_models.ModifyJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_job_group_with_options_async(request, runtime)

    def modify_outbound_call_number_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyOutboundCallNumberResponse(),
            self.do_rpcrequest('ModifyOutboundCallNumber', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_outbound_call_number_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyOutboundCallNumberResponse(),
            await self.do_rpcrequest_async('ModifyOutboundCallNumber', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_outbound_call_number(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_outbound_call_number_with_options(request, runtime)

    async def modify_outbound_call_number_async(
        self,
        request: outbound_bot_20191226_models.ModifyOutboundCallNumberRequest,
    ) -> outbound_bot_20191226_models.ModifyOutboundCallNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_outbound_call_number_with_options_async(request, runtime)

    def modify_script_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptResponse(),
            self.do_rpcrequest('ModifyScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptResponse(),
            await self.do_rpcrequest_async('ModifyScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_script(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_script_with_options(request, runtime)

    async def modify_script_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_script_with_options_async(request, runtime)

    def modify_script_voice_config_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse(),
            self.do_rpcrequest('ModifyScriptVoiceConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_script_voice_config_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse(),
            await self.do_rpcrequest_async('ModifyScriptVoiceConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_script_voice_config(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_script_voice_config_with_options(request, runtime)

    async def modify_script_voice_config_async(
        self,
        request: outbound_bot_20191226_models.ModifyScriptVoiceConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyScriptVoiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_script_voice_config_with_options_async(request, runtime)

    def modify_tag_groups_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTagGroupsResponse(),
            self.do_rpcrequest('ModifyTagGroups', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_tag_groups_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTagGroupsResponse(),
            await self.do_rpcrequest_async('ModifyTagGroups', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_tag_groups(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_groups_with_options(request, runtime)

    async def modify_tag_groups_async(
        self,
        request: outbound_bot_20191226_models.ModifyTagGroupsRequest,
    ) -> outbound_bot_20191226_models.ModifyTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tag_groups_with_options_async(request, runtime)

    def modify_ttsconfig_with_options(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTTSConfigResponse(),
            self.do_rpcrequest('ModifyTTSConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ttsconfig_with_options_async(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ModifyTTSConfigResponse(),
            await self.do_rpcrequest_async('ModifyTTSConfig', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ttsconfig(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ttsconfig_with_options(request, runtime)

    async def modify_ttsconfig_async(
        self,
        request: outbound_bot_20191226_models.ModifyTTSConfigRequest,
    ) -> outbound_bot_20191226_models.ModifyTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ttsconfig_with_options_async(request, runtime)

    def publish_script_with_options(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptResponse(),
            self.do_rpcrequest('PublishScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptResponse(),
            await self.do_rpcrequest_async('PublishScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_script(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_script_with_options(request, runtime)

    async def publish_script_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptRequest,
    ) -> outbound_bot_20191226_models.PublishScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_script_with_options_async(request, runtime)

    def publish_script_for_debug_with_options(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptForDebugResponse(),
            self.do_rpcrequest('PublishScriptForDebug', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_script_for_debug_with_options_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.PublishScriptForDebugResponse(),
            await self.do_rpcrequest_async('PublishScriptForDebug', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_script_for_debug(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_script_for_debug_with_options(request, runtime)

    async def publish_script_for_debug_async(
        self,
        request: outbound_bot_20191226_models.PublishScriptForDebugRequest,
    ) -> outbound_bot_20191226_models.PublishScriptForDebugResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_script_for_debug_with_options_async(request, runtime)

    def query_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryJobsResponse(),
            self.do_rpcrequest('QueryJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryJobsResponse(),
            await self.do_rpcrequest_async('QueryJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_jobs(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_jobs_with_options(request, runtime)

    async def query_jobs_async(
        self,
        request: outbound_bot_20191226_models.QueryJobsRequest,
    ) -> outbound_bot_20191226_models.QueryJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_jobs_with_options_async(request, runtime)

    def query_scripts_by_status_with_options(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptsByStatusResponse(),
            self.do_rpcrequest('QueryScriptsByStatus', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_scripts_by_status_with_options_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptsByStatusResponse(),
            await self.do_rpcrequest_async('QueryScriptsByStatus', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_scripts_by_status(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_scripts_by_status_with_options(request, runtime)

    async def query_scripts_by_status_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptsByStatusRequest,
    ) -> outbound_bot_20191226_models.QueryScriptsByStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_scripts_by_status_with_options_async(request, runtime)

    def query_script_waveforms_with_options(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptWaveformsResponse(),
            self.do_rpcrequest('QueryScriptWaveforms', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_script_waveforms_with_options_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.QueryScriptWaveformsResponse(),
            await self.do_rpcrequest_async('QueryScriptWaveforms', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_script_waveforms(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_script_waveforms_with_options(request, runtime)

    async def query_script_waveforms_async(
        self,
        request: outbound_bot_20191226_models.QueryScriptWaveformsRequest,
    ) -> outbound_bot_20191226_models.QueryScriptWaveformsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_script_waveforms_with_options_async(request, runtime)

    def record_failure_with_options(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RecordFailureResponse(),
            self.do_rpcrequest('RecordFailure', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def record_failure_with_options_async(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RecordFailureResponse(),
            await self.do_rpcrequest_async('RecordFailure', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def record_failure(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        runtime = util_models.RuntimeOptions()
        return self.record_failure_with_options(request, runtime)

    async def record_failure_async(
        self,
        request: outbound_bot_20191226_models.RecordFailureRequest,
    ) -> outbound_bot_20191226_models.RecordFailureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.record_failure_with_options_async(request, runtime)

    def resume_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ResumeJobsResponse(),
            self.do_rpcrequest('ResumeJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.ResumeJobsResponse(),
            await self.do_rpcrequest_async('ResumeJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_jobs(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_jobs_with_options(request, runtime)

    async def resume_jobs_async(
        self,
        request: outbound_bot_20191226_models.ResumeJobsRequest,
    ) -> outbound_bot_20191226_models.ResumeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_jobs_with_options_async(request, runtime)

    def rollback_script_with_options(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RollbackScriptResponse(),
            self.do_rpcrequest('RollbackScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_script_with_options_async(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.RollbackScriptResponse(),
            await self.do_rpcrequest_async('RollbackScript', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_script(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_script_with_options(request, runtime)

    async def rollback_script_async(
        self,
        request: outbound_bot_20191226_models.RollbackScriptRequest,
    ) -> outbound_bot_20191226_models.RollbackScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_script_with_options_async(request, runtime)

    def start_job_with_options(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.StartJobResponse(),
            self.do_rpcrequest('StartJob', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_job_with_options_async(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.StartJobResponse(),
            await self.do_rpcrequest_async('StartJob', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_job(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_job_with_options(request, runtime)

    async def start_job_async(
        self,
        request: outbound_bot_20191226_models.StartJobRequest,
    ) -> outbound_bot_20191226_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_job_with_options_async(request, runtime)

    def submit_batch_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitBatchJobsResponse(),
            self.do_rpcrequest('SubmitBatchJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_batch_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitBatchJobsResponse(),
            await self.do_rpcrequest_async('SubmitBatchJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_batch_jobs(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_batch_jobs_with_options(request, runtime)

    async def submit_batch_jobs_async(
        self,
        request: outbound_bot_20191226_models.SubmitBatchJobsRequest,
    ) -> outbound_bot_20191226_models.SubmitBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_batch_jobs_with_options_async(request, runtime)

    def submit_recording_with_options(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitRecordingResponse(),
            self.do_rpcrequest('SubmitRecording', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_recording_with_options_async(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitRecordingResponse(),
            await self.do_rpcrequest_async('SubmitRecording', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_recording(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_recording_with_options(request, runtime)

    async def submit_recording_async(
        self,
        request: outbound_bot_20191226_models.SubmitRecordingRequest,
    ) -> outbound_bot_20191226_models.SubmitRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_recording_with_options_async(request, runtime)

    def submit_script_review_with_options(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitScriptReviewResponse(),
            self.do_rpcrequest('SubmitScriptReview', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_script_review_with_options_async(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SubmitScriptReviewResponse(),
            await self.do_rpcrequest_async('SubmitScriptReview', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_script_review(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_script_review_with_options(request, runtime)

    async def submit_script_review_async(
        self,
        request: outbound_bot_20191226_models.SubmitScriptReviewRequest,
    ) -> outbound_bot_20191226_models.SubmitScriptReviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_script_review_with_options_async(request, runtime)

    def suspend_jobs_with_options(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendJobsResponse(),
            self.do_rpcrequest('SuspendJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_jobs_with_options_async(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.SuspendJobsResponse(),
            await self.do_rpcrequest_async('SuspendJobs', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_jobs(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_jobs_with_options(request, runtime)

    async def suspend_jobs_async(
        self,
        request: outbound_bot_20191226_models.SuspendJobsRequest,
    ) -> outbound_bot_20191226_models.SuspendJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_jobs_with_options_async(request, runtime)

    def task_preparing_with_options(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TaskPreparingResponse(),
            self.do_rpcrequest('TaskPreparing', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def task_preparing_with_options_async(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.TaskPreparingResponse(),
            await self.do_rpcrequest_async('TaskPreparing', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def task_preparing(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_preparing_with_options(request, runtime)

    async def task_preparing_async(
        self,
        request: outbound_bot_20191226_models.TaskPreparingRequest,
    ) -> outbound_bot_20191226_models.TaskPreparingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_preparing_with_options_async(request, runtime)

    def withdraw_script_review_with_options(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.WithdrawScriptReviewResponse(),
            self.do_rpcrequest('WithdrawScriptReview', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def withdraw_script_review_with_options_async(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            outbound_bot_20191226_models.WithdrawScriptReviewResponse(),
            await self.do_rpcrequest_async('WithdrawScriptReview', '2019-12-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def withdraw_script_review(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.withdraw_script_review_with_options(request, runtime)

    async def withdraw_script_review_async(
        self,
        request: outbound_bot_20191226_models.WithdrawScriptReviewRequest,
    ) -> outbound_bot_20191226_models.WithdrawScriptReviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_script_review_with_options_async(request, runtime)
