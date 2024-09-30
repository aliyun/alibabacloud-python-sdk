# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_docmind_api20220711 import models as docmind_api_20220711_models
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
        self._product_id = 'docmind-api'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.AyncTradeDocumentPackageExtractSmartAppResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocParserResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocParserResultResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocParserResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocParserResultResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocStructureResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocStructureResultResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocStructureResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocStructureResultResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentCompareResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentCompareResultResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentCompareResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentCompareResultResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentConvertResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentConvertResultResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentConvertResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentConvertResultResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentExtractResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentExtractResultResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentExtractResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetDocumentExtractResultResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetPageNumResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetPageNumResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetPageNumResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetPageNumResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetTableUnderstandingResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetTableUnderstandingResultResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.GetTableUnderstandingResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.GetTableUnderstandingResultResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.QueryDocParserStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.QueryDocParserStatusResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.QueryDocParserStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.QueryDocParserStatusResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToMarkdownJobResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToWordJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToWordJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToWordJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertImageToWordJobResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_convert_pdf_to_excel_job_req = docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_excel_job_req)
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
            submit_convert_pdf_to_excel_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_convert_pdf_to_excel_job_resp = self.submit_convert_pdf_to_excel_job_with_options(submit_convert_pdf_to_excel_job_req, runtime)
        return submit_convert_pdf_to_excel_job_resp

    async def submit_convert_pdf_to_excel_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToExcelJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse:
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
            product='docmind-api',
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
        submit_convert_pdf_to_excel_job_req = docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_excel_job_req)
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
            submit_convert_pdf_to_excel_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_convert_pdf_to_image_job_req = docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_image_job_req)
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
            submit_convert_pdf_to_image_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_convert_pdf_to_image_job_resp = self.submit_convert_pdf_to_image_job_with_options(submit_convert_pdf_to_image_job_req, runtime)
        return submit_convert_pdf_to_image_job_resp

    async def submit_convert_pdf_to_image_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToImageJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse:
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
            product='docmind-api',
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
        submit_convert_pdf_to_image_job_req = docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_image_job_req)
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
            submit_convert_pdf_to_image_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_convert_pdf_to_markdown_job_req = docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_markdown_job_req)
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
            submit_convert_pdf_to_markdown_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_convert_pdf_to_markdown_job_resp = self.submit_convert_pdf_to_markdown_job_with_options(submit_convert_pdf_to_markdown_job_req, runtime)
        return submit_convert_pdf_to_markdown_job_resp

    async def submit_convert_pdf_to_markdown_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobResponse:
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
            product='docmind-api',
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
        submit_convert_pdf_to_markdown_job_req = docmind_api_20220711_models.SubmitConvertPdfToMarkdownJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_markdown_job_req)
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
            submit_convert_pdf_to_markdown_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_convert_pdf_to_word_job_req = docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_word_job_req)
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
            submit_convert_pdf_to_word_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_convert_pdf_to_word_job_resp = self.submit_convert_pdf_to_word_job_with_options(submit_convert_pdf_to_word_job_req, runtime)
        return submit_convert_pdf_to_word_job_resp

    async def submit_convert_pdf_to_word_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitConvertPdfToWordJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse:
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
            product='docmind-api',
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
        submit_convert_pdf_to_word_job_req = docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_word_job_req)
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
            submit_convert_pdf_to_word_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_digital_doc_structure_job_req = docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_digital_doc_structure_job_req)
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
            submit_digital_doc_structure_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_digital_doc_structure_job_resp = self.submit_digital_doc_structure_job_with_options(submit_digital_doc_structure_job_req, runtime)
        return submit_digital_doc_structure_job_resp

    async def submit_digital_doc_structure_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDigitalDocStructureJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDigitalDocStructureJobResponse:
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
            product='docmind-api',
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
        submit_digital_doc_structure_job_req = docmind_api_20220711_models.SubmitDigitalDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_digital_doc_structure_job_req)
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
            submit_digital_doc_structure_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocParserJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocParserJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocParserJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocParserJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_doc_parser_job_req = docmind_api_20220711_models.SubmitDocParserJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_parser_job_req)
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
            submit_doc_parser_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_doc_parser_job_resp = self.submit_doc_parser_job_with_options(submit_doc_parser_job_req, runtime)
        return submit_doc_parser_job_resp

    async def submit_doc_parser_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDocParserJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocParserJobResponse:
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
            product='docmind-api',
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
        submit_doc_parser_job_req = docmind_api_20220711_models.SubmitDocParserJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_parser_job_req)
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
            submit_doc_parser_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocStructureJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocStructureJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocStructureJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocStructureJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_doc_structure_job_req = docmind_api_20220711_models.SubmitDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_structure_job_req)
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
            submit_doc_structure_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_doc_structure_job_resp = self.submit_doc_structure_job_with_options(submit_doc_structure_job_req, runtime)
        return submit_doc_structure_job_resp

    async def submit_doc_structure_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDocStructureJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocStructureJobResponse:
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
            product='docmind-api',
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
        submit_doc_structure_job_req = docmind_api_20220711_models.SubmitDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_structure_job_req)
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
            submit_doc_structure_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocumentExtractJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocumentExtractJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocumentExtractJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitDocumentExtractJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_document_extract_job_req = docmind_api_20220711_models.SubmitDocumentExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_document_extract_job_req)
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
            submit_document_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_document_extract_job_resp = self.submit_document_extract_job_with_options(submit_document_extract_job_req, runtime)
        return submit_document_extract_job_resp

    async def submit_document_extract_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitDocumentExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitDocumentExtractJobResponse:
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
            product='docmind-api',
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
        submit_document_extract_job_req = docmind_api_20220711_models.SubmitDocumentExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_document_extract_job_req)
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
            submit_document_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitTableUnderstandingJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitTableUnderstandingJobResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitTableUnderstandingJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                docmind_api_20220711_models.SubmitTableUnderstandingJobResponse(),
                await self.execute_async(params, req, runtime)
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
            product='docmind-api',
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
        submit_table_understanding_job_req = docmind_api_20220711_models.SubmitTableUnderstandingJobRequest()
        OpenApiUtilClient.convert(request, submit_table_understanding_job_req)
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
            submit_table_understanding_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_table_understanding_job_resp = self.submit_table_understanding_job_with_options(submit_table_understanding_job_req, runtime)
        return submit_table_understanding_job_resp

    async def submit_table_understanding_job_advance_async(
        self,
        request: docmind_api_20220711_models.SubmitTableUnderstandingJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220711_models.SubmitTableUnderstandingJobResponse:
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
            product='docmind-api',
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
        submit_table_understanding_job_req = docmind_api_20220711_models.SubmitTableUnderstandingJobRequest()
        OpenApiUtilClient.convert(request, submit_table_understanding_job_req)
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
            submit_table_understanding_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_table_understanding_job_resp = await self.submit_table_understanding_job_with_options_async(submit_table_understanding_job_req, runtime)
        return submit_table_understanding_job_resp
