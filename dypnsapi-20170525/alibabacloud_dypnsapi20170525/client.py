# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dypnsapi20170525 import models as dypnsapi_20170525_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('dypnsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_verify_scheme_with_options(
        self,
        request: dypnsapi_20170525_models.CreateVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.CreateVerifySchemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.CreateVerifySchemeResponse().from_map(
            self.do_rpcrequest('CreateVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_verify_scheme_with_options_async(
        self,
        request: dypnsapi_20170525_models.CreateVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.CreateVerifySchemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.CreateVerifySchemeResponse().from_map(
            await self.do_rpcrequest_async('CreateVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_verify_scheme(
        self,
        request: dypnsapi_20170525_models.CreateVerifySchemeRequest,
    ) -> dypnsapi_20170525_models.CreateVerifySchemeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_verify_scheme_with_options(request, runtime)

    async def create_verify_scheme_async(
        self,
        request: dypnsapi_20170525_models.CreateVerifySchemeRequest,
    ) -> dypnsapi_20170525_models.CreateVerifySchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_verify_scheme_with_options_async(request, runtime)

    def delete_verify_scheme_with_options(
        self,
        request: dypnsapi_20170525_models.DeleteVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.DeleteVerifySchemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.DeleteVerifySchemeResponse().from_map(
            self.do_rpcrequest('DeleteVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_verify_scheme_with_options_async(
        self,
        request: dypnsapi_20170525_models.DeleteVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.DeleteVerifySchemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.DeleteVerifySchemeResponse().from_map(
            await self.do_rpcrequest_async('DeleteVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_verify_scheme(
        self,
        request: dypnsapi_20170525_models.DeleteVerifySchemeRequest,
    ) -> dypnsapi_20170525_models.DeleteVerifySchemeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_verify_scheme_with_options(request, runtime)

    async def delete_verify_scheme_async(
        self,
        request: dypnsapi_20170525_models.DeleteVerifySchemeRequest,
    ) -> dypnsapi_20170525_models.DeleteVerifySchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_verify_scheme_with_options_async(request, runtime)

    def describe_verify_scheme_with_options(
        self,
        request: dypnsapi_20170525_models.DescribeVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.DescribeVerifySchemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.DescribeVerifySchemeResponse().from_map(
            self.do_rpcrequest('DescribeVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_scheme_with_options_async(
        self,
        request: dypnsapi_20170525_models.DescribeVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.DescribeVerifySchemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.DescribeVerifySchemeResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_scheme(
        self,
        request: dypnsapi_20170525_models.DescribeVerifySchemeRequest,
    ) -> dypnsapi_20170525_models.DescribeVerifySchemeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_scheme_with_options(request, runtime)

    async def describe_verify_scheme_async(
        self,
        request: dypnsapi_20170525_models.DescribeVerifySchemeRequest,
    ) -> dypnsapi_20170525_models.DescribeVerifySchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_scheme_with_options_async(request, runtime)

    def get_authorization_url_with_options(
        self,
        request: dypnsapi_20170525_models.GetAuthorizationUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthorizationUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetAuthorizationUrlResponse().from_map(
            self.do_rpcrequest('GetAuthorizationUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_authorization_url_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetAuthorizationUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthorizationUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetAuthorizationUrlResponse().from_map(
            await self.do_rpcrequest_async('GetAuthorizationUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_authorization_url(
        self,
        request: dypnsapi_20170525_models.GetAuthorizationUrlRequest,
    ) -> dypnsapi_20170525_models.GetAuthorizationUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_url_with_options(request, runtime)

    async def get_authorization_url_async(
        self,
        request: dypnsapi_20170525_models.GetAuthorizationUrlRequest,
    ) -> dypnsapi_20170525_models.GetAuthorizationUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_authorization_url_with_options_async(request, runtime)

    def get_auth_token_with_options(
        self,
        request: dypnsapi_20170525_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetAuthTokenResponse().from_map(
            self.do_rpcrequest('GetAuthToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_auth_token_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetAuthTokenResponse().from_map(
            await self.do_rpcrequest_async('GetAuthToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auth_token(
        self,
        request: dypnsapi_20170525_models.GetAuthTokenRequest,
    ) -> dypnsapi_20170525_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    async def get_auth_token_async(
        self,
        request: dypnsapi_20170525_models.GetAuthTokenRequest,
    ) -> dypnsapi_20170525_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auth_token_with_options_async(request, runtime)

    def get_certify_result_with_options(
        self,
        request: dypnsapi_20170525_models.GetCertifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetCertifyResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetCertifyResultResponse().from_map(
            self.do_rpcrequest('GetCertifyResult', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_certify_result_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetCertifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetCertifyResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetCertifyResultResponse().from_map(
            await self.do_rpcrequest_async('GetCertifyResult', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_certify_result(
        self,
        request: dypnsapi_20170525_models.GetCertifyResultRequest,
    ) -> dypnsapi_20170525_models.GetCertifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_certify_result_with_options(request, runtime)

    async def get_certify_result_async(
        self,
        request: dypnsapi_20170525_models.GetCertifyResultRequest,
    ) -> dypnsapi_20170525_models.GetCertifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_certify_result_with_options_async(request, runtime)

    def get_mobile_with_options(
        self,
        request: dypnsapi_20170525_models.GetMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetMobileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetMobileResponse().from_map(
            self.do_rpcrequest('GetMobile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_mobile_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetMobileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.GetMobileResponse().from_map(
            await self.do_rpcrequest_async('GetMobile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mobile(
        self,
        request: dypnsapi_20170525_models.GetMobileRequest,
    ) -> dypnsapi_20170525_models.GetMobileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mobile_with_options(request, runtime)

    async def get_mobile_async(
        self,
        request: dypnsapi_20170525_models.GetMobileRequest,
    ) -> dypnsapi_20170525_models.GetMobileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mobile_with_options_async(request, runtime)

    def twice_tel_verify_with_options(
        self,
        request: dypnsapi_20170525_models.TwiceTelVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.TwiceTelVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.TwiceTelVerifyResponse().from_map(
            self.do_rpcrequest('TwiceTelVerify', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def twice_tel_verify_with_options_async(
        self,
        request: dypnsapi_20170525_models.TwiceTelVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.TwiceTelVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.TwiceTelVerifyResponse().from_map(
            await self.do_rpcrequest_async('TwiceTelVerify', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def twice_tel_verify(
        self,
        request: dypnsapi_20170525_models.TwiceTelVerifyRequest,
    ) -> dypnsapi_20170525_models.TwiceTelVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.twice_tel_verify_with_options(request, runtime)

    async def twice_tel_verify_async(
        self,
        request: dypnsapi_20170525_models.TwiceTelVerifyRequest,
    ) -> dypnsapi_20170525_models.TwiceTelVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.twice_tel_verify_with_options_async(request, runtime)

    def verify_mobile_with_options(
        self,
        request: dypnsapi_20170525_models.VerifyMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifyMobileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.VerifyMobileResponse().from_map(
            self.do_rpcrequest('VerifyMobile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_mobile_with_options_async(
        self,
        request: dypnsapi_20170525_models.VerifyMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifyMobileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.VerifyMobileResponse().from_map(
            await self.do_rpcrequest_async('VerifyMobile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_mobile(
        self,
        request: dypnsapi_20170525_models.VerifyMobileRequest,
    ) -> dypnsapi_20170525_models.VerifyMobileResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_mobile_with_options(request, runtime)

    async def verify_mobile_async(
        self,
        request: dypnsapi_20170525_models.VerifyMobileRequest,
    ) -> dypnsapi_20170525_models.VerifyMobileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_mobile_with_options_async(request, runtime)

    def verify_phone_with_token_with_options(
        self,
        request: dypnsapi_20170525_models.VerifyPhoneWithTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifyPhoneWithTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.VerifyPhoneWithTokenResponse().from_map(
            self.do_rpcrequest('VerifyPhoneWithToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_phone_with_token_with_options_async(
        self,
        request: dypnsapi_20170525_models.VerifyPhoneWithTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifyPhoneWithTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dypnsapi_20170525_models.VerifyPhoneWithTokenResponse().from_map(
            await self.do_rpcrequest_async('VerifyPhoneWithToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_phone_with_token(
        self,
        request: dypnsapi_20170525_models.VerifyPhoneWithTokenRequest,
    ) -> dypnsapi_20170525_models.VerifyPhoneWithTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_phone_with_token_with_options(request, runtime)

    async def verify_phone_with_token_async(
        self,
        request: dypnsapi_20170525_models.VerifyPhoneWithTokenRequest,
    ) -> dypnsapi_20170525_models.VerifyPhoneWithTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_phone_with_token_with_options_async(request, runtime)
