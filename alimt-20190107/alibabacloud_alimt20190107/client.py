# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alimt20190107 import models as alimt_20190107_models
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
        self._endpoint_map = {
            'cn-hangzhou': 'mt.cn-hangzhou.aliyuncs.com',
            'ap-northeast-1': 'mt.aliyuncs.com',
            'ap-northeast-2-pop': 'mt.aliyuncs.com',
            'ap-south-1': 'mt.aliyuncs.com',
            'ap-southeast-1': 'mt.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'mt.aliyuncs.com',
            'ap-southeast-3': 'mt.aliyuncs.com',
            'ap-southeast-5': 'mt.aliyuncs.com',
            'cn-beijing': 'mt.aliyuncs.com',
            'cn-beijing-finance-1': 'mt.aliyuncs.com',
            'cn-beijing-finance-pop': 'mt.aliyuncs.com',
            'cn-beijing-gov-1': 'mt.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mt.aliyuncs.com',
            'cn-chengdu': 'mt.aliyuncs.com',
            'cn-edge-1': 'mt.aliyuncs.com',
            'cn-fujian': 'mt.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mt.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mt.aliyuncs.com',
            'cn-hangzhou-finance': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mt.aliyuncs.com',
            'cn-hangzhou-test-306': 'mt.aliyuncs.com',
            'cn-hongkong': 'mt.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mt.aliyuncs.com',
            'cn-huhehaote': 'mt.aliyuncs.com',
            'cn-north-2-gov-1': 'mt.aliyuncs.com',
            'cn-qingdao': 'mt.aliyuncs.com',
            'cn-qingdao-nebula': 'mt.aliyuncs.com',
            'cn-shanghai': 'mt.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mt.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mt.aliyuncs.com',
            'cn-shanghai-finance-1': 'mt.aliyuncs.com',
            'cn-shanghai-inner': 'mt.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mt.aliyuncs.com',
            'cn-shenzhen': 'mt.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mt.aliyuncs.com',
            'cn-shenzhen-inner': 'mt.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mt.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mt.aliyuncs.com',
            'cn-wuhan': 'mt.aliyuncs.com',
            'cn-yushanfang': 'mt.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mt.aliyuncs.com',
            'cn-zhangjiakou': 'mt.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mt.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mt.aliyuncs.com',
            'eu-central-1': 'mt.aliyuncs.com',
            'eu-west-1': 'mt.aliyuncs.com',
            'eu-west-1-oxs': 'mt.aliyuncs.com',
            'me-east-1': 'mt.aliyuncs.com',
            'rus-west-1-pop': 'mt.aliyuncs.com',
            'us-east-1': 'mt.aliyuncs.com',
            'us-west-1': 'mt.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('alimt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def translate_ecommerce_with_options(
        self,
        request: alimt_20190107_models.TranslateECommerceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190107_models.TranslateECommerceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.format_type):
            query['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            query['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            query['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TranslateECommerce',
            version='2019-01-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190107_models.TranslateECommerceResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_ecommerce_with_options_async(
        self,
        request: alimt_20190107_models.TranslateECommerceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190107_models.TranslateECommerceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.format_type):
            query['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            query['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            query['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TranslateECommerce',
            version='2019-01-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190107_models.TranslateECommerceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_ecommerce(
        self,
        request: alimt_20190107_models.TranslateECommerceRequest,
    ) -> alimt_20190107_models.TranslateECommerceResponse:
        runtime = util_models.RuntimeOptions()
        return self.translate_ecommerce_with_options(request, runtime)

    async def translate_ecommerce_async(
        self,
        request: alimt_20190107_models.TranslateECommerceRequest,
    ) -> alimt_20190107_models.TranslateECommerceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.translate_ecommerce_with_options_async(request, runtime)

    def translate_general_with_options(
        self,
        request: alimt_20190107_models.TranslateGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190107_models.TranslateGeneralResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.format_type):
            query['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            query['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            query['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TranslateGeneral',
            version='2019-01-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190107_models.TranslateGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_general_with_options_async(
        self,
        request: alimt_20190107_models.TranslateGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190107_models.TranslateGeneralResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.format_type):
            query['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            query['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            query['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TranslateGeneral',
            version='2019-01-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190107_models.TranslateGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_general(
        self,
        request: alimt_20190107_models.TranslateGeneralRequest,
    ) -> alimt_20190107_models.TranslateGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.translate_general_with_options(request, runtime)

    async def translate_general_async(
        self,
        request: alimt_20190107_models.TranslateGeneralRequest,
    ) -> alimt_20190107_models.TranslateGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.translate_general_with_options_async(request, runtime)
