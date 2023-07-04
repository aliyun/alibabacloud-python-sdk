# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-southeast-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'dysmsapi.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dysmsapi-proxy.cn-beijing.aliyuncs.com',
            'cn-hongkong': 'dysmsapi-xman.cn-hongkong.aliyuncs.com',
            'eu-central-1': 'dysmsapi.eu-central-1.aliyuncs.com',
            'us-east-1': 'dysmsapi.us-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dysmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.effective_days):
            body['EffectiveDays'] = request.effective_days
        if not UtilClient.is_unset(request.short_url_name):
            body['ShortUrlName'] = request.short_url_name
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.effective_days):
            body['EffectiveDays'] = request.effective_days
        if not UtilClient.is_unset(request.short_url_name):
            body['ShortUrlName'] = request.short_url_name
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_short_url(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_short_url_with_options(request, runtime)

    async def add_short_url_async(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_short_url_with_options_async(request, runtime)

    def add_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sms_sign(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sms_sign_with_options(request, runtime)

    async def add_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sms_sign_with_options_async(request, runtime)

    def add_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sms_template(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sms_template_with_options(request, runtime)

    async def add_sms_template_async(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sms_template_with_options_async(request, runtime)

    def check_mobiles_card_support_with_options(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mobiles):
            query['Mobiles'] = request.mobiles
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CheckMobilesCardSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_mobiles_card_support_with_options_async(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mobiles):
            query['Mobiles'] = request.mobiles
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CheckMobilesCardSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_mobiles_card_support(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_mobiles_card_support_with_options(request, runtime)

    async def check_mobiles_card_support_async(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_mobiles_card_support_with_options_async(request, runtime)

    def conversion_data_intl_with_options(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_rate):
            query['ConversionRate'] = request.conversion_rate
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.report_time):
            query['ReportTime'] = request.report_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConversionDataIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ConversionDataIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def conversion_data_intl_with_options_async(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_rate):
            query['ConversionRate'] = request.conversion_rate
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.report_time):
            query['ReportTime'] = request.report_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConversionDataIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ConversionDataIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def conversion_data_intl(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        runtime = util_models.RuntimeOptions()
        return self.conversion_data_intl_with_options(request, runtime)

    async def conversion_data_intl_async(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.conversion_data_intl_with_options_async(request, runtime)

    def create_card_sms_template_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateCardSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.factorys):
            query['Factorys'] = request.factorys
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.template_shrink):
            query['Template'] = request.template_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateCardSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_card_sms_template_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateCardSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.factorys):
            query['Factorys'] = request.factorys
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.template_shrink):
            query['Template'] = request.template_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateCardSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_card_sms_template(
        self,
        request: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_card_sms_template_with_options(request, runtime)

    async def create_card_sms_template_async(
        self,
        request: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_card_sms_template_with_options_async(request, runtime)

    def create_smart_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_name):
            query['SourceName'] = request.source_name
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmartShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_name):
            query['SourceName'] = request.source_name
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmartShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_smart_short_url(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_smart_short_url_with_options(request, runtime)

    async def create_smart_short_url_async(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_smart_short_url_with_options_async(request, runtime)

    def delete_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_short_url(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_short_url_with_options(request, runtime)

    async def delete_short_url_async(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_short_url_with_options_async(request, runtime)

    def delete_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_sign(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_sign_with_options(request, runtime)

    async def delete_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_sign_with_options_async(request, runtime)

    def delete_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_template(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_template_with_options(request, runtime)

    async def delete_sms_template_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_template_with_options_async(request, runtime)

    def get_card_sms_link_with_options(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_code_type):
            query['CardCodeType'] = request.card_code_type
        if not UtilClient.is_unset(request.card_link_type):
            query['CardLinkType'] = request.card_link_type
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.custom_short_code_json):
            query['CustomShortCodeJson'] = request.custom_short_code_json
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardSmsLink',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetCardSmsLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_sms_link_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_code_type):
            query['CardCodeType'] = request.card_code_type
        if not UtilClient.is_unset(request.card_link_type):
            query['CardLinkType'] = request.card_link_type
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.custom_short_code_json):
            query['CustomShortCodeJson'] = request.custom_short_code_json
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardSmsLink',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetCardSmsLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_sms_link(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_sms_link_with_options(request, runtime)

    async def get_card_sms_link_async(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_sms_link_with_options_async(request, runtime)

    def get_media_resource_id_with_options(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaResourceId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetMediaResourceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_resource_id_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaResourceId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetMediaResourceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_resource_id(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_resource_id_with_options(request, runtime)

    async def get_media_resource_id_async(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_resource_id_with_options_async(request, runtime)

    def get_ossinfo_for_card_template_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOSSInfoForCardTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossinfo_for_card_template_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOSSInfoForCardTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossinfo_for_card_template(self) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ossinfo_for_card_template_with_options(runtime)

    async def get_ossinfo_for_card_template_async(self) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ossinfo_for_card_template_with_options_async(runtime)

    def list_tag_resources_with_options(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sms_sign(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_sign_with_options(request, runtime)

    async def modify_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sms_sign_with_options_async(request, runtime)

    def modify_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sms_template(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_template_with_options(request, runtime)

    async def modify_sms_template_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sms_template_with_options_async(request, runtime)

    def query_card_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_template(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_template_with_options(request, runtime)

    async def query_card_sms_template_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_template_with_options_async(request, runtime)

    def query_card_sms_template_report_with_options(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_codes):
            query['TemplateCodes'] = request.template_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplateReport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_template_report_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_codes):
            query['TemplateCodes'] = request.template_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplateReport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_template_report(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_template_report_with_options(request, runtime)

    async def query_card_sms_template_report_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_template_report_with_options_async(request, runtime)

    def query_mobiles_card_support_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.QueryMobilesCardSupportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.mobiles_shrink):
            query['Mobiles'] = request.mobiles_shrink
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryMobilesCardSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mobiles_card_support_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.QueryMobilesCardSupportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.mobiles_shrink):
            query['Mobiles'] = request.mobiles_shrink
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryMobilesCardSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mobiles_card_support(
        self,
        request: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_mobiles_card_support_with_options(request, runtime)

    async def query_mobiles_card_support_async(
        self,
        request: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_mobiles_card_support_with_options_async(request, runtime)

    def query_page_smart_short_url_log_with_options(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.click_state):
            query['ClickState'] = request.click_state
        if not UtilClient.is_unset(request.create_date_end):
            query['CreateDateEnd'] = request.create_date_end
        if not UtilClient.is_unset(request.create_date_start):
            query['CreateDateStart'] = request.create_date_start
        if not UtilClient.is_unset(request.end_id):
            query['EndId'] = request.end_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.short_name):
            query['ShortName'] = request.short_name
        if not UtilClient.is_unset(request.short_url):
            query['ShortUrl'] = request.short_url
        if not UtilClient.is_unset(request.start_id):
            query['StartId'] = request.start_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPageSmartShortUrlLog',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_page_smart_short_url_log_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.click_state):
            query['ClickState'] = request.click_state
        if not UtilClient.is_unset(request.create_date_end):
            query['CreateDateEnd'] = request.create_date_end
        if not UtilClient.is_unset(request.create_date_start):
            query['CreateDateStart'] = request.create_date_start
        if not UtilClient.is_unset(request.end_id):
            query['EndId'] = request.end_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.short_name):
            query['ShortName'] = request.short_name
        if not UtilClient.is_unset(request.short_url):
            query['ShortUrl'] = request.short_url
        if not UtilClient.is_unset(request.start_id):
            query['StartId'] = request.start_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPageSmartShortUrlLog',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_page_smart_short_url_log(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_page_smart_short_url_log_with_options(request, runtime)

    async def query_page_smart_short_url_log_async(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_page_smart_short_url_log_with_options_async(request, runtime)

    def query_send_details_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetails',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_details_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetails',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_details(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_send_details_with_options(request, runtime)

    async def query_send_details_async(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_send_details_with_options_async(request, runtime)

    def query_send_statistics_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.is_globe):
            query['IsGlobe'] = request.is_globe
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendStatistics',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_statistics_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.is_globe):
            query['IsGlobe'] = request.is_globe
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendStatistics',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_statistics(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_send_statistics_with_options(request, runtime)

    async def query_send_statistics_async(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_send_statistics_with_options_async(request, runtime)

    def query_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.short_url):
            body['ShortUrl'] = request.short_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.short_url):
            body['ShortUrl'] = request.short_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_short_url(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_short_url_with_options(request, runtime)

    async def query_short_url_async(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_short_url_with_options_async(request, runtime)

    def query_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_with_options(request, runtime)

    async def query_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_with_options_async(request, runtime)

    def query_sms_sign_list_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_list_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_list(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_list_with_options(request, runtime)

    async def query_sms_sign_list_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_list_with_options_async(request, runtime)

    def query_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_with_options(request, runtime)

    async def query_sms_template_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_with_options_async(request, runtime)

    def query_sms_template_list_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_list_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_list(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_list_with_options(request, runtime)

    async def query_sms_template_list_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_list_with_options_async(request, runtime)

    def send_batch_card_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param_json):
            query['DigitalTemplateParamJson'] = request.digital_template_param_json
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param_json):
            query['SmsTemplateParamJson'] = request.sms_template_param_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            query['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param_json):
            query['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendBatchCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchCardSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_batch_card_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param_json):
            query['DigitalTemplateParamJson'] = request.digital_template_param_json
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param_json):
            query['SmsTemplateParamJson'] = request.sms_template_param_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            query['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param_json):
            query['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendBatchCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchCardSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_batch_card_sms(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_batch_card_sms_with_options(request, runtime)

    async def send_batch_card_sms_async(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_batch_card_sms_with_options_async(request, runtime)

    def send_batch_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        body = {}
        if not UtilClient.is_unset(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            body['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendBatchSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_batch_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        body = {}
        if not UtilClient.is_unset(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            body['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendBatchSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_batch_sms(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_batch_sms_with_options(request, runtime)

    async def send_batch_sms_async(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_batch_sms_with_options_async(request, runtime)

    def send_card_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_objects):
            query['CardObjects'] = request.card_objects
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param):
            query['DigitalTemplateParam'] = request.digital_template_param
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            query['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendCardSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_card_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_objects):
            query['CardObjects'] = request.card_objects
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param):
            query['DigitalTemplateParam'] = request.digital_template_param
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            query['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendCardSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_card_sms(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_card_sms_with_options(request, runtime)

    async def send_card_sms_async(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_card_sms_with_options_async(request, runtime)

    def send_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sms(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_sms_with_options(request, runtime)

    async def send_sms_async(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_sms_with_options_async(request, runtime)

    def sms_conversion_intl_with_options(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_time):
            query['ConversionTime'] = request.conversion_time
        if not UtilClient.is_unset(request.delivered):
            query['Delivered'] = request.delivered
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsConversionIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SmsConversionIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_conversion_intl_with_options_async(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_time):
            query['ConversionTime'] = request.conversion_time
        if not UtilClient.is_unset(request.delivered):
            query['Delivered'] = request.delivered
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsConversionIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SmsConversionIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_conversion_intl(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        runtime = util_models.RuntimeOptions()
        return self.sms_conversion_intl_with_options(request, runtime)

    async def sms_conversion_intl_async(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sms_conversion_intl_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
