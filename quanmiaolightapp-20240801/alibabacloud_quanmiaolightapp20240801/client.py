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

    def cancel_async_task_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.CancelAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAsyncTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/cancelAsyncTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.CancelAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_async_task_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.CancelAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAsyncTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/cancelAsyncTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.CancelAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_async_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.CancelAsyncTaskRequest,
    ) -> quan_miao_light_app_20240801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @return: CancelAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_async_task_with_options(workspace_id, request, headers, runtime)

    async def cancel_async_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.CancelAsyncTaskRequest,
    ) -> quan_miao_light_app_20240801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @return: CancelAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_async_task_with_options_async(workspace_id, request, headers, runtime)

    def export_analysis_tag_detail_by_task_id_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出挖掘任务明细
        
        @param tmp_req: ExportAnalysisTagDetailByTaskIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportAnalysisTagDetailByTaskId',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/exportAnalysisTagDetailByTaskId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_analysis_tag_detail_by_task_id_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出挖掘任务明细
        
        @param tmp_req: ExportAnalysisTagDetailByTaskIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportAnalysisTagDetailByTaskId',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/exportAnalysisTagDetailByTaskId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_analysis_tag_detail_by_task_id(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出挖掘任务明细
        
        @param request: ExportAnalysisTagDetailByTaskIdRequest
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_analysis_tag_detail_by_task_id_with_options(workspace_id, request, headers, runtime)

    async def export_analysis_tag_detail_by_task_id_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> quan_miao_light_app_20240801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出挖掘任务明细
        
        @param request: ExportAnalysisTagDetailByTaskIdRequest
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_analysis_tag_detail_by_task_id_with_options_async(workspace_id, request, headers, runtime)

    def generate_broadcast_news_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GenerateBroadcastNewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GenerateBroadcastNewsResponse:
        """
        @summary 新闻播报-抽取分类获取播报热点
        
        @param request: GenerateBroadcastNewsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateBroadcastNewsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateBroadcastNews',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/GenerateBroadcastNews',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GenerateBroadcastNewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_broadcast_news_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GenerateBroadcastNewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GenerateBroadcastNewsResponse:
        """
        @summary 新闻播报-抽取分类获取播报热点
        
        @param request: GenerateBroadcastNewsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateBroadcastNewsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateBroadcastNews',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/GenerateBroadcastNews',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GenerateBroadcastNewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_broadcast_news(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GenerateBroadcastNewsRequest,
    ) -> quan_miao_light_app_20240801_models.GenerateBroadcastNewsResponse:
        """
        @summary 新闻播报-抽取分类获取播报热点
        
        @param request: GenerateBroadcastNewsRequest
        @return: GenerateBroadcastNewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_broadcast_news_with_options(workspace_id, request, headers, runtime)

    async def generate_broadcast_news_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GenerateBroadcastNewsRequest,
    ) -> quan_miao_light_app_20240801_models.GenerateBroadcastNewsResponse:
        """
        @summary 新闻播报-抽取分类获取播报热点
        
        @param request: GenerateBroadcastNewsRequest
        @return: GenerateBroadcastNewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_broadcast_news_with_options_async(workspace_id, request, headers, runtime)

    def generate_output_format_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.GenerateOutputFormatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GenerateOutputFormatResponse:
        """
        @summary 轻应用-标签挖掘-获取示例输出格式
        
        @param tmp_req: GenerateOutputFormatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateOutputFormatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.GenerateOutputFormatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateOutputFormat',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/generateOutputFormat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GenerateOutputFormatResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_output_format_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.GenerateOutputFormatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GenerateOutputFormatResponse:
        """
        @summary 轻应用-标签挖掘-获取示例输出格式
        
        @param tmp_req: GenerateOutputFormatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateOutputFormatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.GenerateOutputFormatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateOutputFormat',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/generateOutputFormat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GenerateOutputFormatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_output_format(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GenerateOutputFormatRequest,
    ) -> quan_miao_light_app_20240801_models.GenerateOutputFormatResponse:
        """
        @summary 轻应用-标签挖掘-获取示例输出格式
        
        @param request: GenerateOutputFormatRequest
        @return: GenerateOutputFormatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_output_format_with_options(workspace_id, request, headers, runtime)

    async def generate_output_format_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GenerateOutputFormatRequest,
    ) -> quan_miao_light_app_20240801_models.GenerateOutputFormatResponse:
        """
        @summary 轻应用-标签挖掘-获取示例输出格式
        
        @param request: GenerateOutputFormatRequest
        @return: GenerateOutputFormatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_output_format_with_options_async(workspace_id, request, headers, runtime)

    def get_enterprise_voc_analysis_task_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseVocAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/getEnterpriseVocAnalysisTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_voc_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseVocAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/getEnterpriseVocAnalysisTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_voc_analysis_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_enterprise_voc_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def get_enterprise_voc_analysis_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_enterprise_voc_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def get_essay_correction_task_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetEssayCorrectionTaskResponse:
        """
        @summary 获取作业批改结果
        
        @param request: GetEssayCorrectionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEssayCorrectionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEssayCorrectionTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/getEssayCorrectionTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetEssayCorrectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_essay_correction_task_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetEssayCorrectionTaskResponse:
        """
        @summary 获取作业批改结果
        
        @param request: GetEssayCorrectionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEssayCorrectionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEssayCorrectionTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/getEssayCorrectionTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetEssayCorrectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_essay_correction_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEssayCorrectionTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetEssayCorrectionTaskResponse:
        """
        @summary 获取作业批改结果
        
        @param request: GetEssayCorrectionTaskRequest
        @return: GetEssayCorrectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_essay_correction_task_with_options(workspace_id, request, headers, runtime)

    async def get_essay_correction_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetEssayCorrectionTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetEssayCorrectionTaskResponse:
        """
        @summary 获取作业批改结果
        
        @param request: GetEssayCorrectionTaskRequest
        @return: GetEssayCorrectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_essay_correction_task_with_options_async(workspace_id, request, headers, runtime)

    def get_tag_mining_analysis_task_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskResponse:
        """
        @summary 获取挖掘分析任务结果
        
        @param request: GetTagMiningAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTagMiningAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagMiningAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/getTagMiningAnalysisTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_mining_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskResponse:
        """
        @summary 获取挖掘分析任务结果
        
        @param request: GetTagMiningAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTagMiningAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagMiningAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/getTagMiningAnalysisTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_mining_analysis_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskResponse:
        """
        @summary 获取挖掘分析任务结果
        
        @param request: GetTagMiningAnalysisTaskRequest
        @return: GetTagMiningAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tag_mining_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def get_tag_mining_analysis_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetTagMiningAnalysisTaskResponse:
        """
        @summary 获取挖掘分析任务结果
        
        @param request: GetTagMiningAnalysisTaskRequest
        @return: GetTagMiningAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tag_mining_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def get_video_analysis_config_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisConfigResponse:
        """
        @summary 视频理解-获取配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoAnalysisConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVideoAnalysisConfig',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetVideoAnalysisConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_analysis_config_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisConfigResponse:
        """
        @summary 视频理解-获取配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoAnalysisConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVideoAnalysisConfig',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetVideoAnalysisConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_analysis_config(
        self,
        workspace_id: str,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisConfigResponse:
        """
        @summary 视频理解-获取配置
        
        @return: GetVideoAnalysisConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_analysis_config_with_options(workspace_id, headers, runtime)

    async def get_video_analysis_config_async(
        self,
        workspace_id: str,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisConfigResponse:
        """
        @summary 视频理解-获取配置
        
        @return: GetVideoAnalysisConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_video_analysis_config_with_options_async(workspace_id, headers, runtime)

    def get_video_analysis_task_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisTaskResponse:
        """
        @summary 轻应用-获取视频理解异步任务结果
        
        @param request: GetVideoAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetVideoAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisTaskResponse:
        """
        @summary 轻应用-获取视频理解异步任务结果
        
        @param request: GetVideoAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.GetVideoAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_analysis_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetVideoAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisTaskResponse:
        """
        @summary 轻应用-获取视频理解异步任务结果
        
        @param request: GetVideoAnalysisTaskRequest
        @return: GetVideoAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def get_video_analysis_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.GetVideoAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.GetVideoAnalysisTaskResponse:
        """
        @summary 轻应用-获取视频理解异步任务结果
        
        @param request: GetVideoAnalysisTaskRequest
        @return: GetVideoAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_video_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def hot_news_recommend_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.HotNewsRecommendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.HotNewsRecommendResponse:
        """
        @summary 热点新闻推荐
        
        @param request: HotNewsRecommendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotNewsRecommendResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotNewsRecommend',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/hotNewsRecommend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.HotNewsRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def hot_news_recommend_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.HotNewsRecommendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.HotNewsRecommendResponse:
        """
        @summary 热点新闻推荐
        
        @param request: HotNewsRecommendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotNewsRecommendResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotNewsRecommend',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/hotNewsRecommend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.HotNewsRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hot_news_recommend(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.HotNewsRecommendRequest,
    ) -> quan_miao_light_app_20240801_models.HotNewsRecommendResponse:
        """
        @summary 热点新闻推荐
        
        @param request: HotNewsRecommendRequest
        @return: HotNewsRecommendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.hot_news_recommend_with_options(workspace_id, request, headers, runtime)

    async def hot_news_recommend_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.HotNewsRecommendRequest,
    ) -> quan_miao_light_app_20240801_models.HotNewsRecommendResponse:
        """
        @summary 热点新闻推荐
        
        @param request: HotNewsRecommendRequest
        @return: HotNewsRecommendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.hot_news_recommend_with_options_async(workspace_id, request, headers, runtime)

    def list_analysis_tag_detail_by_task_id_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 获取挖掘分析结果明细列表
        
        @param request: ListAnalysisTagDetailByTaskIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnalysisTagDetailByTaskId',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/listAnalysisTagDetailByTaskId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_analysis_tag_detail_by_task_id_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 获取挖掘分析结果明细列表
        
        @param request: ListAnalysisTagDetailByTaskIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnalysisTagDetailByTaskId',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/listAnalysisTagDetailByTaskId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_analysis_tag_detail_by_task_id(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 获取挖掘分析结果明细列表
        
        @param request: ListAnalysisTagDetailByTaskIdRequest
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_analysis_tag_detail_by_task_id_with_options(workspace_id, request, headers, runtime)

    async def list_analysis_tag_detail_by_task_id_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> quan_miao_light_app_20240801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 获取挖掘分析结果明细列表
        
        @param request: ListAnalysisTagDetailByTaskIdRequest
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_analysis_tag_detail_by_task_id_with_options_async(workspace_id, request, headers, runtime)

    def list_hot_topic_summaries_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListHotTopicSummariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.ListHotTopicSummariesResponse:
        """
        @summary 轻应用-新闻播报-获取热点话题摘要列表
        
        @param request: ListHotTopicSummariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotTopicSummariesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.hot_topic):
            body['hotTopic'] = request.hot_topic
        if not UtilClient.is_unset(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotTopicSummaries',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/listHotTopicSummaries',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.ListHotTopicSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_topic_summaries_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListHotTopicSummariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.ListHotTopicSummariesResponse:
        """
        @summary 轻应用-新闻播报-获取热点话题摘要列表
        
        @param request: ListHotTopicSummariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotTopicSummariesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.hot_topic):
            body['hotTopic'] = request.hot_topic
        if not UtilClient.is_unset(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotTopicSummaries',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/listHotTopicSummaries',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.ListHotTopicSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_topic_summaries(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListHotTopicSummariesRequest,
    ) -> quan_miao_light_app_20240801_models.ListHotTopicSummariesResponse:
        """
        @summary 轻应用-新闻播报-获取热点话题摘要列表
        
        @param request: ListHotTopicSummariesRequest
        @return: ListHotTopicSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hot_topic_summaries_with_options(workspace_id, request, headers, runtime)

    async def list_hot_topic_summaries_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.ListHotTopicSummariesRequest,
    ) -> quan_miao_light_app_20240801_models.ListHotTopicSummariesResponse:
        """
        @summary 轻应用-新闻播报-获取热点话题摘要列表
        
        @param request: ListHotTopicSummariesRequest
        @return: ListHotTopicSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hot_topic_summaries_with_options_async(workspace_id, request, headers, runtime)

    def run_enterprise_voc_analysis_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisResponse:
        """
        @summary 企业VOC分析
        
        @param tmp_req: RunEnterpriseVocAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunEnterpriseVocAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_tags):
            request.filter_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['akProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunEnterpriseVocAnalysis',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runEnterpriseVocAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_enterprise_voc_analysis_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisResponse:
        """
        @summary 企业VOC分析
        
        @param tmp_req: RunEnterpriseVocAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunEnterpriseVocAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_tags):
            request.filter_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.ak_proxy):
            body['akProxy'] = request.ak_proxy
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunEnterpriseVocAnalysis',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runEnterpriseVocAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_enterprise_voc_analysis(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisRequest,
    ) -> quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisResponse:
        """
        @summary 企业VOC分析
        
        @param request: RunEnterpriseVocAnalysisRequest
        @return: RunEnterpriseVocAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_enterprise_voc_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_enterprise_voc_analysis_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisRequest,
    ) -> quan_miao_light_app_20240801_models.RunEnterpriseVocAnalysisResponse:
        """
        @summary 企业VOC分析
        
        @param request: RunEnterpriseVocAnalysisRequest
        @return: RunEnterpriseVocAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_enterprise_voc_analysis_with_options_async(workspace_id, request, headers, runtime)

    def run_essay_correction_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunEssayCorrectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunEssayCorrectionResponse:
        """
        @summary 作业批改
        
        @param request: RunEssayCorrectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunEssayCorrectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.answer):
            body['answer'] = request.answer
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunEssayCorrection',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runEssayCorrection',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunEssayCorrectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_essay_correction_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunEssayCorrectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunEssayCorrectionResponse:
        """
        @summary 作业批改
        
        @param request: RunEssayCorrectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunEssayCorrectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.answer):
            body['answer'] = request.answer
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunEssayCorrection',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runEssayCorrection',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunEssayCorrectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_essay_correction(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunEssayCorrectionRequest,
    ) -> quan_miao_light_app_20240801_models.RunEssayCorrectionResponse:
        """
        @summary 作业批改
        
        @param request: RunEssayCorrectionRequest
        @return: RunEssayCorrectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_essay_correction_with_options(workspace_id, request, headers, runtime)

    async def run_essay_correction_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunEssayCorrectionRequest,
    ) -> quan_miao_light_app_20240801_models.RunEssayCorrectionResponse:
        """
        @summary 作业批改
        
        @param request: RunEssayCorrectionRequest
        @return: RunEssayCorrectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_essay_correction_with_options_async(workspace_id, request, headers, runtime)

    def run_hot_topic_chat_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunHotTopicChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicChatResponse:
        """
        @summary 轻应用-热点播报-问答
        
        @param tmp_req: RunHotTopicChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunHotTopicChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunHotTopicChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.hot_topics):
            request.hot_topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hot_topics, 'hotTopics', 'json')
        if not UtilClient.is_unset(tmp_req.messages):
            request.messages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.messages, 'messages', 'json')
        if not UtilClient.is_unset(tmp_req.step_for_broadcast_content_config):
            request.step_for_broadcast_content_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_broadcast_content_config, 'stepForBroadcastContentConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.hot_topics_shrink):
            body['hotTopics'] = request.hot_topics_shrink
        if not UtilClient.is_unset(request.image_count):
            body['imageCount'] = request.image_count
        if not UtilClient.is_unset(request.messages_shrink):
            body['messages'] = request.messages_shrink
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.step_for_broadcast_content_config_shrink):
            body['stepForBroadcastContentConfig'] = request.step_for_broadcast_content_config_shrink
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunHotTopicChat',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runHotTopicChat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunHotTopicChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_hot_topic_chat_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunHotTopicChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicChatResponse:
        """
        @summary 轻应用-热点播报-问答
        
        @param tmp_req: RunHotTopicChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunHotTopicChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunHotTopicChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.hot_topics):
            request.hot_topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hot_topics, 'hotTopics', 'json')
        if not UtilClient.is_unset(tmp_req.messages):
            request.messages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.messages, 'messages', 'json')
        if not UtilClient.is_unset(tmp_req.step_for_broadcast_content_config):
            request.step_for_broadcast_content_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_broadcast_content_config, 'stepForBroadcastContentConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.hot_topics_shrink):
            body['hotTopics'] = request.hot_topics_shrink
        if not UtilClient.is_unset(request.image_count):
            body['imageCount'] = request.image_count
        if not UtilClient.is_unset(request.messages_shrink):
            body['messages'] = request.messages_shrink
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.step_for_broadcast_content_config_shrink):
            body['stepForBroadcastContentConfig'] = request.step_for_broadcast_content_config_shrink
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunHotTopicChat',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runHotTopicChat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunHotTopicChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_hot_topic_chat(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunHotTopicChatRequest,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicChatResponse:
        """
        @summary 轻应用-热点播报-问答
        
        @param request: RunHotTopicChatRequest
        @return: RunHotTopicChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_hot_topic_chat_with_options(workspace_id, request, headers, runtime)

    async def run_hot_topic_chat_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunHotTopicChatRequest,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicChatResponse:
        """
        @summary 轻应用-热点播报-问答
        
        @param request: RunHotTopicChatRequest
        @return: RunHotTopicChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_hot_topic_chat_with_options_async(workspace_id, request, headers, runtime)

    def run_hot_topic_summary_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunHotTopicSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicSummaryResponse:
        """
        @summary 轻应用-热点播报-热点摘要生成
        
        @param tmp_req: RunHotTopicSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunHotTopicSummaryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunHotTopicSummaryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'stepForCustomSummaryStyleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.topic_ids):
            request.topic_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_ids, 'topicIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.step_for_custom_summary_style_config_shrink):
            body['stepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not UtilClient.is_unset(request.topic_ids_shrink):
            body['topicIds'] = request.topic_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunHotTopicSummary',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runHotTopicSummary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunHotTopicSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_hot_topic_summary_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunHotTopicSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicSummaryResponse:
        """
        @summary 轻应用-热点播报-热点摘要生成
        
        @param tmp_req: RunHotTopicSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunHotTopicSummaryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunHotTopicSummaryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'stepForCustomSummaryStyleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.topic_ids):
            request.topic_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_ids, 'topicIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.step_for_custom_summary_style_config_shrink):
            body['stepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not UtilClient.is_unset(request.topic_ids_shrink):
            body['topicIds'] = request.topic_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunHotTopicSummary',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runHotTopicSummary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunHotTopicSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_hot_topic_summary(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunHotTopicSummaryRequest,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicSummaryResponse:
        """
        @summary 轻应用-热点播报-热点摘要生成
        
        @param request: RunHotTopicSummaryRequest
        @return: RunHotTopicSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_hot_topic_summary_with_options(workspace_id, request, headers, runtime)

    async def run_hot_topic_summary_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunHotTopicSummaryRequest,
    ) -> quan_miao_light_app_20240801_models.RunHotTopicSummaryResponse:
        """
        @summary 轻应用-热点播报-热点摘要生成
        
        @param request: RunHotTopicSummaryRequest
        @return: RunHotTopicSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_hot_topic_summary_with_options_async(workspace_id, request, headers, runtime)

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
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.custom_limitation):
            body['customLimitation'] = request.custom_limitation
        if not UtilClient.is_unset(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not UtilClient.is_unset(request.input_example):
            body['inputExample'] = request.input_example
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_example):
            body['outputExample'] = request.output_example
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
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.custom_limitation):
            body['customLimitation'] = request.custom_limitation
        if not UtilClient.is_unset(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not UtilClient.is_unset(request.input_example):
            body['inputExample'] = request.input_example
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_example):
            body['outputExample'] = request.output_example
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

    def run_network_content_audit_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunNetworkContentAuditRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunNetworkContentAuditResponse:
        """
        @summary 轻应用-网络内容审核
        
        @param tmp_req: RunNetworkContentAuditRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNetworkContentAuditResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunNetworkContentAuditShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunNetworkContentAudit',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runNetworkContentAudit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunNetworkContentAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_network_content_audit_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunNetworkContentAuditRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunNetworkContentAuditResponse:
        """
        @summary 轻应用-网络内容审核
        
        @param tmp_req: RunNetworkContentAuditRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNetworkContentAuditResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunNetworkContentAuditShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunNetworkContentAudit',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runNetworkContentAudit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunNetworkContentAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_network_content_audit(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunNetworkContentAuditRequest,
    ) -> quan_miao_light_app_20240801_models.RunNetworkContentAuditResponse:
        """
        @summary 轻应用-网络内容审核
        
        @param request: RunNetworkContentAuditRequest
        @return: RunNetworkContentAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_network_content_audit_with_options(workspace_id, request, headers, runtime)

    async def run_network_content_audit_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunNetworkContentAuditRequest,
    ) -> quan_miao_light_app_20240801_models.RunNetworkContentAuditResponse:
        """
        @summary 轻应用-网络内容审核
        
        @param request: RunNetworkContentAuditRequest
        @return: RunNetworkContentAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_network_content_audit_with_options_async(workspace_id, request, headers, runtime)

    def run_ocr_parse_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunOcrParseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunOcrParseResponse:
        """
        @summary 作业批改
        
        @param request: RunOcrParseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunOcrParseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunOcrParse',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runOcrParse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunOcrParseResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_ocr_parse_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunOcrParseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunOcrParseResponse:
        """
        @summary 作业批改
        
        @param request: RunOcrParseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunOcrParseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunOcrParse',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runOcrParse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunOcrParseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_ocr_parse(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunOcrParseRequest,
    ) -> quan_miao_light_app_20240801_models.RunOcrParseResponse:
        """
        @summary 作业批改
        
        @param request: RunOcrParseRequest
        @return: RunOcrParseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_ocr_parse_with_options(workspace_id, request, headers, runtime)

    async def run_ocr_parse_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunOcrParseRequest,
    ) -> quan_miao_light_app_20240801_models.RunOcrParseResponse:
        """
        @summary 作业批改
        
        @param request: RunOcrParseRequest
        @return: RunOcrParseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_ocr_parse_with_options_async(workspace_id, request, headers, runtime)

    def run_script_chat_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptChatResponse:
        """
        @summary 长剧本创作
        
        @param request: RunScriptChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptChat',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptChat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_chat_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptChatResponse:
        """
        @summary 长剧本创作
        
        @param request: RunScriptChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptChat',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptChat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_chat(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptChatRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptChatResponse:
        """
        @summary 长剧本创作
        
        @param request: RunScriptChatRequest
        @return: RunScriptChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_script_chat_with_options(workspace_id, request, headers, runtime)

    async def run_script_chat_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptChatRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptChatResponse:
        """
        @summary 长剧本创作
        
        @param request: RunScriptChatRequest
        @return: RunScriptChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_script_chat_with_options_async(workspace_id, request, headers, runtime)

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

    def run_script_refine_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptRefineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptRefineResponse:
        """
        @summary 剧本对话内容的整理
        
        @param request: RunScriptRefineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptRefineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptRefine',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptRefine',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptRefineResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_refine_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptRefineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunScriptRefineResponse:
        """
        @summary 剧本对话内容的整理
        
        @param request: RunScriptRefineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunScriptRefineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunScriptRefine',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runScriptRefine',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunScriptRefineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_refine(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptRefineRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptRefineResponse:
        """
        @summary 剧本对话内容的整理
        
        @param request: RunScriptRefineRequest
        @return: RunScriptRefineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_script_refine_with_options(workspace_id, request, headers, runtime)

    async def run_script_refine_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunScriptRefineRequest,
    ) -> quan_miao_light_app_20240801_models.RunScriptRefineResponse:
        """
        @summary 剧本对话内容的整理
        
        @param request: RunScriptRefineRequest
        @return: RunScriptRefineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_script_refine_with_options_async(workspace_id, request, headers, runtime)

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
        if not UtilClient.is_unset(request.process_stage):
            body['processStage'] = request.process_stage
        if not UtilClient.is_unset(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not UtilClient.is_unset(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not UtilClient.is_unset(request.use_search):
            body['useSearch'] = request.use_search
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
        if not UtilClient.is_unset(request.process_stage):
            body['processStage'] = request.process_stage
        if not UtilClient.is_unset(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not UtilClient.is_unset(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not UtilClient.is_unset(request.use_search):
            body['useSearch'] = request.use_search
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

    def run_tag_mining_analysis_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunTagMiningAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunTagMiningAnalysisResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param tmp_req: RunTagMiningAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTagMiningAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunTagMiningAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTagMiningAnalysis',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runTagMiningAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunTagMiningAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_tag_mining_analysis_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.RunTagMiningAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.RunTagMiningAnalysisResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param tmp_req: RunTagMiningAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTagMiningAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.RunTagMiningAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTagMiningAnalysis',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/runTagMiningAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.RunTagMiningAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_tag_mining_analysis(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunTagMiningAnalysisRequest,
    ) -> quan_miao_light_app_20240801_models.RunTagMiningAnalysisResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param request: RunTagMiningAnalysisRequest
        @return: RunTagMiningAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_tag_mining_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_tag_mining_analysis_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.RunTagMiningAnalysisRequest,
    ) -> quan_miao_light_app_20240801_models.RunTagMiningAnalysisResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param request: RunTagMiningAnalysisRequest
        @return: RunTagMiningAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_tag_mining_analysis_with_options_async(workspace_id, request, headers, runtime)

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
        if not UtilClient.is_unset(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not UtilClient.is_unset(tmp_req.video_caption_info):
            request.video_caption_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_roles):
            request.video_roles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        body = {}
        if not UtilClient.is_unset(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not UtilClient.is_unset(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not UtilClient.is_unset(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not UtilClient.is_unset(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not UtilClient.is_unset(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not UtilClient.is_unset(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not UtilClient.is_unset(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not UtilClient.is_unset(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not UtilClient.is_unset(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not UtilClient.is_unset(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not UtilClient.is_unset(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
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
        if not UtilClient.is_unset(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not UtilClient.is_unset(tmp_req.video_caption_info):
            request.video_caption_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_roles):
            request.video_roles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        body = {}
        if not UtilClient.is_unset(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not UtilClient.is_unset(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not UtilClient.is_unset(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not UtilClient.is_unset(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not UtilClient.is_unset(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not UtilClient.is_unset(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not UtilClient.is_unset(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not UtilClient.is_unset(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not UtilClient.is_unset(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not UtilClient.is_unset(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not UtilClient.is_unset(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
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

    def submit_enterprise_voc_analysis_task_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交企业VOC异步任务
        
        @param tmp_req: SubmitEnterpriseVocAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not UtilClient.is_unset(tmp_req.filter_tags):
            request.filter_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEnterpriseVocAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/submitEnterpriseVocAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_enterprise_voc_analysis_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交企业VOC异步任务
        
        @param tmp_req: SubmitEnterpriseVocAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not UtilClient.is_unset(tmp_req.filter_tags):
            request.filter_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEnterpriseVocAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/submitEnterpriseVocAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_enterprise_voc_analysis_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交企业VOC异步任务
        
        @param request: SubmitEnterpriseVocAnalysisTaskRequest
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_enterprise_voc_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def submit_enterprise_voc_analysis_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交企业VOC异步任务
        
        @param request: SubmitEnterpriseVocAnalysisTaskRequest
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_enterprise_voc_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def submit_essay_correction_task_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskResponse:
        """
        @summary 提交批改任务
        
        @param tmp_req: SubmitEssayCorrectionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEssayCorrectionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tasks):
            request.tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tasks, 'tasks', 'json')
        body = {}
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tasks_shrink):
            body['tasks'] = request.tasks_shrink
        if not UtilClient.is_unset(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEssayCorrectionTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/submitEssayCorrectionTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_essay_correction_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskResponse:
        """
        @summary 提交批改任务
        
        @param tmp_req: SubmitEssayCorrectionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEssayCorrectionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tasks):
            request.tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tasks, 'tasks', 'json')
        body = {}
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tasks_shrink):
            body['tasks'] = request.tasks_shrink
        if not UtilClient.is_unset(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEssayCorrectionTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/submitEssayCorrectionTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_essay_correction_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskResponse:
        """
        @summary 提交批改任务
        
        @param request: SubmitEssayCorrectionTaskRequest
        @return: SubmitEssayCorrectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_essay_correction_task_with_options(workspace_id, request, headers, runtime)

    async def submit_essay_correction_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitEssayCorrectionTaskResponse:
        """
        @summary 提交批改任务
        
        @param request: SubmitEssayCorrectionTaskRequest
        @return: SubmitEssayCorrectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_essay_correction_task_with_options_async(workspace_id, request, headers, runtime)

    def submit_tag_mining_analysis_task_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param tmp_req: SubmitTagMiningAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTagMiningAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTagMiningAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/submitTagMiningAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_tag_mining_analysis_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param tmp_req: SubmitTagMiningAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTagMiningAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['apiKey'] = request.api_key
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.output_format):
            body['outputFormat'] = request.output_format
        if not UtilClient.is_unset(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_description):
            body['taskDescription'] = request.task_description
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTagMiningAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/submitTagMiningAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_tag_mining_analysis_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param request: SubmitTagMiningAnalysisTaskRequest
        @return: SubmitTagMiningAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_tag_mining_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def submit_tag_mining_analysis_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitTagMiningAnalysisTaskResponse:
        """
        @summary 轻应用-标签挖掘
        
        @param request: SubmitTagMiningAnalysisTaskRequest
        @return: SubmitTagMiningAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_tag_mining_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def submit_video_analysis_task_with_options(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskResponse:
        """
        @summary 轻应用-提交视频理解任务
        
        @param tmp_req: SubmitVideoAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitVideoAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not UtilClient.is_unset(tmp_req.video_caption_info):
            request.video_caption_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_roles):
            request.video_roles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        body = {}
        if not UtilClient.is_unset(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not UtilClient.is_unset(request.deduplication_id):
            body['deduplicationId'] = request.deduplication_id
        if not UtilClient.is_unset(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not UtilClient.is_unset(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not UtilClient.is_unset(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not UtilClient.is_unset(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not UtilClient.is_unset(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not UtilClient.is_unset(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not UtilClient.is_unset(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not UtilClient.is_unset(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not UtilClient.is_unset(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not UtilClient.is_unset(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not UtilClient.is_unset(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not UtilClient.is_unset(request.video_url):
            body['videoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitVideoAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/submitVideoAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_analysis_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskResponse:
        """
        @summary 轻应用-提交视频理解任务
        
        @param tmp_req: SubmitVideoAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitVideoAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not UtilClient.is_unset(tmp_req.generate_options):
            request.generate_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not UtilClient.is_unset(tmp_req.video_caption_info):
            request.video_caption_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_roles):
            request.video_roles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        body = {}
        if not UtilClient.is_unset(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not UtilClient.is_unset(request.deduplication_id):
            body['deduplicationId'] = request.deduplication_id
        if not UtilClient.is_unset(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not UtilClient.is_unset(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not UtilClient.is_unset(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not UtilClient.is_unset(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not UtilClient.is_unset(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not UtilClient.is_unset(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not UtilClient.is_unset(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not UtilClient.is_unset(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not UtilClient.is_unset(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not UtilClient.is_unset(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not UtilClient.is_unset(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not UtilClient.is_unset(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not UtilClient.is_unset(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not UtilClient.is_unset(request.video_url):
            body['videoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitVideoAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/submitVideoAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_video_analysis_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskResponse:
        """
        @summary 轻应用-提交视频理解任务
        
        @param request: SubmitVideoAnalysisTaskRequest
        @return: SubmitVideoAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_video_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def submit_video_analysis_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.SubmitVideoAnalysisTaskResponse:
        """
        @summary 轻应用-提交视频理解任务
        
        @param request: SubmitVideoAnalysisTaskRequest
        @return: SubmitVideoAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_video_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def update_video_analysis_config_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigResponse:
        """
        @summary 视频理解-更新配置
        
        @param request: UpdateVideoAnalysisConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVideoAnalysisConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async_concurrency):
            body['asyncConcurrency'] = request.async_concurrency
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVideoAnalysisConfig',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisConfig',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_analysis_config_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigResponse:
        """
        @summary 视频理解-更新配置
        
        @param request: UpdateVideoAnalysisConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVideoAnalysisConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async_concurrency):
            body['asyncConcurrency'] = request.async_concurrency
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVideoAnalysisConfig',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisConfig',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_analysis_config(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigRequest,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigResponse:
        """
        @summary 视频理解-更新配置
        
        @param request: UpdateVideoAnalysisConfigRequest
        @return: UpdateVideoAnalysisConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_video_analysis_config_with_options(workspace_id, request, headers, runtime)

    async def update_video_analysis_config_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigRequest,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisConfigResponse:
        """
        @summary 视频理解-更新配置
        
        @param request: UpdateVideoAnalysisConfigRequest
        @return: UpdateVideoAnalysisConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_video_analysis_config_with_options_async(workspace_id, request, headers, runtime)

    def update_video_analysis_task_with_options(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskResponse:
        """
        @summary 视频理解-修改任务状态
        
        @param request: UpdateVideoAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVideoAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVideoAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisTask',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskResponse:
        """
        @summary 视频理解-修改任务状态
        
        @param request: UpdateVideoAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVideoAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVideoAnalysisTask',
            version='2024-08-01',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisTask',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_analysis_task(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskResponse:
        """
        @summary 视频理解-修改任务状态
        
        @param request: UpdateVideoAnalysisTaskRequest
        @return: UpdateVideoAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_video_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def update_video_analysis_task_async(
        self,
        workspace_id: str,
        request: quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskRequest,
    ) -> quan_miao_light_app_20240801_models.UpdateVideoAnalysisTaskResponse:
        """
        @summary 视频理解-修改任务状态
        
        @param request: UpdateVideoAnalysisTaskRequest
        @return: UpdateVideoAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_video_analysis_task_with_options_async(workspace_id, request, headers, runtime)
