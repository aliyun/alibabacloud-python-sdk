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
from alibabacloud_docmind_api20220711 import models as docmind_api_20220711_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'docmind-api.aliyuncs.com',
            'ap-northeast-2-pop': 'docmind-api.aliyuncs.com',
            'ap-south-1': 'docmind-api.aliyuncs.com',
            'ap-southeast-1': 'docmind-api.aliyuncs.com',
            'ap-southeast-2': 'docmind-api.aliyuncs.com',
            'ap-southeast-3': 'docmind-api.aliyuncs.com',
            'ap-southeast-5': 'docmind-api.aliyuncs.com',
            'cn-beijing': 'docmind-api.aliyuncs.com',
            'cn-beijing-finance-1': 'docmind-api.aliyuncs.com',
            'cn-beijing-finance-pop': 'docmind-api.aliyuncs.com',
            'cn-beijing-gov-1': 'docmind-api.aliyuncs.com',
            'cn-beijing-nu16-b01': 'docmind-api.aliyuncs.com',
            'cn-chengdu': 'docmind-api.aliyuncs.com',
            'cn-edge-1': 'docmind-api.aliyuncs.com',
            'cn-fujian': 'docmind-api.aliyuncs.com',
            'cn-haidian-cm12-c01': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-finance': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-test-306': 'docmind-api.aliyuncs.com',
            'cn-hongkong': 'docmind-api.aliyuncs.com',
            'cn-hongkong-finance-pop': 'docmind-api.aliyuncs.com',
            'cn-huhehaote': 'docmind-api.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'docmind-api.aliyuncs.com',
            'cn-north-2-gov-1': 'docmind-api.aliyuncs.com',
            'cn-qingdao': 'docmind-api.aliyuncs.com',
            'cn-qingdao-nebula': 'docmind-api.aliyuncs.com',
            'cn-shanghai': 'docmind-api.aliyuncs.com',
            'cn-shanghai-et15-b01': 'docmind-api.aliyuncs.com',
            'cn-shanghai-et2-b01': 'docmind-api.aliyuncs.com',
            'cn-shanghai-finance-1': 'docmind-api.aliyuncs.com',
            'cn-shanghai-inner': 'docmind-api.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'docmind-api.aliyuncs.com',
            'cn-shenzhen': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-finance-1': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-inner': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'docmind-api.aliyuncs.com',
            'cn-wuhan': 'docmind-api.aliyuncs.com',
            'cn-wulanchabu': 'docmind-api.aliyuncs.com',
            'cn-yushanfang': 'docmind-api.aliyuncs.com',
            'cn-zhangbei': 'docmind-api.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'docmind-api.aliyuncs.com',
            'cn-zhangjiakou': 'docmind-api.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'docmind-api.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'docmind-api.aliyuncs.com',
            'eu-central-1': 'docmind-api.aliyuncs.com',
            'eu-west-1': 'docmind-api.aliyuncs.com',
            'eu-west-1-oxs': 'docmind-api.aliyuncs.com',
            'me-east-1': 'docmind-api.aliyuncs.com',
            'rus-west-1-pop': 'docmind-api.aliyuncs.com',
            'us-east-1': 'docmind-api.aliyuncs.com',
            'us-west-1': 'docmind-api.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('docmind-api', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def aync_trade_document_package_extract_smart_app_with_options(
        self,
        tmp_req: docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        """
        @summary 整票识别
        
        @param tmp_req: AyncTradeDocumentPackageExtractSmartAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AyncTradeDocumentPackageExtractSmartAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_extraction_range):
            request.custom_extraction_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_extraction_range, 'CustomExtractionRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_extraction_range_shrink):
            query['CustomExtractionRange'] = request.custom_extraction_range_shrink
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AyncTradeDocumentPackageExtractSmartApp',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def aync_trade_document_package_extract_smart_app_with_options_async(
        self,
        tmp_req: docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        """
        @summary 整票识别
        
        @param tmp_req: AyncTradeDocumentPackageExtractSmartAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AyncTradeDocumentPackageExtractSmartAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_extraction_range):
            request.custom_extraction_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_extraction_range, 'CustomExtractionRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_extraction_range_shrink):
            query['CustomExtractionRange'] = request.custom_extraction_range_shrink
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AyncTradeDocumentPackageExtractSmartApp',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aync_trade_document_package_extract_smart_app(
        self,
        request: docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppRequest,
    ) -> docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        """
        @summary 整票识别
        
        @param request: AyncTradeDocumentPackageExtractSmartAppRequest
        @return: AyncTradeDocumentPackageExtractSmartAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.aync_trade_document_package_extract_smart_app_with_options(request, runtime)

    async def aync_trade_document_package_extract_smart_app_async(
        self,
        request: docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppRequest,
    ) -> docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        """
        @summary 整票识别
        
        @param request: AyncTradeDocumentPackageExtractSmartAppRequest
        @return: AyncTradeDocumentPackageExtractSmartAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.aync_trade_document_package_extract_smart_app_with_options_async(request, runtime)

    def get_doc_parser_result_with_options(
        self,
        request: docmind_api_20220711_models.GetDocParserResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocParserResultResponse:
        """
        @summary 文档结构化流式接口
        
        @param request: GetDocParserResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocParserResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.layout_num):
            query['LayoutNum'] = request.layout_num
        if not UtilClient.is_unset(request.layout_step_size):
            query['LayoutStepSize'] = request.layout_step_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocParserResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocParserResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_parser_result_with_options_async(
        self,
        request: docmind_api_20220711_models.GetDocParserResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocParserResultResponse:
        """
        @summary 文档结构化流式接口
        
        @param request: GetDocParserResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocParserResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.layout_num):
            query['LayoutNum'] = request.layout_num
        if not UtilClient.is_unset(request.layout_step_size):
            query['LayoutStepSize'] = request.layout_step_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocParserResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocParserResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_parser_result(
        self,
        request: docmind_api_20220711_models.GetDocParserResultRequest,
    ) -> docmind_api_20220711_models.GetDocParserResultResponse:
        """
        @summary 文档结构化流式接口
        
        @param request: GetDocParserResultRequest
        @return: GetDocParserResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doc_parser_result_with_options(request, runtime)

    async def get_doc_parser_result_async(
        self,
        request: docmind_api_20220711_models.GetDocParserResultRequest,
    ) -> docmind_api_20220711_models.GetDocParserResultResponse:
        """
        @summary 文档结构化流式接口
        
        @param request: GetDocParserResultRequest
        @return: GetDocParserResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doc_parser_result_with_options_async(request, runtime)

    def get_doc_structure_result_with_options(
        self,
        request: docmind_api_20220711_models.GetDocStructureResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocStructureResultResponse:
        """
        @summary 文档智能解析结果查询
        
        @param request: GetDocStructureResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocStructureResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not UtilClient.is_unset(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not UtilClient.is_unset(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocStructureResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocStructureResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_structure_result_with_options_async(
        self,
        request: docmind_api_20220711_models.GetDocStructureResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocStructureResultResponse:
        """
        @summary 文档智能解析结果查询
        
        @param request: GetDocStructureResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocStructureResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not UtilClient.is_unset(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not UtilClient.is_unset(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocStructureResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocStructureResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_structure_result(
        self,
        request: docmind_api_20220711_models.GetDocStructureResultRequest,
    ) -> docmind_api_20220711_models.GetDocStructureResultResponse:
        """
        @summary 文档智能解析结果查询
        
        @param request: GetDocStructureResultRequest
        @return: GetDocStructureResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doc_structure_result_with_options(request, runtime)

    async def get_doc_structure_result_async(
        self,
        request: docmind_api_20220711_models.GetDocStructureResultRequest,
    ) -> docmind_api_20220711_models.GetDocStructureResultResponse:
        """
        @summary 文档智能解析结果查询
        
        @param request: GetDocStructureResultRequest
        @return: GetDocStructureResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doc_structure_result_with_options_async(request, runtime)

    def get_document_compare_result_with_options(
        self,
        request: docmind_api_20220711_models.GetDocumentCompareResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocumentCompareResultResponse:
        """
        @summary 文档对比结果查询
        
        @param request: GetDocumentCompareResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentCompareResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentCompareResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentCompareResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_compare_result_with_options_async(
        self,
        request: docmind_api_20220711_models.GetDocumentCompareResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocumentCompareResultResponse:
        """
        @summary 文档对比结果查询
        
        @param request: GetDocumentCompareResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentCompareResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentCompareResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentCompareResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_compare_result(
        self,
        request: docmind_api_20220711_models.GetDocumentCompareResultRequest,
    ) -> docmind_api_20220711_models.GetDocumentCompareResultResponse:
        """
        @summary 文档对比结果查询
        
        @param request: GetDocumentCompareResultRequest
        @return: GetDocumentCompareResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_document_compare_result_with_options(request, runtime)

    async def get_document_compare_result_async(
        self,
        request: docmind_api_20220711_models.GetDocumentCompareResultRequest,
    ) -> docmind_api_20220711_models.GetDocumentCompareResultResponse:
        """
        @summary 文档对比结果查询
        
        @param request: GetDocumentCompareResultRequest
        @return: GetDocumentCompareResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_document_compare_result_with_options_async(request, runtime)

    def get_document_convert_result_with_options(
        self,
        request: docmind_api_20220711_models.GetDocumentConvertResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocumentConvertResultResponse:
        """
        @summary 文档转换结果查询
        
        @param request: GetDocumentConvertResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentConvertResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentConvertResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentConvertResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_convert_result_with_options_async(
        self,
        request: docmind_api_20220711_models.GetDocumentConvertResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocumentConvertResultResponse:
        """
        @summary 文档转换结果查询
        
        @param request: GetDocumentConvertResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentConvertResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentConvertResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentConvertResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_convert_result(
        self,
        request: docmind_api_20220711_models.GetDocumentConvertResultRequest,
    ) -> docmind_api_20220711_models.GetDocumentConvertResultResponse:
        """
        @summary 文档转换结果查询
        
        @param request: GetDocumentConvertResultRequest
        @return: GetDocumentConvertResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_document_convert_result_with_options(request, runtime)

    async def get_document_convert_result_async(
        self,
        request: docmind_api_20220711_models.GetDocumentConvertResultRequest,
    ) -> docmind_api_20220711_models.GetDocumentConvertResultResponse:
        """
        @summary 文档转换结果查询
        
        @param request: GetDocumentConvertResultRequest
        @return: GetDocumentConvertResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_document_convert_result_with_options_async(request, runtime)

    def get_document_extract_result_with_options(
        self,
        request: docmind_api_20220711_models.GetDocumentExtractResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocumentExtractResultResponse:
        """
        @summary 文档抽取结果查询
        
        @param request: GetDocumentExtractResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentExtractResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentExtractResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentExtractResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_extract_result_with_options_async(
        self,
        request: docmind_api_20220711_models.GetDocumentExtractResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetDocumentExtractResultResponse:
        """
        @summary 文档抽取结果查询
        
        @param request: GetDocumentExtractResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentExtractResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentExtractResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentExtractResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_extract_result(
        self,
        request: docmind_api_20220711_models.GetDocumentExtractResultRequest,
    ) -> docmind_api_20220711_models.GetDocumentExtractResultResponse:
        """
        @summary 文档抽取结果查询
        
        @param request: GetDocumentExtractResultRequest
        @return: GetDocumentExtractResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_document_extract_result_with_options(request, runtime)

    async def get_document_extract_result_async(
        self,
        request: docmind_api_20220711_models.GetDocumentExtractResultRequest,
    ) -> docmind_api_20220711_models.GetDocumentExtractResultResponse:
        """
        @summary 文档抽取结果查询
        
        @param request: GetDocumentExtractResultRequest
        @return: GetDocumentExtractResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_document_extract_result_with_options_async(request, runtime)

    def get_page_num_with_options(
        self,
        request: docmind_api_20220711_models.GetPageNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetPageNumResponse:
        """
        @summary openmind
        
        @param request: GetPageNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPageNumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPageNum',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetPageNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_page_num_with_options_async(
        self,
        request: docmind_api_20220711_models.GetPageNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetPageNumResponse:
        """
        @summary openmind
        
        @param request: GetPageNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPageNumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPageNum',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetPageNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_page_num(
        self,
        request: docmind_api_20220711_models.GetPageNumRequest,
    ) -> docmind_api_20220711_models.GetPageNumResponse:
        """
        @summary openmind
        
        @param request: GetPageNumRequest
        @return: GetPageNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_page_num_with_options(request, runtime)

    async def get_page_num_async(
        self,
        request: docmind_api_20220711_models.GetPageNumRequest,
    ) -> docmind_api_20220711_models.GetPageNumResponse:
        """
        @summary openmind
        
        @param request: GetPageNumRequest
        @return: GetPageNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_page_num_with_options_async(request, runtime)

    def get_table_understanding_result_with_options(
        self,
        request: docmind_api_20220711_models.GetTableUnderstandingResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetTableUnderstandingResultResponse:
        """
        @summary 表格智能解析结果查询
        
        @param request: GetTableUnderstandingResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableUnderstandingResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableUnderstandingResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetTableUnderstandingResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_understanding_result_with_options_async(
        self,
        request: docmind_api_20220711_models.GetTableUnderstandingResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.GetTableUnderstandingResultResponse:
        """
        @summary 表格智能解析结果查询
        
        @param request: GetTableUnderstandingResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableUnderstandingResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableUnderstandingResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetTableUnderstandingResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_understanding_result(
        self,
        request: docmind_api_20220711_models.GetTableUnderstandingResultRequest,
    ) -> docmind_api_20220711_models.GetTableUnderstandingResultResponse:
        """
        @summary 表格智能解析结果查询
        
        @param request: GetTableUnderstandingResultRequest
        @return: GetTableUnderstandingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_table_understanding_result_with_options(request, runtime)

    async def get_table_understanding_result_async(
        self,
        request: docmind_api_20220711_models.GetTableUnderstandingResultRequest,
    ) -> docmind_api_20220711_models.GetTableUnderstandingResultResponse:
        """
        @summary 表格智能解析结果查询
        
        @param request: GetTableUnderstandingResultRequest
        @return: GetTableUnderstandingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_table_understanding_result_with_options_async(request, runtime)

    def query_doc_parser_status_with_options(
        self,
        request: docmind_api_20220711_models.QueryDocParserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.QueryDocParserStatusResponse:
        """
        @summary 获取文档智能解析处理状态
        
        @param request: QueryDocParserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDocParserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDocParserStatus',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.QueryDocParserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_doc_parser_status_with_options_async(
        self,
        request: docmind_api_20220711_models.QueryDocParserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.QueryDocParserStatusResponse:
        """
        @summary 获取文档智能解析处理状态
        
        @param request: QueryDocParserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDocParserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDocParserStatus',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.QueryDocParserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_doc_parser_status(
        self,
        request: docmind_api_20220711_models.QueryDocParserStatusRequest,
    ) -> docmind_api_20220711_models.QueryDocParserStatusResponse:
        """
        @summary 获取文档智能解析处理状态
        
        @param request: QueryDocParserStatusRequest
        @return: QueryDocParserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_doc_parser_status_with_options(request, runtime)

    async def query_doc_parser_status_async(
        self,
        request: docmind_api_20220711_models.QueryDocParserStatusRequest,
    ) -> docmind_api_20220711_models.QueryDocParserStatusResponse:
        """
        @summary 获取文档智能解析处理状态
        
        @param request: QueryDocParserStatusRequest
        @return: QueryDocParserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_doc_parser_status_with_options_async(request, runtime)

    def submit_convert_image_to_excel_job_with_options(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToExcelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse:
        """
        @summary 图片转excel
        
        @param tmp_req: SubmitConvertImageToExcelJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToExcelJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToExcelJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToExcelJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_excel_job_with_options_async(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToExcelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse:
        """
        @summary 图片转excel
        
        @param tmp_req: SubmitConvertImageToExcelJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToExcelJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToExcelJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToExcelJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_excel_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToExcelJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse:
        """
        @summary 图片转excel
        
        @param request: SubmitConvertImageToExcelJobRequest
        @return: SubmitConvertImageToExcelJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_image_to_excel_job_with_options(request, runtime)

    async def submit_convert_image_to_excel_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToExcelJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse:
        """
        @summary 图片转excel
        
        @param request: SubmitConvertImageToExcelJobRequest
        @return: SubmitConvertImageToExcelJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_image_to_excel_job_with_options_async(request, runtime)

    def submit_convert_image_to_markdown_job_with_options(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToMarkdownJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse:
        """
        @summary 图片转markdown
        
        @param tmp_req: SubmitConvertImageToMarkdownJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToMarkdownJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToMarkdownJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToMarkdownJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_markdown_job_with_options_async(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToMarkdownJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse:
        """
        @summary 图片转markdown
        
        @param tmp_req: SubmitConvertImageToMarkdownJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToMarkdownJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToMarkdownJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToMarkdownJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_markdown_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToMarkdownJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse:
        """
        @summary 图片转markdown
        
        @param request: SubmitConvertImageToMarkdownJobRequest
        @return: SubmitConvertImageToMarkdownJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_image_to_markdown_job_with_options(request, runtime)

    async def submit_convert_image_to_markdown_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToMarkdownJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse:
        """
        @summary 图片转markdown
        
        @param request: SubmitConvertImageToMarkdownJobRequest
        @return: SubmitConvertImageToMarkdownJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_image_to_markdown_job_with_options_async(request, runtime)

    def submit_convert_image_to_pdf_job_with_options(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToPdfJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse:
        """
        @summary 图片转pdf
        
        @param tmp_req: SubmitConvertImageToPdfJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToPdfJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToPdfJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToPdfJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_pdf_job_with_options_async(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToPdfJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse:
        """
        @summary 图片转pdf
        
        @param tmp_req: SubmitConvertImageToPdfJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToPdfJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToPdfJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToPdfJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_pdf_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToPdfJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse:
        """
        @summary 图片转pdf
        
        @param request: SubmitConvertImageToPdfJobRequest
        @return: SubmitConvertImageToPdfJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_image_to_pdf_job_with_options(request, runtime)

    async def submit_convert_image_to_pdf_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToPdfJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse:
        """
        @summary 图片转pdf
        
        @param request: SubmitConvertImageToPdfJobRequest
        @return: SubmitConvertImageToPdfJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_image_to_pdf_job_with_options_async(request, runtime)

    def submit_convert_image_to_word_job_with_options(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToWordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToWordJobResponse:
        """
        @summary 图片转word
        
        @param tmp_req: SubmitConvertImageToWordJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToWordJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToWordJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToWordJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToWordJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_word_job_with_options_async(
        self,
        tmp_req: docmind_api_20220711_models.SubmitConvertImageToWordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertImageToWordJobResponse:
        """
        @summary 图片转word
        
        @param tmp_req: SubmitConvertImageToWordJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertImageToWordJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToWordJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToWordJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToWordJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_word_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToWordJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToWordJobResponse:
        """
        @summary 图片转word
        
        @param request: SubmitConvertImageToWordJobRequest
        @return: SubmitConvertImageToWordJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_image_to_word_job_with_options(request, runtime)

    async def submit_convert_image_to_word_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertImageToWordJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertImageToWordJobResponse:
        """
        @summary 图片转word
        
        @param request: SubmitConvertImageToWordJobRequest
        @return: SubmitConvertImageToWordJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_image_to_word_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_excel_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse:
        """
        @summary pdf转excel
        
        @param request: SubmitConvertPdfToExcelJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToExcelJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not UtilClient.is_unset(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToExcelJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_excel_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse:
        """
        @summary pdf转excel
        
        @param request: SubmitConvertPdfToExcelJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToExcelJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not UtilClient.is_unset(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToExcelJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_excel_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse:
        """
        @summary pdf转excel
        
        @param request: SubmitConvertPdfToExcelJobRequest
        @return: SubmitConvertPdfToExcelJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_pdf_to_excel_job_with_options(request, runtime)

    async def submit_convert_pdf_to_excel_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse:
        """
        @summary pdf转excel
        
        @param request: SubmitConvertPdfToExcelJobRequest
        @return: SubmitConvertPdfToExcelJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_pdf_to_excel_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_excel_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToExcelJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_excel_job_req = docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_excel_job_req)
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
            submit_convert_pdf_to_excel_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_excel_job_resp = self.submit_convert_pdf_to_excel_job_with_options(submit_convert_pdf_to_excel_job_req, runtime)
        return submit_convert_pdf_to_excel_job_resp

    async def submit_convert_pdf_to_excel_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToExcelJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_excel_job_req = docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_excel_job_req)
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
            submit_convert_pdf_to_excel_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_excel_job_resp = await self.submit_convert_pdf_to_excel_job_with_options_async(submit_convert_pdf_to_excel_job_req, runtime)
        return submit_convert_pdf_to_excel_job_resp

    def submit_convert_pdf_to_image_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse:
        """
        @summary pdf转图片
        
        @param request: SubmitConvertPdfToImageJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToImageJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToImageJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_image_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse:
        """
        @summary pdf转图片
        
        @param request: SubmitConvertPdfToImageJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToImageJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToImageJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_image_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse:
        """
        @summary pdf转图片
        
        @param request: SubmitConvertPdfToImageJobRequest
        @return: SubmitConvertPdfToImageJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_pdf_to_image_job_with_options(request, runtime)

    async def submit_convert_pdf_to_image_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse:
        """
        @summary pdf转图片
        
        @param request: SubmitConvertPdfToImageJobRequest
        @return: SubmitConvertPdfToImageJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_pdf_to_image_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_image_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToImageJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_image_job_req = docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_image_job_req)
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
            submit_convert_pdf_to_image_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_image_job_resp = self.submit_convert_pdf_to_image_job_with_options(submit_convert_pdf_to_image_job_req, runtime)
        return submit_convert_pdf_to_image_job_resp

    async def submit_convert_pdf_to_image_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToImageJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_image_job_req = docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_image_job_req)
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
            submit_convert_pdf_to_image_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_image_job_resp = await self.submit_convert_pdf_to_image_job_with_options_async(submit_convert_pdf_to_image_job_req, runtime)
        return submit_convert_pdf_to_image_job_resp

    def submit_convert_pdf_to_markdown_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse:
        """
        @summary pdf转markdown
        
        @param request: SubmitConvertPdfToMarkdownJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToMarkdownJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToMarkdownJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_markdown_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse:
        """
        @summary pdf转markdown
        
        @param request: SubmitConvertPdfToMarkdownJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToMarkdownJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToMarkdownJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_markdown_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse:
        """
        @summary pdf转markdown
        
        @param request: SubmitConvertPdfToMarkdownJobRequest
        @return: SubmitConvertPdfToMarkdownJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_pdf_to_markdown_job_with_options(request, runtime)

    async def submit_convert_pdf_to_markdown_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse:
        """
        @summary pdf转markdown
        
        @param request: SubmitConvertPdfToMarkdownJobRequest
        @return: SubmitConvertPdfToMarkdownJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_pdf_to_markdown_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_markdown_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_markdown_job_req = docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_markdown_job_req)
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
            submit_convert_pdf_to_markdown_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_markdown_job_resp = self.submit_convert_pdf_to_markdown_job_with_options(submit_convert_pdf_to_markdown_job_req, runtime)
        return submit_convert_pdf_to_markdown_job_resp

    async def submit_convert_pdf_to_markdown_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_markdown_job_req = docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_markdown_job_req)
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
            submit_convert_pdf_to_markdown_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_markdown_job_resp = await self.submit_convert_pdf_to_markdown_job_with_options_async(submit_convert_pdf_to_markdown_job_req, runtime)
        return submit_convert_pdf_to_markdown_job_resp

    def submit_convert_pdf_to_word_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse:
        """
        @summary pdf转word
        
        @param request: SubmitConvertPdfToWordJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToWordJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not UtilClient.is_unset(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToWordJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_word_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse:
        """
        @summary pdf转word
        
        @param request: SubmitConvertPdfToWordJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitConvertPdfToWordJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not UtilClient.is_unset(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToWordJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_word_job(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse:
        """
        @summary pdf转word
        
        @param request: SubmitConvertPdfToWordJobRequest
        @return: SubmitConvertPdfToWordJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_pdf_to_word_job_with_options(request, runtime)

    async def submit_convert_pdf_to_word_job_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse:
        """
        @summary pdf转word
        
        @param request: SubmitConvertPdfToWordJobRequest
        @return: SubmitConvertPdfToWordJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_convert_pdf_to_word_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_word_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToWordJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_word_job_req = docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_word_job_req)
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
            submit_convert_pdf_to_word_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_word_job_resp = self.submit_convert_pdf_to_word_job_with_options(submit_convert_pdf_to_word_job_req, runtime)
        return submit_convert_pdf_to_word_job_resp

    async def submit_convert_pdf_to_word_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToWordJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse:
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
            'Product': 'docmind-api',
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
        submit_convert_pdf_to_word_job_req = docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_word_job_req)
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
            submit_convert_pdf_to_word_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_convert_pdf_to_word_job_resp = await self.submit_convert_pdf_to_word_job_with_options_async(submit_convert_pdf_to_word_job_req, runtime)
        return submit_convert_pdf_to_word_job_resp

    def submit_digital_doc_structure_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse:
        """
        @summary 电子解析
        
        @param request: SubmitDigitalDocStructureJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDigitalDocStructureJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not UtilClient.is_unset(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDigitalDocStructureJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_digital_doc_structure_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse:
        """
        @summary 电子解析
        
        @param request: SubmitDigitalDocStructureJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDigitalDocStructureJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not UtilClient.is_unset(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDigitalDocStructureJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_digital_doc_structure_job(
        self,
        request: docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest,
    ) -> docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse:
        """
        @summary 电子解析
        
        @param request: SubmitDigitalDocStructureJobRequest
        @return: SubmitDigitalDocStructureJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_digital_doc_structure_job_with_options(request, runtime)

    async def submit_digital_doc_structure_job_async(
        self,
        request: docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest,
    ) -> docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse:
        """
        @summary 电子解析
        
        @param request: SubmitDigitalDocStructureJobRequest
        @return: SubmitDigitalDocStructureJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_digital_doc_structure_job_with_options_async(request, runtime)

    def submit_digital_doc_structure_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitDigitalDocStructureJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse:
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
            'Product': 'docmind-api',
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
        submit_digital_doc_structure_job_req = docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_digital_doc_structure_job_req)
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
            submit_digital_doc_structure_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_digital_doc_structure_job_resp = self.submit_digital_doc_structure_job_with_options(submit_digital_doc_structure_job_req, runtime)
        return submit_digital_doc_structure_job_resp

    async def submit_digital_doc_structure_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDigitalDocStructureJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse:
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
            'Product': 'docmind-api',
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
        submit_digital_doc_structure_job_req = docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_digital_doc_structure_job_req)
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
            submit_digital_doc_structure_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_digital_doc_structure_job_resp = await self.submit_digital_doc_structure_job_with_options_async(submit_digital_doc_structure_job_req, runtime)
        return submit_digital_doc_structure_job_resp

    def submit_doc_parser_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitDocParserJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocParserJobResponse:
        """
        @summary 文档智能解析流式输出
        
        @param request: SubmitDocParserJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocParserJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not UtilClient.is_unset(request.llm_enhancement):
            query['LlmEnhancement'] = request.llm_enhancement
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.output_html_table):
            query['OutputHtmlTable'] = request.output_html_table
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocParserJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocParserJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_parser_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitDocParserJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocParserJobResponse:
        """
        @summary 文档智能解析流式输出
        
        @param request: SubmitDocParserJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocParserJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not UtilClient.is_unset(request.llm_enhancement):
            query['LlmEnhancement'] = request.llm_enhancement
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.output_html_table):
            query['OutputHtmlTable'] = request.output_html_table
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocParserJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocParserJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_parser_job(
        self,
        request: docmind_api_20220711_models.SubmitDocParserJobRequest,
    ) -> docmind_api_20220711_models.SubmitDocParserJobResponse:
        """
        @summary 文档智能解析流式输出
        
        @param request: SubmitDocParserJobRequest
        @return: SubmitDocParserJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_doc_parser_job_with_options(request, runtime)

    async def submit_doc_parser_job_async(
        self,
        request: docmind_api_20220711_models.SubmitDocParserJobRequest,
    ) -> docmind_api_20220711_models.SubmitDocParserJobResponse:
        """
        @summary 文档智能解析流式输出
        
        @param request: SubmitDocParserJobRequest
        @return: SubmitDocParserJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_doc_parser_job_with_options_async(request, runtime)

    def submit_doc_parser_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitDocParserJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocParserJobResponse:
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
            'Product': 'docmind-api',
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
        submit_doc_parser_job_req = docmind_api_20220711_models.SubmitDocParserJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_parser_job_req)
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
            submit_doc_parser_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_parser_job_resp = self.submit_doc_parser_job_with_options(submit_doc_parser_job_req, runtime)
        return submit_doc_parser_job_resp

    async def submit_doc_parser_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDocParserJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocParserJobResponse:
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
            'Product': 'docmind-api',
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
        submit_doc_parser_job_req = docmind_api_20220711_models.SubmitDocParserJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_parser_job_req)
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
            submit_doc_parser_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_parser_job_resp = await self.submit_doc_parser_job_with_options_async(submit_doc_parser_job_req, runtime)
        return submit_doc_parser_job_resp

    def submit_doc_structure_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitDocStructureJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocStructureJobResponse:
        """
        @summary 文档智能解析
        
        @param request: SubmitDocStructureJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocStructureJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ppt_format):
            query['AllowPptFormat'] = request.allow_ppt_format
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.structure_type):
            query['StructureType'] = request.structure_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocStructureJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocStructureJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_structure_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitDocStructureJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocStructureJobResponse:
        """
        @summary 文档智能解析
        
        @param request: SubmitDocStructureJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocStructureJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ppt_format):
            query['AllowPptFormat'] = request.allow_ppt_format
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.structure_type):
            query['StructureType'] = request.structure_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocStructureJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocStructureJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_structure_job(
        self,
        request: docmind_api_20220711_models.SubmitDocStructureJobRequest,
    ) -> docmind_api_20220711_models.SubmitDocStructureJobResponse:
        """
        @summary 文档智能解析
        
        @param request: SubmitDocStructureJobRequest
        @return: SubmitDocStructureJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_doc_structure_job_with_options(request, runtime)

    async def submit_doc_structure_job_async(
        self,
        request: docmind_api_20220711_models.SubmitDocStructureJobRequest,
    ) -> docmind_api_20220711_models.SubmitDocStructureJobResponse:
        """
        @summary 文档智能解析
        
        @param request: SubmitDocStructureJobRequest
        @return: SubmitDocStructureJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_doc_structure_job_with_options_async(request, runtime)

    def submit_doc_structure_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitDocStructureJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocStructureJobResponse:
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
            'Product': 'docmind-api',
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
        submit_doc_structure_job_req = docmind_api_20220711_models.SubmitDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_structure_job_req)
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
            submit_doc_structure_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_structure_job_resp = self.submit_doc_structure_job_with_options(submit_doc_structure_job_req, runtime)
        return submit_doc_structure_job_resp

    async def submit_doc_structure_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDocStructureJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocStructureJobResponse:
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
            'Product': 'docmind-api',
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
        submit_doc_structure_job_req = docmind_api_20220711_models.SubmitDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_structure_job_req)
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
            submit_doc_structure_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_structure_job_resp = await self.submit_doc_structure_job_with_options_async(submit_doc_structure_job_req, runtime)
        return submit_doc_structure_job_resp

    def submit_document_extract_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitDocumentExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocumentExtractJobResponse:
        """
        @summary 文档抽取
        
        @param request: SubmitDocumentExtractJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocumentExtractJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocumentExtractJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocumentExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_document_extract_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitDocumentExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocumentExtractJobResponse:
        """
        @summary 文档抽取
        
        @param request: SubmitDocumentExtractJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocumentExtractJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocumentExtractJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocumentExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_document_extract_job(
        self,
        request: docmind_api_20220711_models.SubmitDocumentExtractJobRequest,
    ) -> docmind_api_20220711_models.SubmitDocumentExtractJobResponse:
        """
        @summary 文档抽取
        
        @param request: SubmitDocumentExtractJobRequest
        @return: SubmitDocumentExtractJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_document_extract_job_with_options(request, runtime)

    async def submit_document_extract_job_async(
        self,
        request: docmind_api_20220711_models.SubmitDocumentExtractJobRequest,
    ) -> docmind_api_20220711_models.SubmitDocumentExtractJobResponse:
        """
        @summary 文档抽取
        
        @param request: SubmitDocumentExtractJobRequest
        @return: SubmitDocumentExtractJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_document_extract_job_with_options_async(request, runtime)

    def submit_document_extract_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitDocumentExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocumentExtractJobResponse:
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
            'Product': 'docmind-api',
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
        submit_document_extract_job_req = docmind_api_20220711_models.SubmitDocumentExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_document_extract_job_req)
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
            submit_document_extract_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_document_extract_job_resp = self.submit_document_extract_job_with_options(submit_document_extract_job_req, runtime)
        return submit_document_extract_job_resp

    async def submit_document_extract_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDocumentExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocumentExtractJobResponse:
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
            'Product': 'docmind-api',
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
        submit_document_extract_job_req = docmind_api_20220711_models.SubmitDocumentExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_document_extract_job_req)
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
            submit_document_extract_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_document_extract_job_resp = await self.submit_document_extract_job_with_options_async(submit_document_extract_job_req, runtime)
        return submit_document_extract_job_resp

    def submit_table_understanding_job_with_options(
        self,
        request: docmind_api_20220711_models.SubmitTableUnderstandingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitTableUnderstandingJobResponse:
        """
        @summary 表格智能解析
        
        @param request: SubmitTableUnderstandingJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTableUnderstandingJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTableUnderstandingJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitTableUnderstandingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_table_understanding_job_with_options_async(
        self,
        request: docmind_api_20220711_models.SubmitTableUnderstandingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitTableUnderstandingJobResponse:
        """
        @summary 表格智能解析
        
        @param request: SubmitTableUnderstandingJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTableUnderstandingJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTableUnderstandingJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitTableUnderstandingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_table_understanding_job(
        self,
        request: docmind_api_20220711_models.SubmitTableUnderstandingJobRequest,
    ) -> docmind_api_20220711_models.SubmitTableUnderstandingJobResponse:
        """
        @summary 表格智能解析
        
        @param request: SubmitTableUnderstandingJobRequest
        @return: SubmitTableUnderstandingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_table_understanding_job_with_options(request, runtime)

    async def submit_table_understanding_job_async(
        self,
        request: docmind_api_20220711_models.SubmitTableUnderstandingJobRequest,
    ) -> docmind_api_20220711_models.SubmitTableUnderstandingJobResponse:
        """
        @summary 表格智能解析
        
        @param request: SubmitTableUnderstandingJobRequest
        @return: SubmitTableUnderstandingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_table_understanding_job_with_options_async(request, runtime)

    def submit_table_understanding_job_advance(
        self,
        request: docmind_api_20220711_models.SubmitTableUnderstandingJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitTableUnderstandingJobResponse:
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
            'Product': 'docmind-api',
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
        submit_table_understanding_job_req = docmind_api_20220711_models.SubmitTableUnderstandingJobRequest()
        OpenApiUtilClient.convert(request, submit_table_understanding_job_req)
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
            submit_table_understanding_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_table_understanding_job_resp = self.submit_table_understanding_job_with_options(submit_table_understanding_job_req, runtime)
        return submit_table_understanding_job_resp

    async def submit_table_understanding_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitTableUnderstandingJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitTableUnderstandingJobResponse:
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
            'Product': 'docmind-api',
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
        submit_table_understanding_job_req = docmind_api_20220711_models.SubmitTableUnderstandingJobRequest()
        OpenApiUtilClient.convert(request, submit_table_understanding_job_req)
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
            submit_table_understanding_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_table_understanding_job_resp = await self.submit_table_understanding_job_with_options_async(submit_table_understanding_job_req, runtime)
        return submit_table_understanding_job_resp
