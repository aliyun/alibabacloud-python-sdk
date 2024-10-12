# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dianjin20240628 import models as dian_jin_20240628_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models


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
        self._endpoint = self.get_endpoint('dianjin', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_annual_doc_summary_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateAnnualDocSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateAnnualDocSummaryTaskResponse:
        """
        @summary 创建按年文档总结任务
        
        @param request: CreateAnnualDocSummaryTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnnualDocSummaryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ana_years):
            body['anaYears'] = request.ana_years
        if not UtilClient.is_unset(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not UtilClient.is_unset(request.enable_table):
            body['enableTable'] = request.enable_table
        if not UtilClient.is_unset(request.instruction):
            body['instruction'] = request.instruction
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAnnualDocSummaryTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary/doc/annual',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateAnnualDocSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_annual_doc_summary_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateAnnualDocSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateAnnualDocSummaryTaskResponse:
        """
        @summary 创建按年文档总结任务
        
        @param request: CreateAnnualDocSummaryTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnnualDocSummaryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ana_years):
            body['anaYears'] = request.ana_years
        if not UtilClient.is_unset(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not UtilClient.is_unset(request.enable_table):
            body['enableTable'] = request.enable_table
        if not UtilClient.is_unset(request.instruction):
            body['instruction'] = request.instruction
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAnnualDocSummaryTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary/doc/annual',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateAnnualDocSummaryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_annual_doc_summary_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateAnnualDocSummaryTaskRequest,
    ) -> dian_jin_20240628_models.CreateAnnualDocSummaryTaskResponse:
        """
        @summary 创建按年文档总结任务
        
        @param request: CreateAnnualDocSummaryTaskRequest
        @return: CreateAnnualDocSummaryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_annual_doc_summary_task_with_options(workspace_id, request, headers, runtime)

    async def create_annual_doc_summary_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateAnnualDocSummaryTaskRequest,
    ) -> dian_jin_20240628_models.CreateAnnualDocSummaryTaskResponse:
        """
        @summary 创建按年文档总结任务
        
        @param request: CreateAnnualDocSummaryTaskRequest
        @return: CreateAnnualDocSummaryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_annual_doc_summary_task_with_options_async(workspace_id, request, headers, runtime)

    def create_docs_summary_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDocsSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateDocsSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateDocsSummaryTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocsSummaryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not UtilClient.is_unset(request.enable_table):
            body['enableTable'] = request.enable_table
        if not UtilClient.is_unset(request.instruction):
            body['instruction'] = request.instruction
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDocsSummaryTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary/docs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateDocsSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_docs_summary_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDocsSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateDocsSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateDocsSummaryTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocsSummaryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not UtilClient.is_unset(request.enable_table):
            body['enableTable'] = request.enable_table
        if not UtilClient.is_unset(request.instruction):
            body['instruction'] = request.instruction
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDocsSummaryTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary/docs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateDocsSummaryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_docs_summary_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDocsSummaryTaskRequest,
    ) -> dian_jin_20240628_models.CreateDocsSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateDocsSummaryTaskRequest
        @return: CreateDocsSummaryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_docs_summary_task_with_options(workspace_id, request, headers, runtime)

    async def create_docs_summary_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDocsSummaryTaskRequest,
    ) -> dian_jin_20240628_models.CreateDocsSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateDocsSummaryTaskRequest
        @return: CreateDocsSummaryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_docs_summary_task_with_options_async(workspace_id, request, headers, runtime)

    def create_fin_report_summary_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateFinReportSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateFinReportSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateFinReportSummaryTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFinReportSummaryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.enable_table):
            body['enableTable'] = request.enable_table
        if not UtilClient.is_unset(request.end_page):
            body['endPage'] = request.end_page
        if not UtilClient.is_unset(request.instruction):
            body['instruction'] = request.instruction
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.start_page):
            body['startPage'] = request.start_page
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFinReportSummaryTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateFinReportSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fin_report_summary_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateFinReportSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateFinReportSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateFinReportSummaryTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFinReportSummaryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.enable_table):
            body['enableTable'] = request.enable_table
        if not UtilClient.is_unset(request.end_page):
            body['endPage'] = request.end_page
        if not UtilClient.is_unset(request.instruction):
            body['instruction'] = request.instruction
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.start_page):
            body['startPage'] = request.start_page
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFinReportSummaryTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateFinReportSummaryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fin_report_summary_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateFinReportSummaryTaskRequest,
    ) -> dian_jin_20240628_models.CreateFinReportSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateFinReportSummaryTaskRequest
        @return: CreateFinReportSummaryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_fin_report_summary_task_with_options(workspace_id, request, headers, runtime)

    async def create_fin_report_summary_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateFinReportSummaryTaskRequest,
    ) -> dian_jin_20240628_models.CreateFinReportSummaryTaskResponse:
        """
        @summary 创建财报总结任务
        
        @param request: CreateFinReportSummaryTaskRequest
        @return: CreateFinReportSummaryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_fin_report_summary_task_with_options_async(workspace_id, request, headers, runtime)

    def create_library_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateLibraryResponse:
        """
        @summary 创建文档库
        
        @param request: CreateLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLibraryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not UtilClient.is_unset(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateLibraryResponse:
        """
        @summary 创建文档库
        
        @param request: CreateLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLibraryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not UtilClient.is_unset(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_library(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateLibraryRequest,
    ) -> dian_jin_20240628_models.CreateLibraryResponse:
        """
        @summary 创建文档库
        
        @param request: CreateLibraryRequest
        @return: CreateLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_library_with_options(workspace_id, request, headers, runtime)

    async def create_library_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateLibraryRequest,
    ) -> dian_jin_20240628_models.CreateLibraryResponse:
        """
        @summary 创建文档库
        
        @param request: CreateLibraryRequest
        @return: CreateLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_library_with_options_async(workspace_id, request, headers, runtime)

    def create_pdf_translate_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePdfTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreatePdfTranslateTaskResponse:
        """
        @summary 创建PDF翻译任务
        
        @param request: CreatePdfTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePdfTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.knowledge):
            body['knowledge'] = request.knowledge
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.translate_to):
            body['translateTo'] = request.translate_to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePdfTranslateTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/pdfTranslate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreatePdfTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdf_translate_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePdfTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreatePdfTranslateTaskResponse:
        """
        @summary 创建PDF翻译任务
        
        @param request: CreatePdfTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePdfTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.knowledge):
            body['knowledge'] = request.knowledge
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.translate_to):
            body['translateTo'] = request.translate_to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePdfTranslateTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/pdfTranslate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreatePdfTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdf_translate_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePdfTranslateTaskRequest,
    ) -> dian_jin_20240628_models.CreatePdfTranslateTaskResponse:
        """
        @summary 创建PDF翻译任务
        
        @param request: CreatePdfTranslateTaskRequest
        @return: CreatePdfTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pdf_translate_task_with_options(workspace_id, request, headers, runtime)

    async def create_pdf_translate_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePdfTranslateTaskRequest,
    ) -> dian_jin_20240628_models.CreatePdfTranslateTaskResponse:
        """
        @summary 创建PDF翻译任务
        
        @param request: CreatePdfTranslateTaskRequest
        @return: CreatePdfTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pdf_translate_task_with_options_async(workspace_id, request, headers, runtime)

    def create_predefined_document_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePredefinedDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreatePredefinedDocumentResponse:
        """
        @summary 创建预定义文档
        
        @param request: CreatePredefinedDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePredefinedDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chunks):
            body['chunks'] = request.chunks
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.metadata):
            body['metadata'] = request.metadata
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePredefinedDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/createPredefinedDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreatePredefinedDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_predefined_document_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePredefinedDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreatePredefinedDocumentResponse:
        """
        @summary 创建预定义文档
        
        @param request: CreatePredefinedDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePredefinedDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chunks):
            body['chunks'] = request.chunks
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.metadata):
            body['metadata'] = request.metadata
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePredefinedDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/createPredefinedDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreatePredefinedDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_predefined_document(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePredefinedDocumentRequest,
    ) -> dian_jin_20240628_models.CreatePredefinedDocumentResponse:
        """
        @summary 创建预定义文档
        
        @param request: CreatePredefinedDocumentRequest
        @return: CreatePredefinedDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_predefined_document_with_options(workspace_id, request, headers, runtime)

    async def create_predefined_document_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreatePredefinedDocumentRequest,
    ) -> dian_jin_20240628_models.CreatePredefinedDocumentResponse:
        """
        @summary 创建预定义文档
        
        @param request: CreatePredefinedDocumentRequest
        @return: CreatePredefinedDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_predefined_document_with_options_async(workspace_id, request, headers, runtime)

    def create_quality_check_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateQualityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateQualityCheckTaskResponse:
        """
        @summary 创建财报总结的任务
        
        @param request: CreateQualityCheckTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityCheckTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not UtilClient.is_unset(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.quality_group):
            body['qualityGroup'] = request.quality_group
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityCheckTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/qualitycheck/task/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateQualityCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_check_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateQualityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateQualityCheckTaskResponse:
        """
        @summary 创建财报总结的任务
        
        @param request: CreateQualityCheckTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityCheckTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not UtilClient.is_unset(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.quality_group):
            body['qualityGroup'] = request.quality_group
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityCheckTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/qualitycheck/task/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateQualityCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_check_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateQualityCheckTaskRequest,
    ) -> dian_jin_20240628_models.CreateQualityCheckTaskResponse:
        """
        @summary 创建财报总结的任务
        
        @param request: CreateQualityCheckTaskRequest
        @return: CreateQualityCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quality_check_task_with_options(workspace_id, request, headers, runtime)

    async def create_quality_check_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateQualityCheckTaskRequest,
    ) -> dian_jin_20240628_models.CreateQualityCheckTaskResponse:
        """
        @summary 创建财报总结的任务
        
        @param request: CreateQualityCheckTaskRequest
        @return: CreateQualityCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_quality_check_task_with_options_async(workspace_id, request, headers, runtime)

    def delete_document_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.DeleteDocumentResponse:
        """
        @summary 删除文档
        
        @param request: DeleteDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_ids):
            body['docIds'] = request.doc_ids
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.DeleteDocumentResponse:
        """
        @summary 删除文档
        
        @param request: DeleteDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_ids):
            body['docIds'] = request.doc_ids
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteDocumentRequest,
    ) -> dian_jin_20240628_models.DeleteDocumentResponse:
        """
        @summary 删除文档
        
        @param request: DeleteDocumentRequest
        @return: DeleteDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_document_with_options(workspace_id, request, headers, runtime)

    async def delete_document_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteDocumentRequest,
    ) -> dian_jin_20240628_models.DeleteDocumentResponse:
        """
        @summary 删除文档
        
        @param request: DeleteDocumentRequest
        @return: DeleteDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_document_with_options_async(workspace_id, request, headers, runtime)

    def delete_library_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.DeleteLibraryResponse:
        """
        @summary 删除文档库
        
        @param request: DeleteLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.DeleteLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_library_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.DeleteLibraryResponse:
        """
        @summary 删除文档库
        
        @param request: DeleteLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.DeleteLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_library(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteLibraryRequest,
    ) -> dian_jin_20240628_models.DeleteLibraryResponse:
        """
        @summary 删除文档库
        
        @param request: DeleteLibraryRequest
        @return: DeleteLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_library_with_options(workspace_id, request, headers, runtime)

    async def delete_library_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.DeleteLibraryRequest,
    ) -> dian_jin_20240628_models.DeleteLibraryResponse:
        """
        @summary 删除文档库
        
        @param request: DeleteLibraryRequest
        @return: DeleteLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_library_with_options_async(workspace_id, request, headers, runtime)

    def evict_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.EvictTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.EvictTaskResponse:
        """
        @summary 中断任务
        
        @param request: EvictTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvictTaskResponse
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
            action='EvictTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/evict',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.EvictTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def evict_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.EvictTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.EvictTaskResponse:
        """
        @summary 中断任务
        
        @param request: EvictTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvictTaskResponse
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
            action='EvictTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/evict',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.EvictTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evict_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.EvictTaskRequest,
    ) -> dian_jin_20240628_models.EvictTaskResponse:
        """
        @summary 中断任务
        
        @param request: EvictTaskRequest
        @return: EvictTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.evict_task_with_options(workspace_id, request, headers, runtime)

    async def evict_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.EvictTaskRequest,
    ) -> dian_jin_20240628_models.EvictTaskResponse:
        """
        @summary 中断任务
        
        @param request: EvictTaskRequest
        @return: EvictTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.evict_task_with_options_async(workspace_id, request, headers, runtime)

    def get_app_config_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetAppConfigResponse:
        """
        @summary 获取app配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppConfig',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/app/config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_config_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetAppConfigResponse:
        """
        @summary 获取app配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppConfig',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/app/config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_config(
        self,
        workspace_id: str,
    ) -> dian_jin_20240628_models.GetAppConfigResponse:
        """
        @summary 获取app配置
        
        @return: GetAppConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_config_with_options(workspace_id, headers, runtime)

    async def get_app_config_async(
        self,
        workspace_id: str,
    ) -> dian_jin_20240628_models.GetAppConfigResponse:
        """
        @summary 获取app配置
        
        @return: GetAppConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_app_config_with_options_async(workspace_id, headers, runtime)

    def get_document_chunk_list_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentChunkListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDocumentChunkListResponse:
        """
        @summary 获取文档的chunk列表
        
        @param request: GetDocumentChunkListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentChunkListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chunk_id_list):
            body['chunkIdList'] = request.chunk_id_list
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            body['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentChunkList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/getDocumentChunk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDocumentChunkListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_chunk_list_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentChunkListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDocumentChunkListResponse:
        """
        @summary 获取文档的chunk列表
        
        @param request: GetDocumentChunkListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentChunkListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chunk_id_list):
            body['chunkIdList'] = request.chunk_id_list
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            body['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentChunkList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/getDocumentChunk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDocumentChunkListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_chunk_list(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentChunkListRequest,
    ) -> dian_jin_20240628_models.GetDocumentChunkListResponse:
        """
        @summary 获取文档的chunk列表
        
        @param request: GetDocumentChunkListRequest
        @return: GetDocumentChunkListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_document_chunk_list_with_options(workspace_id, request, headers, runtime)

    async def get_document_chunk_list_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentChunkListRequest,
    ) -> dian_jin_20240628_models.GetDocumentChunkListResponse:
        """
        @summary 获取文档的chunk列表
        
        @param request: GetDocumentChunkListRequest
        @return: GetDocumentChunkListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_document_chunk_list_with_options_async(workspace_id, request, headers, runtime)

    def get_document_list_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDocumentListResponse:
        """
        @summary 分页查询文档库的文档列表
        
        @param request: GetDocumentListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_id):
            query['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/listDocument',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDocumentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_list_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDocumentListResponse:
        """
        @summary 分页查询文档库的文档列表
        
        @param request: GetDocumentListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_id):
            query['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/listDocument',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDocumentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_list(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentListRequest,
    ) -> dian_jin_20240628_models.GetDocumentListResponse:
        """
        @summary 分页查询文档库的文档列表
        
        @param request: GetDocumentListRequest
        @return: GetDocumentListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_document_list_with_options(workspace_id, request, headers, runtime)

    async def get_document_list_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentListRequest,
    ) -> dian_jin_20240628_models.GetDocumentListResponse:
        """
        @summary 分页查询文档库的文档列表
        
        @param request: GetDocumentListRequest
        @return: GetDocumentListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_document_list_with_options_async(workspace_id, request, headers, runtime)

    def get_document_url_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDocumentUrlResponse:
        """
        @summary 获取文档URL
        
        @param request: GetDocumentUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentUrl',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/url',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDocumentUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_url_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDocumentUrlResponse:
        """
        @summary 获取文档URL
        
        @param request: GetDocumentUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentUrl',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/url',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDocumentUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_url(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentUrlRequest,
    ) -> dian_jin_20240628_models.GetDocumentUrlResponse:
        """
        @summary 获取文档URL
        
        @param request: GetDocumentUrlRequest
        @return: GetDocumentUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_document_url_with_options(workspace_id, request, headers, runtime)

    async def get_document_url_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDocumentUrlRequest,
    ) -> dian_jin_20240628_models.GetDocumentUrlResponse:
        """
        @summary 获取文档URL
        
        @param request: GetDocumentUrlRequest
        @return: GetDocumentUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_document_url_with_options_async(workspace_id, request, headers, runtime)

    def get_filter_document_list_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetFilterDocumentListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetFilterDocumentListResponse:
        """
        @summary 带条件的分页查询文档库的文档列表
        
        @param request: GetFilterDocumentListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFilterDocumentListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.and_):
            body['and'] = request.and_
        if not UtilClient.is_unset(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.or_):
            body['or'] = request.or_
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFilterDocumentList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/filterDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetFilterDocumentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_filter_document_list_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetFilterDocumentListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetFilterDocumentListResponse:
        """
        @summary 带条件的分页查询文档库的文档列表
        
        @param request: GetFilterDocumentListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFilterDocumentListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.and_):
            body['and'] = request.and_
        if not UtilClient.is_unset(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.or_):
            body['or'] = request.or_
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFilterDocumentList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/filterDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetFilterDocumentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_filter_document_list(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetFilterDocumentListRequest,
    ) -> dian_jin_20240628_models.GetFilterDocumentListResponse:
        """
        @summary 带条件的分页查询文档库的文档列表
        
        @param request: GetFilterDocumentListRequest
        @return: GetFilterDocumentListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_filter_document_list_with_options(workspace_id, request, headers, runtime)

    async def get_filter_document_list_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetFilterDocumentListRequest,
    ) -> dian_jin_20240628_models.GetFilterDocumentListResponse:
        """
        @summary 带条件的分页查询文档库的文档列表
        
        @param request: GetFilterDocumentListRequest
        @return: GetFilterDocumentListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_filter_document_list_with_options_async(workspace_id, request, headers, runtime)

    def get_history_list_by_biz_type_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetHistoryListByBizTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetHistoryListByBizTypeResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetHistoryListByBizTypeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoryListByBizTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryListByBizType',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/history/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetHistoryListByBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_history_list_by_biz_type_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetHistoryListByBizTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetHistoryListByBizTypeResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetHistoryListByBizTypeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoryListByBizTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryListByBizType',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/history/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetHistoryListByBizTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_history_list_by_biz_type(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetHistoryListByBizTypeRequest,
    ) -> dian_jin_20240628_models.GetHistoryListByBizTypeResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetHistoryListByBizTypeRequest
        @return: GetHistoryListByBizTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_history_list_by_biz_type_with_options(workspace_id, request, headers, runtime)

    async def get_history_list_by_biz_type_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetHistoryListByBizTypeRequest,
    ) -> dian_jin_20240628_models.GetHistoryListByBizTypeResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetHistoryListByBizTypeRequest
        @return: GetHistoryListByBizTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_history_list_by_biz_type_with_options_async(workspace_id, request, headers, runtime)

    def get_library_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetLibraryResponse:
        """
        @summary 获取文档库配置详情
        
        @param request: GetLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetLibraryResponse:
        """
        @summary 获取文档库配置详情
        
        @param request: GetLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryRequest,
    ) -> dian_jin_20240628_models.GetLibraryResponse:
        """
        @summary 获取文档库配置详情
        
        @param request: GetLibraryRequest
        @return: GetLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_library_with_options(workspace_id, request, headers, runtime)

    async def get_library_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryRequest,
    ) -> dian_jin_20240628_models.GetLibraryResponse:
        """
        @summary 获取文档库配置详情
        
        @param request: GetLibraryRequest
        @return: GetLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_library_with_options_async(workspace_id, request, headers, runtime)

    def get_library_list_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetLibraryListResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetLibraryListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLibraryListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLibraryList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetLibraryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_list_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetLibraryListResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetLibraryListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLibraryListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLibraryList',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetLibraryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library_list(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryListRequest,
    ) -> dian_jin_20240628_models.GetLibraryListResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetLibraryListRequest
        @return: GetLibraryListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_library_list_with_options(workspace_id, request, headers, runtime)

    async def get_library_list_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetLibraryListRequest,
    ) -> dian_jin_20240628_models.GetLibraryListResponse:
        """
        @summary 分页查询文档库列表
        
        @param request: GetLibraryListRequest
        @return: GetLibraryListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_library_list_with_options_async(workspace_id, request, headers, runtime)

    def get_parse_result_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetParseResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetParseResultResponse:
        """
        @summary 获取解析结果
        
        @param request: GetParseResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParseResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetParseResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/getParseResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetParseResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parse_result_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetParseResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetParseResultResponse:
        """
        @summary 获取解析结果
        
        @param request: GetParseResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParseResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetParseResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/getParseResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetParseResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parse_result(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetParseResultRequest,
    ) -> dian_jin_20240628_models.GetParseResultResponse:
        """
        @summary 获取解析结果
        
        @param request: GetParseResultRequest
        @return: GetParseResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_parse_result_with_options(workspace_id, request, headers, runtime)

    async def get_parse_result_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetParseResultRequest,
    ) -> dian_jin_20240628_models.GetParseResultResponse:
        """
        @summary 获取解析结果
        
        @param request: GetParseResultRequest
        @return: GetParseResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_parse_result_with_options_async(workspace_id, request, headers, runtime)

    def get_quality_check_task_result_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetQualityCheckTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetQualityCheckTaskResultResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetQualityCheckTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityCheckTaskResultResponse
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
            action='GetQualityCheckTaskResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/qualitycheck/task/query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetQualityCheckTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_check_task_result_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetQualityCheckTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetQualityCheckTaskResultResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetQualityCheckTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityCheckTaskResultResponse
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
            action='GetQualityCheckTaskResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/qualitycheck/task/query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetQualityCheckTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_check_task_result(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetQualityCheckTaskResultRequest,
    ) -> dian_jin_20240628_models.GetQualityCheckTaskResultResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetQualityCheckTaskResultRequest
        @return: GetQualityCheckTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quality_check_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_quality_check_task_result_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetQualityCheckTaskResultRequest,
    ) -> dian_jin_20240628_models.GetQualityCheckTaskResultResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetQualityCheckTaskResultRequest
        @return: GetQualityCheckTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quality_check_task_result_with_options_async(workspace_id, request, headers, runtime)

    def get_summary_task_result_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetSummaryTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetSummaryTaskResultResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetSummaryTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSummaryTaskResultResponse
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
            action='GetSummaryTaskResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetSummaryTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_task_result_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetSummaryTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetSummaryTaskResultResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetSummaryTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSummaryTaskResultResponse
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
            action='GetSummaryTaskResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/summary/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetSummaryTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_task_result(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetSummaryTaskResultRequest,
    ) -> dian_jin_20240628_models.GetSummaryTaskResultResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetSummaryTaskResultRequest
        @return: GetSummaryTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_summary_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_summary_task_result_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetSummaryTaskResultRequest,
    ) -> dian_jin_20240628_models.GetSummaryTaskResultResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetSummaryTaskResultRequest
        @return: GetSummaryTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_summary_task_result_with_options_async(workspace_id, request, headers, runtime)

    def get_task_result_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetTaskResultResponse:
        """
        @summary 获取异步任务结果
        
        @param request: GetTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResultResponse
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
            action='GetTaskResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_result_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetTaskResultResponse:
        """
        @summary 获取异步任务结果
        
        @param request: GetTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResultResponse
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
            action='GetTaskResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_result(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskResultRequest,
    ) -> dian_jin_20240628_models.GetTaskResultResponse:
        """
        @summary 获取异步任务结果
        
        @param request: GetTaskResultRequest
        @return: GetTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_task_result_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskResultRequest,
    ) -> dian_jin_20240628_models.GetTaskResultResponse:
        """
        @summary 获取异步任务结果
        
        @param request: GetTaskResultRequest
        @return: GetTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_result_with_options_async(workspace_id, request, headers, runtime)

    def get_task_status_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetTaskStatusResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusResponse
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
            action='GetTaskStatus',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetTaskStatusResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusResponse
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
            action='GetTaskStatus',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskStatusRequest,
    ) -> dian_jin_20240628_models.GetTaskStatusResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetTaskStatusRequest
        @return: GetTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_status_with_options(workspace_id, request, headers, runtime)

    async def get_task_status_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetTaskStatusRequest,
    ) -> dian_jin_20240628_models.GetTaskStatusResponse:
        """
        @summary 获取财报总结任务结果
        
        @param request: GetTaskStatusRequest
        @return: GetTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_status_with_options_async(workspace_id, request, headers, runtime)

    def invoke_plugin_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.InvokePluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.InvokePluginResponse:
        """
        @summary 插件调试接口
        
        @param request: InvokePluginRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokePluginResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokePlugin',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/plugin/invoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.InvokePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_plugin_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.InvokePluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.InvokePluginResponse:
        """
        @summary 插件调试接口
        
        @param request: InvokePluginRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokePluginResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokePlugin',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/plugin/invoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.InvokePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_plugin(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.InvokePluginRequest,
    ) -> dian_jin_20240628_models.InvokePluginResponse:
        """
        @summary 插件调试接口
        
        @param request: InvokePluginRequest
        @return: InvokePluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.invoke_plugin_with_options(workspace_id, request, headers, runtime)

    async def invoke_plugin_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.InvokePluginRequest,
    ) -> dian_jin_20240628_models.InvokePluginResponse:
        """
        @summary 插件调试接口
        
        @param request: InvokePluginRequest
        @return: InvokePluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.invoke_plugin_with_options_async(workspace_id, request, headers, runtime)

    def preview_document_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.PreviewDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.PreviewDocumentResponse:
        """
        @summary 获取文档预览
        
        @param request: PreviewDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/preview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.PreviewDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_document_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.PreviewDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.PreviewDocumentResponse:
        """
        @summary 获取文档预览
        
        @param request: PreviewDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/preview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.PreviewDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_document(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.PreviewDocumentRequest,
    ) -> dian_jin_20240628_models.PreviewDocumentResponse:
        """
        @summary 获取文档预览
        
        @param request: PreviewDocumentRequest
        @return: PreviewDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.preview_document_with_options(workspace_id, request, headers, runtime)

    async def preview_document_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.PreviewDocumentRequest,
    ) -> dian_jin_20240628_models.PreviewDocumentResponse:
        """
        @summary 获取文档预览
        
        @param request: PreviewDocumentRequest
        @return: PreviewDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.preview_document_with_options_async(workspace_id, request, headers, runtime)

    def re_index_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.ReIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.ReIndexResponse:
        """
        @summary 重新索引
        
        @param request: ReIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReIndex',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/reIndex',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.ReIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_index_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.ReIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.ReIndexResponse:
        """
        @summary 重新索引
        
        @param request: ReIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReIndex',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/reIndex',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.ReIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_index(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.ReIndexRequest,
    ) -> dian_jin_20240628_models.ReIndexResponse:
        """
        @summary 重新索引
        
        @param request: ReIndexRequest
        @return: ReIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.re_index_with_options(workspace_id, request, headers, runtime)

    async def re_index_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.ReIndexRequest,
    ) -> dian_jin_20240628_models.ReIndexResponse:
        """
        @summary 重新索引
        
        @param request: ReIndexRequest
        @return: ReIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.re_index_with_options_async(workspace_id, request, headers, runtime)

    def recall_document_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecallDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RecallDocumentResponse:
        """
        @summary 文档召回。
        
        @param request: RecallDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecallDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.filters):
            body['filters'] = request.filters
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.rearrangement):
            body['rearrangement'] = request.rearrangement
        if not UtilClient.is_unset(request.top_k):
            body['topK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecallDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/recallDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RecallDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def recall_document_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecallDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RecallDocumentResponse:
        """
        @summary 文档召回。
        
        @param request: RecallDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecallDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.filters):
            body['filters'] = request.filters
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.rearrangement):
            body['rearrangement'] = request.rearrangement
        if not UtilClient.is_unset(request.top_k):
            body['topK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecallDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/recallDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RecallDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recall_document(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecallDocumentRequest,
    ) -> dian_jin_20240628_models.RecallDocumentResponse:
        """
        @summary 文档召回。
        
        @param request: RecallDocumentRequest
        @return: RecallDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recall_document_with_options(workspace_id, request, headers, runtime)

    async def recall_document_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecallDocumentRequest,
    ) -> dian_jin_20240628_models.RecallDocumentResponse:
        """
        @summary 文档召回。
        
        @param request: RecallDocumentRequest
        @return: RecallDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recall_document_with_options_async(workspace_id, request, headers, runtime)

    def recognize_intention_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecognizeIntentionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RecognizeIntentionResponse:
        """
        @summary 意图识别
        
        @param request: RecognizeIntentionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeIntentionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis):
            body['analysis'] = request.analysis
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.conversation):
            body['conversation'] = request.conversation
        if not UtilClient.is_unset(request.global_intention_list):
            body['globalIntentionList'] = request.global_intention_list
        if not UtilClient.is_unset(request.hierarchical_intention_list):
            body['hierarchicalIntentionList'] = request.hierarchical_intention_list
        if not UtilClient.is_unset(request.intention_list):
            body['intentionList'] = request.intention_list
        if not UtilClient.is_unset(request.op_type):
            body['opType'] = request.op_type
        if not UtilClient.is_unset(request.recommend):
            body['recommend'] = request.recommend
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeIntention',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/recog/intent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RecognizeIntentionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_intention_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecognizeIntentionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RecognizeIntentionResponse:
        """
        @summary 意图识别
        
        @param request: RecognizeIntentionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeIntentionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis):
            body['analysis'] = request.analysis
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.conversation):
            body['conversation'] = request.conversation
        if not UtilClient.is_unset(request.global_intention_list):
            body['globalIntentionList'] = request.global_intention_list
        if not UtilClient.is_unset(request.hierarchical_intention_list):
            body['hierarchicalIntentionList'] = request.hierarchical_intention_list
        if not UtilClient.is_unset(request.intention_list):
            body['intentionList'] = request.intention_list
        if not UtilClient.is_unset(request.op_type):
            body['opType'] = request.op_type
        if not UtilClient.is_unset(request.recommend):
            body['recommend'] = request.recommend
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeIntention',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/recog/intent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RecognizeIntentionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_intention(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecognizeIntentionRequest,
    ) -> dian_jin_20240628_models.RecognizeIntentionResponse:
        """
        @summary 意图识别
        
        @param request: RecognizeIntentionRequest
        @return: RecognizeIntentionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recognize_intention_with_options(workspace_id, request, headers, runtime)

    async def recognize_intention_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RecognizeIntentionRequest,
    ) -> dian_jin_20240628_models.RecognizeIntentionResponse:
        """
        @summary 意图识别
        
        @param request: RecognizeIntentionRequest
        @return: RecognizeIntentionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recognize_intention_with_options_async(workspace_id, request, headers, runtime)

    def run_chat_result_generation_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunChatResultGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RunChatResultGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunChatResultGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunChatResultGenerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inference_parameters):
            body['inferenceParameters'] = request.inference_parameters
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.tools):
            body['tools'] = request.tools
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunChatResultGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/run/chat/generation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RunChatResultGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_chat_result_generation_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunChatResultGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RunChatResultGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunChatResultGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunChatResultGenerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inference_parameters):
            body['inferenceParameters'] = request.inference_parameters
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.tools):
            body['tools'] = request.tools
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunChatResultGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/run/chat/generation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RunChatResultGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_chat_result_generation(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunChatResultGenerationRequest,
    ) -> dian_jin_20240628_models.RunChatResultGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunChatResultGenerationRequest
        @return: RunChatResultGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_chat_result_generation_with_options(workspace_id, request, headers, runtime)

    async def run_chat_result_generation_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunChatResultGenerationRequest,
    ) -> dian_jin_20240628_models.RunChatResultGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunChatResultGenerationRequest
        @return: RunChatResultGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_chat_result_generation_with_options_async(workspace_id, request, headers, runtime)

    def run_library_chat_generation_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunLibraryChatGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RunLibraryChatGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunLibraryChatGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunLibraryChatGenerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not UtilClient.is_unset(request.enable_follow_up):
            body['enableFollowUp'] = request.enable_follow_up
        if not UtilClient.is_unset(request.enable_multi_query):
            body['enableMultiQuery'] = request.enable_multi_query
        if not UtilClient.is_unset(request.enable_open_qa):
            body['enableOpenQa'] = request.enable_open_qa
        if not UtilClient.is_unset(request.follow_up_llm):
            body['followUpLlm'] = request.follow_up_llm
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.llm_type):
            body['llmType'] = request.llm_type
        if not UtilClient.is_unset(request.multi_query_llm):
            body['multiQueryLlm'] = request.multi_query_llm
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.query_criteria):
            body['queryCriteria'] = request.query_criteria
        if not UtilClient.is_unset(request.rerank_type):
            body['rerankType'] = request.rerank_type
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.sub_query_list):
            body['subQueryList'] = request.sub_query_list
        if not UtilClient.is_unset(request.text_search_parameter):
            body['textSearchParameter'] = request.text_search_parameter
        if not UtilClient.is_unset(request.top_k):
            body['topK'] = request.top_k
        if not UtilClient.is_unset(request.vector_search_parameter):
            body['vectorSearchParameter'] = request.vector_search_parameter
        if not UtilClient.is_unset(request.with_document_reference):
            body['withDocumentReference'] = request.with_document_reference
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunLibraryChatGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/run/library/chat/generation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RunLibraryChatGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_library_chat_generation_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunLibraryChatGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RunLibraryChatGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunLibraryChatGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunLibraryChatGenerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not UtilClient.is_unset(request.enable_follow_up):
            body['enableFollowUp'] = request.enable_follow_up
        if not UtilClient.is_unset(request.enable_multi_query):
            body['enableMultiQuery'] = request.enable_multi_query
        if not UtilClient.is_unset(request.enable_open_qa):
            body['enableOpenQa'] = request.enable_open_qa
        if not UtilClient.is_unset(request.follow_up_llm):
            body['followUpLlm'] = request.follow_up_llm
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.llm_type):
            body['llmType'] = request.llm_type
        if not UtilClient.is_unset(request.multi_query_llm):
            body['multiQueryLlm'] = request.multi_query_llm
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.query_criteria):
            body['queryCriteria'] = request.query_criteria
        if not UtilClient.is_unset(request.rerank_type):
            body['rerankType'] = request.rerank_type
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.sub_query_list):
            body['subQueryList'] = request.sub_query_list
        if not UtilClient.is_unset(request.text_search_parameter):
            body['textSearchParameter'] = request.text_search_parameter
        if not UtilClient.is_unset(request.top_k):
            body['topK'] = request.top_k
        if not UtilClient.is_unset(request.vector_search_parameter):
            body['vectorSearchParameter'] = request.vector_search_parameter
        if not UtilClient.is_unset(request.with_document_reference):
            body['withDocumentReference'] = request.with_document_reference
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunLibraryChatGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/run/library/chat/generation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RunLibraryChatGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_library_chat_generation(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunLibraryChatGenerationRequest,
    ) -> dian_jin_20240628_models.RunLibraryChatGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunLibraryChatGenerationRequest
        @return: RunLibraryChatGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_library_chat_generation_with_options(workspace_id, request, headers, runtime)

    async def run_library_chat_generation_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunLibraryChatGenerationRequest,
    ) -> dian_jin_20240628_models.RunLibraryChatGenerationResponse:
        """
        @summary 获取生成式对话结果
        
        @param request: RunLibraryChatGenerationRequest
        @return: RunLibraryChatGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_library_chat_generation_with_options_async(workspace_id, request, headers, runtime)

    def update_document_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateDocumentResponse:
        """
        @summary 更新文档
        
        @param request: UpdateDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.meta):
            body['meta'] = request.meta
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/updateDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_document_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateDocumentResponse:
        """
        @summary 更新文档
        
        @param request: UpdateDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.meta):
            body['meta'] = request.meta
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/updateDocument',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_document(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentRequest,
    ) -> dian_jin_20240628_models.UpdateDocumentResponse:
        """
        @summary 更新文档
        
        @param request: UpdateDocumentRequest
        @return: UpdateDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_document_with_options(workspace_id, request, headers, runtime)

    async def update_document_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentRequest,
    ) -> dian_jin_20240628_models.UpdateDocumentResponse:
        """
        @summary 更新文档
        
        @param request: UpdateDocumentRequest
        @return: UpdateDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_document_with_options_async(workspace_id, request, headers, runtime)

    def update_library_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateLibraryResponse:
        """
        @summary 更新文档库配置
        
        @param request: UpdateLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLibraryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_library_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateLibraryResponse:
        """
        @summary 更新文档库配置
        
        @param request: UpdateLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLibraryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_library(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateLibraryRequest,
    ) -> dian_jin_20240628_models.UpdateLibraryResponse:
        """
        @summary 更新文档库配置
        
        @param request: UpdateLibraryRequest
        @return: UpdateLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_library_with_options(workspace_id, request, headers, runtime)

    async def update_library_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateLibraryRequest,
    ) -> dian_jin_20240628_models.UpdateLibraryResponse:
        """
        @summary 更新文档库配置
        
        @param request: UpdateLibraryRequest
        @return: UpdateLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_library_with_options_async(workspace_id, request, headers, runtime)

    def upload_document_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UploadDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UploadDocumentResponse:
        """
        @summary 上传文档到文档库
        
        @param request: UploadDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            body['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UploadDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_document_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UploadDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UploadDocumentResponse:
        """
        @summary 上传文档到文档库
        
        @param request: UploadDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            body['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDocument',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/document/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UploadDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_document(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UploadDocumentRequest,
    ) -> dian_jin_20240628_models.UploadDocumentResponse:
        """
        @summary 上传文档到文档库
        
        @param request: UploadDocumentRequest
        @return: UploadDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_document_with_options(workspace_id, request, headers, runtime)

    async def upload_document_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UploadDocumentRequest,
    ) -> dian_jin_20240628_models.UploadDocumentResponse:
        """
        @summary 上传文档到文档库
        
        @param request: UploadDocumentRequest
        @return: UploadDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_document_with_options_async(workspace_id, request, headers, runtime)

    def upload_document_advance(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UploadDocumentAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UploadDocumentResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='DianJin',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upload_document_req = dian_jin_20240628_models.UploadDocumentRequest()
        OpenApiUtilClient.convert(request, upload_document_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            upload_document_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        upload_document_resp = self.upload_document_with_options(workspace_id, upload_document_req, headers, runtime)
        return upload_document_resp

    async def upload_document_advance_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UploadDocumentAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UploadDocumentResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='DianJin',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upload_document_req = dian_jin_20240628_models.UploadDocumentRequest()
        OpenApiUtilClient.convert(request, upload_document_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            upload_document_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        upload_document_resp = await self.upload_document_with_options_async(workspace_id, upload_document_req, headers, runtime)
        return upload_document_resp
