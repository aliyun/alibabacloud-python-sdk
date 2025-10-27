# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_captcha20230305 import models as captcha_20230305_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('captcha', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def verify_captcha_with_options(
        self,
        request: captcha_20230305_models.VerifyCaptchaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> captcha_20230305_models.VerifyCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyCaptchaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyCaptchaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.captcha_verify_param):
            query['CaptchaVerifyParam'] = request.captcha_verify_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCaptcha',
            version='2023-03-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            captcha_20230305_models.VerifyCaptchaResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_captcha_with_options_async(
        self,
        request: captcha_20230305_models.VerifyCaptchaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> captcha_20230305_models.VerifyCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyCaptchaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyCaptchaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.captcha_verify_param):
            query['CaptchaVerifyParam'] = request.captcha_verify_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCaptcha',
            version='2023-03-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            captcha_20230305_models.VerifyCaptchaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_captcha(
        self,
        request: captcha_20230305_models.VerifyCaptchaRequest,
    ) -> captcha_20230305_models.VerifyCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyCaptchaRequest
        @return: VerifyCaptchaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_captcha_with_options(request, runtime)

    async def verify_captcha_async(
        self,
        request: captcha_20230305_models.VerifyCaptchaRequest,
    ) -> captcha_20230305_models.VerifyCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyCaptchaRequest
        @return: VerifyCaptchaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_captcha_with_options_async(request, runtime)

    def verify_intelligent_captcha_with_options(
        self,
        request: captcha_20230305_models.VerifyIntelligentCaptchaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> captcha_20230305_models.VerifyIntelligentCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyIntelligentCaptchaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyIntelligentCaptchaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.captcha_verify_param):
            body['CaptchaVerifyParam'] = request.captcha_verify_param
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyIntelligentCaptcha',
            version='2023-03-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            captcha_20230305_models.VerifyIntelligentCaptchaResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_intelligent_captcha_with_options_async(
        self,
        request: captcha_20230305_models.VerifyIntelligentCaptchaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> captcha_20230305_models.VerifyIntelligentCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyIntelligentCaptchaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyIntelligentCaptchaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.captcha_verify_param):
            body['CaptchaVerifyParam'] = request.captcha_verify_param
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyIntelligentCaptcha',
            version='2023-03-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            captcha_20230305_models.VerifyIntelligentCaptchaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_intelligent_captcha(
        self,
        request: captcha_20230305_models.VerifyIntelligentCaptchaRequest,
    ) -> captcha_20230305_models.VerifyIntelligentCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyIntelligentCaptchaRequest
        @return: VerifyIntelligentCaptchaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_intelligent_captcha_with_options(request, runtime)

    async def verify_intelligent_captcha_async(
        self,
        request: captcha_20230305_models.VerifyIntelligentCaptchaRequest,
    ) -> captcha_20230305_models.VerifyIntelligentCaptchaResponse:
        """
        @summary 验证码验证
        
        @param request: VerifyIntelligentCaptchaRequest
        @return: VerifyIntelligentCaptchaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_intelligent_captcha_with_options_async(request, runtime)
