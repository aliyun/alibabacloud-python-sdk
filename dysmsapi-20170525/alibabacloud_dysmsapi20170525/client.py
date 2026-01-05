# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dysmsapi20170525 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_ext_code_sign_with_options(
        self,
        request: main_models.AddExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ext_code_sign_with_options_async(
        self,
        request: main_models.AddExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ext_code_sign(
        self,
        request: main_models.AddExtCodeSignRequest,
    ) -> main_models.AddExtCodeSignResponse:
        runtime = RuntimeOptions()
        return self.add_ext_code_sign_with_options(request, runtime)

    async def add_ext_code_sign_async(
        self,
        request: main_models.AddExtCodeSignRequest,
    ) -> main_models.AddExtCodeSignResponse:
        runtime = RuntimeOptions()
        return await self.add_ext_code_sign_with_options_async(request, runtime)

    def add_short_url_with_options(
        self,
        request: main_models.AddShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.effective_days):
            body['EffectiveDays'] = request.effective_days
        if not DaraCore.is_null(request.short_url_name):
            body['ShortUrlName'] = request.short_url_name
        if not DaraCore.is_null(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_short_url_with_options_async(
        self,
        request: main_models.AddShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.effective_days):
            body['EffectiveDays'] = request.effective_days
        if not DaraCore.is_null(request.short_url_name):
            body['ShortUrlName'] = request.short_url_name
        if not DaraCore.is_null(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_short_url(
        self,
        request: main_models.AddShortUrlRequest,
    ) -> main_models.AddShortUrlResponse:
        runtime = RuntimeOptions()
        return self.add_short_url_with_options(request, runtime)

    async def add_short_url_async(
        self,
        request: main_models.AddShortUrlRequest,
    ) -> main_models.AddShortUrlResponse:
        runtime = RuntimeOptions()
        return await self.add_short_url_with_options_async(request, runtime)

    def add_sms_sign_with_options(
        self,
        request: main_models.AddSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not DaraCore.is_null(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sms_sign_with_options_async(
        self,
        request: main_models.AddSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not DaraCore.is_null(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sms_sign(
        self,
        request: main_models.AddSmsSignRequest,
    ) -> main_models.AddSmsSignResponse:
        runtime = RuntimeOptions()
        return self.add_sms_sign_with_options(request, runtime)

    async def add_sms_sign_async(
        self,
        request: main_models.AddSmsSignRequest,
    ) -> main_models.AddSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.add_sms_sign_with_options_async(request, runtime)

    def add_sms_template_with_options(
        self,
        request: main_models.AddSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sms_template_with_options_async(
        self,
        request: main_models.AddSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sms_template(
        self,
        request: main_models.AddSmsTemplateRequest,
    ) -> main_models.AddSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.add_sms_template_with_options(request, runtime)

    async def add_sms_template_async(
        self,
        request: main_models.AddSmsTemplateRequest,
    ) -> main_models.AddSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.add_sms_template_with_options_async(request, runtime)

    def change_signature_qualification_with_options(
        self,
        request: main_models.ChangeSignatureQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeSignatureQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeSignatureQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeSignatureQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_signature_qualification_with_options_async(
        self,
        request: main_models.ChangeSignatureQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeSignatureQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeSignatureQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeSignatureQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_signature_qualification(
        self,
        request: main_models.ChangeSignatureQualificationRequest,
    ) -> main_models.ChangeSignatureQualificationResponse:
        runtime = RuntimeOptions()
        return self.change_signature_qualification_with_options(request, runtime)

    async def change_signature_qualification_async(
        self,
        request: main_models.ChangeSignatureQualificationRequest,
    ) -> main_models.ChangeSignatureQualificationResponse:
        runtime = RuntimeOptions()
        return await self.change_signature_qualification_with_options_async(request, runtime)

    def check_mobiles_card_support_with_options(
        self,
        request: main_models.CheckMobilesCardSupportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMobilesCardSupportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mobiles):
            query['Mobiles'] = request.mobiles
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckMobilesCardSupport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMobilesCardSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_mobiles_card_support_with_options_async(
        self,
        request: main_models.CheckMobilesCardSupportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMobilesCardSupportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mobiles):
            query['Mobiles'] = request.mobiles
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckMobilesCardSupport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMobilesCardSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_mobiles_card_support(
        self,
        request: main_models.CheckMobilesCardSupportRequest,
    ) -> main_models.CheckMobilesCardSupportResponse:
        runtime = RuntimeOptions()
        return self.check_mobiles_card_support_with_options(request, runtime)

    async def check_mobiles_card_support_async(
        self,
        request: main_models.CheckMobilesCardSupportRequest,
    ) -> main_models.CheckMobilesCardSupportResponse:
        runtime = RuntimeOptions()
        return await self.check_mobiles_card_support_with_options_async(request, runtime)

    def conversion_data_intl_with_options(
        self,
        request: main_models.ConversionDataIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConversionDataIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversion_rate):
            query['ConversionRate'] = request.conversion_rate
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.report_time):
            query['ReportTime'] = request.report_time
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConversionDataIntl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConversionDataIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def conversion_data_intl_with_options_async(
        self,
        request: main_models.ConversionDataIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConversionDataIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversion_rate):
            query['ConversionRate'] = request.conversion_rate
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.report_time):
            query['ReportTime'] = request.report_time
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConversionDataIntl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConversionDataIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def conversion_data_intl(
        self,
        request: main_models.ConversionDataIntlRequest,
    ) -> main_models.ConversionDataIntlResponse:
        runtime = RuntimeOptions()
        return self.conversion_data_intl_with_options(request, runtime)

    async def conversion_data_intl_async(
        self,
        request: main_models.ConversionDataIntlRequest,
    ) -> main_models.ConversionDataIntlResponse:
        runtime = RuntimeOptions()
        return await self.conversion_data_intl_with_options_async(request, runtime)

    def create_card_sms_template_with_options(
        self,
        tmp_req: main_models.CreateCardSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCardSmsTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateCardSmsTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.factorys):
            query['Factorys'] = request.factorys
        if not DaraCore.is_null(request.memo):
            query['Memo'] = request.memo
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCardSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCardSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_card_sms_template_with_options_async(
        self,
        tmp_req: main_models.CreateCardSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCardSmsTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateCardSmsTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.factorys):
            query['Factorys'] = request.factorys
        if not DaraCore.is_null(request.memo):
            query['Memo'] = request.memo
        if not DaraCore.is_null(request.template_shrink):
            query['Template'] = request.template_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCardSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCardSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_card_sms_template(
        self,
        request: main_models.CreateCardSmsTemplateRequest,
    ) -> main_models.CreateCardSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_card_sms_template_with_options(request, runtime)

    async def create_card_sms_template_async(
        self,
        request: main_models.CreateCardSmsTemplateRequest,
    ) -> main_models.CreateCardSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_card_sms_template_with_options_async(request, runtime)

    def create_smart_short_url_with_options(
        self,
        request: main_models.CreateSmartShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_url):
            query['SourceUrl'] = request.source_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_short_url_with_options_async(
        self,
        request: main_models.CreateSmartShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_url):
            query['SourceUrl'] = request.source_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_smart_short_url(
        self,
        request: main_models.CreateSmartShortUrlRequest,
    ) -> main_models.CreateSmartShortUrlResponse:
        runtime = RuntimeOptions()
        return self.create_smart_short_url_with_options(request, runtime)

    async def create_smart_short_url_async(
        self,
        request: main_models.CreateSmartShortUrlRequest,
    ) -> main_models.CreateSmartShortUrlResponse:
        runtime = RuntimeOptions()
        return await self.create_smart_short_url_with_options_async(request, runtime)

    def create_sms_app_icp_record_with_options(
        self,
        request: main_models.CreateSmsAppIcpRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsAppIcpRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_approval_date):
            query['AppApprovalDate'] = request.app_approval_date
        if not DaraCore.is_null(request.app_icp_license_number):
            query['AppIcpLicenseNumber'] = request.app_icp_license_number
        if not DaraCore.is_null(request.app_icp_record_pic):
            query['AppIcpRecordPic'] = request.app_icp_record_pic
        if not DaraCore.is_null(request.app_principal_unit_name):
            query['AppPrincipalUnitName'] = request.app_principal_unit_name
        if not DaraCore.is_null(request.app_service_name):
            query['AppServiceName'] = request.app_service_name
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsAppIcpRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsAppIcpRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_app_icp_record_with_options_async(
        self,
        request: main_models.CreateSmsAppIcpRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsAppIcpRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_approval_date):
            query['AppApprovalDate'] = request.app_approval_date
        if not DaraCore.is_null(request.app_icp_license_number):
            query['AppIcpLicenseNumber'] = request.app_icp_license_number
        if not DaraCore.is_null(request.app_icp_record_pic):
            query['AppIcpRecordPic'] = request.app_icp_record_pic
        if not DaraCore.is_null(request.app_principal_unit_name):
            query['AppPrincipalUnitName'] = request.app_principal_unit_name
        if not DaraCore.is_null(request.app_service_name):
            query['AppServiceName'] = request.app_service_name
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsAppIcpRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsAppIcpRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_app_icp_record(
        self,
        request: main_models.CreateSmsAppIcpRecordRequest,
    ) -> main_models.CreateSmsAppIcpRecordResponse:
        runtime = RuntimeOptions()
        return self.create_sms_app_icp_record_with_options(request, runtime)

    async def create_sms_app_icp_record_async(
        self,
        request: main_models.CreateSmsAppIcpRecordRequest,
    ) -> main_models.CreateSmsAppIcpRecordResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_app_icp_record_with_options_async(request, runtime)

    def create_sms_authorization_letter_with_options(
        self,
        tmp_req: main_models.CreateSmsAuthorizationLetterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsAuthorizationLetterResponse:
        tmp_req.validate()
        request = main_models.CreateSmsAuthorizationLetterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sign_list):
            request.sign_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sign_list, 'SignList', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization):
            query['Authorization'] = request.authorization
        if not DaraCore.is_null(request.authorization_letter_exp_date):
            query['AuthorizationLetterExpDate'] = request.authorization_letter_exp_date
        if not DaraCore.is_null(request.authorization_letter_name):
            query['AuthorizationLetterName'] = request.authorization_letter_name
        if not DaraCore.is_null(request.authorization_letter_pic):
            query['AuthorizationLetterPic'] = request.authorization_letter_pic
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.proxy_authorization):
            query['ProxyAuthorization'] = request.proxy_authorization
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_list_shrink):
            query['SignList'] = request.sign_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsAuthorizationLetter',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsAuthorizationLetterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_authorization_letter_with_options_async(
        self,
        tmp_req: main_models.CreateSmsAuthorizationLetterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsAuthorizationLetterResponse:
        tmp_req.validate()
        request = main_models.CreateSmsAuthorizationLetterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sign_list):
            request.sign_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sign_list, 'SignList', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization):
            query['Authorization'] = request.authorization
        if not DaraCore.is_null(request.authorization_letter_exp_date):
            query['AuthorizationLetterExpDate'] = request.authorization_letter_exp_date
        if not DaraCore.is_null(request.authorization_letter_name):
            query['AuthorizationLetterName'] = request.authorization_letter_name
        if not DaraCore.is_null(request.authorization_letter_pic):
            query['AuthorizationLetterPic'] = request.authorization_letter_pic
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.proxy_authorization):
            query['ProxyAuthorization'] = request.proxy_authorization
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_list_shrink):
            query['SignList'] = request.sign_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsAuthorizationLetter',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsAuthorizationLetterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_authorization_letter(
        self,
        request: main_models.CreateSmsAuthorizationLetterRequest,
    ) -> main_models.CreateSmsAuthorizationLetterResponse:
        runtime = RuntimeOptions()
        return self.create_sms_authorization_letter_with_options(request, runtime)

    async def create_sms_authorization_letter_async(
        self,
        request: main_models.CreateSmsAuthorizationLetterRequest,
    ) -> main_models.CreateSmsAuthorizationLetterResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_authorization_letter_with_options_async(request, runtime)

    def create_sms_sign_with_options(
        self,
        tmp_req: main_models.CreateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsSignResponse:
        tmp_req.validate()
        request = main_models.CreateSmsSignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_icp_record_id):
            query['AppIcpRecordId'] = request.app_icp_record_id
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        if not DaraCore.is_null(request.third_party):
            query['ThirdParty'] = request.third_party
        if not DaraCore.is_null(request.trademark_id):
            query['TrademarkId'] = request.trademark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_sign_with_options_async(
        self,
        tmp_req: main_models.CreateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsSignResponse:
        tmp_req.validate()
        request = main_models.CreateSmsSignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_icp_record_id):
            query['AppIcpRecordId'] = request.app_icp_record_id
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        if not DaraCore.is_null(request.third_party):
            query['ThirdParty'] = request.third_party
        if not DaraCore.is_null(request.trademark_id):
            query['TrademarkId'] = request.trademark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_sign(
        self,
        request: main_models.CreateSmsSignRequest,
    ) -> main_models.CreateSmsSignResponse:
        runtime = RuntimeOptions()
        return self.create_sms_sign_with_options(request, runtime)

    async def create_sms_sign_async(
        self,
        request: main_models.CreateSmsSignRequest,
    ) -> main_models.CreateSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_sign_with_options_async(request, runtime)

    def create_sms_template_with_options(
        self,
        tmp_req: main_models.CreateSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateSmsTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.intl_type):
            query['IntlType'] = request.intl_type
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_template_with_options_async(
        self,
        tmp_req: main_models.CreateSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateSmsTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.intl_type):
            query['IntlType'] = request.intl_type
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_template(
        self,
        request: main_models.CreateSmsTemplateRequest,
    ) -> main_models.CreateSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_sms_template_with_options(request, runtime)

    async def create_sms_template_async(
        self,
        request: main_models.CreateSmsTemplateRequest,
    ) -> main_models.CreateSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_template_with_options_async(request, runtime)

    def create_sms_trademark_with_options(
        self,
        request: main_models.CreateSmsTrademarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsTrademarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trademark_applicant_name):
            query['TrademarkApplicantName'] = request.trademark_applicant_name
        if not DaraCore.is_null(request.trademark_eff_exp_date):
            query['TrademarkEffExpDate'] = request.trademark_eff_exp_date
        if not DaraCore.is_null(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not DaraCore.is_null(request.trademark_pic):
            query['TrademarkPic'] = request.trademark_pic
        if not DaraCore.is_null(request.trademark_registration_number):
            query['TrademarkRegistrationNumber'] = request.trademark_registration_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsTrademark',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsTrademarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_trademark_with_options_async(
        self,
        request: main_models.CreateSmsTrademarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsTrademarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trademark_applicant_name):
            query['TrademarkApplicantName'] = request.trademark_applicant_name
        if not DaraCore.is_null(request.trademark_eff_exp_date):
            query['TrademarkEffExpDate'] = request.trademark_eff_exp_date
        if not DaraCore.is_null(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not DaraCore.is_null(request.trademark_pic):
            query['TrademarkPic'] = request.trademark_pic
        if not DaraCore.is_null(request.trademark_registration_number):
            query['TrademarkRegistrationNumber'] = request.trademark_registration_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsTrademark',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsTrademarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_trademark(
        self,
        request: main_models.CreateSmsTrademarkRequest,
    ) -> main_models.CreateSmsTrademarkResponse:
        runtime = RuntimeOptions()
        return self.create_sms_trademark_with_options(request, runtime)

    async def create_sms_trademark_async(
        self,
        request: main_models.CreateSmsTrademarkRequest,
    ) -> main_models.CreateSmsTrademarkResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_trademark_with_options_async(request, runtime)

    def delete_ext_code_sign_with_options(
        self,
        request: main_models.DeleteExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ext_code_sign_with_options_async(
        self,
        request: main_models.DeleteExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ext_code_sign(
        self,
        request: main_models.DeleteExtCodeSignRequest,
    ) -> main_models.DeleteExtCodeSignResponse:
        runtime = RuntimeOptions()
        return self.delete_ext_code_sign_with_options(request, runtime)

    async def delete_ext_code_sign_async(
        self,
        request: main_models.DeleteExtCodeSignRequest,
    ) -> main_models.DeleteExtCodeSignResponse:
        runtime = RuntimeOptions()
        return await self.delete_ext_code_sign_with_options_async(request, runtime)

    def delete_short_url_with_options(
        self,
        request: main_models.DeleteShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_short_url_with_options_async(
        self,
        request: main_models.DeleteShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_short_url(
        self,
        request: main_models.DeleteShortUrlRequest,
    ) -> main_models.DeleteShortUrlResponse:
        runtime = RuntimeOptions()
        return self.delete_short_url_with_options(request, runtime)

    async def delete_short_url_async(
        self,
        request: main_models.DeleteShortUrlRequest,
    ) -> main_models.DeleteShortUrlResponse:
        runtime = RuntimeOptions()
        return await self.delete_short_url_with_options_async(request, runtime)

    def delete_sms_qualification_with_options(
        self,
        request: main_models.DeleteSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmsQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_qualification_with_options_async(
        self,
        request: main_models.DeleteSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmsQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_qualification(
        self,
        request: main_models.DeleteSmsQualificationRequest,
    ) -> main_models.DeleteSmsQualificationResponse:
        runtime = RuntimeOptions()
        return self.delete_sms_qualification_with_options(request, runtime)

    async def delete_sms_qualification_async(
        self,
        request: main_models.DeleteSmsQualificationRequest,
    ) -> main_models.DeleteSmsQualificationResponse:
        runtime = RuntimeOptions()
        return await self.delete_sms_qualification_with_options_async(request, runtime)

    def delete_sms_sign_with_options(
        self,
        request: main_models.DeleteSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_sign_with_options_async(
        self,
        request: main_models.DeleteSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_sign(
        self,
        request: main_models.DeleteSmsSignRequest,
    ) -> main_models.DeleteSmsSignResponse:
        runtime = RuntimeOptions()
        return self.delete_sms_sign_with_options(request, runtime)

    async def delete_sms_sign_async(
        self,
        request: main_models.DeleteSmsSignRequest,
    ) -> main_models.DeleteSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.delete_sms_sign_with_options_async(request, runtime)

    def delete_sms_template_with_options(
        self,
        request: main_models.DeleteSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_template_with_options_async(
        self,
        request: main_models.DeleteSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_template(
        self,
        request: main_models.DeleteSmsTemplateRequest,
    ) -> main_models.DeleteSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_sms_template_with_options(request, runtime)

    async def delete_sms_template_async(
        self,
        request: main_models.DeleteSmsTemplateRequest,
    ) -> main_models.DeleteSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_sms_template_with_options_async(request, runtime)

    def get_card_sms_details_with_options(
        self,
        request: main_models.GetCardSmsDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCardSmsDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_card_id):
            query['BizCardId'] = request.biz_card_id
        if not DaraCore.is_null(request.biz_digit_id):
            query['BizDigitId'] = request.biz_digit_id
        if not DaraCore.is_null(request.biz_sms_id):
            query['BizSmsId'] = request.biz_sms_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCardSmsDetails',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCardSmsDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_sms_details_with_options_async(
        self,
        request: main_models.GetCardSmsDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCardSmsDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_card_id):
            query['BizCardId'] = request.biz_card_id
        if not DaraCore.is_null(request.biz_digit_id):
            query['BizDigitId'] = request.biz_digit_id
        if not DaraCore.is_null(request.biz_sms_id):
            query['BizSmsId'] = request.biz_sms_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCardSmsDetails',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCardSmsDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_sms_details(
        self,
        request: main_models.GetCardSmsDetailsRequest,
    ) -> main_models.GetCardSmsDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_card_sms_details_with_options(request, runtime)

    async def get_card_sms_details_async(
        self,
        request: main_models.GetCardSmsDetailsRequest,
    ) -> main_models.GetCardSmsDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_card_sms_details_with_options_async(request, runtime)

    def get_card_sms_link_with_options(
        self,
        request: main_models.GetCardSmsLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCardSmsLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_code_type):
            query['CardCodeType'] = request.card_code_type
        if not DaraCore.is_null(request.card_link_type):
            query['CardLinkType'] = request.card_link_type
        if not DaraCore.is_null(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not DaraCore.is_null(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not DaraCore.is_null(request.custom_short_code_json):
            query['CustomShortCodeJson'] = request.custom_short_code_json
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not DaraCore.is_null(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCardSmsLink',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCardSmsLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_sms_link_with_options_async(
        self,
        request: main_models.GetCardSmsLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCardSmsLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_code_type):
            query['CardCodeType'] = request.card_code_type
        if not DaraCore.is_null(request.card_link_type):
            query['CardLinkType'] = request.card_link_type
        if not DaraCore.is_null(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not DaraCore.is_null(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not DaraCore.is_null(request.custom_short_code_json):
            query['CustomShortCodeJson'] = request.custom_short_code_json
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not DaraCore.is_null(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCardSmsLink',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCardSmsLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_sms_link(
        self,
        request: main_models.GetCardSmsLinkRequest,
    ) -> main_models.GetCardSmsLinkResponse:
        runtime = RuntimeOptions()
        return self.get_card_sms_link_with_options(request, runtime)

    async def get_card_sms_link_async(
        self,
        request: main_models.GetCardSmsLinkRequest,
    ) -> main_models.GetCardSmsLinkResponse:
        runtime = RuntimeOptions()
        return await self.get_card_sms_link_with_options_async(request, runtime)

    def get_media_resource_id_with_options(
        self,
        request: main_models.GetMediaResourceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaResourceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.memo):
            query['Memo'] = request.memo
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaResourceId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaResourceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_resource_id_with_options_async(
        self,
        request: main_models.GetMediaResourceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaResourceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.memo):
            query['Memo'] = request.memo
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaResourceId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaResourceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_resource_id(
        self,
        request: main_models.GetMediaResourceIdRequest,
    ) -> main_models.GetMediaResourceIdResponse:
        runtime = RuntimeOptions()
        return self.get_media_resource_id_with_options(request, runtime)

    async def get_media_resource_id_async(
        self,
        request: main_models.GetMediaResourceIdRequest,
    ) -> main_models.GetMediaResourceIdResponse:
        runtime = RuntimeOptions()
        return await self.get_media_resource_id_with_options_async(request, runtime)

    def get_ossinfo_for_card_template_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSInfoForCardTemplateResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetOSSInfoForCardTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSInfoForCardTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossinfo_for_card_template_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSInfoForCardTemplateResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetOSSInfoForCardTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSInfoForCardTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossinfo_for_card_template(self) -> main_models.GetOSSInfoForCardTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_ossinfo_for_card_template_with_options(runtime)

    async def get_ossinfo_for_card_template_async(self) -> main_models.GetOSSInfoForCardTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_ossinfo_for_card_template_with_options_async(runtime)

    def get_ossinfo_for_upload_file_with_options(
        self,
        request: main_models.GetOSSInfoForUploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSInfoForUploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOSSInfoForUploadFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSInfoForUploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossinfo_for_upload_file_with_options_async(
        self,
        request: main_models.GetOSSInfoForUploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSInfoForUploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOSSInfoForUploadFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSInfoForUploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossinfo_for_upload_file(
        self,
        request: main_models.GetOSSInfoForUploadFileRequest,
    ) -> main_models.GetOSSInfoForUploadFileResponse:
        runtime = RuntimeOptions()
        return self.get_ossinfo_for_upload_file_with_options(request, runtime)

    async def get_ossinfo_for_upload_file_async(
        self,
        request: main_models.GetOSSInfoForUploadFileRequest,
    ) -> main_models.GetOSSInfoForUploadFileResponse:
        runtime = RuntimeOptions()
        return await self.get_ossinfo_for_upload_file_with_options_async(request, runtime)

    def get_qualification_oss_info_with_options(
        self,
        request: main_models.GetQualificationOssInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualificationOssInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualificationOssInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualificationOssInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qualification_oss_info_with_options_async(
        self,
        request: main_models.GetQualificationOssInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualificationOssInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualificationOssInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualificationOssInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qualification_oss_info(
        self,
        request: main_models.GetQualificationOssInfoRequest,
    ) -> main_models.GetQualificationOssInfoResponse:
        runtime = RuntimeOptions()
        return self.get_qualification_oss_info_with_options(request, runtime)

    async def get_qualification_oss_info_async(
        self,
        request: main_models.GetQualificationOssInfoRequest,
    ) -> main_models.GetQualificationOssInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_qualification_oss_info_with_options_async(request, runtime)

    def get_sms_ocr_oss_info_with_options(
        self,
        request: main_models.GetSmsOcrOssInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsOcrOssInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsOcrOssInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsOcrOssInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_ocr_oss_info_with_options_async(
        self,
        request: main_models.GetSmsOcrOssInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsOcrOssInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsOcrOssInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsOcrOssInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_ocr_oss_info(
        self,
        request: main_models.GetSmsOcrOssInfoRequest,
    ) -> main_models.GetSmsOcrOssInfoResponse:
        runtime = RuntimeOptions()
        return self.get_sms_ocr_oss_info_with_options(request, runtime)

    async def get_sms_ocr_oss_info_async(
        self,
        request: main_models.GetSmsOcrOssInfoRequest,
    ) -> main_models.GetSmsOcrOssInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_sms_ocr_oss_info_with_options_async(request, runtime)

    def get_sms_sign_with_options(
        self,
        request: main_models.GetSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_sign_with_options_async(
        self,
        request: main_models.GetSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_sign(
        self,
        request: main_models.GetSmsSignRequest,
    ) -> main_models.GetSmsSignResponse:
        runtime = RuntimeOptions()
        return self.get_sms_sign_with_options(request, runtime)

    async def get_sms_sign_async(
        self,
        request: main_models.GetSmsSignRequest,
    ) -> main_models.GetSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.get_sms_sign_with_options_async(request, runtime)

    def get_sms_template_with_options(
        self,
        request: main_models.GetSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_template_with_options_async(
        self,
        request: main_models.GetSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_template(
        self,
        request: main_models.GetSmsTemplateRequest,
    ) -> main_models.GetSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_sms_template_with_options(request, runtime)

    async def get_sms_template_async(
        self,
        request: main_models.GetSmsTemplateRequest,
    ) -> main_models.GetSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_sms_template_with_options_async(request, runtime)

    def get_sms_template_list_with_options(
        self,
        tmp_req: main_models.GetSmsTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsTemplateListResponse:
        tmp_req.validate()
        request = main_models.GetSmsTemplateListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.usable_state_list):
            request.usable_state_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.usable_state_list, 'UsableStateList', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_tag):
            query['TemplateTag'] = request.template_tag
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.usable_state_list_shrink):
            query['UsableStateList'] = request.usable_state_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsTemplateList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_template_list_with_options_async(
        self,
        tmp_req: main_models.GetSmsTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsTemplateListResponse:
        tmp_req.validate()
        request = main_models.GetSmsTemplateListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.usable_state_list):
            request.usable_state_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.usable_state_list, 'UsableStateList', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_tag):
            query['TemplateTag'] = request.template_tag
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.usable_state_list_shrink):
            query['UsableStateList'] = request.usable_state_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsTemplateList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_template_list(
        self,
        request: main_models.GetSmsTemplateListRequest,
    ) -> main_models.GetSmsTemplateListResponse:
        runtime = RuntimeOptions()
        return self.get_sms_template_list_with_options(request, runtime)

    async def get_sms_template_list_async(
        self,
        request: main_models.GetSmsTemplateListRequest,
    ) -> main_models.GetSmsTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.get_sms_template_list_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_sms_sign_with_options(
        self,
        request: main_models.ModifySmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not DaraCore.is_null(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sms_sign_with_options_async(
        self,
        request: main_models.ModifySmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not DaraCore.is_null(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sms_sign(
        self,
        request: main_models.ModifySmsSignRequest,
    ) -> main_models.ModifySmsSignResponse:
        runtime = RuntimeOptions()
        return self.modify_sms_sign_with_options(request, runtime)

    async def modify_sms_sign_async(
        self,
        request: main_models.ModifySmsSignRequest,
    ) -> main_models.ModifySmsSignResponse:
        runtime = RuntimeOptions()
        return await self.modify_sms_sign_with_options_async(request, runtime)

    def modify_sms_template_with_options(
        self,
        request: main_models.ModifySmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sms_template_with_options_async(
        self,
        request: main_models.ModifySmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sms_template(
        self,
        request: main_models.ModifySmsTemplateRequest,
    ) -> main_models.ModifySmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_sms_template_with_options(request, runtime)

    async def modify_sms_template_async(
        self,
        request: main_models.ModifySmsTemplateRequest,
    ) -> main_models.ModifySmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_sms_template_with_options_async(request, runtime)

    def query_card_sms_template_with_options(
        self,
        request: main_models.QueryCardSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCardSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCardSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCardSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_template_with_options_async(
        self,
        request: main_models.QueryCardSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCardSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCardSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCardSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_template(
        self,
        request: main_models.QueryCardSmsTemplateRequest,
    ) -> main_models.QueryCardSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.query_card_sms_template_with_options(request, runtime)

    async def query_card_sms_template_async(
        self,
        request: main_models.QueryCardSmsTemplateRequest,
    ) -> main_models.QueryCardSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.query_card_sms_template_with_options_async(request, runtime)

    def query_card_sms_template_report_with_options(
        self,
        request: main_models.QueryCardSmsTemplateReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCardSmsTemplateReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.template_codes):
            query['TemplateCodes'] = request.template_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCardSmsTemplateReport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCardSmsTemplateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_template_report_with_options_async(
        self,
        request: main_models.QueryCardSmsTemplateReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCardSmsTemplateReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.template_codes):
            query['TemplateCodes'] = request.template_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCardSmsTemplateReport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCardSmsTemplateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_template_report(
        self,
        request: main_models.QueryCardSmsTemplateReportRequest,
    ) -> main_models.QueryCardSmsTemplateReportResponse:
        runtime = RuntimeOptions()
        return self.query_card_sms_template_report_with_options(request, runtime)

    async def query_card_sms_template_report_async(
        self,
        request: main_models.QueryCardSmsTemplateReportRequest,
    ) -> main_models.QueryCardSmsTemplateReportResponse:
        runtime = RuntimeOptions()
        return await self.query_card_sms_template_report_with_options_async(request, runtime)

    def query_ext_code_sign_with_options(
        self,
        request: main_models.QueryExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ext_code_sign_with_options_async(
        self,
        request: main_models.QueryExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ext_code_sign(
        self,
        request: main_models.QueryExtCodeSignRequest,
    ) -> main_models.QueryExtCodeSignResponse:
        runtime = RuntimeOptions()
        return self.query_ext_code_sign_with_options(request, runtime)

    async def query_ext_code_sign_async(
        self,
        request: main_models.QueryExtCodeSignRequest,
    ) -> main_models.QueryExtCodeSignResponse:
        runtime = RuntimeOptions()
        return await self.query_ext_code_sign_with_options_async(request, runtime)

    def query_mobiles_card_support_with_options(
        self,
        tmp_req: main_models.QueryMobilesCardSupportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMobilesCardSupportResponse:
        tmp_req.validate()
        request = main_models.QueryMobilesCardSupportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.mobiles):
            request.mobiles_shrink = Utils.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        query = {}
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.mobiles_shrink):
            query['Mobiles'] = request.mobiles_shrink
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMobilesCardSupport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMobilesCardSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mobiles_card_support_with_options_async(
        self,
        tmp_req: main_models.QueryMobilesCardSupportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMobilesCardSupportResponse:
        tmp_req.validate()
        request = main_models.QueryMobilesCardSupportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.mobiles):
            request.mobiles_shrink = Utils.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        query = {}
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.mobiles_shrink):
            query['Mobiles'] = request.mobiles_shrink
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMobilesCardSupport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMobilesCardSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mobiles_card_support(
        self,
        request: main_models.QueryMobilesCardSupportRequest,
    ) -> main_models.QueryMobilesCardSupportResponse:
        runtime = RuntimeOptions()
        return self.query_mobiles_card_support_with_options(request, runtime)

    async def query_mobiles_card_support_async(
        self,
        request: main_models.QueryMobilesCardSupportRequest,
    ) -> main_models.QueryMobilesCardSupportResponse:
        runtime = RuntimeOptions()
        return await self.query_mobiles_card_support_with_options_async(request, runtime)

    def query_page_smart_short_url_log_with_options(
        self,
        request: main_models.QueryPageSmartShortUrlLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPageSmartShortUrlLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_date_end):
            query['CreateDateEnd'] = request.create_date_end
        if not DaraCore.is_null(request.create_date_start):
            query['CreateDateStart'] = request.create_date_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.short_url):
            query['ShortUrl'] = request.short_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPageSmartShortUrlLog',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPageSmartShortUrlLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_page_smart_short_url_log_with_options_async(
        self,
        request: main_models.QueryPageSmartShortUrlLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPageSmartShortUrlLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_date_end):
            query['CreateDateEnd'] = request.create_date_end
        if not DaraCore.is_null(request.create_date_start):
            query['CreateDateStart'] = request.create_date_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.short_url):
            query['ShortUrl'] = request.short_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPageSmartShortUrlLog',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPageSmartShortUrlLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_page_smart_short_url_log(
        self,
        request: main_models.QueryPageSmartShortUrlLogRequest,
    ) -> main_models.QueryPageSmartShortUrlLogResponse:
        runtime = RuntimeOptions()
        return self.query_page_smart_short_url_log_with_options(request, runtime)

    async def query_page_smart_short_url_log_async(
        self,
        request: main_models.QueryPageSmartShortUrlLogRequest,
    ) -> main_models.QueryPageSmartShortUrlLogResponse:
        runtime = RuntimeOptions()
        return await self.query_page_smart_short_url_log_with_options_async(request, runtime)

    def query_send_details_with_options(
        self,
        request: main_models.QuerySendDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySendDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySendDetails',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySendDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_details_with_options_async(
        self,
        request: main_models.QuerySendDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySendDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySendDetails',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySendDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_details(
        self,
        request: main_models.QuerySendDetailsRequest,
    ) -> main_models.QuerySendDetailsResponse:
        runtime = RuntimeOptions()
        return self.query_send_details_with_options(request, runtime)

    async def query_send_details_async(
        self,
        request: main_models.QuerySendDetailsRequest,
    ) -> main_models.QuerySendDetailsResponse:
        runtime = RuntimeOptions()
        return await self.query_send_details_with_options_async(request, runtime)

    def query_send_statistics_with_options(
        self,
        request: main_models.QuerySendStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySendStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.is_globe):
            query['IsGlobe'] = request.is_globe
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySendStatistics',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySendStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_statistics_with_options_async(
        self,
        request: main_models.QuerySendStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySendStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.is_globe):
            query['IsGlobe'] = request.is_globe
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySendStatistics',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySendStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_statistics(
        self,
        request: main_models.QuerySendStatisticsRequest,
    ) -> main_models.QuerySendStatisticsResponse:
        runtime = RuntimeOptions()
        return self.query_send_statistics_with_options(request, runtime)

    async def query_send_statistics_async(
        self,
        request: main_models.QuerySendStatisticsRequest,
    ) -> main_models.QuerySendStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.query_send_statistics_with_options_async(request, runtime)

    def query_short_url_with_options(
        self,
        request: main_models.QueryShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.short_url):
            body['ShortUrl'] = request.short_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_short_url_with_options_async(
        self,
        request: main_models.QueryShortUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryShortUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.short_url):
            body['ShortUrl'] = request.short_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryShortUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_short_url(
        self,
        request: main_models.QueryShortUrlRequest,
    ) -> main_models.QueryShortUrlResponse:
        runtime = RuntimeOptions()
        return self.query_short_url_with_options(request, runtime)

    async def query_short_url_async(
        self,
        request: main_models.QueryShortUrlRequest,
    ) -> main_models.QueryShortUrlResponse:
        runtime = RuntimeOptions()
        return await self.query_short_url_with_options_async(request, runtime)

    def query_single_sms_qualification_with_options(
        self,
        request: main_models.QuerySingleSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySingleSmsQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySingleSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySingleSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_sms_qualification_with_options_async(
        self,
        request: main_models.QuerySingleSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySingleSmsQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySingleSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySingleSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_sms_qualification(
        self,
        request: main_models.QuerySingleSmsQualificationRequest,
    ) -> main_models.QuerySingleSmsQualificationResponse:
        runtime = RuntimeOptions()
        return self.query_single_sms_qualification_with_options(request, runtime)

    async def query_single_sms_qualification_async(
        self,
        request: main_models.QuerySingleSmsQualificationRequest,
    ) -> main_models.QuerySingleSmsQualificationResponse:
        runtime = RuntimeOptions()
        return await self.query_single_sms_qualification_with_options_async(request, runtime)

    def query_sms_app_icp_record_with_options(
        self,
        tmp_req: main_models.QuerySmsAppIcpRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsAppIcpRecordResponse:
        tmp_req.validate()
        request = main_models.QuerySmsAppIcpRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_icp_record_id_list):
            request.app_icp_record_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_icp_record_id_list, 'AppIcpRecordIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_icp_record_id_list_shrink):
            query['AppIcpRecordIdList'] = request.app_icp_record_id_list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsAppIcpRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsAppIcpRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_app_icp_record_with_options_async(
        self,
        tmp_req: main_models.QuerySmsAppIcpRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsAppIcpRecordResponse:
        tmp_req.validate()
        request = main_models.QuerySmsAppIcpRecordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_icp_record_id_list):
            request.app_icp_record_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_icp_record_id_list, 'AppIcpRecordIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_icp_record_id_list_shrink):
            query['AppIcpRecordIdList'] = request.app_icp_record_id_list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsAppIcpRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsAppIcpRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_app_icp_record(
        self,
        request: main_models.QuerySmsAppIcpRecordRequest,
    ) -> main_models.QuerySmsAppIcpRecordResponse:
        runtime = RuntimeOptions()
        return self.query_sms_app_icp_record_with_options(request, runtime)

    async def query_sms_app_icp_record_async(
        self,
        request: main_models.QuerySmsAppIcpRecordRequest,
    ) -> main_models.QuerySmsAppIcpRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_app_icp_record_with_options_async(request, runtime)

    def query_sms_authorization_letter_with_options(
        self,
        tmp_req: main_models.QuerySmsAuthorizationLetterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsAuthorizationLetterResponse:
        tmp_req.validate()
        request = main_models.QuerySmsAuthorizationLetterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.authorization_letter_id_list):
            request.authorization_letter_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.authorization_letter_id_list, 'AuthorizationLetterIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization_letter_id_list_shrink):
            query['AuthorizationLetterIdList'] = request.authorization_letter_id_list_shrink
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsAuthorizationLetter',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsAuthorizationLetterResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_authorization_letter_with_options_async(
        self,
        tmp_req: main_models.QuerySmsAuthorizationLetterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsAuthorizationLetterResponse:
        tmp_req.validate()
        request = main_models.QuerySmsAuthorizationLetterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.authorization_letter_id_list):
            request.authorization_letter_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.authorization_letter_id_list, 'AuthorizationLetterIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization_letter_id_list_shrink):
            query['AuthorizationLetterIdList'] = request.authorization_letter_id_list_shrink
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsAuthorizationLetter',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsAuthorizationLetterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_authorization_letter(
        self,
        request: main_models.QuerySmsAuthorizationLetterRequest,
    ) -> main_models.QuerySmsAuthorizationLetterResponse:
        runtime = RuntimeOptions()
        return self.query_sms_authorization_letter_with_options(request, runtime)

    async def query_sms_authorization_letter_async(
        self,
        request: main_models.QuerySmsAuthorizationLetterRequest,
    ) -> main_models.QuerySmsAuthorizationLetterResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_authorization_letter_with_options_async(request, runtime)

    def query_sms_qualification_record_with_options(
        self,
        request: main_models.QuerySmsQualificationRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsQualificationRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qualification_group_name):
            query['QualificationGroupName'] = request.qualification_group_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not DaraCore.is_null(request.work_order_id):
            query['WorkOrderId'] = request.work_order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsQualificationRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsQualificationRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_qualification_record_with_options_async(
        self,
        request: main_models.QuerySmsQualificationRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsQualificationRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qualification_group_name):
            query['QualificationGroupName'] = request.qualification_group_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not DaraCore.is_null(request.work_order_id):
            query['WorkOrderId'] = request.work_order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsQualificationRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsQualificationRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_qualification_record(
        self,
        request: main_models.QuerySmsQualificationRecordRequest,
    ) -> main_models.QuerySmsQualificationRecordResponse:
        runtime = RuntimeOptions()
        return self.query_sms_qualification_record_with_options(request, runtime)

    async def query_sms_qualification_record_async(
        self,
        request: main_models.QuerySmsQualificationRecordRequest,
    ) -> main_models.QuerySmsQualificationRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_qualification_record_with_options_async(request, runtime)

    def query_sms_sign_with_options(
        self,
        request: main_models.QuerySmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_with_options_async(
        self,
        request: main_models.QuerySmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign(
        self,
        request: main_models.QuerySmsSignRequest,
    ) -> main_models.QuerySmsSignResponse:
        runtime = RuntimeOptions()
        return self.query_sms_sign_with_options(request, runtime)

    async def query_sms_sign_async(
        self,
        request: main_models.QuerySmsSignRequest,
    ) -> main_models.QuerySmsSignResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_sign_with_options_async(request, runtime)

    def query_sms_sign_list_with_options(
        self,
        request: main_models.QuerySmsSignListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsSignListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsSignList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsSignListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_list_with_options_async(
        self,
        request: main_models.QuerySmsSignListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsSignListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsSignList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsSignListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_list(
        self,
        request: main_models.QuerySmsSignListRequest,
    ) -> main_models.QuerySmsSignListResponse:
        runtime = RuntimeOptions()
        return self.query_sms_sign_list_with_options(request, runtime)

    async def query_sms_sign_list_async(
        self,
        request: main_models.QuerySmsSignListRequest,
    ) -> main_models.QuerySmsSignListResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_sign_list_with_options_async(request, runtime)

    def query_sms_template_with_options(
        self,
        request: main_models.QuerySmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_with_options_async(
        self,
        request: main_models.QuerySmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template(
        self,
        request: main_models.QuerySmsTemplateRequest,
    ) -> main_models.QuerySmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.query_sms_template_with_options(request, runtime)

    async def query_sms_template_async(
        self,
        request: main_models.QuerySmsTemplateRequest,
    ) -> main_models.QuerySmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_template_with_options_async(request, runtime)

    def query_sms_template_list_with_options(
        self,
        request: main_models.QuerySmsTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsTemplateList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_list_with_options_async(
        self,
        request: main_models.QuerySmsTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsTemplateList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_list(
        self,
        request: main_models.QuerySmsTemplateListRequest,
    ) -> main_models.QuerySmsTemplateListResponse:
        runtime = RuntimeOptions()
        return self.query_sms_template_list_with_options(request, runtime)

    async def query_sms_template_list_async(
        self,
        request: main_models.QuerySmsTemplateListRequest,
    ) -> main_models.QuerySmsTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_template_list_with_options_async(request, runtime)

    def query_sms_trademark_with_options(
        self,
        tmp_req: main_models.QuerySmsTrademarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsTrademarkResponse:
        tmp_req.validate()
        request = main_models.QuerySmsTrademarkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.trademark_id_list):
            request.trademark_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.trademark_id_list, 'TrademarkIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trademark_id_list_shrink):
            query['TrademarkIdList'] = request.trademark_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsTrademark',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsTrademarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_trademark_with_options_async(
        self,
        tmp_req: main_models.QuerySmsTrademarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmsTrademarkResponse:
        tmp_req.validate()
        request = main_models.QuerySmsTrademarkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.trademark_id_list):
            request.trademark_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.trademark_id_list, 'TrademarkIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trademark_id_list_shrink):
            query['TrademarkIdList'] = request.trademark_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmsTrademark',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmsTrademarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_trademark(
        self,
        request: main_models.QuerySmsTrademarkRequest,
    ) -> main_models.QuerySmsTrademarkResponse:
        runtime = RuntimeOptions()
        return self.query_sms_trademark_with_options(request, runtime)

    async def query_sms_trademark_async(
        self,
        request: main_models.QuerySmsTrademarkRequest,
    ) -> main_models.QuerySmsTrademarkResponse:
        runtime = RuntimeOptions()
        return await self.query_sms_trademark_with_options_async(request, runtime)

    def required_phone_code_with_options(
        self,
        request: main_models.RequiredPhoneCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequiredPhoneCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequiredPhoneCode',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequiredPhoneCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def required_phone_code_with_options_async(
        self,
        request: main_models.RequiredPhoneCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequiredPhoneCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequiredPhoneCode',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequiredPhoneCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def required_phone_code(
        self,
        request: main_models.RequiredPhoneCodeRequest,
    ) -> main_models.RequiredPhoneCodeResponse:
        runtime = RuntimeOptions()
        return self.required_phone_code_with_options(request, runtime)

    async def required_phone_code_async(
        self,
        request: main_models.RequiredPhoneCodeRequest,
    ) -> main_models.RequiredPhoneCodeResponse:
        runtime = RuntimeOptions()
        return await self.required_phone_code_with_options_async(request, runtime)

    def send_batch_card_sms_with_options(
        self,
        request: main_models.SendBatchCardSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendBatchCardSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not DaraCore.is_null(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not DaraCore.is_null(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not DaraCore.is_null(request.digital_template_param_json):
            query['DigitalTemplateParamJson'] = request.digital_template_param_json
        if not DaraCore.is_null(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not DaraCore.is_null(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        if not DaraCore.is_null(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param_json):
            query['SmsTemplateParamJson'] = request.sms_template_param_json
        if not DaraCore.is_null(request.sms_up_extend_code_json):
            query['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param_json):
            query['TemplateParamJson'] = request.template_param_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendBatchCardSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendBatchCardSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_batch_card_sms_with_options_async(
        self,
        request: main_models.SendBatchCardSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendBatchCardSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not DaraCore.is_null(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not DaraCore.is_null(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not DaraCore.is_null(request.digital_template_param_json):
            query['DigitalTemplateParamJson'] = request.digital_template_param_json
        if not DaraCore.is_null(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not DaraCore.is_null(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        if not DaraCore.is_null(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param_json):
            query['SmsTemplateParamJson'] = request.sms_template_param_json
        if not DaraCore.is_null(request.sms_up_extend_code_json):
            query['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param_json):
            query['TemplateParamJson'] = request.template_param_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendBatchCardSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendBatchCardSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_batch_card_sms(
        self,
        request: main_models.SendBatchCardSmsRequest,
    ) -> main_models.SendBatchCardSmsResponse:
        runtime = RuntimeOptions()
        return self.send_batch_card_sms_with_options(request, runtime)

    async def send_batch_card_sms_async(
        self,
        request: main_models.SendBatchCardSmsRequest,
    ) -> main_models.SendBatchCardSmsResponse:
        runtime = RuntimeOptions()
        return await self.send_batch_card_sms_with_options_async(request, runtime)

    def send_batch_sms_with_options(
        self,
        request: main_models.SendBatchSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendBatchSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        body = {}
        if not DaraCore.is_null(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not DaraCore.is_null(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not DaraCore.is_null(request.sms_up_extend_code_json):
            body['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not DaraCore.is_null(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendBatchSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendBatchSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_batch_sms_with_options_async(
        self,
        request: main_models.SendBatchSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendBatchSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        body = {}
        if not DaraCore.is_null(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not DaraCore.is_null(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not DaraCore.is_null(request.sms_up_extend_code_json):
            body['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not DaraCore.is_null(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendBatchSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendBatchSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_batch_sms(
        self,
        request: main_models.SendBatchSmsRequest,
    ) -> main_models.SendBatchSmsResponse:
        runtime = RuntimeOptions()
        return self.send_batch_sms_with_options(request, runtime)

    async def send_batch_sms_async(
        self,
        request: main_models.SendBatchSmsRequest,
    ) -> main_models.SendBatchSmsResponse:
        runtime = RuntimeOptions()
        return await self.send_batch_sms_with_options_async(request, runtime)

    def send_card_sms_with_options(
        self,
        request: main_models.SendCardSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCardSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_objects):
            query['CardObjects'] = request.card_objects
        if not DaraCore.is_null(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not DaraCore.is_null(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not DaraCore.is_null(request.digital_template_param):
            query['DigitalTemplateParam'] = request.digital_template_param
        if not DaraCore.is_null(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param):
            query['SmsTemplateParam'] = request.sms_template_param
        if not DaraCore.is_null(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCardSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCardSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_card_sms_with_options_async(
        self,
        request: main_models.SendCardSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCardSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_objects):
            query['CardObjects'] = request.card_objects
        if not DaraCore.is_null(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not DaraCore.is_null(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not DaraCore.is_null(request.digital_template_param):
            query['DigitalTemplateParam'] = request.digital_template_param
        if not DaraCore.is_null(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not DaraCore.is_null(request.sms_template_param):
            query['SmsTemplateParam'] = request.sms_template_param
        if not DaraCore.is_null(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCardSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCardSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_card_sms(
        self,
        request: main_models.SendCardSmsRequest,
    ) -> main_models.SendCardSmsResponse:
        runtime = RuntimeOptions()
        return self.send_card_sms_with_options(request, runtime)

    async def send_card_sms_async(
        self,
        request: main_models.SendCardSmsRequest,
    ) -> main_models.SendCardSmsResponse:
        runtime = RuntimeOptions()
        return await self.send_card_sms_with_options_async(request, runtime)

    def send_logistics_sms_with_options(
        self,
        request: main_models.SendLogisticsSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendLogisticsSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not DaraCore.is_null(request.mail_no):
            query['MailNo'] = request.mail_no
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendLogisticsSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendLogisticsSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_logistics_sms_with_options_async(
        self,
        request: main_models.SendLogisticsSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendLogisticsSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not DaraCore.is_null(request.mail_no):
            query['MailNo'] = request.mail_no
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendLogisticsSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendLogisticsSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_logistics_sms(
        self,
        request: main_models.SendLogisticsSmsRequest,
    ) -> main_models.SendLogisticsSmsResponse:
        runtime = RuntimeOptions()
        return self.send_logistics_sms_with_options(request, runtime)

    async def send_logistics_sms_async(
        self,
        request: main_models.SendLogisticsSmsRequest,
    ) -> main_models.SendLogisticsSmsResponse:
        runtime = RuntimeOptions()
        return await self.send_logistics_sms_with_options_async(request, runtime)

    def send_sms_with_options(
        self,
        request: main_models.SendSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sms_with_options_async(
        self,
        request: main_models.SendSmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendSmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendSms',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sms(
        self,
        request: main_models.SendSmsRequest,
    ) -> main_models.SendSmsResponse:
        runtime = RuntimeOptions()
        return self.send_sms_with_options(request, runtime)

    async def send_sms_async(
        self,
        request: main_models.SendSmsRequest,
    ) -> main_models.SendSmsResponse:
        runtime = RuntimeOptions()
        return await self.send_sms_with_options_async(request, runtime)

    def sms_conversion_intl_with_options(
        self,
        request: main_models.SmsConversionIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmsConversionIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversion_time):
            query['ConversionTime'] = request.conversion_time
        if not DaraCore.is_null(request.delivered):
            query['Delivered'] = request.delivered
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmsConversionIntl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmsConversionIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_conversion_intl_with_options_async(
        self,
        request: main_models.SmsConversionIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmsConversionIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversion_time):
            query['ConversionTime'] = request.conversion_time
        if not DaraCore.is_null(request.delivered):
            query['Delivered'] = request.delivered
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmsConversionIntl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmsConversionIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_conversion_intl(
        self,
        request: main_models.SmsConversionIntlRequest,
    ) -> main_models.SmsConversionIntlResponse:
        runtime = RuntimeOptions()
        return self.sms_conversion_intl_with_options(request, runtime)

    async def sms_conversion_intl_async(
        self,
        request: main_models.SmsConversionIntlRequest,
    ) -> main_models.SmsConversionIntlResponse:
        runtime = RuntimeOptions()
        return await self.sms_conversion_intl_with_options_async(request, runtime)

    def submit_sms_qualification_with_options(
        self,
        tmp_req: main_models.SubmitSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmsQualificationResponse:
        tmp_req.validate()
        request = main_models.SubmitSmsQualificationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.business_license_pics):
            request.business_license_pics_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not DaraCore.is_null(tmp_req.other_files):
            request.other_files_shrink = Utils.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not DaraCore.is_null(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not DaraCore.is_null(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not DaraCore.is_null(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not DaraCore.is_null(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not DaraCore.is_null(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not DaraCore.is_null(request.admin_name):
            query['AdminName'] = request.admin_name
        if not DaraCore.is_null(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not DaraCore.is_null(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not DaraCore.is_null(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not DaraCore.is_null(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.company_type):
            query['CompanyType'] = request.company_type
        if not DaraCore.is_null(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not DaraCore.is_null(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not DaraCore.is_null(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not DaraCore.is_null(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not DaraCore.is_null(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_name):
            query['QualificationName'] = request.qualification_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not DaraCore.is_null(request.whether_share):
            query['WhetherShare'] = request.whether_share
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sms_qualification_with_options_async(
        self,
        tmp_req: main_models.SubmitSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmsQualificationResponse:
        tmp_req.validate()
        request = main_models.SubmitSmsQualificationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.business_license_pics):
            request.business_license_pics_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not DaraCore.is_null(tmp_req.other_files):
            request.other_files_shrink = Utils.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not DaraCore.is_null(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not DaraCore.is_null(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not DaraCore.is_null(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not DaraCore.is_null(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not DaraCore.is_null(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not DaraCore.is_null(request.admin_name):
            query['AdminName'] = request.admin_name
        if not DaraCore.is_null(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not DaraCore.is_null(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not DaraCore.is_null(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not DaraCore.is_null(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.company_type):
            query['CompanyType'] = request.company_type
        if not DaraCore.is_null(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not DaraCore.is_null(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not DaraCore.is_null(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not DaraCore.is_null(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not DaraCore.is_null(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_name):
            query['QualificationName'] = request.qualification_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not DaraCore.is_null(request.whether_share):
            query['WhetherShare'] = request.whether_share
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sms_qualification(
        self,
        request: main_models.SubmitSmsQualificationRequest,
    ) -> main_models.SubmitSmsQualificationResponse:
        runtime = RuntimeOptions()
        return self.submit_sms_qualification_with_options(request, runtime)

    async def submit_sms_qualification_async(
        self,
        request: main_models.SubmitSmsQualificationRequest,
    ) -> main_models.SubmitSmsQualificationResponse:
        runtime = RuntimeOptions()
        return await self.submit_sms_qualification_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_ext_code_sign_with_options(
        self,
        request: main_models.UpdateExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exist_ext_code):
            query['ExistExtCode'] = request.exist_ext_code
        if not DaraCore.is_null(request.new_ext_code):
            query['NewExtCode'] = request.new_ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ext_code_sign_with_options_async(
        self,
        request: main_models.UpdateExtCodeSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExtCodeSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exist_ext_code):
            query['ExistExtCode'] = request.exist_ext_code
        if not DaraCore.is_null(request.new_ext_code):
            query['NewExtCode'] = request.new_ext_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExtCodeSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ext_code_sign(
        self,
        request: main_models.UpdateExtCodeSignRequest,
    ) -> main_models.UpdateExtCodeSignResponse:
        runtime = RuntimeOptions()
        return self.update_ext_code_sign_with_options(request, runtime)

    async def update_ext_code_sign_async(
        self,
        request: main_models.UpdateExtCodeSignRequest,
    ) -> main_models.UpdateExtCodeSignResponse:
        runtime = RuntimeOptions()
        return await self.update_ext_code_sign_with_options_async(request, runtime)

    def update_sms_qualification_with_options(
        self,
        tmp_req: main_models.UpdateSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsQualificationResponse:
        tmp_req.validate()
        request = main_models.UpdateSmsQualificationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.business_license_pics):
            request.business_license_pics_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not DaraCore.is_null(tmp_req.other_files):
            request.other_files_shrink = Utils.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not DaraCore.is_null(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not DaraCore.is_null(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not DaraCore.is_null(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not DaraCore.is_null(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not DaraCore.is_null(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not DaraCore.is_null(request.admin_name):
            query['AdminName'] = request.admin_name
        if not DaraCore.is_null(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not DaraCore.is_null(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not DaraCore.is_null(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not DaraCore.is_null(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not DaraCore.is_null(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not DaraCore.is_null(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not DaraCore.is_null(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not DaraCore.is_null(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sms_qualification_with_options_async(
        self,
        tmp_req: main_models.UpdateSmsQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsQualificationResponse:
        tmp_req.validate()
        request = main_models.UpdateSmsQualificationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.business_license_pics):
            request.business_license_pics_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not DaraCore.is_null(tmp_req.other_files):
            request.other_files_shrink = Utils.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not DaraCore.is_null(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not DaraCore.is_null(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not DaraCore.is_null(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not DaraCore.is_null(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not DaraCore.is_null(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not DaraCore.is_null(request.admin_name):
            query['AdminName'] = request.admin_name
        if not DaraCore.is_null(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not DaraCore.is_null(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not DaraCore.is_null(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not DaraCore.is_null(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not DaraCore.is_null(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not DaraCore.is_null(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not DaraCore.is_null(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not DaraCore.is_null(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmsQualification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sms_qualification(
        self,
        request: main_models.UpdateSmsQualificationRequest,
    ) -> main_models.UpdateSmsQualificationResponse:
        runtime = RuntimeOptions()
        return self.update_sms_qualification_with_options(request, runtime)

    async def update_sms_qualification_async(
        self,
        request: main_models.UpdateSmsQualificationRequest,
    ) -> main_models.UpdateSmsQualificationResponse:
        runtime = RuntimeOptions()
        return await self.update_sms_qualification_with_options_async(request, runtime)

    def update_sms_sign_with_options(
        self,
        tmp_req: main_models.UpdateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsSignResponse:
        tmp_req.validate()
        request = main_models.UpdateSmsSignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_icp_record_id):
            query['AppIcpRecordId'] = request.app_icp_record_id
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        if not DaraCore.is_null(request.third_party):
            query['ThirdParty'] = request.third_party
        if not DaraCore.is_null(request.trademark_id):
            query['TrademarkId'] = request.trademark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sms_sign_with_options_async(
        self,
        tmp_req: main_models.UpdateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsSignResponse:
        tmp_req.validate()
        request = main_models.UpdateSmsSignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.app_icp_record_id):
            query['AppIcpRecordId'] = request.app_icp_record_id
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.sign_source):
            query['SignSource'] = request.sign_source
        if not DaraCore.is_null(request.sign_type):
            query['SignType'] = request.sign_type
        if not DaraCore.is_null(request.third_party):
            query['ThirdParty'] = request.third_party
        if not DaraCore.is_null(request.trademark_id):
            query['TrademarkId'] = request.trademark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sms_sign(
        self,
        request: main_models.UpdateSmsSignRequest,
    ) -> main_models.UpdateSmsSignResponse:
        runtime = RuntimeOptions()
        return self.update_sms_sign_with_options(request, runtime)

    async def update_sms_sign_async(
        self,
        request: main_models.UpdateSmsSignRequest,
    ) -> main_models.UpdateSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.update_sms_sign_with_options_async(request, runtime)

    def update_sms_template_with_options(
        self,
        tmp_req: main_models.UpdateSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateSmsTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.intl_type):
            query['IntlType'] = request.intl_type
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sms_template_with_options_async(
        self,
        tmp_req: main_models.UpdateSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateSmsTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.more_data):
            request.more_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not DaraCore.is_null(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not DaraCore.is_null(request.intl_type):
            query['IntlType'] = request.intl_type
        if not DaraCore.is_null(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmsTemplate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sms_template(
        self,
        request: main_models.UpdateSmsTemplateRequest,
    ) -> main_models.UpdateSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_sms_template_with_options(request, runtime)

    async def update_sms_template_async(
        self,
        request: main_models.UpdateSmsTemplateRequest,
    ) -> main_models.UpdateSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_sms_template_with_options_async(request, runtime)

    def valid_phone_code_with_options(
        self,
        request: main_models.ValidPhoneCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidPhoneCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidPhoneCode',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidPhoneCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def valid_phone_code_with_options_async(
        self,
        request: main_models.ValidPhoneCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidPhoneCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidPhoneCode',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidPhoneCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valid_phone_code(
        self,
        request: main_models.ValidPhoneCodeRequest,
    ) -> main_models.ValidPhoneCodeResponse:
        runtime = RuntimeOptions()
        return self.valid_phone_code_with_options(request, runtime)

    async def valid_phone_code_async(
        self,
        request: main_models.ValidPhoneCodeRequest,
    ) -> main_models.ValidPhoneCodeResponse:
        runtime = RuntimeOptions()
        return await self.valid_phone_code_with_options_async(request, runtime)

    def verify_logistics_sms_mail_no_with_options(
        self,
        request: main_models.VerifyLogisticsSmsMailNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyLogisticsSmsMailNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not DaraCore.is_null(request.mail_no):
            query['MailNo'] = request.mail_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyLogisticsSmsMailNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyLogisticsSmsMailNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_logistics_sms_mail_no_with_options_async(
        self,
        request: main_models.VerifyLogisticsSmsMailNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyLogisticsSmsMailNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not DaraCore.is_null(request.mail_no):
            query['MailNo'] = request.mail_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyLogisticsSmsMailNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyLogisticsSmsMailNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_logistics_sms_mail_no(
        self,
        request: main_models.VerifyLogisticsSmsMailNoRequest,
    ) -> main_models.VerifyLogisticsSmsMailNoResponse:
        runtime = RuntimeOptions()
        return self.verify_logistics_sms_mail_no_with_options(request, runtime)

    async def verify_logistics_sms_mail_no_async(
        self,
        request: main_models.VerifyLogisticsSmsMailNoRequest,
    ) -> main_models.VerifyLogisticsSmsMailNoResponse:
        runtime = RuntimeOptions()
        return await self.verify_logistics_sms_mail_no_with_options_async(request, runtime)
