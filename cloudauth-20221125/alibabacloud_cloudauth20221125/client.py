# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20221125 import models as cloudauth_20221125_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def ent_element_verify_with_options(
        self,
        request: cloudauth_20221125_models.EntElementVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntElementVerifyResponse:
        """
        @summary 企业要素核验
        
        @param request: EntElementVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntElementVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntElementVerify',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntElementVerifyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntElementVerifyResponse(),
                self.execute(params, req, runtime)
            )

    async def ent_element_verify_with_options_async(
        self,
        request: cloudauth_20221125_models.EntElementVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntElementVerifyResponse:
        """
        @summary 企业要素核验
        
        @param request: EntElementVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntElementVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntElementVerify',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntElementVerifyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntElementVerifyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def ent_element_verify(
        self,
        request: cloudauth_20221125_models.EntElementVerifyRequest,
    ) -> cloudauth_20221125_models.EntElementVerifyResponse:
        """
        @summary 企业要素核验
        
        @param request: EntElementVerifyRequest
        @return: EntElementVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ent_element_verify_with_options(request, runtime)

    async def ent_element_verify_async(
        self,
        request: cloudauth_20221125_models.EntElementVerifyRequest,
    ) -> cloudauth_20221125_models.EntElementVerifyResponse:
        """
        @summary 企业要素核验
        
        @param request: EntElementVerifyRequest
        @return: EntElementVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ent_element_verify_with_options_async(request, runtime)

    def ent_element_verify_v2with_options(
        self,
        request: cloudauth_20221125_models.EntElementVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntElementVerifyV2Response:
        """
        @summary 企业要素验证V2
        
        @param request: EntElementVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntElementVerifyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntElementVerifyV2',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntElementVerifyV2Response(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntElementVerifyV2Response(),
                self.execute(params, req, runtime)
            )

    async def ent_element_verify_v2with_options_async(
        self,
        request: cloudauth_20221125_models.EntElementVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntElementVerifyV2Response:
        """
        @summary 企业要素验证V2
        
        @param request: EntElementVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntElementVerifyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntElementVerifyV2',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntElementVerifyV2Response(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntElementVerifyV2Response(),
                await self.execute_async(params, req, runtime)
            )

    def ent_element_verify_v2(
        self,
        request: cloudauth_20221125_models.EntElementVerifyV2Request,
    ) -> cloudauth_20221125_models.EntElementVerifyV2Response:
        """
        @summary 企业要素验证V2
        
        @param request: EntElementVerifyV2Request
        @return: EntElementVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.ent_element_verify_v2with_options(request, runtime)

    async def ent_element_verify_v2_async(
        self,
        request: cloudauth_20221125_models.EntElementVerifyV2Request,
    ) -> cloudauth_20221125_models.EntElementVerifyV2Response:
        """
        @summary 企业要素验证V2
        
        @param request: EntElementVerifyV2Request
        @return: EntElementVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.ent_element_verify_v2with_options_async(request, runtime)

    def ent_risk_query_with_options(
        self,
        request: cloudauth_20221125_models.EntRiskQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntRiskQueryResponse:
        """
        @summary 企业经营异常查询
        
        @param request: EntRiskQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntRiskQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.param_value):
            query['ParamValue'] = request.param_value
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntRiskQuery',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntRiskQueryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntRiskQueryResponse(),
                self.execute(params, req, runtime)
            )

    async def ent_risk_query_with_options_async(
        self,
        request: cloudauth_20221125_models.EntRiskQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntRiskQueryResponse:
        """
        @summary 企业经营异常查询
        
        @param request: EntRiskQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntRiskQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.param_value):
            query['ParamValue'] = request.param_value
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntRiskQuery',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntRiskQueryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntRiskQueryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def ent_risk_query(
        self,
        request: cloudauth_20221125_models.EntRiskQueryRequest,
    ) -> cloudauth_20221125_models.EntRiskQueryResponse:
        """
        @summary 企业经营异常查询
        
        @param request: EntRiskQueryRequest
        @return: EntRiskQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ent_risk_query_with_options(request, runtime)

    async def ent_risk_query_async(
        self,
        request: cloudauth_20221125_models.EntRiskQueryRequest,
    ) -> cloudauth_20221125_models.EntRiskQueryResponse:
        """
        @summary 企业经营异常查询
        
        @param request: EntRiskQueryRequest
        @return: EntRiskQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ent_risk_query_with_options_async(request, runtime)

    def ent_verify_with_options(
        self,
        request: cloudauth_20221125_models.EntVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntVerifyResponse:
        """
        @summary 企业认证
        
        @param request: EntVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_no):
            query['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_mobile):
            query['LegalPersonMobile'] = request.legal_person_mobile
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.risk_model_version):
            query['RiskModelVersion'] = request.risk_model_version
        if not UtilClient.is_unset(request.risk_verify_type):
            query['RiskVerifyType'] = request.risk_verify_type
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntVerify',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntVerifyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntVerifyResponse(),
                self.execute(params, req, runtime)
            )

    async def ent_verify_with_options_async(
        self,
        request: cloudauth_20221125_models.EntVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20221125_models.EntVerifyResponse:
        """
        @summary 企业认证
        
        @param request: EntVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EntVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_no):
            query['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_mobile):
            query['LegalPersonMobile'] = request.legal_person_mobile
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.risk_model_version):
            query['RiskModelVersion'] = request.risk_model_version
        if not UtilClient.is_unset(request.risk_verify_type):
            query['RiskVerifyType'] = request.risk_verify_type
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntVerify',
            version='2022-11-25',
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
                cloudauth_20221125_models.EntVerifyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cloudauth_20221125_models.EntVerifyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def ent_verify(
        self,
        request: cloudauth_20221125_models.EntVerifyRequest,
    ) -> cloudauth_20221125_models.EntVerifyResponse:
        """
        @summary 企业认证
        
        @param request: EntVerifyRequest
        @return: EntVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ent_verify_with_options(request, runtime)

    async def ent_verify_async(
        self,
        request: cloudauth_20221125_models.EntVerifyRequest,
    ) -> cloudauth_20221125_models.EntVerifyResponse:
        """
        @summary 企业认证
        
        @param request: EntVerifyRequest
        @return: EntVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ent_verify_with_options_async(request, runtime)
