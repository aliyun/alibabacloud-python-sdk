# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quanmiaolightapp20240801 import models as quan_miao_light_app_20240801_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('quanmiaolightapp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def run_marketing_information_extract_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunMarketingInformationExtractRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationExtractResponse:
        """
        @summary 营销信息抽取服务
        
        @param tmp_req: RunMarketingInformationExtractRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMarketingInformationExtractResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunMarketingInformationExtractShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_materials):
            request.source_materials_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_materials, 'sourceMaterials', 'json')
        body = {}
        if not UtilClient.is_unset(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not UtilClient.is_unset(request.extract_type):
            body['extractType'] = request.extract_type
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.source_materials_shrink):
            body['sourceMaterials'] = request.source_materials_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMarketingInformationExtract',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runMarketingInformationExtract',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunMarketingInformationExtractResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_marketing_information_extract_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunMarketingInformationExtractRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationExtractResponse:
        """
        @summary 营销信息抽取服务
        
        @param tmp_req: RunMarketingInformationExtractRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMarketingInformationExtractResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunMarketingInformationExtractShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_materials):
            request.source_materials_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_materials, 'sourceMaterials', 'json')
        body = {}
        if not UtilClient.is_unset(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not UtilClient.is_unset(request.extract_type):
            body['extractType'] = request.extract_type
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.source_materials_shrink):
            body['sourceMaterials'] = request.source_materials_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMarketingInformationExtract',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runMarketingInformationExtract',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunMarketingInformationExtractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_marketing_information_extract(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunMarketingInformationExtractRequest,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationExtractResponse:
        """
        @summary 营销信息抽取服务
        
        @param request: RunMarketingInformationExtractRequest
        @return: RunMarketingInformationExtractResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_marketing_information_extract_with_options(workspace_id, request, headers, runtime)

    async def run_marketing_information_extract_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunMarketingInformationExtractRequest,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationExtractResponse:
        """
        @summary 营销信息抽取服务
        
        @param request: RunMarketingInformationExtractRequest
        @return: RunMarketingInformationExtractResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_marketing_information_extract_with_options_async(workspace_id, request, headers, runtime)

    def run_marketing_information_writing_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunMarketingInformationWritingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationWritingResponse:
        """
        @summary 营销文案写作服务
        
        @param request: RunMarketingInformationWritingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMarketingInformationWritingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.source_material):
            body['sourceMaterial'] = request.source_material
        if not UtilClient.is_unset(request.writing_type):
            body['writingType'] = request.writing_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMarketingInformationWriting',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runMarketingInformationWriting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunMarketingInformationWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_marketing_information_writing_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunMarketingInformationWritingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationWritingResponse:
        """
        @summary 营销文案写作服务
        
        @param request: RunMarketingInformationWritingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMarketingInformationWritingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.source_material):
            body['sourceMaterial'] = request.source_material
        if not UtilClient.is_unset(request.writing_type):
            body['writingType'] = request.writing_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMarketingInformationWriting',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runMarketingInformationWriting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunMarketingInformationWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_marketing_information_writing(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunMarketingInformationWritingRequest,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationWritingResponse:
        """
        @summary 营销文案写作服务
        
        @param request: RunMarketingInformationWritingRequest
        @return: RunMarketingInformationWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_marketing_information_writing_with_options(workspace_id, request, headers, runtime)

    async def run_marketing_information_writing_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunMarketingInformationWritingRequest,
    ) -> quan_miao_light_app_20240801_models.RunMarketingInformationWritingResponse:
        """
        @summary 营销文案写作服务
        
        @param request: RunMarketingInformationWritingRequest
        @return: RunMarketingInformationWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_marketing_information_writing_with_options_async(workspace_id, request, headers, runtime)

    def run_script_continue_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptContinueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptContinueResponse:
        """
        @summary 剧本续写
        
        @param request: RunScriptContinueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptContinueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not UtilClient.is_unset(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        if not UtilClient.is_unset(request.user_provided_content):
            body['userProvidedContent'] = request.user_provided_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptContinue',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptContinue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptContinueResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_continue_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptContinueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptContinueResponse:
        """
        @summary 剧本续写
        
        @param request: RunScriptContinueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptContinueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not UtilClient.is_unset(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        if not UtilClient.is_unset(request.user_provided_content):
            body['userProvidedContent'] = request.user_provided_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptContinue',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptContinue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptContinueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_continue(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptContinueRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptContinueResponse:
        """
        @summary 剧本续写
        
        @param request: RunScriptContinueRequest
        @return: RunScriptContinueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_script_continue_with_options(workspace_id, request, headers, runtime)

    async def run_script_continue_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptContinueRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptContinueResponse:
        """
        @summary 剧本续写
        
        @param request: RunScriptContinueRequest
        @return: RunScriptContinueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_script_continue_with_options_async(workspace_id, request, headers, runtime)

    def run_script_planning_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptPlanningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptPlanningResponse:
        """
        @summary 剧本策划
        
        @param request: RunScriptPlanningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptPlanningResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_note):
            body['additionalNote'] = request.additional_note
        if not UtilClient.is_unset(request.dialogue_in_scene):
            body['dialogueInScene'] = request.dialogue_in_scene
        if not UtilClient.is_unset(request.plot_conflict):
            body['plotConflict'] = request.plot_conflict
        if not UtilClient.is_unset(request.script_name):
            body['scriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_shot_count):
            body['scriptShotCount'] = request.script_shot_count
        if not UtilClient.is_unset(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not UtilClient.is_unset(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptPlanning',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptPlanning',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptPlanningResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_planning_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptPlanningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptPlanningResponse:
        """
        @summary 剧本策划
        
        @param request: RunScriptPlanningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptPlanningResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_note):
            body['additionalNote'] = request.additional_note
        if not UtilClient.is_unset(request.dialogue_in_scene):
            body['dialogueInScene'] = request.dialogue_in_scene
        if not UtilClient.is_unset(request.plot_conflict):
            body['plotConflict'] = request.plot_conflict
        if not UtilClient.is_unset(request.script_name):
            body['scriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_shot_count):
            body['scriptShotCount'] = request.script_shot_count
        if not UtilClient.is_unset(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not UtilClient.is_unset(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptPlanning',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptPlanning',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptPlanningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_planning(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptPlanningRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptPlanningResponse:
        """
        @summary 剧本策划
        
        @param request: RunScriptPlanningRequest
        @return: RunScriptPlanningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_script_planning_with_options(workspace_id, request, headers, runtime)

    async def run_script_planning_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptPlanningRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptPlanningResponse:
        """
        @summary 剧本策划
        
        @param request: RunScriptPlanningRequest
        @return: RunScriptPlanningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_script_planning_with_options_async(workspace_id, request, headers, runtime)

    def run_style_writing_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunStyleWritingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunStyleWritingResponse:
        """
        @summary 文体学习和写作推理服务
        
        @param tmp_req: RunStyleWritingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStyleWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunStyleWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.learning_samples):
            request.learning_samples_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.learning_samples, 'learningSamples', 'json')
        if not UtilClient.is_unset(tmp_req.reference_materials):
            request.reference_materials_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_materials, 'referenceMaterials', 'json')
        body = {}
        if not UtilClient.is_unset(request.learning_samples_shrink):
            body['learningSamples'] = request.learning_samples_shrink
        if not UtilClient.is_unset(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not UtilClient.is_unset(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not UtilClient.is_unset(request.writing_theme):
            body['writingTheme'] = request.writing_theme
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStyleWriting',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runStyleWriting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunStyleWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_style_writing_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunStyleWritingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunStyleWritingResponse:
        """
        @summary 文体学习和写作推理服务
        
        @param tmp_req: RunStyleWritingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStyleWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunStyleWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.learning_samples):
            request.learning_samples_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.learning_samples, 'learningSamples', 'json')
        if not UtilClient.is_unset(tmp_req.reference_materials):
            request.reference_materials_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_materials, 'referenceMaterials', 'json')
        body = {}
        if not UtilClient.is_unset(request.learning_samples_shrink):
            body['learningSamples'] = request.learning_samples_shrink
        if not UtilClient.is_unset(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not UtilClient.is_unset(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not UtilClient.is_unset(request.writing_theme):
            body['writingTheme'] = request.writing_theme
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStyleWriting',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runStyleWriting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunStyleWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_style_writing(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunStyleWritingRequest,
    ) -> quan_miao_light_app_20240801_models.RunStyleWritingResponse:
        """
        @summary 文体学习和写作推理服务
        
        @param request: RunStyleWritingRequest
        @return: RunStyleWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_style_writing_with_options(workspace_id, request, headers, runtime)

    async def run_style_writing_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunStyleWritingRequest,
    ) -> quan_miao_light_app_20240801_models.RunStyleWritingResponse:
        """
        @summary 文体学习和写作推理服务
        
        @param request: RunStyleWritingRequest
        @return: RunStyleWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_style_writing_with_options_async(workspace_id, request, headers, runtime)

    def run_video_analysis_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunVideoAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunVideoAnalysisResponse:
        """
        @summary 轻应用-视频理解
        
        @param tmp_req: RunVideoAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunVideoAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunVideoAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        body = {}
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not UtilClient.is_unset(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not UtilClient.is_unset(request.video_url):
            body['videoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunVideoAnalysis',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runVideoAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunVideoAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_video_analysis_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunVideoAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunVideoAnalysisResponse:
        """
        @summary 轻应用-视频理解
        
        @param tmp_req: RunVideoAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunVideoAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunVideoAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        body = {}
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not UtilClient.is_unset(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not UtilClient.is_unset(request.video_url):
            body['videoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunVideoAnalysis',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runVideoAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunVideoAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_video_analysis(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunVideoAnalysisRequest,
    ) -> quan_miao_light_app_20240801_models.RunVideoAnalysisResponse:
        """
        @summary 轻应用-视频理解
        
        @param request: RunVideoAnalysisRequest
        @return: RunVideoAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_video_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_video_analysis_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunVideoAnalysisRequest,
    ) -> quan_miao_light_app_20240801_models.RunVideoAnalysisResponse:
        """
        @summary 轻应用-视频理解
        
        @param request: RunVideoAnalysisRequest
        @return: RunVideoAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_video_analysis_with_options_async(workspace_id, request, headers, runtime)
