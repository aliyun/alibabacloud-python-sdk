# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_docmind_api20220711 import models as main_models
from alibabacloud_tea_openapi import exceptions as open_api_exceptions
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore
from darabonba.core import DaraCore as DaraCore
from darabonba.request import DaraRequest
from darabonba.runtime import RuntimeOptions
from darabonba.utils.form import FileField
from darabonba.utils.form import Form as DaraForm
from darabonba.utils.stream import Stream as DaraStream
from darabonba.utils.xml import XML as DaraXML

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        form: dict,
    ) -> dict:
        _request = DaraRequest()
        boundary = DaraForm.get_boundary()
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': str(form.get("host")),
            'date': Utils.get_date_utcstring(),
            'user-agent': Utils.get_user_agent('')
        }
        _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
        _request.body = DaraForm.to_file_form(form, boundary)
        _last_request = _request
        _response = DaraCore.do_action(_request)
        resp_map = None
        body_str = DaraStream.read_as_string(_response.body)
        if (_response.status_code >= 400) and (_response.status_code < 600):
            resp_map = DaraXML.parse_xml(body_str, None)
            err = resp_map.get("Error")
            raise open_api_exceptions.ClientException(
                code = str(err.get("Code")),
                message = str(err.get("Message")),
                data = {
                    'httpCode': _response.status_code,
                    'requestId': str(err.get("RequestId")),
                    'hostId': str(err.get("HostId"))
                }
            )
        resp_map = DaraXML.parse_xml(body_str, None)
        return DaraCore.merge({}, resp_map)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        form: dict,
    ) -> dict:
        _request = DaraRequest()
        boundary = DaraForm.get_boundary()
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': str(form.get("host")),
            'date': Utils.get_date_utcstring(),
            'user-agent': Utils.get_user_agent('')
        }
        _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
        _request.body = DaraForm.to_file_form(form, boundary)
        _last_request = _request
        _response = await DaraCore.async_do_action(_request)
        resp_map = None
        body_str = await DaraStream.read_as_string_async(_response.body)
        if (_response.status_code >= 400) and (_response.status_code < 600):
            resp_map = DaraXML.parse_xml(body_str, None)
            err = resp_map.get("Error")
            raise open_api_exceptions.ClientException(
                code = str(err.get("Code")),
                message = str(err.get("Message")),
                data = {
                    'httpCode': _response.status_code,
                    'requestId': str(err.get("RequestId")),
                    'hostId': str(err.get("HostId"))
                }
            )
        resp_map = DaraXML.parse_xml(body_str, None)
        return DaraCore.merge({}, resp_map)

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

    def aync_trade_document_package_extract_smart_app_with_options(
        self,
        tmp_req: main_models.AyncTradeDocumentPackageExtractSmartAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        tmp_req.validate()
        request = main_models.AyncTradeDocumentPackageExtractSmartAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_extraction_range):
            request.custom_extraction_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_extraction_range, 'CustomExtractionRange', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_extraction_range_shrink):
            query['CustomExtractionRange'] = request.custom_extraction_range_shrink
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AyncTradeDocumentPackageExtractSmartApp',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def aync_trade_document_package_extract_smart_app_with_options_async(
        self,
        tmp_req: main_models.AyncTradeDocumentPackageExtractSmartAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        tmp_req.validate()
        request = main_models.AyncTradeDocumentPackageExtractSmartAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_extraction_range):
            request.custom_extraction_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_extraction_range, 'CustomExtractionRange', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_extraction_range_shrink):
            query['CustomExtractionRange'] = request.custom_extraction_range_shrink
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AyncTradeDocumentPackageExtractSmartApp',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aync_trade_document_package_extract_smart_app(
        self,
        request: main_models.AyncTradeDocumentPackageExtractSmartAppRequest,
    ) -> main_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        runtime = RuntimeOptions()
        return self.aync_trade_document_package_extract_smart_app_with_options(request, runtime)

    async def aync_trade_document_package_extract_smart_app_async(
        self,
        request: main_models.AyncTradeDocumentPackageExtractSmartAppRequest,
    ) -> main_models.AyncTradeDocumentPackageExtractSmartAppResponse:
        runtime = RuntimeOptions()
        return await self.aync_trade_document_package_extract_smart_app_with_options_async(request, runtime)

    def get_doc_parser_result_with_options(
        self,
        request: main_models.GetDocParserResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocParserResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.layout_num):
            query['LayoutNum'] = request.layout_num
        if not DaraCore.is_null(request.layout_step_size):
            query['LayoutStepSize'] = request.layout_step_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocParserResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocParserResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_parser_result_with_options_async(
        self,
        request: main_models.GetDocParserResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocParserResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.layout_num):
            query['LayoutNum'] = request.layout_num
        if not DaraCore.is_null(request.layout_step_size):
            query['LayoutStepSize'] = request.layout_step_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocParserResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocParserResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_parser_result(
        self,
        request: main_models.GetDocParserResultRequest,
    ) -> main_models.GetDocParserResultResponse:
        runtime = RuntimeOptions()
        return self.get_doc_parser_result_with_options(request, runtime)

    async def get_doc_parser_result_async(
        self,
        request: main_models.GetDocParserResultRequest,
    ) -> main_models.GetDocParserResultResponse:
        runtime = RuntimeOptions()
        return await self.get_doc_parser_result_with_options_async(request, runtime)

    def get_doc_structure_result_with_options(
        self,
        request: main_models.GetDocStructureResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocStructureResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not DaraCore.is_null(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not DaraCore.is_null(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocStructureResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocStructureResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_structure_result_with_options_async(
        self,
        request: main_models.GetDocStructureResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocStructureResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not DaraCore.is_null(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not DaraCore.is_null(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocStructureResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocStructureResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_structure_result(
        self,
        request: main_models.GetDocStructureResultRequest,
    ) -> main_models.GetDocStructureResultResponse:
        runtime = RuntimeOptions()
        return self.get_doc_structure_result_with_options(request, runtime)

    async def get_doc_structure_result_async(
        self,
        request: main_models.GetDocStructureResultRequest,
    ) -> main_models.GetDocStructureResultResponse:
        runtime = RuntimeOptions()
        return await self.get_doc_structure_result_with_options_async(request, runtime)

    def get_document_compare_result_with_options(
        self,
        request: main_models.GetDocumentCompareResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentCompareResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentCompareResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentCompareResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_compare_result_with_options_async(
        self,
        request: main_models.GetDocumentCompareResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentCompareResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentCompareResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentCompareResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_compare_result(
        self,
        request: main_models.GetDocumentCompareResultRequest,
    ) -> main_models.GetDocumentCompareResultResponse:
        runtime = RuntimeOptions()
        return self.get_document_compare_result_with_options(request, runtime)

    async def get_document_compare_result_async(
        self,
        request: main_models.GetDocumentCompareResultRequest,
    ) -> main_models.GetDocumentCompareResultResponse:
        runtime = RuntimeOptions()
        return await self.get_document_compare_result_with_options_async(request, runtime)

    def get_document_convert_result_with_options(
        self,
        request: main_models.GetDocumentConvertResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentConvertResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentConvertResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentConvertResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_convert_result_with_options_async(
        self,
        request: main_models.GetDocumentConvertResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentConvertResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentConvertResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentConvertResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_convert_result(
        self,
        request: main_models.GetDocumentConvertResultRequest,
    ) -> main_models.GetDocumentConvertResultResponse:
        runtime = RuntimeOptions()
        return self.get_document_convert_result_with_options(request, runtime)

    async def get_document_convert_result_async(
        self,
        request: main_models.GetDocumentConvertResultRequest,
    ) -> main_models.GetDocumentConvertResultResponse:
        runtime = RuntimeOptions()
        return await self.get_document_convert_result_with_options_async(request, runtime)

    def get_document_extract_result_with_options(
        self,
        request: main_models.GetDocumentExtractResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentExtractResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentExtractResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentExtractResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_extract_result_with_options_async(
        self,
        request: main_models.GetDocumentExtractResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentExtractResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentExtractResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentExtractResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_extract_result(
        self,
        request: main_models.GetDocumentExtractResultRequest,
    ) -> main_models.GetDocumentExtractResultResponse:
        runtime = RuntimeOptions()
        return self.get_document_extract_result_with_options(request, runtime)

    async def get_document_extract_result_async(
        self,
        request: main_models.GetDocumentExtractResultRequest,
    ) -> main_models.GetDocumentExtractResultResponse:
        runtime = RuntimeOptions()
        return await self.get_document_extract_result_with_options_async(request, runtime)

    def get_page_num_with_options(
        self,
        request: main_models.GetPageNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPageNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPageNum',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPageNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_page_num_with_options_async(
        self,
        request: main_models.GetPageNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPageNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPageNum',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPageNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_page_num(
        self,
        request: main_models.GetPageNumRequest,
    ) -> main_models.GetPageNumResponse:
        runtime = RuntimeOptions()
        return self.get_page_num_with_options(request, runtime)

    async def get_page_num_async(
        self,
        request: main_models.GetPageNumRequest,
    ) -> main_models.GetPageNumResponse:
        runtime = RuntimeOptions()
        return await self.get_page_num_with_options_async(request, runtime)

    def get_table_understanding_result_with_options(
        self,
        request: main_models.GetTableUnderstandingResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableUnderstandingResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableUnderstandingResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableUnderstandingResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_understanding_result_with_options_async(
        self,
        request: main_models.GetTableUnderstandingResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableUnderstandingResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableUnderstandingResult',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableUnderstandingResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_understanding_result(
        self,
        request: main_models.GetTableUnderstandingResultRequest,
    ) -> main_models.GetTableUnderstandingResultResponse:
        runtime = RuntimeOptions()
        return self.get_table_understanding_result_with_options(request, runtime)

    async def get_table_understanding_result_async(
        self,
        request: main_models.GetTableUnderstandingResultRequest,
    ) -> main_models.GetTableUnderstandingResultResponse:
        runtime = RuntimeOptions()
        return await self.get_table_understanding_result_with_options_async(request, runtime)

    def query_doc_parser_status_with_options(
        self,
        request: main_models.QueryDocParserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDocParserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDocParserStatus',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDocParserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_doc_parser_status_with_options_async(
        self,
        request: main_models.QueryDocParserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDocParserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDocParserStatus',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDocParserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_doc_parser_status(
        self,
        request: main_models.QueryDocParserStatusRequest,
    ) -> main_models.QueryDocParserStatusResponse:
        runtime = RuntimeOptions()
        return self.query_doc_parser_status_with_options(request, runtime)

    async def query_doc_parser_status_async(
        self,
        request: main_models.QueryDocParserStatusRequest,
    ) -> main_models.QueryDocParserStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_doc_parser_status_with_options_async(request, runtime)

    def submit_convert_image_to_excel_job_with_options(
        self,
        tmp_req: main_models.SubmitConvertImageToExcelJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToExcelJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToExcelJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToExcelJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToExcelJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_excel_job_with_options_async(
        self,
        tmp_req: main_models.SubmitConvertImageToExcelJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToExcelJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToExcelJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToExcelJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToExcelJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_excel_job(
        self,
        request: main_models.SubmitConvertImageToExcelJobRequest,
    ) -> main_models.SubmitConvertImageToExcelJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_image_to_excel_job_with_options(request, runtime)

    async def submit_convert_image_to_excel_job_async(
        self,
        request: main_models.SubmitConvertImageToExcelJobRequest,
    ) -> main_models.SubmitConvertImageToExcelJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_image_to_excel_job_with_options_async(request, runtime)

    def submit_convert_image_to_markdown_job_with_options(
        self,
        tmp_req: main_models.SubmitConvertImageToMarkdownJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToMarkdownJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToMarkdownJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToMarkdownJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToMarkdownJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_markdown_job_with_options_async(
        self,
        tmp_req: main_models.SubmitConvertImageToMarkdownJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToMarkdownJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToMarkdownJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToMarkdownJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToMarkdownJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_markdown_job(
        self,
        request: main_models.SubmitConvertImageToMarkdownJobRequest,
    ) -> main_models.SubmitConvertImageToMarkdownJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_image_to_markdown_job_with_options(request, runtime)

    async def submit_convert_image_to_markdown_job_async(
        self,
        request: main_models.SubmitConvertImageToMarkdownJobRequest,
    ) -> main_models.SubmitConvertImageToMarkdownJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_image_to_markdown_job_with_options_async(request, runtime)

    def submit_convert_image_to_pdf_job_with_options(
        self,
        tmp_req: main_models.SubmitConvertImageToPdfJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToPdfJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToPdfJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToPdfJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToPdfJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_pdf_job_with_options_async(
        self,
        tmp_req: main_models.SubmitConvertImageToPdfJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToPdfJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToPdfJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToPdfJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToPdfJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_pdf_job(
        self,
        request: main_models.SubmitConvertImageToPdfJobRequest,
    ) -> main_models.SubmitConvertImageToPdfJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_image_to_pdf_job_with_options(request, runtime)

    async def submit_convert_image_to_pdf_job_async(
        self,
        request: main_models.SubmitConvertImageToPdfJobRequest,
    ) -> main_models.SubmitConvertImageToPdfJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_image_to_pdf_job_with_options_async(request, runtime)

    def submit_convert_image_to_word_job_with_options(
        self,
        tmp_req: main_models.SubmitConvertImageToWordJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToWordJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToWordJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToWordJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToWordJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_image_to_word_job_with_options_async(
        self,
        tmp_req: main_models.SubmitConvertImageToWordJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertImageToWordJobResponse:
        tmp_req.validate()
        request = main_models.SubmitConvertImageToWordJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not DaraCore.is_null(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertImageToWordJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertImageToWordJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_image_to_word_job(
        self,
        request: main_models.SubmitConvertImageToWordJobRequest,
    ) -> main_models.SubmitConvertImageToWordJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_image_to_word_job_with_options(request, runtime)

    async def submit_convert_image_to_word_job_async(
        self,
        request: main_models.SubmitConvertImageToWordJobRequest,
    ) -> main_models.SubmitConvertImageToWordJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_image_to_word_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_excel_job_with_options(
        self,
        request: main_models.SubmitConvertPdfToExcelJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToExcelJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not DaraCore.is_null(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToExcelJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToExcelJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_excel_job_with_options_async(
        self,
        request: main_models.SubmitConvertPdfToExcelJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToExcelJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not DaraCore.is_null(request.force_merge_excel):
            query['ForceMergeExcel'] = request.force_merge_excel
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToExcelJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToExcelJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_excel_job(
        self,
        request: main_models.SubmitConvertPdfToExcelJobRequest,
    ) -> main_models.SubmitConvertPdfToExcelJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_pdf_to_excel_job_with_options(request, runtime)

    async def submit_convert_pdf_to_excel_job_async(
        self,
        request: main_models.SubmitConvertPdfToExcelJobRequest,
    ) -> main_models.SubmitConvertPdfToExcelJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_pdf_to_excel_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_excel_job_advance(
        self,
        request: main_models.SubmitConvertPdfToExcelJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToExcelJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_excel_job_req = main_models.SubmitConvertPdfToExcelJobRequest()
        Utils.convert(request, submit_convert_pdf_to_excel_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitConvertPdfToExcelJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToExcelJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_excel_job_req = main_models.SubmitConvertPdfToExcelJobRequest()
        Utils.convert(request, submit_convert_pdf_to_excel_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitConvertPdfToImageJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToImageJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToImageJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_image_job_with_options_async(
        self,
        request: main_models.SubmitConvertPdfToImageJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToImageJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToImageJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToImageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_image_job(
        self,
        request: main_models.SubmitConvertPdfToImageJobRequest,
    ) -> main_models.SubmitConvertPdfToImageJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_pdf_to_image_job_with_options(request, runtime)

    async def submit_convert_pdf_to_image_job_async(
        self,
        request: main_models.SubmitConvertPdfToImageJobRequest,
    ) -> main_models.SubmitConvertPdfToImageJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_pdf_to_image_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_image_job_advance(
        self,
        request: main_models.SubmitConvertPdfToImageJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToImageJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_image_job_req = main_models.SubmitConvertPdfToImageJobRequest()
        Utils.convert(request, submit_convert_pdf_to_image_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitConvertPdfToImageJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToImageJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_image_job_req = main_models.SubmitConvertPdfToImageJobRequest()
        Utils.convert(request, submit_convert_pdf_to_image_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitConvertPdfToMarkdownJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToMarkdownJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToMarkdownJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToMarkdownJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_markdown_job_with_options_async(
        self,
        request: main_models.SubmitConvertPdfToMarkdownJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToMarkdownJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToMarkdownJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToMarkdownJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_markdown_job(
        self,
        request: main_models.SubmitConvertPdfToMarkdownJobRequest,
    ) -> main_models.SubmitConvertPdfToMarkdownJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_pdf_to_markdown_job_with_options(request, runtime)

    async def submit_convert_pdf_to_markdown_job_async(
        self,
        request: main_models.SubmitConvertPdfToMarkdownJobRequest,
    ) -> main_models.SubmitConvertPdfToMarkdownJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_pdf_to_markdown_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_markdown_job_advance(
        self,
        request: main_models.SubmitConvertPdfToMarkdownJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToMarkdownJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_markdown_job_req = main_models.SubmitConvertPdfToMarkdownJobRequest()
        Utils.convert(request, submit_convert_pdf_to_markdown_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitConvertPdfToMarkdownJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToMarkdownJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_markdown_job_req = main_models.SubmitConvertPdfToMarkdownJobRequest()
        Utils.convert(request, submit_convert_pdf_to_markdown_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitConvertPdfToWordJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToWordJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not DaraCore.is_null(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToWordJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToWordJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_convert_pdf_to_word_job_with_options_async(
        self,
        request: main_models.SubmitConvertPdfToWordJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToWordJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.force_export_inner_image):
            query['ForceExportInnerImage'] = request.force_export_inner_image
        if not DaraCore.is_null(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitConvertPdfToWordJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitConvertPdfToWordJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_convert_pdf_to_word_job(
        self,
        request: main_models.SubmitConvertPdfToWordJobRequest,
    ) -> main_models.SubmitConvertPdfToWordJobResponse:
        runtime = RuntimeOptions()
        return self.submit_convert_pdf_to_word_job_with_options(request, runtime)

    async def submit_convert_pdf_to_word_job_async(
        self,
        request: main_models.SubmitConvertPdfToWordJobRequest,
    ) -> main_models.SubmitConvertPdfToWordJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_convert_pdf_to_word_job_with_options_async(request, runtime)

    def submit_convert_pdf_to_word_job_advance(
        self,
        request: main_models.SubmitConvertPdfToWordJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToWordJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_word_job_req = main_models.SubmitConvertPdfToWordJobRequest()
        Utils.convert(request, submit_convert_pdf_to_word_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitConvertPdfToWordJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitConvertPdfToWordJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_convert_pdf_to_word_job_req = main_models.SubmitConvertPdfToWordJobRequest()
        Utils.convert(request, submit_convert_pdf_to_word_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDigitalDocStructureJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDigitalDocStructureJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not DaraCore.is_null(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDigitalDocStructureJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDigitalDocStructureJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_digital_doc_structure_job_with_options_async(
        self,
        request: main_models.SubmitDigitalDocStructureJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDigitalDocStructureJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.image_strategy):
            query['ImageStrategy'] = request.image_strategy
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.reveal_markdown):
            query['RevealMarkdown'] = request.reveal_markdown
        if not DaraCore.is_null(request.use_url_response_body):
            query['UseUrlResponseBody'] = request.use_url_response_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDigitalDocStructureJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDigitalDocStructureJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_digital_doc_structure_job(
        self,
        request: main_models.SubmitDigitalDocStructureJobRequest,
    ) -> main_models.SubmitDigitalDocStructureJobResponse:
        runtime = RuntimeOptions()
        return self.submit_digital_doc_structure_job_with_options(request, runtime)

    async def submit_digital_doc_structure_job_async(
        self,
        request: main_models.SubmitDigitalDocStructureJobRequest,
    ) -> main_models.SubmitDigitalDocStructureJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_digital_doc_structure_job_with_options_async(request, runtime)

    def submit_digital_doc_structure_job_advance(
        self,
        request: main_models.SubmitDigitalDocStructureJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDigitalDocStructureJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_digital_doc_structure_job_req = main_models.SubmitDigitalDocStructureJobRequest()
        Utils.convert(request, submit_digital_doc_structure_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDigitalDocStructureJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDigitalDocStructureJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_digital_doc_structure_job_req = main_models.SubmitDigitalDocStructureJobRequest()
        Utils.convert(request, submit_digital_doc_structure_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDocParserJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParserJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enhancement_mode):
            query['EnhancementMode'] = request.enhancement_mode
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not DaraCore.is_null(request.llm_enhancement):
            query['LlmEnhancement'] = request.llm_enhancement
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.output_html_table):
            query['OutputHtmlTable'] = request.output_html_table
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocParserJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocParserJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_parser_job_with_options_async(
        self,
        request: main_models.SubmitDocParserJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParserJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enhancement_mode):
            query['EnhancementMode'] = request.enhancement_mode
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not DaraCore.is_null(request.llm_enhancement):
            query['LlmEnhancement'] = request.llm_enhancement
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.output_html_table):
            query['OutputHtmlTable'] = request.output_html_table
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocParserJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocParserJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_parser_job(
        self,
        request: main_models.SubmitDocParserJobRequest,
    ) -> main_models.SubmitDocParserJobResponse:
        runtime = RuntimeOptions()
        return self.submit_doc_parser_job_with_options(request, runtime)

    async def submit_doc_parser_job_async(
        self,
        request: main_models.SubmitDocParserJobRequest,
    ) -> main_models.SubmitDocParserJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_doc_parser_job_with_options_async(request, runtime)

    def submit_doc_parser_job_advance(
        self,
        request: main_models.SubmitDocParserJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParserJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_doc_parser_job_req = main_models.SubmitDocParserJobRequest()
        Utils.convert(request, submit_doc_parser_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDocParserJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParserJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_doc_parser_job_req = main_models.SubmitDocParserJobRequest()
        Utils.convert(request, submit_doc_parser_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDocStructureJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocStructureJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_ppt_format):
            query['AllowPptFormat'] = request.allow_ppt_format
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.structure_type):
            query['StructureType'] = request.structure_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocStructureJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocStructureJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_structure_job_with_options_async(
        self,
        request: main_models.SubmitDocStructureJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocStructureJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_ppt_format):
            query['AllowPptFormat'] = request.allow_ppt_format
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.formula_enhancement):
            query['FormulaEnhancement'] = request.formula_enhancement
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.structure_type):
            query['StructureType'] = request.structure_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocStructureJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocStructureJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_structure_job(
        self,
        request: main_models.SubmitDocStructureJobRequest,
    ) -> main_models.SubmitDocStructureJobResponse:
        runtime = RuntimeOptions()
        return self.submit_doc_structure_job_with_options(request, runtime)

    async def submit_doc_structure_job_async(
        self,
        request: main_models.SubmitDocStructureJobRequest,
    ) -> main_models.SubmitDocStructureJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_doc_structure_job_with_options_async(request, runtime)

    def submit_doc_structure_job_advance(
        self,
        request: main_models.SubmitDocStructureJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocStructureJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_doc_structure_job_req = main_models.SubmitDocStructureJobRequest()
        Utils.convert(request, submit_doc_structure_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDocStructureJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocStructureJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_doc_structure_job_req = main_models.SubmitDocStructureJobRequest()
        Utils.convert(request, submit_doc_structure_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDocumentExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocumentExtractJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocumentExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_document_extract_job_with_options_async(
        self,
        request: main_models.SubmitDocumentExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocumentExtractJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocumentExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_document_extract_job(
        self,
        request: main_models.SubmitDocumentExtractJobRequest,
    ) -> main_models.SubmitDocumentExtractJobResponse:
        runtime = RuntimeOptions()
        return self.submit_document_extract_job_with_options(request, runtime)

    async def submit_document_extract_job_async(
        self,
        request: main_models.SubmitDocumentExtractJobRequest,
    ) -> main_models.SubmitDocumentExtractJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_document_extract_job_with_options_async(request, runtime)

    def submit_document_extract_job_advance(
        self,
        request: main_models.SubmitDocumentExtractJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentExtractJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_document_extract_job_req = main_models.SubmitDocumentExtractJobRequest()
        Utils.convert(request, submit_document_extract_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitDocumentExtractJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentExtractJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_document_extract_job_req = main_models.SubmitDocumentExtractJobRequest()
        Utils.convert(request, submit_document_extract_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitTableUnderstandingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTableUnderstandingJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTableUnderstandingJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTableUnderstandingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_table_understanding_job_with_options_async(
        self,
        request: main_models.SubmitTableUnderstandingJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTableUnderstandingJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTableUnderstandingJob',
            version = '2022-07-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTableUnderstandingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_table_understanding_job(
        self,
        request: main_models.SubmitTableUnderstandingJobRequest,
    ) -> main_models.SubmitTableUnderstandingJobResponse:
        runtime = RuntimeOptions()
        return self.submit_table_understanding_job_with_options(request, runtime)

    async def submit_table_understanding_job_async(
        self,
        request: main_models.SubmitTableUnderstandingJobRequest,
    ) -> main_models.SubmitTableUnderstandingJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_table_understanding_job_with_options_async(request, runtime)

    def submit_table_understanding_job_advance(
        self,
        request: main_models.SubmitTableUnderstandingJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTableUnderstandingJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_table_understanding_job_req = main_models.SubmitTableUnderstandingJobRequest()
        Utils.convert(request, submit_table_understanding_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
        request: main_models.SubmitTableUnderstandingJobAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTableUnderstandingJobResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'docmind-api',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        submit_table_understanding_job_req = main_models.SubmitTableUnderstandingJobRequest()
        Utils.convert(request, submit_table_understanding_job_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
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
