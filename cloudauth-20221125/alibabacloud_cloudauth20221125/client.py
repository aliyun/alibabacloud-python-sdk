# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudauth20221125 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def ent_element_verify_with_options(
        self,
        request: main_models.EntElementVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntElementVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntElementVerify',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntElementVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ent_element_verify_with_options_async(
        self,
        request: main_models.EntElementVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntElementVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntElementVerify',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntElementVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ent_element_verify(
        self,
        request: main_models.EntElementVerifyRequest,
    ) -> main_models.EntElementVerifyResponse:
        runtime = RuntimeOptions()
        return self.ent_element_verify_with_options(request, runtime)

    async def ent_element_verify_async(
        self,
        request: main_models.EntElementVerifyRequest,
    ) -> main_models.EntElementVerifyResponse:
        runtime = RuntimeOptions()
        return await self.ent_element_verify_with_options_async(request, runtime)

    def ent_element_verify_prowith_options(
        self,
        request: main_models.EntElementVerifyPRORequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntElementVerifyPROResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntElementVerifyPRO',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntElementVerifyPROResponse(),
            self.call_api(params, req, runtime)
        )

    async def ent_element_verify_prowith_options_async(
        self,
        request: main_models.EntElementVerifyPRORequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntElementVerifyPROResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntElementVerifyPRO',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntElementVerifyPROResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ent_element_verify_pro(
        self,
        request: main_models.EntElementVerifyPRORequest,
    ) -> main_models.EntElementVerifyPROResponse:
        runtime = RuntimeOptions()
        return self.ent_element_verify_prowith_options(request, runtime)

    async def ent_element_verify_pro_async(
        self,
        request: main_models.EntElementVerifyPRORequest,
    ) -> main_models.EntElementVerifyPROResponse:
        runtime = RuntimeOptions()
        return await self.ent_element_verify_prowith_options_async(request, runtime)

    def ent_element_verify_v2with_options(
        self,
        request: main_models.EntElementVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.EntElementVerifyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntElementVerifyV2',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntElementVerifyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def ent_element_verify_v2with_options_async(
        self,
        request: main_models.EntElementVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.EntElementVerifyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntElementVerifyV2',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntElementVerifyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def ent_element_verify_v2(
        self,
        request: main_models.EntElementVerifyV2Request,
    ) -> main_models.EntElementVerifyV2Response:
        runtime = RuntimeOptions()
        return self.ent_element_verify_v2with_options(request, runtime)

    async def ent_element_verify_v2_async(
        self,
        request: main_models.EntElementVerifyV2Request,
    ) -> main_models.EntElementVerifyV2Response:
        runtime = RuntimeOptions()
        return await self.ent_element_verify_v2with_options_async(request, runtime)

    def ent_risk_query_with_options(
        self,
        request: main_models.EntRiskQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntRiskQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.param_value):
            query['ParamValue'] = request.param_value
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntRiskQuery',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntRiskQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def ent_risk_query_with_options_async(
        self,
        request: main_models.EntRiskQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntRiskQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.param_value):
            query['ParamValue'] = request.param_value
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntRiskQuery',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntRiskQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ent_risk_query(
        self,
        request: main_models.EntRiskQueryRequest,
    ) -> main_models.EntRiskQueryResponse:
        runtime = RuntimeOptions()
        return self.ent_risk_query_with_options(request, runtime)

    async def ent_risk_query_async(
        self,
        request: main_models.EntRiskQueryRequest,
    ) -> main_models.EntRiskQueryResponse:
        runtime = RuntimeOptions()
        return await self.ent_risk_query_with_options_async(request, runtime)

    def ent_verify_with_options(
        self,
        request: main_models.EntVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_no):
            query['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_mobile):
            query['LegalPersonMobile'] = request.legal_person_mobile
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.risk_model_version):
            query['RiskModelVersion'] = request.risk_model_version
        if not DaraCore.is_null(request.risk_verify_type):
            query['RiskVerifyType'] = request.risk_verify_type
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntVerify',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ent_verify_with_options_async(
        self,
        request: main_models.EntVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EntVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_no):
            query['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.ent_name):
            query['EntName'] = request.ent_name
        if not DaraCore.is_null(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not DaraCore.is_null(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not DaraCore.is_null(request.legal_person_mobile):
            query['LegalPersonMobile'] = request.legal_person_mobile
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.license_no):
            query['LicenseNo'] = request.license_no
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.risk_model_version):
            query['RiskModelVersion'] = request.risk_model_version
        if not DaraCore.is_null(request.risk_verify_type):
            query['RiskVerifyType'] = request.risk_verify_type
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EntVerify',
            version = '2022-11-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EntVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ent_verify(
        self,
        request: main_models.EntVerifyRequest,
    ) -> main_models.EntVerifyResponse:
        runtime = RuntimeOptions()
        return self.ent_verify_with_options(request, runtime)

    async def ent_verify_async(
        self,
        request: main_models.EntVerifyRequest,
    ) -> main_models.EntVerifyResponse:
        runtime = RuntimeOptions()
        return await self.ent_verify_with_options_async(request, runtime)
