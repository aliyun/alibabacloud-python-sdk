# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.request import TeaRequest
from Tea.exceptions import TeaException
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_fileform.client import Client as FileFormClient
from alibabacloud_tea_xml.client import Client as XMLClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dianjin20240628 import models as dian_jin_20240628_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_fileform import models as file_form_models


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

    def _post_ossobject(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
        _request = TeaRequest()
        form = UtilClient.assert_as_map(data)
        boundary = FileFormClient.get_boundary()
        host = UtilClient.assert_as_string(form.get('host'))
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': host,
            'date': UtilClient.get_date_utcstring(),
            'user-agent': UtilClient.get_user_agent('')
        }
        _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
        _request.body = FileFormClient.to_file_form(form, boundary)
        _last_request = _request
        _response = TeaCore.do_action(_request)
        resp_map = None
        body_str = UtilClient.read_as_string(_response.body)
        if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
            resp_map = XMLClient.parse_xml(body_str, None)
            err = UtilClient.assert_as_map(resp_map.get('Error'))
            raise TeaException({
                'code': err.get('Code'),
                'message': err.get('Message'),
                'data': {
                    'httpCode': _response.status_code,
                    'requestId': err.get('RequestId'),
                    'hostId': err.get('HostId')
                }
            })
        resp_map = XMLClient.parse_xml(body_str, None)
        return TeaCore.merge(resp_map)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
        _request = TeaRequest()
        form = UtilClient.assert_as_map(data)
        boundary = FileFormClient.get_boundary()
        host = UtilClient.assert_as_string(form.get('host'))
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': host,
            'date': UtilClient.get_date_utcstring(),
            'user-agent': UtilClient.get_user_agent('')
        }
        _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
        _request.body = FileFormClient.to_file_form(form, boundary)
        _last_request = _request
        _response = await TeaCore.async_do_action(_request)
        resp_map = None
        body_str = await UtilClient.read_as_string_async(_response.body)
        if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
            resp_map = XMLClient.parse_xml(body_str, None)
            err = UtilClient.assert_as_map(resp_map.get('Error'))
            raise TeaException({
                'code': err.get('Code'),
                'message': err.get('Message'),
                'data': {
                    'httpCode': _response.status_code,
                    'requestId': err.get('RequestId'),
                    'hostId': err.get('HostId')
                }
            })
        resp_map = XMLClient.parse_xml(body_str, None)
        return TeaCore.merge(resp_map)

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

    def create_dialog_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateDialogResponse:
        """
        @summary 创建外呼会话
        
        @param request: CreateDialogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDialogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.enable_library):
            body['enableLibrary'] = request.enable_library
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.play_code):
            body['playCode'] = request.play_code
        if not UtilClient.is_unset(request.qa_library_list):
            body['qaLibraryList'] = request.qa_library_list
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.self_directed):
            body['selfDirected'] = request.self_directed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDialog',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialog_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateDialogResponse:
        """
        @summary 创建外呼会话
        
        @param request: CreateDialogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDialogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.enable_library):
            body['enableLibrary'] = request.enable_library
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.play_code):
            body['playCode'] = request.play_code
        if not UtilClient.is_unset(request.qa_library_list):
            body['qaLibraryList'] = request.qa_library_list
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.self_directed):
            body['selfDirected'] = request.self_directed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDialog',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialog(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogRequest,
    ) -> dian_jin_20240628_models.CreateDialogResponse:
        """
        @summary 创建外呼会话
        
        @param request: CreateDialogRequest
        @return: CreateDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dialog_with_options(workspace_id, request, headers, runtime)

    async def create_dialog_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogRequest,
    ) -> dian_jin_20240628_models.CreateDialogResponse:
        """
        @summary 创建外呼会话
        
        @param request: CreateDialogRequest
        @return: CreateDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dialog_with_options_async(workspace_id, request, headers, runtime)

    def create_dialog_analysis_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateDialogAnalysisTaskResponse:
        """
        @summary 创建会话分析任务
        
        @param request: CreateDialogAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDialogAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis_nodes):
            body['analysisNodes'] = request.analysis_nodes
        if not UtilClient.is_unset(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.play_code):
            body['playCode'] = request.play_code
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDialogAnalysisTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/analysis/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateDialogAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialog_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.CreateDialogAnalysisTaskResponse:
        """
        @summary 创建会话分析任务
        
        @param request: CreateDialogAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDialogAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis_nodes):
            body['analysisNodes'] = request.analysis_nodes
        if not UtilClient.is_unset(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.play_code):
            body['playCode'] = request.play_code
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDialogAnalysisTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/analysis/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.CreateDialogAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialog_analysis_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogAnalysisTaskRequest,
    ) -> dian_jin_20240628_models.CreateDialogAnalysisTaskResponse:
        """
        @summary 创建会话分析任务
        
        @param request: CreateDialogAnalysisTaskRequest
        @return: CreateDialogAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dialog_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def create_dialog_analysis_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.CreateDialogAnalysisTaskRequest,
    ) -> dian_jin_20240628_models.CreateDialogAnalysisTaskResponse:
        """
        @summary 创建会话分析任务
        
        @param request: CreateDialogAnalysisTaskRequest
        @return: CreateDialogAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dialog_analysis_task_with_options_async(workspace_id, request, headers, runtime)

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

    def gen_doc_qa_result_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GenDocQaResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GenDocQaResultResponse:
        """
        @summary 根据文档解析问答QA
        
        @param request: GenDocQaResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenDocQaResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenDocQaResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/qa/parse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GenDocQaResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def gen_doc_qa_result_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GenDocQaResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GenDocQaResultResponse:
        """
        @summary 根据文档解析问答QA
        
        @param request: GenDocQaResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenDocQaResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['docId'] = request.doc_id
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenDocQaResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/qa/parse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GenDocQaResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gen_doc_qa_result(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GenDocQaResultRequest,
    ) -> dian_jin_20240628_models.GenDocQaResultResponse:
        """
        @summary 根据文档解析问答QA
        
        @param request: GenDocQaResultRequest
        @return: GenDocQaResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.gen_doc_qa_result_with_options(workspace_id, request, headers, runtime)

    async def gen_doc_qa_result_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GenDocQaResultRequest,
    ) -> dian_jin_20240628_models.GenDocQaResultResponse:
        """
        @summary 根据文档解析问答QA
        
        @param request: GenDocQaResultRequest
        @return: GenDocQaResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.gen_doc_qa_result_with_options_async(workspace_id, request, headers, runtime)

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

    def get_chat_question_resp_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetChatQuestionRespRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetChatQuestionRespResponse:
        """
        @summary 获取问答结果
        
        @param request: GetChatQuestionRespRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatQuestionRespResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['batchId'] = request.batch_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetChatQuestionResp',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/chat/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetChatQuestionRespResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_question_resp_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetChatQuestionRespRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetChatQuestionRespResponse:
        """
        @summary 获取问答结果
        
        @param request: GetChatQuestionRespRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatQuestionRespResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['batchId'] = request.batch_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetChatQuestionResp',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/chat/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetChatQuestionRespResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_question_resp(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetChatQuestionRespRequest,
    ) -> dian_jin_20240628_models.GetChatQuestionRespResponse:
        """
        @summary 获取问答结果
        
        @param request: GetChatQuestionRespRequest
        @return: GetChatQuestionRespResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_chat_question_resp_with_options(workspace_id, request, headers, runtime)

    async def get_chat_question_resp_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetChatQuestionRespRequest,
    ) -> dian_jin_20240628_models.GetChatQuestionRespResponse:
        """
        @summary 获取问答结果
        
        @param request: GetChatQuestionRespRequest
        @return: GetChatQuestionRespResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_chat_question_resp_with_options_async(workspace_id, request, headers, runtime)

    def get_dialog_analysis_result_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogAnalysisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDialogAnalysisResultResponse:
        """
        @summary 获取外呼会话分析结果
        
        @param request: GetDialogAnalysisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDialogAnalysisResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asc):
            body['asc'] = request.asc
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.session_ids):
            body['sessionIds'] = request.session_ids
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.use_url):
            body['useUrl'] = request.use_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDialogAnalysisResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDialogAnalysisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dialog_analysis_result_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogAnalysisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDialogAnalysisResultResponse:
        """
        @summary 获取外呼会话分析结果
        
        @param request: GetDialogAnalysisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDialogAnalysisResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asc):
            body['asc'] = request.asc
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.session_ids):
            body['sessionIds'] = request.session_ids
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.use_url):
            body['useUrl'] = request.use_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDialogAnalysisResult',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDialogAnalysisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dialog_analysis_result(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogAnalysisResultRequest,
    ) -> dian_jin_20240628_models.GetDialogAnalysisResultResponse:
        """
        @summary 获取外呼会话分析结果
        
        @param request: GetDialogAnalysisResultRequest
        @return: GetDialogAnalysisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dialog_analysis_result_with_options(workspace_id, request, headers, runtime)

    async def get_dialog_analysis_result_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogAnalysisResultRequest,
    ) -> dian_jin_20240628_models.GetDialogAnalysisResultResponse:
        """
        @summary 获取外呼会话分析结果
        
        @param request: GetDialogAnalysisResultRequest
        @return: GetDialogAnalysisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dialog_analysis_result_with_options_async(workspace_id, request, headers, runtime)

    def get_dialog_detail_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDialogDetailResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetDialogDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDialogDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDialogDetail',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDialogDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dialog_detail_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDialogDetailResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetDialogDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDialogDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDialogDetail',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/dialog/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDialogDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dialog_detail(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogDetailRequest,
    ) -> dian_jin_20240628_models.GetDialogDetailResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetDialogDetailRequest
        @return: GetDialogDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dialog_detail_with_options(workspace_id, request, headers, runtime)

    async def get_dialog_detail_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogDetailRequest,
    ) -> dian_jin_20240628_models.GetDialogDetailResponse:
        """
        @summary 获取异步任务的结果
        
        @param request: GetDialogDetailRequest
        @return: GetDialogDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dialog_detail_with_options_async(workspace_id, request, headers, runtime)

    def get_dialog_log_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDialogLogResponse:
        """
        @summary 查询会话日志
        
        @param request: GetDialogLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDialogLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDialogLog',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/dialog/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDialogLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dialog_log_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.GetDialogLogResponse:
        """
        @summary 查询会话日志
        
        @param request: GetDialogLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDialogLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDialogLog',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/dialog/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.GetDialogLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dialog_log(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogLogRequest,
    ) -> dian_jin_20240628_models.GetDialogLogResponse:
        """
        @summary 查询会话日志
        
        @param request: GetDialogLogRequest
        @return: GetDialogLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dialog_log_with_options(workspace_id, request, headers, runtime)

    async def get_dialog_log_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.GetDialogLogRequest,
    ) -> dian_jin_20240628_models.GetDialogLogResponse:
        """
        @summary 查询会话日志
        
        @param request: GetDialogLogRequest
        @return: GetDialogLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dialog_log_with_options_async(workspace_id, request, headers, runtime)

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
        if not UtilClient.is_unset(request.use_url_result):
            body['useUrlResult'] = request.use_url_result
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
        if not UtilClient.is_unset(request.use_url_result):
            body['useUrlResult'] = request.use_url_result
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

    def real_time_dialog_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RealTimeDialogResponse:
        """
        @summary 实时对话
        
        @param request: RealTimeDialogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RealTimeDialogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis):
            body['analysis'] = request.analysis
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not UtilClient.is_unset(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.op_type):
            body['opType'] = request.op_type
        if not UtilClient.is_unset(request.recommend):
            body['recommend'] = request.recommend
        if not UtilClient.is_unset(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RealTimeDialog',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/realtime/dialog/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RealTimeDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def real_time_dialog_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RealTimeDialogResponse:
        """
        @summary 实时对话
        
        @param request: RealTimeDialogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RealTimeDialogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis):
            body['analysis'] = request.analysis
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not UtilClient.is_unset(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.op_type):
            body['opType'] = request.op_type
        if not UtilClient.is_unset(request.recommend):
            body['recommend'] = request.recommend
        if not UtilClient.is_unset(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RealTimeDialog',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/realtime/dialog/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RealTimeDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def real_time_dialog(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealTimeDialogRequest,
    ) -> dian_jin_20240628_models.RealTimeDialogResponse:
        """
        @summary 实时对话
        
        @param request: RealTimeDialogRequest
        @return: RealTimeDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.real_time_dialog_with_options(workspace_id, request, headers, runtime)

    async def real_time_dialog_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealTimeDialogRequest,
    ) -> dian_jin_20240628_models.RealTimeDialogResponse:
        """
        @summary 实时对话
        
        @param request: RealTimeDialogRequest
        @return: RealTimeDialogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.real_time_dialog_with_options_async(workspace_id, request, headers, runtime)

    def realtime_dialog_assist_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealtimeDialogAssistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RealtimeDialogAssistResponse:
        """
        @summary 实时会话辅助
        
        @param request: RealtimeDialogAssistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RealtimeDialogAssistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis):
            body['analysis'] = request.analysis
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not UtilClient.is_unset(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not UtilClient.is_unset(request.hang_up_dialog):
            body['hangUpDialog'] = request.hang_up_dialog
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RealtimeDialogAssist',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/realtime/dialog/assist',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RealtimeDialogAssistResponse(),
            self.call_api(params, req, runtime)
        )

    async def realtime_dialog_assist_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealtimeDialogAssistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RealtimeDialogAssistResponse:
        """
        @summary 实时会话辅助
        
        @param request: RealtimeDialogAssistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RealtimeDialogAssistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis):
            body['analysis'] = request.analysis
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not UtilClient.is_unset(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not UtilClient.is_unset(request.hang_up_dialog):
            body['hangUpDialog'] = request.hang_up_dialog
        if not UtilClient.is_unset(request.meta_data):
            body['metaData'] = request.meta_data
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RealtimeDialogAssist',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/realtime/dialog/assist',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RealtimeDialogAssistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def realtime_dialog_assist(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealtimeDialogAssistRequest,
    ) -> dian_jin_20240628_models.RealtimeDialogAssistResponse:
        """
        @summary 实时会话辅助
        
        @param request: RealtimeDialogAssistRequest
        @return: RealtimeDialogAssistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.realtime_dialog_assist_with_options(workspace_id, request, headers, runtime)

    async def realtime_dialog_assist_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RealtimeDialogAssistRequest,
    ) -> dian_jin_20240628_models.RealtimeDialogAssistResponse:
        """
        @summary 实时会话辅助
        
        @param request: RealtimeDialogAssistRequest
        @return: RealtimeDialogAssistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.realtime_dialog_assist_with_options_async(workspace_id, request, headers, runtime)

    def rebuild_task_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RebuildTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RebuildTaskResponse:
        """
        @summary 重建任务
        
        @param request: RebuildTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebuildTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebuildTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/rebuild',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RebuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebuild_task_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RebuildTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RebuildTaskResponse:
        """
        @summary 重建任务
        
        @param request: RebuildTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebuildTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebuildTask',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/task/rebuild',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RebuildTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebuild_task(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RebuildTaskRequest,
    ) -> dian_jin_20240628_models.RebuildTaskResponse:
        """
        @summary 重建任务
        
        @param request: RebuildTaskRequest
        @return: RebuildTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rebuild_task_with_options(workspace_id, request, headers, runtime)

    async def rebuild_task_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RebuildTaskRequest,
    ) -> dian_jin_20240628_models.RebuildTaskResponse:
        """
        @summary 重建任务
        
        @param request: RebuildTaskRequest
        @return: RebuildTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rebuild_task_with_options_async(workspace_id, request, headers, runtime)

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
        if not UtilClient.is_unset(request.intention_domain_code):
            body['intentionDomainCode'] = request.intention_domain_code
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
        if not UtilClient.is_unset(request.intention_domain_code):
            body['intentionDomainCode'] = request.intention_domain_code
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

    def run_agent_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RunAgentResponse:
        """
        @summary 运行智能体
        
        @param request: RunAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bot_id):
            body['botId'] = request.bot_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.thread_id):
            body['threadId'] = request.thread_id
        if not UtilClient.is_unset(request.use_draft):
            body['useDraft'] = request.use_draft
        if not UtilClient.is_unset(request.user_content):
            body['userContent'] = request.user_content
        if not UtilClient.is_unset(request.user_inputs):
            body['userInputs'] = request.user_inputs
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAgent',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/bot/thread/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RunAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_agent_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.RunAgentResponse:
        """
        @summary 运行智能体
        
        @param request: RunAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bot_id):
            body['botId'] = request.bot_id
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.thread_id):
            body['threadId'] = request.thread_id
        if not UtilClient.is_unset(request.use_draft):
            body['useDraft'] = request.use_draft
        if not UtilClient.is_unset(request.user_content):
            body['userContent'] = request.user_content
        if not UtilClient.is_unset(request.user_inputs):
            body['userInputs'] = request.user_inputs
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAgent',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/bot/thread/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.RunAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_agent(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunAgentRequest,
    ) -> dian_jin_20240628_models.RunAgentResponse:
        """
        @summary 运行智能体
        
        @param request: RunAgentRequest
        @return: RunAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_agent_with_options(workspace_id, request, headers, runtime)

    async def run_agent_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.RunAgentRequest,
    ) -> dian_jin_20240628_models.RunAgentResponse:
        """
        @summary 运行智能体
        
        @param request: RunAgentRequest
        @return: RunAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_agent_with_options_async(workspace_id, request, headers, runtime)

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

    def submit_chat_question_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.SubmitChatQuestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.SubmitChatQuestionResponse:
        """
        @summary 提交问题列表
        
        @param request: SubmitChatQuestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitChatQuestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not UtilClient.is_unset(request.live_script_content):
            body['liveScriptContent'] = request.live_script_content
        if not UtilClient.is_unset(request.open_small_talk):
            body['openSmallTalk'] = request.open_small_talk
        if not UtilClient.is_unset(request.question_list):
            body['questionList'] = request.question_list
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitChatQuestion',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/chat/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.SubmitChatQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_chat_question_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.SubmitChatQuestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.SubmitChatQuestionResponse:
        """
        @summary 提交问题列表
        
        @param request: SubmitChatQuestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitChatQuestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not UtilClient.is_unset(request.live_script_content):
            body['liveScriptContent'] = request.live_script_content
        if not UtilClient.is_unset(request.open_small_talk):
            body['openSmallTalk'] = request.open_small_talk
        if not UtilClient.is_unset(request.question_list):
            body['questionList'] = request.question_list
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitChatQuestion',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/chat/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.SubmitChatQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_chat_question(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.SubmitChatQuestionRequest,
    ) -> dian_jin_20240628_models.SubmitChatQuestionResponse:
        """
        @summary 提交问题列表
        
        @param request: SubmitChatQuestionRequest
        @return: SubmitChatQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_chat_question_with_options(workspace_id, request, headers, runtime)

    async def submit_chat_question_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.SubmitChatQuestionRequest,
    ) -> dian_jin_20240628_models.SubmitChatQuestionResponse:
        """
        @summary 提交问题列表
        
        @param request: SubmitChatQuestionRequest
        @return: SubmitChatQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_chat_question_with_options_async(workspace_id, request, headers, runtime)

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

    def update_document_chunk_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentChunkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateDocumentChunkResponse:
        """
        @summary 更新文档的chunk
        
        @param request: UpdateDocumentChunkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDocumentChunkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chunks):
            body['chunks'] = request.chunks
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDocumentChunk',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/updateDocumentChunk',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateDocumentChunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_document_chunk_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentChunkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateDocumentChunkResponse:
        """
        @summary 更新文档的chunk
        
        @param request: UpdateDocumentChunkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDocumentChunkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chunks):
            body['chunks'] = request.chunks
        if not UtilClient.is_unset(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDocumentChunk',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/library/updateDocumentChunk',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateDocumentChunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_document_chunk(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentChunkRequest,
    ) -> dian_jin_20240628_models.UpdateDocumentChunkResponse:
        """
        @summary 更新文档的chunk
        
        @param request: UpdateDocumentChunkRequest
        @return: UpdateDocumentChunkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_document_chunk_with_options(workspace_id, request, headers, runtime)

    async def update_document_chunk_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateDocumentChunkRequest,
    ) -> dian_jin_20240628_models.UpdateDocumentChunkResponse:
        """
        @summary 更新文档的chunk
        
        @param request: UpdateDocumentChunkRequest
        @return: UpdateDocumentChunkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_document_chunk_with_options_async(workspace_id, request, headers, runtime)

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

    def update_qa_library_with_options(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateQaLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateQaLibraryResponse:
        """
        @summary 更新QA问答库
        
        @param request: UpdateQaLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQaLibraryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parse_qa_results):
            body['parseQaResults'] = request.parse_qa_results
        if not UtilClient.is_unset(request.qa_library_id):
            body['qaLibraryId'] = request.qa_library_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQaLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/qa/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateQaLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_qa_library_with_options_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateQaLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dian_jin_20240628_models.UpdateQaLibraryResponse:
        """
        @summary 更新QA问答库
        
        @param request: UpdateQaLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQaLibraryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parse_qa_results):
            body['parseQaResults'] = request.parse_qa_results
        if not UtilClient.is_unset(request.qa_library_id):
            body['qaLibraryId'] = request.qa_library_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQaLibrary',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/api/virtualHuman/qa/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dian_jin_20240628_models.UpdateQaLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_qa_library(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateQaLibraryRequest,
    ) -> dian_jin_20240628_models.UpdateQaLibraryResponse:
        """
        @summary 更新QA问答库
        
        @param request: UpdateQaLibraryRequest
        @return: UpdateQaLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_qa_library_with_options(workspace_id, request, headers, runtime)

    async def update_qa_library_async(
        self,
        workspace_id: str,
        request: dian_jin_20240628_models.UpdateQaLibraryRequest,
    ) -> dian_jin_20240628_models.UpdateQaLibraryResponse:
        """
        @summary 更新QA问答库
        
        @param request: UpdateQaLibraryRequest
        @return: UpdateQaLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_qa_library_with_options_async(workspace_id, request, headers, runtime)

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
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'DianJin',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        upload_document_req = dian_jin_20240628_models.UploadDocumentRequest()
        OpenApiUtilClient.convert(request, upload_document_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            upload_document_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
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
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'DianJin',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        upload_document_req = dian_jin_20240628_models.UploadDocumentRequest()
        OpenApiUtilClient.convert(request, upload_document_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            upload_document_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_document_resp = await self.upload_document_with_options_async(workspace_id, upload_document_req, headers, runtime)
        return upload_document_resp
