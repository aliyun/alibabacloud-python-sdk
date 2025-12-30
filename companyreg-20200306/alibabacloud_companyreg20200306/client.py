# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_companyreg20200306 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'companyreg.aliyuncs.com',
            'ap-northeast-2-pop': 'companyreg.aliyuncs.com',
            'ap-south-1': 'companyreg.aliyuncs.com',
            'ap-southeast-1': 'companyreg.aliyuncs.com',
            'ap-southeast-2': 'companyreg.aliyuncs.com',
            'ap-southeast-3': 'companyreg.aliyuncs.com',
            'ap-southeast-5': 'companyreg.aliyuncs.com',
            'cn-beijing': 'companyreg.aliyuncs.com',
            'cn-beijing-finance-1': 'companyreg.aliyuncs.com',
            'cn-beijing-finance-pop': 'companyreg.aliyuncs.com',
            'cn-beijing-gov-1': 'companyreg.aliyuncs.com',
            'cn-beijing-nu16-b01': 'companyreg.aliyuncs.com',
            'cn-chengdu': 'companyreg.aliyuncs.com',
            'cn-edge-1': 'companyreg.aliyuncs.com',
            'cn-fujian': 'companyreg.aliyuncs.com',
            'cn-haidian-cm12-c01': 'companyreg.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'companyreg.aliyuncs.com',
            'cn-hangzhou-finance': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'companyreg.aliyuncs.com',
            'cn-hangzhou-test-306': 'companyreg.aliyuncs.com',
            'cn-hongkong': 'companyreg.aliyuncs.com',
            'cn-hongkong-finance-pop': 'companyreg.aliyuncs.com',
            'cn-huhehaote': 'companyreg.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'companyreg.aliyuncs.com',
            'cn-north-2-gov-1': 'companyreg.aliyuncs.com',
            'cn-qingdao': 'companyreg.aliyuncs.com',
            'cn-qingdao-nebula': 'companyreg.aliyuncs.com',
            'cn-shanghai': 'companyreg.aliyuncs.com',
            'cn-shanghai-et15-b01': 'companyreg.aliyuncs.com',
            'cn-shanghai-et2-b01': 'companyreg.aliyuncs.com',
            'cn-shanghai-finance-1': 'companyreg.aliyuncs.com',
            'cn-shanghai-inner': 'companyreg.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'companyreg.aliyuncs.com',
            'cn-shenzhen': 'companyreg.aliyuncs.com',
            'cn-shenzhen-finance-1': 'companyreg.aliyuncs.com',
            'cn-shenzhen-inner': 'companyreg.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'companyreg.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'companyreg.aliyuncs.com',
            'cn-wuhan': 'companyreg.aliyuncs.com',
            'cn-wulanchabu': 'companyreg.aliyuncs.com',
            'cn-yushanfang': 'companyreg.aliyuncs.com',
            'cn-zhangbei': 'companyreg.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'companyreg.aliyuncs.com',
            'cn-zhangjiakou': 'companyreg.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'companyreg.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'companyreg.aliyuncs.com',
            'eu-central-1': 'companyreg.aliyuncs.com',
            'eu-west-1': 'companyreg.aliyuncs.com',
            'eu-west-1-oxs': 'companyreg.aliyuncs.com',
            'me-east-1': 'companyreg.aliyuncs.com',
            'rus-west-1-pop': 'companyreg.aliyuncs.com',
            'us-east-1': 'companyreg.aliyuncs.com',
            'us-west-1': 'companyreg.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('companyreg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_produce_authorization_with_options(
        self,
        request: main_models.BindProduceAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindProduceAuthorizationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorized_user_ids):
            body['AuthorizedUserIds'] = request.authorized_user_ids
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindProduceAuthorization',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindProduceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_produce_authorization_with_options_async(
        self,
        request: main_models.BindProduceAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindProduceAuthorizationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorized_user_ids):
            body['AuthorizedUserIds'] = request.authorized_user_ids
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindProduceAuthorization',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindProduceAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_produce_authorization(
        self,
        request: main_models.BindProduceAuthorizationRequest,
    ) -> main_models.BindProduceAuthorizationResponse:
        runtime = RuntimeOptions()
        return self.bind_produce_authorization_with_options(request, runtime)

    async def bind_produce_authorization_async(
        self,
        request: main_models.BindProduceAuthorizationRequest,
    ) -> main_models.BindProduceAuthorizationResponse:
        runtime = RuntimeOptions()
        return await self.bind_produce_authorization_with_options_async(request, runtime)

    def close_intention_for_partner_with_options(
        self,
        request: main_models.CloseIntentionForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseIntentionForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseIntentionForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseIntentionForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_intention_for_partner_with_options_async(
        self,
        request: main_models.CloseIntentionForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseIntentionForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseIntentionForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseIntentionForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_intention_for_partner(
        self,
        request: main_models.CloseIntentionForPartnerRequest,
    ) -> main_models.CloseIntentionForPartnerResponse:
        runtime = RuntimeOptions()
        return self.close_intention_for_partner_with_options(request, runtime)

    async def close_intention_for_partner_async(
        self,
        request: main_models.CloseIntentionForPartnerRequest,
    ) -> main_models.CloseIntentionForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.close_intention_for_partner_with_options_async(request, runtime)

    def close_user_intention_with_options(
        self,
        request: main_models.CloseUserIntentionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseUserIntentionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseUserIntention',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseUserIntentionResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_user_intention_with_options_async(
        self,
        request: main_models.CloseUserIntentionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseUserIntentionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseUserIntention',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseUserIntentionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_user_intention(
        self,
        request: main_models.CloseUserIntentionRequest,
    ) -> main_models.CloseUserIntentionResponse:
        runtime = RuntimeOptions()
        return self.close_user_intention_with_options(request, runtime)

    async def close_user_intention_async(
        self,
        request: main_models.CloseUserIntentionRequest,
    ) -> main_models.CloseUserIntentionResponse:
        runtime = RuntimeOptions()
        return await self.close_user_intention_with_options_async(request, runtime)

    def create_business_opportunity_with_options(
        self,
        request: main_models.CreateBusinessOpportunityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBusinessOpportunityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.vcode):
            query['VCode'] = request.vcode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBusinessOpportunity',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBusinessOpportunityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_business_opportunity_with_options_async(
        self,
        request: main_models.CreateBusinessOpportunityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBusinessOpportunityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.vcode):
            query['VCode'] = request.vcode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBusinessOpportunity',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBusinessOpportunityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_business_opportunity(
        self,
        request: main_models.CreateBusinessOpportunityRequest,
    ) -> main_models.CreateBusinessOpportunityResponse:
        runtime = RuntimeOptions()
        return self.create_business_opportunity_with_options(request, runtime)

    async def create_business_opportunity_async(
        self,
        request: main_models.CreateBusinessOpportunityRequest,
    ) -> main_models.CreateBusinessOpportunityResponse:
        runtime = RuntimeOptions()
        return await self.create_business_opportunity_with_options_async(request, runtime)

    def create_produce_for_partner_with_options(
        self,
        request: main_models.CreateProduceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProduceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduceForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProduceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_produce_for_partner_with_options_async(
        self,
        request: main_models.CreateProduceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProduceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduceForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProduceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_produce_for_partner(
        self,
        request: main_models.CreateProduceForPartnerRequest,
    ) -> main_models.CreateProduceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.create_produce_for_partner_with_options(request, runtime)

    async def create_produce_for_partner_async(
        self,
        request: main_models.CreateProduceForPartnerRequest,
    ) -> main_models.CreateProduceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.create_produce_for_partner_with_options_async(request, runtime)

    def describe_partner_config_with_options(
        self,
        request: main_models.DescribePartnerConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePartnerConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.partner_code):
            query['PartnerCode'] = request.partner_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePartnerConfig',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePartnerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_partner_config_with_options_async(
        self,
        request: main_models.DescribePartnerConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePartnerConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.partner_code):
            query['PartnerCode'] = request.partner_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePartnerConfig',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePartnerConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_partner_config(
        self,
        request: main_models.DescribePartnerConfigRequest,
    ) -> main_models.DescribePartnerConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_partner_config_with_options(request, runtime)

    async def describe_partner_config_async(
        self,
        request: main_models.DescribePartnerConfigRequest,
    ) -> main_models.DescribePartnerConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_partner_config_with_options_async(request, runtime)

    def generate_upload_file_policy_with_options(
        self,
        request: main_models.GenerateUploadFilePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadFilePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadFilePolicy',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadFilePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_file_policy_with_options_async(
        self,
        request: main_models.GenerateUploadFilePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadFilePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadFilePolicy',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadFilePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_file_policy(
        self,
        request: main_models.GenerateUploadFilePolicyRequest,
    ) -> main_models.GenerateUploadFilePolicyResponse:
        runtime = RuntimeOptions()
        return self.generate_upload_file_policy_with_options(request, runtime)

    async def generate_upload_file_policy_async(
        self,
        request: main_models.GenerateUploadFilePolicyRequest,
    ) -> main_models.GenerateUploadFilePolicyResponse:
        runtime = RuntimeOptions()
        return await self.generate_upload_file_policy_with_options_async(request, runtime)

    def get_alipay_url_with_options(
        self,
        request: main_models.GetAlipayUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlipayUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlipayUrl',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlipayUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alipay_url_with_options_async(
        self,
        request: main_models.GetAlipayUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlipayUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlipayUrl',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlipayUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alipay_url(
        self,
        request: main_models.GetAlipayUrlRequest,
    ) -> main_models.GetAlipayUrlResponse:
        runtime = RuntimeOptions()
        return self.get_alipay_url_with_options(request, runtime)

    async def get_alipay_url_async(
        self,
        request: main_models.GetAlipayUrlRequest,
    ) -> main_models.GetAlipayUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_alipay_url_with_options_async(request, runtime)

    def list_intention_note_with_options(
        self,
        request: main_models.ListIntentionNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentionNoteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntentionNote',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentionNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intention_note_with_options_async(
        self,
        request: main_models.ListIntentionNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentionNoteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntentionNote',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentionNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intention_note(
        self,
        request: main_models.ListIntentionNoteRequest,
    ) -> main_models.ListIntentionNoteResponse:
        runtime = RuntimeOptions()
        return self.list_intention_note_with_options(request, runtime)

    async def list_intention_note_async(
        self,
        request: main_models.ListIntentionNoteRequest,
    ) -> main_models.ListIntentionNoteResponse:
        runtime = RuntimeOptions()
        return await self.list_intention_note_with_options_async(request, runtime)

    def list_produce_authorization_with_options(
        self,
        request: main_models.ListProduceAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProduceAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProduceAuthorization',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProduceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_produce_authorization_with_options_async(
        self,
        request: main_models.ListProduceAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProduceAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProduceAuthorization',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProduceAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_produce_authorization(
        self,
        request: main_models.ListProduceAuthorizationRequest,
    ) -> main_models.ListProduceAuthorizationResponse:
        runtime = RuntimeOptions()
        return self.list_produce_authorization_with_options(request, runtime)

    async def list_produce_authorization_async(
        self,
        request: main_models.ListProduceAuthorizationRequest,
    ) -> main_models.ListProduceAuthorizationResponse:
        runtime = RuntimeOptions()
        return await self.list_produce_authorization_with_options_async(request, runtime)

    def list_user_detail_solutions_with_options(
        self,
        request: main_models.ListUserDetailSolutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDetailSolutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDetailSolutions',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDetailSolutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_detail_solutions_with_options_async(
        self,
        request: main_models.ListUserDetailSolutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDetailSolutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDetailSolutions',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDetailSolutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_detail_solutions(
        self,
        request: main_models.ListUserDetailSolutionsRequest,
    ) -> main_models.ListUserDetailSolutionsResponse:
        runtime = RuntimeOptions()
        return self.list_user_detail_solutions_with_options(request, runtime)

    async def list_user_detail_solutions_async(
        self,
        request: main_models.ListUserDetailSolutionsRequest,
    ) -> main_models.ListUserDetailSolutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_detail_solutions_with_options_async(request, runtime)

    def list_user_intention_notes_with_options(
        self,
        request: main_models.ListUserIntentionNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserIntentionNotesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserIntentionNotes',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserIntentionNotesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_intention_notes_with_options_async(
        self,
        request: main_models.ListUserIntentionNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserIntentionNotesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserIntentionNotes',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserIntentionNotesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_intention_notes(
        self,
        request: main_models.ListUserIntentionNotesRequest,
    ) -> main_models.ListUserIntentionNotesResponse:
        runtime = RuntimeOptions()
        return self.list_user_intention_notes_with_options(request, runtime)

    async def list_user_intention_notes_async(
        self,
        request: main_models.ListUserIntentionNotesRequest,
    ) -> main_models.ListUserIntentionNotesResponse:
        runtime = RuntimeOptions()
        return await self.list_user_intention_notes_with_options_async(request, runtime)

    def list_user_intentions_with_options(
        self,
        request: main_models.ListUserIntentionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserIntentionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_filed):
            query['SortFiled'] = request.sort_filed
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.with_ext_info):
            query['WithExtInfo'] = request.with_ext_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserIntentions',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserIntentionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_intentions_with_options_async(
        self,
        request: main_models.ListUserIntentionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserIntentionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_filed):
            query['SortFiled'] = request.sort_filed
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.with_ext_info):
            query['WithExtInfo'] = request.with_ext_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserIntentions',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserIntentionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_intentions(
        self,
        request: main_models.ListUserIntentionsRequest,
    ) -> main_models.ListUserIntentionsResponse:
        runtime = RuntimeOptions()
        return self.list_user_intentions_with_options(request, runtime)

    async def list_user_intentions_async(
        self,
        request: main_models.ListUserIntentionsRequest,
    ) -> main_models.ListUserIntentionsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_intentions_with_options_async(request, runtime)

    def list_user_produce_operate_logs_with_options(
        self,
        request: main_models.ListUserProduceOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserProduceOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserProduceOperateLogs',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserProduceOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_produce_operate_logs_with_options_async(
        self,
        request: main_models.ListUserProduceOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserProduceOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserProduceOperateLogs',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserProduceOperateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_produce_operate_logs(
        self,
        request: main_models.ListUserProduceOperateLogsRequest,
    ) -> main_models.ListUserProduceOperateLogsResponse:
        runtime = RuntimeOptions()
        return self.list_user_produce_operate_logs_with_options(request, runtime)

    async def list_user_produce_operate_logs_async(
        self,
        request: main_models.ListUserProduceOperateLogsRequest,
    ) -> main_models.ListUserProduceOperateLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_produce_operate_logs_with_options_async(request, runtime)

    def list_user_solutions_with_options(
        self,
        tmp_req: main_models.ListUserSolutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserSolutionsResponse:
        tmp_req.validate()
        request = main_models.ListUserSolutionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exist_status):
            request.exist_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.exist_status, 'ExistStatus', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.exist_status_shrink):
            query['ExistStatus'] = request.exist_status_shrink
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserSolutions',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserSolutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_solutions_with_options_async(
        self,
        tmp_req: main_models.ListUserSolutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserSolutionsResponse:
        tmp_req.validate()
        request = main_models.ListUserSolutionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exist_status):
            request.exist_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.exist_status, 'ExistStatus', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.exist_status_shrink):
            query['ExistStatus'] = request.exist_status_shrink
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserSolutions',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserSolutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_solutions(
        self,
        request: main_models.ListUserSolutionsRequest,
    ) -> main_models.ListUserSolutionsResponse:
        runtime = RuntimeOptions()
        return self.list_user_solutions_with_options(request, runtime)

    async def list_user_solutions_async(
        self,
        request: main_models.ListUserSolutionsRequest,
    ) -> main_models.ListUserSolutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_solutions_with_options_async(request, runtime)

    def operate_call_center_for_partner_with_options(
        self,
        request: main_models.OperateCallCenterForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateCallCenterForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.call_action):
            query['CallAction'] = request.call_action
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.request):
            query['Request'] = request.request
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateCallCenterForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateCallCenterForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_call_center_for_partner_with_options_async(
        self,
        request: main_models.OperateCallCenterForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateCallCenterForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.call_action):
            query['CallAction'] = request.call_action
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.request):
            query['Request'] = request.request
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateCallCenterForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateCallCenterForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_call_center_for_partner(
        self,
        request: main_models.OperateCallCenterForPartnerRequest,
    ) -> main_models.OperateCallCenterForPartnerResponse:
        runtime = RuntimeOptions()
        return self.operate_call_center_for_partner_with_options(request, runtime)

    async def operate_call_center_for_partner_async(
        self,
        request: main_models.OperateCallCenterForPartnerRequest,
    ) -> main_models.OperateCallCenterForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.operate_call_center_for_partner_with_options_async(request, runtime)

    def operate_produce_for_partner_with_options(
        self,
        request: main_models.OperateProduceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateProduceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateProduceForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateProduceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_produce_for_partner_with_options_async(
        self,
        request: main_models.OperateProduceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateProduceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateProduceForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateProduceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_produce_for_partner(
        self,
        request: main_models.OperateProduceForPartnerRequest,
    ) -> main_models.OperateProduceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.operate_produce_for_partner_with_options(request, runtime)

    async def operate_produce_for_partner_async(
        self,
        request: main_models.OperateProduceForPartnerRequest,
    ) -> main_models.OperateProduceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.operate_produce_for_partner_with_options_async(request, runtime)

    def put_measure_data_with_options(
        self,
        request: main_models.PutMeasureDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMeasureDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutMeasureData',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMeasureDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_measure_data_with_options_async(
        self,
        request: main_models.PutMeasureDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMeasureDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutMeasureData',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMeasureDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_measure_data(
        self,
        request: main_models.PutMeasureDataRequest,
    ) -> main_models.PutMeasureDataResponse:
        runtime = RuntimeOptions()
        return self.put_measure_data_with_options(request, runtime)

    async def put_measure_data_async(
        self,
        request: main_models.PutMeasureDataRequest,
    ) -> main_models.PutMeasureDataResponse:
        runtime = RuntimeOptions()
        return await self.put_measure_data_with_options_async(request, runtime)

    def put_measure_ready_flag_with_options(
        self,
        request: main_models.PutMeasureReadyFlagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMeasureReadyFlagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ready_flag):
            query['ReadyFlag'] = request.ready_flag
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMeasureReadyFlag',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMeasureReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_measure_ready_flag_with_options_async(
        self,
        request: main_models.PutMeasureReadyFlagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMeasureReadyFlagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ready_flag):
            query['ReadyFlag'] = request.ready_flag
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMeasureReadyFlag',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMeasureReadyFlagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_measure_ready_flag(
        self,
        request: main_models.PutMeasureReadyFlagRequest,
    ) -> main_models.PutMeasureReadyFlagResponse:
        runtime = RuntimeOptions()
        return self.put_measure_ready_flag_with_options(request, runtime)

    async def put_measure_ready_flag_async(
        self,
        request: main_models.PutMeasureReadyFlagRequest,
    ) -> main_models.PutMeasureReadyFlagResponse:
        runtime = RuntimeOptions()
        return await self.put_measure_ready_flag_with_options_async(request, runtime)

    def query_available_numbers_with_options(
        self,
        request: main_models.QueryAvailableNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableNumbers',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_available_numbers_with_options_async(
        self,
        request: main_models.QueryAvailableNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableNumbers',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_available_numbers(
        self,
        request: main_models.QueryAvailableNumbersRequest,
    ) -> main_models.QueryAvailableNumbersResponse:
        runtime = RuntimeOptions()
        return self.query_available_numbers_with_options(request, runtime)

    async def query_available_numbers_async(
        self,
        request: main_models.QueryAvailableNumbersRequest,
    ) -> main_models.QueryAvailableNumbersResponse:
        runtime = RuntimeOptions()
        return await self.query_available_numbers_with_options_async(request, runtime)

    def query_bag_remaining_with_options(
        self,
        request: main_models.QueryBagRemainingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBagRemainingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBagRemaining',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBagRemainingResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bag_remaining_with_options_async(
        self,
        request: main_models.QueryBagRemainingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBagRemainingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBagRemaining',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBagRemainingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bag_remaining(
        self,
        request: main_models.QueryBagRemainingRequest,
    ) -> main_models.QueryBagRemainingResponse:
        runtime = RuntimeOptions()
        return self.query_bag_remaining_with_options(request, runtime)

    async def query_bag_remaining_async(
        self,
        request: main_models.QueryBagRemainingRequest,
    ) -> main_models.QueryBagRemainingResponse:
        runtime = RuntimeOptions()
        return await self.query_bag_remaining_with_options_async(request, runtime)

    def query_call_record_list_with_options(
        self,
        request: main_models.QueryCallRecordListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallRecordListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.skill_type):
            query['SkillType'] = request.skill_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallRecordList',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallRecordListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_record_list_with_options_async(
        self,
        request: main_models.QueryCallRecordListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallRecordListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.skill_type):
            query['SkillType'] = request.skill_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallRecordList',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallRecordListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_record_list(
        self,
        request: main_models.QueryCallRecordListRequest,
    ) -> main_models.QueryCallRecordListResponse:
        runtime = RuntimeOptions()
        return self.query_call_record_list_with_options(request, runtime)

    async def query_call_record_list_async(
        self,
        request: main_models.QueryCallRecordListRequest,
    ) -> main_models.QueryCallRecordListResponse:
        runtime = RuntimeOptions()
        return await self.query_call_record_list_with_options_async(request, runtime)

    def query_instance_with_options(
        self,
        request: main_models.QueryInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstance',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_with_options_async(
        self,
        request: main_models.QueryInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstance',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance(
        self,
        request: main_models.QueryInstanceRequest,
    ) -> main_models.QueryInstanceResponse:
        runtime = RuntimeOptions()
        return self.query_instance_with_options(request, runtime)

    async def query_instance_async(
        self,
        request: main_models.QueryInstanceRequest,
    ) -> main_models.QueryInstanceResponse:
        runtime = RuntimeOptions()
        return await self.query_instance_with_options_async(request, runtime)

    def query_partner_intention_list_with_options(
        self,
        request: main_models.QueryPartnerIntentionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPartnerIntentionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPartnerIntentionList',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPartnerIntentionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_partner_intention_list_with_options_async(
        self,
        request: main_models.QueryPartnerIntentionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPartnerIntentionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPartnerIntentionList',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPartnerIntentionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_partner_intention_list(
        self,
        request: main_models.QueryPartnerIntentionListRequest,
    ) -> main_models.QueryPartnerIntentionListResponse:
        runtime = RuntimeOptions()
        return self.query_partner_intention_list_with_options(request, runtime)

    async def query_partner_intention_list_async(
        self,
        request: main_models.QueryPartnerIntentionListRequest,
    ) -> main_models.QueryPartnerIntentionListResponse:
        runtime = RuntimeOptions()
        return await self.query_partner_intention_list_with_options_async(request, runtime)

    def query_partner_produce_list_with_options(
        self,
        request: main_models.QueryPartnerProduceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPartnerProduceListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPartnerProduceList',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPartnerProduceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_partner_produce_list_with_options_async(
        self,
        request: main_models.QueryPartnerProduceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPartnerProduceListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPartnerProduceList',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPartnerProduceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_partner_produce_list(
        self,
        request: main_models.QueryPartnerProduceListRequest,
    ) -> main_models.QueryPartnerProduceListResponse:
        runtime = RuntimeOptions()
        return self.query_partner_produce_list_with_options(request, runtime)

    async def query_partner_produce_list_async(
        self,
        request: main_models.QueryPartnerProduceListRequest,
    ) -> main_models.QueryPartnerProduceListResponse:
        runtime = RuntimeOptions()
        return await self.query_partner_produce_list_with_options_async(request, runtime)

    def query_user_need_auth_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserNeedAuthResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryUserNeedAuth',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserNeedAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_need_auth_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserNeedAuthResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryUserNeedAuth',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserNeedAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_need_auth(self) -> main_models.QueryUserNeedAuthResponse:
        runtime = RuntimeOptions()
        return self.query_user_need_auth_with_options(runtime)

    async def query_user_need_auth_async(self) -> main_models.QueryUserNeedAuthResponse:
        runtime = RuntimeOptions()
        return await self.query_user_need_auth_with_options_async(runtime)

    def record_call_center_event_for_partner_with_options(
        self,
        request: main_models.RecordCallCenterEventForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordCallCenterEventForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.call_action):
            query['CallAction'] = request.call_action
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.conn_id):
            query['ConnId'] = request.conn_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.related_id):
            query['RelatedId'] = request.related_id
        if not DaraCore.is_null(request.secret_mobile):
            query['SecretMobile'] = request.secret_mobile
        if not DaraCore.is_null(request.skill_type):
            query['SkillType'] = request.skill_type
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordCallCenterEventForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordCallCenterEventForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_call_center_event_for_partner_with_options_async(
        self,
        request: main_models.RecordCallCenterEventForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordCallCenterEventForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.call_action):
            query['CallAction'] = request.call_action
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.conn_id):
            query['ConnId'] = request.conn_id
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.related_id):
            query['RelatedId'] = request.related_id
        if not DaraCore.is_null(request.secret_mobile):
            query['SecretMobile'] = request.secret_mobile
        if not DaraCore.is_null(request.skill_type):
            query['SkillType'] = request.skill_type
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordCallCenterEventForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordCallCenterEventForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_call_center_event_for_partner(
        self,
        request: main_models.RecordCallCenterEventForPartnerRequest,
    ) -> main_models.RecordCallCenterEventForPartnerResponse:
        runtime = RuntimeOptions()
        return self.record_call_center_event_for_partner_with_options(request, runtime)

    async def record_call_center_event_for_partner_async(
        self,
        request: main_models.RecordCallCenterEventForPartnerRequest,
    ) -> main_models.RecordCallCenterEventForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.record_call_center_event_for_partner_with_options_async(request, runtime)

    def record_post_back_with_options(
        self,
        request: main_models.RecordPostBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordPostBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['bizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.contactor):
            query['contactor'] = request.contactor
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.entity_key):
            query['entityKey'] = request.entity_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordPostBack',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordPostBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_post_back_with_options_async(
        self,
        request: main_models.RecordPostBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordPostBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['bizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.contactor):
            query['contactor'] = request.contactor
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.entity_key):
            query['entityKey'] = request.entity_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordPostBack',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordPostBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_post_back(
        self,
        request: main_models.RecordPostBackRequest,
    ) -> main_models.RecordPostBackResponse:
        runtime = RuntimeOptions()
        return self.record_post_back_with_options(request, runtime)

    async def record_post_back_async(
        self,
        request: main_models.RecordPostBackRequest,
    ) -> main_models.RecordPostBackResponse:
        runtime = RuntimeOptions()
        return await self.record_post_back_with_options_async(request, runtime)

    def reject_solution_with_options(
        self,
        request: main_models.RejectSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.solution_biz_id):
            query['SolutionBizId'] = request.solution_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectSolution',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_solution_with_options_async(
        self,
        request: main_models.RejectSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.solution_biz_id):
            query['SolutionBizId'] = request.solution_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectSolution',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_solution(
        self,
        request: main_models.RejectSolutionRequest,
    ) -> main_models.RejectSolutionResponse:
        runtime = RuntimeOptions()
        return self.reject_solution_with_options(request, runtime)

    async def reject_solution_async(
        self,
        request: main_models.RejectSolutionRequest,
    ) -> main_models.RejectSolutionResponse:
        runtime = RuntimeOptions()
        return await self.reject_solution_with_options_async(request, runtime)

    def reject_user_solution_with_options(
        self,
        request: main_models.RejectUserSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectUserSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.solution_biz_id):
            query['SolutionBizId'] = request.solution_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectUserSolution',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectUserSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_user_solution_with_options_async(
        self,
        request: main_models.RejectUserSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectUserSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.solution_biz_id):
            query['SolutionBizId'] = request.solution_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectUserSolution',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectUserSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_user_solution(
        self,
        request: main_models.RejectUserSolutionRequest,
    ) -> main_models.RejectUserSolutionResponse:
        runtime = RuntimeOptions()
        return self.reject_user_solution_with_options(request, runtime)

    async def reject_user_solution_async(
        self,
        request: main_models.RejectUserSolutionRequest,
    ) -> main_models.RejectUserSolutionResponse:
        runtime = RuntimeOptions()
        return await self.reject_user_solution_with_options_async(request, runtime)

    def release_produce_authorization_with_options(
        self,
        request: main_models.ReleaseProduceAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseProduceAuthorizationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorized_user_id):
            body['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseProduceAuthorization',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseProduceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_produce_authorization_with_options_async(
        self,
        request: main_models.ReleaseProduceAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseProduceAuthorizationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorized_user_id):
            body['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseProduceAuthorization',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseProduceAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_produce_authorization(
        self,
        request: main_models.ReleaseProduceAuthorizationRequest,
    ) -> main_models.ReleaseProduceAuthorizationResponse:
        runtime = RuntimeOptions()
        return self.release_produce_authorization_with_options(request, runtime)

    async def release_produce_authorization_async(
        self,
        request: main_models.ReleaseProduceAuthorizationRequest,
    ) -> main_models.ReleaseProduceAuthorizationResponse:
        runtime = RuntimeOptions()
        return await self.release_produce_authorization_with_options_async(request, runtime)

    def start_back_to_back_call_with_options(
        self,
        request: main_models.StartBackToBackCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBackToBackCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.call_center_number):
            query['CallCenterNumber'] = request.call_center_number
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.mobile_key):
            query['MobileKey'] = request.mobile_key
        if not DaraCore.is_null(request.skill_type):
            query['SkillType'] = request.skill_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBackToBackCall',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBackToBackCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_back_to_back_call_with_options_async(
        self,
        request: main_models.StartBackToBackCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBackToBackCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.call_center_number):
            query['CallCenterNumber'] = request.call_center_number
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.mobile_key):
            query['MobileKey'] = request.mobile_key
        if not DaraCore.is_null(request.skill_type):
            query['SkillType'] = request.skill_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBackToBackCall',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBackToBackCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_back_to_back_call(
        self,
        request: main_models.StartBackToBackCallRequest,
    ) -> main_models.StartBackToBackCallResponse:
        runtime = RuntimeOptions()
        return self.start_back_to_back_call_with_options(request, runtime)

    async def start_back_to_back_call_async(
        self,
        request: main_models.StartBackToBackCallRequest,
    ) -> main_models.StartBackToBackCallResponse:
        runtime = RuntimeOptions()
        return await self.start_back_to_back_call_with_options_async(request, runtime)

    def submit_intention_for_partner_with_options(
        self,
        request: main_models.SubmitIntentionForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIntentionForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.commodity_type):
            query['CommodityType'] = request.commodity_type
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.grade):
            query['Grade'] = request.grade
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIntentionForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIntentionForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_intention_for_partner_with_options_async(
        self,
        request: main_models.SubmitIntentionForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIntentionForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.commodity_type):
            query['CommodityType'] = request.commodity_type
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not DaraCore.is_null(request.grade):
            query['Grade'] = request.grade
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIntentionForPartner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIntentionForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_intention_for_partner(
        self,
        request: main_models.SubmitIntentionForPartnerRequest,
    ) -> main_models.SubmitIntentionForPartnerResponse:
        runtime = RuntimeOptions()
        return self.submit_intention_for_partner_with_options(request, runtime)

    async def submit_intention_for_partner_async(
        self,
        request: main_models.SubmitIntentionForPartnerRequest,
    ) -> main_models.SubmitIntentionForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.submit_intention_for_partner_with_options_async(request, runtime)

    def submit_intention_note_with_options(
        self,
        request: main_models.SubmitIntentionNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIntentionNoteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIntentionNote',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIntentionNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_intention_note_with_options_async(
        self,
        request: main_models.SubmitIntentionNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIntentionNoteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIntentionNote',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIntentionNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_intention_note(
        self,
        request: main_models.SubmitIntentionNoteRequest,
    ) -> main_models.SubmitIntentionNoteResponse:
        runtime = RuntimeOptions()
        return self.submit_intention_note_with_options(request, runtime)

    async def submit_intention_note_async(
        self,
        request: main_models.SubmitIntentionNoteRequest,
    ) -> main_models.SubmitIntentionNoteResponse:
        runtime = RuntimeOptions()
        return await self.submit_intention_note_with_options_async(request, runtime)

    def submit_solution_with_options(
        self,
        request: main_models.SubmitSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.solution):
            query['Solution'] = request.solution
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSolution',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_solution_with_options_async(
        self,
        request: main_models.SubmitSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.solution):
            query['Solution'] = request.solution
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSolution',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_solution(
        self,
        request: main_models.SubmitSolutionRequest,
    ) -> main_models.SubmitSolutionResponse:
        runtime = RuntimeOptions()
        return self.submit_solution_with_options(request, runtime)

    async def submit_solution_async(
        self,
        request: main_models.SubmitSolutionRequest,
    ) -> main_models.SubmitSolutionResponse:
        runtime = RuntimeOptions()
        return await self.submit_solution_with_options_async(request, runtime)

    def transfer_intention_owner_with_options(
        self,
        request: main_models.TransferIntentionOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferIntentionOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferIntentionOwner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferIntentionOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_intention_owner_with_options_async(
        self,
        request: main_models.TransferIntentionOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferIntentionOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferIntentionOwner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferIntentionOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_intention_owner(
        self,
        request: main_models.TransferIntentionOwnerRequest,
    ) -> main_models.TransferIntentionOwnerResponse:
        runtime = RuntimeOptions()
        return self.transfer_intention_owner_with_options(request, runtime)

    async def transfer_intention_owner_async(
        self,
        request: main_models.TransferIntentionOwnerRequest,
    ) -> main_models.TransferIntentionOwnerResponse:
        runtime = RuntimeOptions()
        return await self.transfer_intention_owner_with_options_async(request, runtime)

    def transfer_produce_owner_with_options(
        self,
        request: main_models.TransferProduceOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferProduceOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferProduceOwner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferProduceOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_produce_owner_with_options_async(
        self,
        request: main_models.TransferProduceOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferProduceOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.employee_code):
            query['EmployeeCode'] = request.employee_code
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferProduceOwner',
            version = '2020-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferProduceOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_produce_owner(
        self,
        request: main_models.TransferProduceOwnerRequest,
    ) -> main_models.TransferProduceOwnerResponse:
        runtime = RuntimeOptions()
        return self.transfer_produce_owner_with_options(request, runtime)

    async def transfer_produce_owner_async(
        self,
        request: main_models.TransferProduceOwnerRequest,
    ) -> main_models.TransferProduceOwnerResponse:
        runtime = RuntimeOptions()
        return await self.transfer_produce_owner_with_options_async(request, runtime)
