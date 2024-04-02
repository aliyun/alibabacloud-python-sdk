# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20170823 import models as green_20170823_models
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
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def audit_item_submit_with_options(
        self,
        request: green_20170823_models.AuditItemSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.AuditItemSubmitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditItemSubmit',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.AuditItemSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    async def audit_item_submit_with_options_async(
        self,
        request: green_20170823_models.AuditItemSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.AuditItemSubmitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditItemSubmit',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.AuditItemSubmitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def audit_item_submit(
        self,
        request: green_20170823_models.AuditItemSubmitRequest,
    ) -> green_20170823_models.AuditItemSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return self.audit_item_submit_with_options(request, runtime)

    async def audit_item_submit_async(
        self,
        request: green_20170823_models.AuditItemSubmitRequest,
    ) -> green_20170823_models.AuditItemSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.audit_item_submit_with_options_async(request, runtime)

    def creat_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.img_url):
            query['ImgUrl'] = request.img_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recognize_area):
            query['RecognizeArea'] = request.recognize_area
        if not UtilClient.is_unset(request.refer_area):
            query['ReferArea'] = request.refer_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreatCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def creat_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.img_url):
            query['ImgUrl'] = request.img_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recognize_area):
            query['RecognizeArea'] = request.recognize_area
        if not UtilClient.is_unset(request.refer_area):
            query['ReferArea'] = request.refer_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreatCustomOcrTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def creat_custom_ocr_template(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.creat_custom_ocr_template_with_options(request, runtime)

    async def creat_custom_ocr_template_async(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.creat_custom_ocr_template_with_options_async(request, runtime)

    def create_audit_callback_with_options(
        self,
        request: green_20170823_models.CreateAuditCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateAuditCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_suggestions):
            query['CallbackSuggestions'] = request.callback_suggestions
        if not UtilClient.is_unset(request.callback_types):
            query['CallbackTypes'] = request.callback_types
        if not UtilClient.is_unset(request.crypt_type):
            query['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateAuditCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_audit_callback_with_options_async(
        self,
        request: green_20170823_models.CreateAuditCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateAuditCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_suggestions):
            query['CallbackSuggestions'] = request.callback_suggestions
        if not UtilClient.is_unset(request.callback_types):
            query['CallbackTypes'] = request.callback_types
        if not UtilClient.is_unset(request.crypt_type):
            query['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateAuditCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_audit_callback(
        self,
        request: green_20170823_models.CreateAuditCallbackRequest,
    ) -> green_20170823_models.CreateAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_audit_callback_with_options(request, runtime)

    async def create_audit_callback_async(
        self,
        request: green_20170823_models.CreateAuditCallbackRequest,
    ) -> green_20170823_models.CreateAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_audit_callback_with_options_async(request, runtime)

    def create_biz_type_with_options(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateBizTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_import):
            query['BizTypeImport'] = request.biz_type_import
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.cite_template):
            query['CiteTemplate'] = request.cite_template
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.industry_info):
            query['IndustryInfo'] = request.industry_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_type_with_options_async(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateBizTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_import):
            query['BizTypeImport'] = request.biz_type_import
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.cite_template):
            query['CiteTemplate'] = request.cite_template
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.industry_info):
            query['IndustryInfo'] = request.industry_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateBizTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_type(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
    ) -> green_20170823_models.CreateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_biz_type_with_options(request, runtime)

    async def create_biz_type_async(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
    ) -> green_20170823_models.CreateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_biz_type_with_options_async(request, runtime)

    def create_cdi_bag_with_options(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdiBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdi_bag_with_options_async(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdiBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdi_bag(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
    ) -> green_20170823_models.CreateCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdi_bag_with_options(request, runtime)

    async def create_cdi_bag_async(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
    ) -> green_20170823_models.CreateCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdi_bag_with_options_async(request, runtime)

    def create_cdi_base_bag_with_options(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBaseBagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdi_base_bag_with_options_async(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBaseBagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdi_base_bag(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdi_base_bag_with_options(request, runtime)

    async def create_cdi_base_bag_async(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdi_base_bag_with_options_async(request, runtime)

    def create_image_lib_with_options(
        self,
        request: green_20170823_models.CreateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_lib_with_options_async(
        self,
        request: green_20170823_models.CreateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_lib(
        self,
        request: green_20170823_models.CreateImageLibRequest,
    ) -> green_20170823_models.CreateImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_lib_with_options(request, runtime)

    async def create_image_lib_async(
        self,
        request: green_20170823_models.CreateImageLibRequest,
    ) -> green_20170823_models.CreateImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_lib_with_options_async(request, runtime)

    def create_keyword_with_options(
        self,
        request: green_20170823_models.CreateKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_keyword_with_options_async(
        self,
        request: green_20170823_models.CreateKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_keyword(
        self,
        request: green_20170823_models.CreateKeywordRequest,
    ) -> green_20170823_models.CreateKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_keyword_with_options(request, runtime)

    async def create_keyword_async(
        self,
        request: green_20170823_models.CreateKeywordRequest,
    ) -> green_20170823_models.CreateKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_keyword_with_options_async(request, runtime)

    def create_keyword_lib_with_options(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_keyword_lib(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_keyword_lib_with_options(request, runtime)

    async def create_keyword_lib_async(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_keyword_lib_with_options_async(request, runtime)

    def create_web_site_instance_with_options(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebSiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_site_instance_with_options_async(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebSiteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_site_instance(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_web_site_instance_with_options(request, runtime)

    async def create_web_site_instance_async(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_web_site_instance_with_options_async(request, runtime)

    def create_website_index_page_baseline_with_options(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebsiteIndexPageBaseline',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebsiteIndexPageBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_website_index_page_baseline_with_options_async(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebsiteIndexPageBaseline',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebsiteIndexPageBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_website_index_page_baseline(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_website_index_page_baseline_with_options(request, runtime)

    async def create_website_index_page_baseline_async(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_website_index_page_baseline_with_options_async(request, runtime)

    def delete_biz_type_with_options(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_type_with_options_async(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteBizTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_type(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_type_with_options(request, runtime)

    async def delete_biz_type_async(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_biz_type_with_options_async(request, runtime)

    def delete_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteCustomOcrTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_ocr_template(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_ocr_template_with_options(request, runtime)

    async def delete_custom_ocr_template_async(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_ocr_template_with_options_async(request, runtime)

    def delete_image_from_lib_with_options(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageFromLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_from_lib_with_options_async(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageFromLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageFromLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_from_lib(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_from_lib_with_options(request, runtime)

    async def delete_image_from_lib_async(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_from_lib_with_options_async(request, runtime)

    def delete_image_lib_with_options(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_lib_with_options_async(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_lib(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
    ) -> green_20170823_models.DeleteImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_lib_with_options(request, runtime)

    async def delete_image_lib_async(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
    ) -> green_20170823_models.DeleteImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_lib_with_options_async(request, runtime)

    def delete_keyword_with_options(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_keyword_with_options_async(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_keyword(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
    ) -> green_20170823_models.DeleteKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_with_options(request, runtime)

    async def delete_keyword_async(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
    ) -> green_20170823_models.DeleteKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_keyword_with_options_async(request, runtime)

    def delete_keyword_lib_with_options(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_keyword_lib(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_lib_with_options(request, runtime)

    async def delete_keyword_lib_async(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_keyword_lib_with_options_async(request, runtime)

    def delete_notification_contacts_with_options(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_types):
            query['ContactTypes'] = request.contact_types
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationContacts',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteNotificationContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_notification_contacts_with_options_async(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_types):
            query['ContactTypes'] = request.contact_types
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationContacts',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteNotificationContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_notification_contacts(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_contacts_with_options(request, runtime)

    async def delete_notification_contacts_async(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_notification_contacts_with_options_async(request, runtime)

    def describe_app_info_with_options(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_info_with_options_async(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_info(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info_with_options(request, runtime)

    async def describe_app_info_async(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_info_with_options_async(request, runtime)

    def describe_audit_callback_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditCallbackResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_callback_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditCallbackResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_callback(self) -> green_20170823_models.DescribeAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_callback_with_options(runtime)

    async def describe_audit_callback_async(self) -> green_20170823_models.DescribeAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_callback_with_options_async(runtime)

    def describe_audit_callback_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditCallbackListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditCallbackList',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_callback_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditCallbackListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditCallbackList',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_callback_list(self) -> green_20170823_models.DescribeAuditCallbackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_callback_list_with_options(runtime)

    async def describe_audit_callback_list_async(self) -> green_20170823_models.DescribeAuditCallbackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_callback_list_with_options_async(runtime)

    def describe_audit_content_with_options(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keyword_id):
            query['KeywordId'] = request.keyword_id
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_content_with_options_async(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keyword_id):
            query['KeywordId'] = request.keyword_id
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_content(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_content_with_options(request, runtime)

    async def describe_audit_content_async(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_content_with_options_async(request, runtime)

    def describe_audit_content_item_with_options(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditContentItem',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_content_item_with_options_async(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditContentItem',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_content_item(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_content_item_with_options(request, runtime)

    async def describe_audit_content_item_async(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_content_item_with_options_async(request, runtime)

    def describe_audit_range_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditRangeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditRange',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_range_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditRangeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditRange',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_range(self) -> green_20170823_models.DescribeAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_range_with_options(runtime)

    async def describe_audit_range_async(self) -> green_20170823_models.DescribeAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_range_with_options_async(runtime)

    def describe_audit_setting_with_options(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_setting(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_setting_with_options(request, runtime)

    async def describe_audit_setting_async(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_setting_with_options_async(request, runtime)

    def describe_biz_type_image_lib_with_options(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_biz_type_image_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_biz_type_image_lib(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_image_lib_with_options(request, runtime)

    async def describe_biz_type_image_lib_async(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_type_image_lib_with_options_async(request, runtime)

    def describe_biz_type_setting_with_options(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_biz_type_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_biz_type_setting(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_setting_with_options(request, runtime)

    async def describe_biz_type_setting_async(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_type_setting_with_options_async(request, runtime)

    def describe_biz_type_text_lib_with_options(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeTextLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeTextLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_biz_type_text_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeTextLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeTextLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_biz_type_text_lib(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_text_lib_with_options(request, runtime)

    async def describe_biz_type_text_lib_async(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_type_text_lib_with_options_async(request, runtime)

    def describe_biz_types_with_options(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.import_flag):
            query['ImportFlag'] = request.import_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypes',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_biz_types_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.import_flag):
            query['ImportFlag'] = request.import_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypes',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_biz_types(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_types_with_options(request, runtime)

    async def describe_biz_types_async(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_types_with_options_async(request, runtime)

    def describe_cloud_monitor_services_with_options(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudMonitorServices',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCloudMonitorServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_monitor_services_with_options_async(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudMonitorServices',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCloudMonitorServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_monitor_services(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_monitor_services_with_options(request, runtime)

    async def describe_cloud_monitor_services_async(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_monitor_services_with_options_async(request, runtime)

    def describe_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCustomOcrTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_ocr_template(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_ocr_template_with_options(request, runtime)

    async def describe_custom_ocr_template_async(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_ocr_template_with_options_async(request, runtime)

    def describe_image_from_lib_with_options(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image_lib_id):
            query['ImageLibId'] = request.image_lib_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFromLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_from_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image_lib_id):
            query['ImageLibId'] = request.image_lib_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFromLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageFromLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_from_lib(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_from_lib_with_options(request, runtime)

    async def describe_image_from_lib_async(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_from_lib_with_options_async(request, runtime)

    def describe_image_lib_with_options(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_lib(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
    ) -> green_20170823_models.DescribeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_lib_with_options(request, runtime)

    async def describe_image_lib_async(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
    ) -> green_20170823_models.DescribeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_lib_with_options_async(request, runtime)

    def describe_image_upload_info_with_options(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageUploadInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_upload_info_with_options_async(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageUploadInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageUploadInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_upload_info(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_upload_info_with_options(request, runtime)

    async def describe_image_upload_info_async(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_upload_info_with_options_async(request, runtime)

    def describe_keyword_with_options(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_keyword_with_options_async(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_keyword(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
    ) -> green_20170823_models.DescribeKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_keyword_with_options(request, runtime)

    async def describe_keyword_async(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
    ) -> green_20170823_models.DescribeKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_keyword_with_options_async(request, runtime)

    def describe_keyword_lib_with_options(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_keyword_lib(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_keyword_lib_with_options(request, runtime)

    async def describe_keyword_lib_async(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_keyword_lib_with_options_async(request, runtime)

    def describe_notification_setting_with_options(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeNotificationSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notification_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeNotificationSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notification_setting(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_setting_with_options(request, runtime)

    async def describe_notification_setting_async(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_setting_with_options_async(request, runtime)

    def describe_open_api_rcp_stats_with_options(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiRcpStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiRcpStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_open_api_rcp_stats_with_options_async(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiRcpStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiRcpStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_open_api_rcp_stats(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_rcp_stats_with_options(request, runtime)

    async def describe_open_api_rcp_stats_async(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_api_rcp_stats_with_options_async(request, runtime)

    def describe_open_api_usage_with_options(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiUsage',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_open_api_usage_with_options_async(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiUsage',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_open_api_usage(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_usage_with_options(request, runtime)

    async def describe_open_api_usage_async(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_api_usage_with_options_async(request, runtime)

    def describe_oss_callback_setting_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssCallbackSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssCallbackSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_callback_setting_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssCallbackSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssCallbackSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_callback_setting(self) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_callback_setting_with_options(runtime)

    async def describe_oss_callback_setting_async(self) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_callback_setting_with_options_async(runtime)

    def describe_oss_increment_check_setting_with_options(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementCheckSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementCheckSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_increment_check_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementCheckSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementCheckSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_increment_check_setting(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_check_setting_with_options(request, runtime)

    async def describe_oss_increment_check_setting_async(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_increment_check_setting_with_options_async(request, runtime)

    def describe_oss_increment_overview_with_options(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementOverview',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_increment_overview_with_options_async(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementOverview',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_increment_overview(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_overview_with_options(request, runtime)

    async def describe_oss_increment_overview_async(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_increment_overview_with_options_async(request, runtime)

    def describe_oss_increment_stats_with_options(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_increment_stats_with_options_async(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_increment_stats(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_stats_with_options(request, runtime)

    async def describe_oss_increment_stats_async(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_increment_stats_with_options_async(request, runtime)

    def describe_oss_result_items_with_options(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_score):
            query['MaxScore'] = request.max_score
        if not UtilClient.is_unset(request.min_score):
            query['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.object):
            query['Object'] = request.object
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssResultItems',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssResultItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_result_items_with_options_async(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_score):
            query['MaxScore'] = request.max_score
        if not UtilClient.is_unset(request.min_score):
            query['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.object):
            query['Object'] = request.object
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssResultItems',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssResultItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_result_items(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_result_items_with_options(request, runtime)

    async def describe_oss_result_items_async(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_result_items_with_options_async(request, runtime)

    def describe_oss_stock_status_with_options(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssStockStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssStockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_stock_status_with_options_async(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssStockStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssStockStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_stock_status(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_stock_status_with_options(request, runtime)

    async def describe_oss_stock_status_async(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_stock_status_with_options_async(request, runtime)

    def describe_sdk_url_with_options(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSdkUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeSdkUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdk_url_with_options_async(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSdkUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeSdkUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdk_url(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url_with_options(request, runtime)

    async def describe_sdk_url_async(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdk_url_with_options_async(request, runtime)

    def describe_update_package_result_with_options(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpdatePackageResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUpdatePackageResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_update_package_result_with_options_async(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpdatePackageResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUpdatePackageResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_update_package_result(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result_with_options(request, runtime)

    async def describe_update_package_result_async(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_update_package_result_with_options_async(request, runtime)

    def describe_upload_info_with_options(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUploadInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_upload_info_with_options_async(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUploadInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUploadInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_upload_info(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info_with_options(request, runtime)

    async def describe_upload_info_async(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upload_info_with_options_async(request, runtime)

    def describe_usage_bill_with_options(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageBill',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUsageBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_bill_with_options_async(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageBill',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUsageBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_bill(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_bill_with_options(request, runtime)

    async def describe_usage_bill_async(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_usage_bill_with_options_async(request, runtime)

    def describe_user_biz_types_with_options(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customized):
            query['Customized'] = request.customized
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBizTypes',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserBizTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_biz_types_with_options_async(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customized):
            query['Customized'] = request.customized
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBizTypes',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserBizTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_biz_types(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_biz_types_with_options(request, runtime)

    async def describe_user_biz_types_async(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_biz_types_with_options_async(request, runtime)

    def describe_user_status_with_options(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_status_with_options_async(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_status(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(request, runtime)

    async def describe_user_status_async(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_status_with_options_async(request, runtime)

    def describe_view_content_with_options(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeViewContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.keyword_id):
            query['KeywordId'] = request.keyword_id
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeViewContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeViewContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_view_content_with_options_async(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeViewContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.keyword_id):
            query['KeywordId'] = request.keyword_id
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeViewContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeViewContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_view_content(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
    ) -> green_20170823_models.DescribeViewContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_view_content_with_options(request, runtime)

    async def describe_view_content_async(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
    ) -> green_20170823_models.DescribeViewContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_view_content_with_options_async(request, runtime)

    def describe_website_index_page_baseline_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteIndexPageBaseline',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteIndexPageBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_index_page_baseline_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteIndexPageBaseline',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteIndexPageBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_index_page_baseline(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_index_page_baseline_with_options(request, runtime)

    async def describe_website_index_page_baseline_async(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_index_page_baseline_with_options_async(request, runtime)

    def describe_website_instance_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_instance_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_instance(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_with_options(request, runtime)

    async def describe_website_instance_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_instance_with_options_async(request, runtime)

    def describe_website_instance_id_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstanceId',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_instance_id_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstanceId',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_instance_id(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_id_with_options(request, runtime)

    async def describe_website_instance_id_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_instance_id_with_options_async(request, runtime)

    def describe_website_instance_key_url_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstanceKeyUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_instance_key_url_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstanceKeyUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_instance_key_url(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_key_url_with_options(request, runtime)

    async def describe_website_instance_key_url_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_instance_key_url_with_options_async(request, runtime)

    def describe_website_scan_result_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.handle_status):
            query['HandleStatus'] = request.handle_status
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.site_url):
            query['SiteUrl'] = request.site_url
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.sub_service_module):
            query['SubServiceModule'] = request.sub_service_module
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteScanResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_scan_result_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.handle_status):
            query['HandleStatus'] = request.handle_status
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.site_url):
            query['SiteUrl'] = request.site_url
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.sub_service_module):
            query['SubServiceModule'] = request.sub_service_module
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteScanResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_scan_result(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_scan_result_with_options(request, runtime)

    async def describe_website_scan_result_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_scan_result_with_options_async(request, runtime)

    def describe_website_scan_result_detail_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteScanResultDetail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_scan_result_detail_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteScanResultDetail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_scan_result_detail(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_scan_result_detail_with_options(request, runtime)

    async def describe_website_scan_result_detail_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_scan_result_detail_with_options_async(request, runtime)

    def describe_website_stat_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteStat',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_stat_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteStat',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_stat(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_stat_with_options(request, runtime)

    async def describe_website_stat_async(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_stat_with_options_async(request, runtime)

    def describe_website_verify_info_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteVerifyInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteVerifyInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_website_verify_info_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteVerifyInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteVerifyInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_website_verify_info(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_verify_info_with_options(request, runtime)

    async def describe_website_verify_info_async(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_verify_info_with_options_async(request, runtime)

    def export_keywords_with_options(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportKeywordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportKeywords',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_keywords_with_options_async(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportKeywordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportKeywords',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportKeywordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_keywords(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
    ) -> green_20170823_models.ExportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_keywords_with_options(request, runtime)

    async def export_keywords_async(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
    ) -> green_20170823_models.ExportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_keywords_with_options_async(request, runtime)

    def export_open_api_rcp_stats_with_options(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportOpenApiRcpStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOpenApiRcpStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_open_api_rcp_stats_with_options_async(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportOpenApiRcpStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOpenApiRcpStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_open_api_rcp_stats(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_open_api_rcp_stats_with_options(request, runtime)

    async def export_open_api_rcp_stats_async(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_open_api_rcp_stats_with_options_async(request, runtime)

    def export_oss_result_with_options(
        self,
        request: green_20170823_models.ExportOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOssResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_score):
            query['MaxScore'] = request.max_score
        if not UtilClient.is_unset(request.min_score):
            query['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportOssResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOssResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_oss_result_with_options_async(
        self,
        request: green_20170823_models.ExportOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOssResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_score):
            query['MaxScore'] = request.max_score
        if not UtilClient.is_unset(request.min_score):
            query['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportOssResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOssResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_oss_result(
        self,
        request: green_20170823_models.ExportOssResultRequest,
    ) -> green_20170823_models.ExportOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_oss_result_with_options(request, runtime)

    async def export_oss_result_async(
        self,
        request: green_20170823_models.ExportOssResultRequest,
    ) -> green_20170823_models.ExportOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_oss_result_with_options_async(request, runtime)

    def get_audit_item_detail_with_options(
        self,
        request: green_20170823_models.GetAuditItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.GetAuditItemDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditItemDetail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditItemDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_item_detail_with_options_async(
        self,
        request: green_20170823_models.GetAuditItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.GetAuditItemDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditItemDetail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditItemDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_item_detail(
        self,
        request: green_20170823_models.GetAuditItemDetailRequest,
    ) -> green_20170823_models.GetAuditItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audit_item_detail_with_options(request, runtime)

    async def get_audit_item_detail_async(
        self,
        request: green_20170823_models.GetAuditItemDetailRequest,
    ) -> green_20170823_models.GetAuditItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_item_detail_with_options_async(request, runtime)

    def get_audit_item_list_with_options(
        self,
        request: green_20170823_models.GetAuditItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.GetAuditItemListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditItemList',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_item_list_with_options_async(
        self,
        request: green_20170823_models.GetAuditItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.GetAuditItemListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditItemList',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_item_list(
        self,
        request: green_20170823_models.GetAuditItemListRequest,
    ) -> green_20170823_models.GetAuditItemListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audit_item_list_with_options(request, runtime)

    async def get_audit_item_list_async(
        self,
        request: green_20170823_models.GetAuditItemListRequest,
    ) -> green_20170823_models.GetAuditItemListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_item_list_with_options_async(request, runtime)

    def get_audit_user_conf_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.GetAuditUserConfResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAuditUserConf',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditUserConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_user_conf_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.GetAuditUserConfResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAuditUserConf',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditUserConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_user_conf(self) -> green_20170823_models.GetAuditUserConfResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audit_user_conf_with_options(runtime)

    async def get_audit_user_conf_async(self) -> green_20170823_models.GetAuditUserConfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_user_conf_with_options_async(runtime)

    def import_keywords_with_options(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ImportKeywordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords_object):
            query['KeywordsObject'] = request.keywords_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeywords',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ImportKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_keywords_with_options_async(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ImportKeywordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords_object):
            query['KeywordsObject'] = request.keywords_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeywords',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ImportKeywordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_keywords(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
    ) -> green_20170823_models.ImportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_keywords_with_options(request, runtime)

    async def import_keywords_async(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
    ) -> green_20170823_models.ImportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_keywords_with_options_async(request, runtime)

    def mark_audit_content_with_options(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_illegal_reasons):
            query['AuditIllegalReasons'] = request.audit_illegal_reasons
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkAuditContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def mark_audit_content_with_options_async(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_illegal_reasons):
            query['AuditIllegalReasons'] = request.audit_illegal_reasons
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkAuditContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mark_audit_content(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
    ) -> green_20170823_models.MarkAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_audit_content_with_options(request, runtime)

    async def mark_audit_content_async(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
    ) -> green_20170823_models.MarkAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_audit_content_with_options_async(request, runtime)

    def mark_audit_content_item_with_options(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_illegal_reasons):
            query['AuditIllegalReasons'] = request.audit_illegal_reasons
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkAuditContentItem',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def mark_audit_content_item_with_options_async(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_illegal_reasons):
            query['AuditIllegalReasons'] = request.audit_illegal_reasons
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkAuditContentItem',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mark_audit_content_item(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_audit_content_item_with_options(request, runtime)

    async def mark_audit_content_item_async(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_audit_content_item_with_options_async(request, runtime)

    def mark_oss_result_with_options(
        self,
        request: green_20170823_models.MarkOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkOssResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkOssResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkOssResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def mark_oss_result_with_options_async(
        self,
        request: green_20170823_models.MarkOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkOssResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkOssResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkOssResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mark_oss_result(
        self,
        request: green_20170823_models.MarkOssResultRequest,
    ) -> green_20170823_models.MarkOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_oss_result_with_options(request, runtime)

    async def mark_oss_result_async(
        self,
        request: green_20170823_models.MarkOssResultRequest,
    ) -> green_20170823_models.MarkOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_oss_result_with_options_async(request, runtime)

    def mark_website_scan_result_with_options(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkWebsiteScanResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkWebsiteScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def mark_website_scan_result_with_options_async(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkWebsiteScanResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkWebsiteScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mark_website_scan_result(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_website_scan_result_with_options(request, runtime)

    async def mark_website_scan_result_async(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_website_scan_result_with_options_async(request, runtime)

    def refund_cdi_bag_with_options(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundCdiBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBagResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_cdi_bag_with_options_async(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundCdiBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_cdi_bag(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
    ) -> green_20170823_models.RefundCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_cdi_bag_with_options(request, runtime)

    async def refund_cdi_bag_async(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
    ) -> green_20170823_models.RefundCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_cdi_bag_with_options_async(request, runtime)

    def refund_cdi_base_bag_with_options(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBaseBagResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_cdi_base_bag_with_options_async(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBaseBagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_cdi_base_bag(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_cdi_base_bag_with_options(request, runtime)

    async def refund_cdi_base_bag_async(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_cdi_base_bag_with_options_async(request, runtime)

    def refund_web_site_instance_with_options(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundWebSiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_web_site_instance_with_options_async(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundWebSiteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_web_site_instance(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_web_site_instance_with_options(request, runtime)

    async def refund_web_site_instance_async(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_web_site_instance_with_options_async(request, runtime)

    def renew_web_site_instance_with_options(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RenewWebSiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_web_site_instance_with_options_async(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RenewWebSiteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_web_site_instance(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_web_site_instance_with_options(request, runtime)

    async def renew_web_site_instance_async(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_web_site_instance_with_options_async(request, runtime)

    def send_verify_code_to_email_with_options(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCodeToEmail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verify_code_to_email_with_options_async(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCodeToEmail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verify_code_to_email(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_to_email_with_options(request, runtime)

    async def send_verify_code_to_email_async(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verify_code_to_email_with_options_async(request, runtime)

    def send_verify_code_to_phone_with_options(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCodeToPhone',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verify_code_to_phone_with_options_async(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCodeToPhone',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verify_code_to_phone(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_to_phone_with_options(request, runtime)

    async def send_verify_code_to_phone_async(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verify_code_to_phone_with_options_async(request, runtime)

    def send_website_feedback_with_options(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendWebsiteFeedback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendWebsiteFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_website_feedback_with_options_async(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendWebsiteFeedback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendWebsiteFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_website_feedback(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_website_feedback_with_options(request, runtime)

    async def send_website_feedback_async(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_website_feedback_with_options_async(request, runtime)

    def update_app_package_with_options(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppPackage',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAppPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_package_with_options_async(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppPackage',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAppPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_package(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_package_with_options(request, runtime)

    async def update_app_package_async(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_package_with_options_async(request, runtime)

    def update_audit_callback_with_options(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.crypt_type):
            query['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.seed):
            query['Seed'] = request.seed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_audit_callback_with_options_async(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.crypt_type):
            query['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.seed):
            query['Seed'] = request.seed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_audit_callback(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_audit_callback_with_options(request, runtime)

    async def update_audit_callback_async(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_audit_callback_with_options_async(request, runtime)

    def update_audit_range_with_options(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_range):
            query['AuditRange'] = request.audit_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditRange',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_audit_range_with_options_async(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_range):
            query['AuditRange'] = request.audit_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditRange',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_audit_range(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_audit_range_with_options(request, runtime)

    async def update_audit_range_async(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_audit_range_with_options_async(request, runtime)

    def update_audit_setting_with_options(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_range):
            query['AuditRange'] = request.audit_range
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.seed):
            query['Seed'] = request.seed
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_audit_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_range):
            query['AuditRange'] = request.audit_range
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.seed):
            query['Seed'] = request.seed
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_audit_setting(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_audit_setting_with_options(request, runtime)

    async def update_audit_setting_async(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_audit_setting_with_options_async(request, runtime)

    def update_biz_type_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_type_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_type(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_with_options(request, runtime)

    async def update_biz_type_async(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_with_options_async(request, runtime)

    def update_biz_type_image_lib_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.black):
            query['Black'] = request.black
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.review):
            query['Review'] = request.review
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.white):
            query['White'] = request.white
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_type_image_lib_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.black):
            query['Black'] = request.black
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.review):
            query['Review'] = request.review
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.white):
            query['White'] = request.white
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_type_image_lib(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_image_lib_with_options(request, runtime)

    async def update_biz_type_image_lib_async(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_image_lib_with_options_async(request, runtime)

    def update_biz_type_setting_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad):
            query['Ad'] = request.ad
        if not UtilClient.is_unset(request.antispam):
            query['Antispam'] = request.antispam
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.live):
            query['Live'] = request.live
        if not UtilClient.is_unset(request.porn):
            query['Porn'] = request.porn
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.terrorism):
            query['Terrorism'] = request.terrorism
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_type_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad):
            query['Ad'] = request.ad
        if not UtilClient.is_unset(request.antispam):
            query['Antispam'] = request.antispam
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.live):
            query['Live'] = request.live
        if not UtilClient.is_unset(request.porn):
            query['Porn'] = request.porn
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.terrorism):
            query['Terrorism'] = request.terrorism
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_type_setting(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_setting_with_options(request, runtime)

    async def update_biz_type_setting_async(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_setting_with_options_async(request, runtime)

    def update_biz_type_text_lib_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.black):
            query['Black'] = request.black
        if not UtilClient.is_unset(request.ignore):
            query['Ignore'] = request.ignore
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.review):
            query['Review'] = request.review
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.white):
            query['White'] = request.white
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeTextLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeTextLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_type_text_lib_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.black):
            query['Black'] = request.black
        if not UtilClient.is_unset(request.ignore):
            query['Ignore'] = request.ignore
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.review):
            query['Review'] = request.review
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.white):
            query['White'] = request.white
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeTextLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeTextLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_type_text_lib(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_text_lib_with_options(request, runtime)

    async def update_biz_type_text_lib_async(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_text_lib_with_options_async(request, runtime)

    def update_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recognize_area):
            query['RecognizeArea'] = request.recognize_area
        if not UtilClient.is_unset(request.refer_area):
            query['ReferArea'] = request.refer_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recognize_area):
            query['RecognizeArea'] = request.recognize_area
        if not UtilClient.is_unset(request.refer_area):
            query['ReferArea'] = request.refer_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateCustomOcrTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_ocr_template(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_custom_ocr_template_with_options(request, runtime)

    async def update_custom_ocr_template_async(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_ocr_template_with_options_async(request, runtime)

    def update_keyword_lib_with_options(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_keyword_lib(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_keyword_lib_with_options(request, runtime)

    async def update_keyword_lib_async(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_keyword_lib_with_options_async(request, runtime)

    def update_notification_setting_with_options(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.realtime_message_list):
            query['RealtimeMessageList'] = request.realtime_message_list
        if not UtilClient.is_unset(request.reminder_mode_list):
            query['ReminderModeList'] = request.reminder_mode_list
        if not UtilClient.is_unset(request.schedule_message_time):
            query['ScheduleMessageTime'] = request.schedule_message_time
        if not UtilClient.is_unset(request.schedule_message_time_zone):
            query['ScheduleMessageTimeZone'] = request.schedule_message_time_zone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNotificationSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateNotificationSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_notification_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.realtime_message_list):
            query['RealtimeMessageList'] = request.realtime_message_list
        if not UtilClient.is_unset(request.reminder_mode_list):
            query['ReminderModeList'] = request.reminder_mode_list
        if not UtilClient.is_unset(request.schedule_message_time):
            query['ScheduleMessageTime'] = request.schedule_message_time
        if not UtilClient.is_unset(request.schedule_message_time_zone):
            query['ScheduleMessageTimeZone'] = request.schedule_message_time_zone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNotificationSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateNotificationSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_notification_setting(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_notification_setting_with_options(request, runtime)

    async def update_notification_setting_async(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_notification_setting_with_options_async(request, runtime)

    def update_oss_callback_setting_with_options(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_callback):
            query['AuditCallback'] = request.audit_callback
        if not UtilClient.is_unset(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.scan_callback):
            query['ScanCallback'] = request.scan_callback
        if not UtilClient.is_unset(request.scan_callback_suggestions):
            query['ScanCallbackSuggestions'] = request.scan_callback_suggestions
        if not UtilClient.is_unset(request.service_modules):
            query['ServiceModules'] = request.service_modules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssCallbackSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssCallbackSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_callback_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_callback):
            query['AuditCallback'] = request.audit_callback
        if not UtilClient.is_unset(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.scan_callback):
            query['ScanCallback'] = request.scan_callback
        if not UtilClient.is_unset(request.scan_callback_suggestions):
            query['ScanCallbackSuggestions'] = request.scan_callback_suggestions
        if not UtilClient.is_unset(request.service_modules):
            query['ServiceModules'] = request.service_modules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssCallbackSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssCallbackSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_callback_setting(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_oss_callback_setting_with_options(request, runtime)

    async def update_oss_callback_setting_async(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_oss_callback_setting_with_options_async(request, runtime)

    def update_oss_increment_check_setting_with_options(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_antispam_freeze_config):
            query['AudioAntispamFreezeConfig'] = request.audio_antispam_freeze_config
        if not UtilClient.is_unset(request.audio_auto_freeze_opened):
            query['AudioAutoFreezeOpened'] = request.audio_auto_freeze_opened
        if not UtilClient.is_unset(request.audio_max_size):
            query['AudioMaxSize'] = request.audio_max_size
        if not UtilClient.is_unset(request.audio_scan_limit):
            query['AudioScanLimit'] = request.audio_scan_limit
        if not UtilClient.is_unset(request.audio_scene_list):
            query['AudioSceneList'] = request.audio_scene_list
        if not UtilClient.is_unset(request.auto_freeze_type):
            query['AutoFreezeType'] = request.auto_freeze_type
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.bucket_config_list):
            query['BucketConfigList'] = request.bucket_config_list
        if not UtilClient.is_unset(request.callback_id):
            query['CallbackId'] = request.callback_id
        if not UtilClient.is_unset(request.image_ad_freeze_config):
            query['ImageAdFreezeConfig'] = request.image_ad_freeze_config
        if not UtilClient.is_unset(request.image_auto_freeze):
            query['ImageAutoFreeze'] = request.image_auto_freeze
        if not UtilClient.is_unset(request.image_auto_freeze_opened):
            query['ImageAutoFreezeOpened'] = request.image_auto_freeze_opened
        if not UtilClient.is_unset(request.image_live_freeze_config):
            query['ImageLiveFreezeConfig'] = request.image_live_freeze_config
        if not UtilClient.is_unset(request.image_porn_freeze_config):
            query['ImagePornFreezeConfig'] = request.image_porn_freeze_config
        if not UtilClient.is_unset(request.image_scan_limit):
            query['ImageScanLimit'] = request.image_scan_limit
        if not UtilClient.is_unset(request.image_scene_list):
            query['ImageSceneList'] = request.image_scene_list
        if not UtilClient.is_unset(request.image_terrorism_freeze_config):
            query['ImageTerrorismFreezeConfig'] = request.image_terrorism_freeze_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.scan_image_no_file_type):
            query['ScanImageNoFileType'] = request.scan_image_no_file_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.video_ad_freeze_config):
            query['VideoAdFreezeConfig'] = request.video_ad_freeze_config
        if not UtilClient.is_unset(request.video_auto_freeze_opened):
            query['VideoAutoFreezeOpened'] = request.video_auto_freeze_opened
        if not UtilClient.is_unset(request.video_auto_freeze_scene_list):
            query['VideoAutoFreezeSceneList'] = request.video_auto_freeze_scene_list
        if not UtilClient.is_unset(request.video_frame_interval):
            query['VideoFrameInterval'] = request.video_frame_interval
        if not UtilClient.is_unset(request.video_live_freeze_config):
            query['VideoLiveFreezeConfig'] = request.video_live_freeze_config
        if not UtilClient.is_unset(request.video_max_frames):
            query['VideoMaxFrames'] = request.video_max_frames
        if not UtilClient.is_unset(request.video_max_size):
            query['VideoMaxSize'] = request.video_max_size
        if not UtilClient.is_unset(request.video_porn_freeze_config):
            query['VideoPornFreezeConfig'] = request.video_porn_freeze_config
        if not UtilClient.is_unset(request.video_scan_limit):
            query['VideoScanLimit'] = request.video_scan_limit
        if not UtilClient.is_unset(request.video_scene_list):
            query['VideoSceneList'] = request.video_scene_list
        if not UtilClient.is_unset(request.video_terrorism_freeze_config):
            query['VideoTerrorismFreezeConfig'] = request.video_terrorism_freeze_config
        if not UtilClient.is_unset(request.video_voice_antispam_freeze_config):
            query['VideoVoiceAntispamFreezeConfig'] = request.video_voice_antispam_freeze_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssIncrementCheckSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssIncrementCheckSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_increment_check_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_antispam_freeze_config):
            query['AudioAntispamFreezeConfig'] = request.audio_antispam_freeze_config
        if not UtilClient.is_unset(request.audio_auto_freeze_opened):
            query['AudioAutoFreezeOpened'] = request.audio_auto_freeze_opened
        if not UtilClient.is_unset(request.audio_max_size):
            query['AudioMaxSize'] = request.audio_max_size
        if not UtilClient.is_unset(request.audio_scan_limit):
            query['AudioScanLimit'] = request.audio_scan_limit
        if not UtilClient.is_unset(request.audio_scene_list):
            query['AudioSceneList'] = request.audio_scene_list
        if not UtilClient.is_unset(request.auto_freeze_type):
            query['AutoFreezeType'] = request.auto_freeze_type
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.bucket_config_list):
            query['BucketConfigList'] = request.bucket_config_list
        if not UtilClient.is_unset(request.callback_id):
            query['CallbackId'] = request.callback_id
        if not UtilClient.is_unset(request.image_ad_freeze_config):
            query['ImageAdFreezeConfig'] = request.image_ad_freeze_config
        if not UtilClient.is_unset(request.image_auto_freeze):
            query['ImageAutoFreeze'] = request.image_auto_freeze
        if not UtilClient.is_unset(request.image_auto_freeze_opened):
            query['ImageAutoFreezeOpened'] = request.image_auto_freeze_opened
        if not UtilClient.is_unset(request.image_live_freeze_config):
            query['ImageLiveFreezeConfig'] = request.image_live_freeze_config
        if not UtilClient.is_unset(request.image_porn_freeze_config):
            query['ImagePornFreezeConfig'] = request.image_porn_freeze_config
        if not UtilClient.is_unset(request.image_scan_limit):
            query['ImageScanLimit'] = request.image_scan_limit
        if not UtilClient.is_unset(request.image_scene_list):
            query['ImageSceneList'] = request.image_scene_list
        if not UtilClient.is_unset(request.image_terrorism_freeze_config):
            query['ImageTerrorismFreezeConfig'] = request.image_terrorism_freeze_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.scan_image_no_file_type):
            query['ScanImageNoFileType'] = request.scan_image_no_file_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.video_ad_freeze_config):
            query['VideoAdFreezeConfig'] = request.video_ad_freeze_config
        if not UtilClient.is_unset(request.video_auto_freeze_opened):
            query['VideoAutoFreezeOpened'] = request.video_auto_freeze_opened
        if not UtilClient.is_unset(request.video_auto_freeze_scene_list):
            query['VideoAutoFreezeSceneList'] = request.video_auto_freeze_scene_list
        if not UtilClient.is_unset(request.video_frame_interval):
            query['VideoFrameInterval'] = request.video_frame_interval
        if not UtilClient.is_unset(request.video_live_freeze_config):
            query['VideoLiveFreezeConfig'] = request.video_live_freeze_config
        if not UtilClient.is_unset(request.video_max_frames):
            query['VideoMaxFrames'] = request.video_max_frames
        if not UtilClient.is_unset(request.video_max_size):
            query['VideoMaxSize'] = request.video_max_size
        if not UtilClient.is_unset(request.video_porn_freeze_config):
            query['VideoPornFreezeConfig'] = request.video_porn_freeze_config
        if not UtilClient.is_unset(request.video_scan_limit):
            query['VideoScanLimit'] = request.video_scan_limit
        if not UtilClient.is_unset(request.video_scene_list):
            query['VideoSceneList'] = request.video_scene_list
        if not UtilClient.is_unset(request.video_terrorism_freeze_config):
            query['VideoTerrorismFreezeConfig'] = request.video_terrorism_freeze_config
        if not UtilClient.is_unset(request.video_voice_antispam_freeze_config):
            query['VideoVoiceAntispamFreezeConfig'] = request.video_voice_antispam_freeze_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssIncrementCheckSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssIncrementCheckSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_increment_check_setting(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_oss_increment_check_setting_with_options(request, runtime)

    async def update_oss_increment_check_setting_async(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_oss_increment_check_setting_with_options_async(request, runtime)

    def update_oss_stock_status_with_options(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_auto_freeze_scene_list):
            query['AudioAutoFreezeSceneList'] = request.audio_auto_freeze_scene_list
        if not UtilClient.is_unset(request.audio_max_size):
            query['AudioMaxSize'] = request.audio_max_size
        if not UtilClient.is_unset(request.auto_freeze_type):
            query['AutoFreezeType'] = request.auto_freeze_type
        if not UtilClient.is_unset(request.bucket_config_list):
            query['BucketConfigList'] = request.bucket_config_list
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_auto_freeze):
            query['ImageAutoFreeze'] = request.image_auto_freeze
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.scene_list):
            query['SceneList'] = request.scene_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.video_auto_freeze_scene_list):
            query['VideoAutoFreezeSceneList'] = request.video_auto_freeze_scene_list
        if not UtilClient.is_unset(request.video_frame_interval):
            query['VideoFrameInterval'] = request.video_frame_interval
        if not UtilClient.is_unset(request.video_max_frames):
            query['VideoMaxFrames'] = request.video_max_frames
        if not UtilClient.is_unset(request.video_max_size):
            query['VideoMaxSize'] = request.video_max_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssStockStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssStockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_stock_status_with_options_async(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_auto_freeze_scene_list):
            query['AudioAutoFreezeSceneList'] = request.audio_auto_freeze_scene_list
        if not UtilClient.is_unset(request.audio_max_size):
            query['AudioMaxSize'] = request.audio_max_size
        if not UtilClient.is_unset(request.auto_freeze_type):
            query['AutoFreezeType'] = request.auto_freeze_type
        if not UtilClient.is_unset(request.bucket_config_list):
            query['BucketConfigList'] = request.bucket_config_list
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_auto_freeze):
            query['ImageAutoFreeze'] = request.image_auto_freeze
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.scene_list):
            query['SceneList'] = request.scene_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.video_auto_freeze_scene_list):
            query['VideoAutoFreezeSceneList'] = request.video_auto_freeze_scene_list
        if not UtilClient.is_unset(request.video_frame_interval):
            query['VideoFrameInterval'] = request.video_frame_interval
        if not UtilClient.is_unset(request.video_max_frames):
            query['VideoMaxFrames'] = request.video_max_frames
        if not UtilClient.is_unset(request.video_max_size):
            query['VideoMaxSize'] = request.video_max_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssStockStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssStockStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_stock_status(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_oss_stock_status_with_options(request, runtime)

    async def update_oss_stock_status_async(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_oss_stock_status_with_options_async(request, runtime)

    def update_website_instance_with_options(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.index_page):
            query['IndexPage'] = request.index_page
        if not UtilClient.is_unset(request.index_page_scan_interval):
            query['IndexPageScanInterval'] = request.index_page_scan_interval
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.site_protocol):
            query['SiteProtocol'] = request.site_protocol
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.website_scan_interval):
            query['WebsiteScanInterval'] = request.website_scan_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_website_instance_with_options_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.index_page):
            query['IndexPage'] = request.index_page
        if not UtilClient.is_unset(request.index_page_scan_interval):
            query['IndexPageScanInterval'] = request.index_page_scan_interval
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.site_protocol):
            query['SiteProtocol'] = request.site_protocol
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.website_scan_interval):
            query['WebsiteScanInterval'] = request.website_scan_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_website_instance(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_with_options(request, runtime)

    async def update_website_instance_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_website_instance_with_options_async(request, runtime)

    def update_website_instance_key_url_with_options(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstanceKeyUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_website_instance_key_url_with_options_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstanceKeyUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_website_instance_key_url(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_key_url_with_options(request, runtime)

    async def update_website_instance_key_url_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_website_instance_key_url_with_options_async(request, runtime)

    def update_website_instance_status_with_options(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstanceStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_website_instance_status_with_options_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstanceStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_website_instance_status(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_status_with_options(request, runtime)

    async def update_website_instance_status_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_website_instance_status_with_options_async(request, runtime)

    def upgrade_cdi_base_bag_with_options(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpgradeCdiBaseBagResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cdi_base_bag_with_options_async(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpgradeCdiBaseBagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cdi_base_bag(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cdi_base_bag_with_options(request, runtime)

    async def upgrade_cdi_base_bag_async(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_cdi_base_bag_with_options_async(request, runtime)

    def upload_image_to_lib_with_options(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UploadImageToLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_lib_id):
            query['ImageLibId'] = request.image_lib_id
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadImageToLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UploadImageToLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_image_to_lib_with_options_async(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UploadImageToLibResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_lib_id):
            query['ImageLibId'] = request.image_lib_id
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadImageToLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UploadImageToLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_image_to_lib(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
    ) -> green_20170823_models.UploadImageToLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_image_to_lib_with_options(request, runtime)

    async def upload_image_to_lib_async(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
    ) -> green_20170823_models.UploadImageToLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_image_to_lib_with_options_async(request, runtime)

    def verify_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.test_img_url):
            query['TestImgUrl'] = request.test_img_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.test_img_url):
            query['TestImgUrl'] = request.test_img_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyCustomOcrTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_custom_ocr_template(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_custom_ocr_template_with_options(request, runtime)

    async def verify_custom_ocr_template_async(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_custom_ocr_template_with_options_async(request, runtime)

    def verify_email_with_options(
        self,
        request: green_20170823_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyEmail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_email_with_options_async(
        self,
        request: green_20170823_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyEmail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_email(
        self,
        request: green_20170823_models.VerifyEmailRequest,
    ) -> green_20170823_models.VerifyEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_email_with_options(request, runtime)

    async def verify_email_async(
        self,
        request: green_20170823_models.VerifyEmailRequest,
    ) -> green_20170823_models.VerifyEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_email_with_options_async(request, runtime)

    def verify_phone_with_options(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyPhone',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_phone_with_options_async(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyPhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyPhone',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_phone(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
    ) -> green_20170823_models.VerifyPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_phone_with_options(request, runtime)

    async def verify_phone_async(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
    ) -> green_20170823_models.VerifyPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_phone_with_options_async(request, runtime)

    def verify_website_instance_with_options(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_method):
            query['VerifyMethod'] = request.verify_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyWebsiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_website_instance_with_options_async(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_method):
            query['VerifyMethod'] = request.verify_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyWebsiteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_website_instance(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_website_instance_with_options(request, runtime)

    async def verify_website_instance_async(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_website_instance_with_options_async(request, runtime)
