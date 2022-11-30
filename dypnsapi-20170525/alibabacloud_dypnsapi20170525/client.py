# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dypnsapi20170525 import models as dypnsapi_20170525_models
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
        self._signature_algorithm = 'v2'
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
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not UtilClient.is_unset(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not UtilClient.is_unset(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pack_name):
            query['PackName'] = request.pack_name
        if not UtilClient.is_unset(request.pack_sign):
            query['PackSign'] = request.pack_sign
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not UtilClient.is_unset(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVerifyScheme',
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
            dypnsapi_20170525_models.CreateVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_verify_scheme_with_options_async(
        self,
        request: dypnsapi_20170525_models.CreateVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.CreateVerifySchemeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not UtilClient.is_unset(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not UtilClient.is_unset(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pack_name):
            query['PackName'] = request.pack_name
        if not UtilClient.is_unset(request.pack_sign):
            query['PackSign'] = request.pack_sign
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not UtilClient.is_unset(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVerifyScheme',
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
            dypnsapi_20170525_models.CreateVerifySchemeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_code):
            query['SchemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVerifyScheme',
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
            dypnsapi_20170525_models.DeleteVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_verify_scheme_with_options_async(
        self,
        request: dypnsapi_20170525_models.DeleteVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.DeleteVerifySchemeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_code):
            query['SchemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVerifyScheme',
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
            dypnsapi_20170525_models.DeleteVerifySchemeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_code):
            query['SchemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyScheme',
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
            dypnsapi_20170525_models.DescribeVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_scheme_with_options_async(
        self,
        request: dypnsapi_20170525_models.DescribeVerifySchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.DescribeVerifySchemeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_code):
            query['SchemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyScheme',
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
            dypnsapi_20170525_models.DescribeVerifySchemeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_auth_token_with_options(
        self,
        request: dypnsapi_20170525_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthToken',
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
            dypnsapi_20170525_models.GetAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auth_token_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthToken',
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
            dypnsapi_20170525_models.GetAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_authorization_url_with_options(
        self,
        request: dypnsapi_20170525_models.GetAuthorizationUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthorizationUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorizationUrl',
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
            dypnsapi_20170525_models.GetAuthorizationUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_authorization_url_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetAuthorizationUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetAuthorizationUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorizationUrl',
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
            dypnsapi_20170525_models.GetAuthorizationUrlResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_certify_result_with_options(
        self,
        request: dypnsapi_20170525_models.GetCertifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetCertifyResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCertifyResult',
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
            dypnsapi_20170525_models.GetCertifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_certify_result_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetCertifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetCertifyResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCertifyResult',
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
            dypnsapi_20170525_models.GetCertifyResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
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
            action='GetMobile',
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
            dypnsapi_20170525_models.GetMobileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mobile_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetMobileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
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
            action='GetMobile',
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
            dypnsapi_20170525_models.GetMobileResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_phone_with_token_with_options(
        self,
        request: dypnsapi_20170525_models.GetPhoneWithTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetPhoneWithTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sp_token):
            query['SpToken'] = request.sp_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneWithToken',
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
            dypnsapi_20170525_models.GetPhoneWithTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_with_token_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetPhoneWithTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetPhoneWithTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sp_token):
            query['SpToken'] = request.sp_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneWithToken',
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
            dypnsapi_20170525_models.GetPhoneWithTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_with_token(
        self,
        request: dypnsapi_20170525_models.GetPhoneWithTokenRequest,
    ) -> dypnsapi_20170525_models.GetPhoneWithTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_phone_with_token_with_options(request, runtime)

    async def get_phone_with_token_async(
        self,
        request: dypnsapi_20170525_models.GetPhoneWithTokenRequest,
    ) -> dypnsapi_20170525_models.GetPhoneWithTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_phone_with_token_with_options_async(request, runtime)

    def get_sms_auth_tokens_with_options(
        self,
        request: dypnsapi_20170525_models.GetSmsAuthTokensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetSmsAuthTokensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_code_expire):
            query['SmsCodeExpire'] = request.sms_code_expire
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsAuthTokens',
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
            dypnsapi_20170525_models.GetSmsAuthTokensResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_auth_tokens_with_options_async(
        self,
        request: dypnsapi_20170525_models.GetSmsAuthTokensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.GetSmsAuthTokensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_code_expire):
            query['SmsCodeExpire'] = request.sms_code_expire
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsAuthTokens',
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
            dypnsapi_20170525_models.GetSmsAuthTokensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_auth_tokens(
        self,
        request: dypnsapi_20170525_models.GetSmsAuthTokensRequest,
    ) -> dypnsapi_20170525_models.GetSmsAuthTokensResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sms_auth_tokens_with_options(request, runtime)

    async def get_sms_auth_tokens_async(
        self,
        request: dypnsapi_20170525_models.GetSmsAuthTokensRequest,
    ) -> dypnsapi_20170525_models.GetSmsAuthTokensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sms_auth_tokens_with_options_async(request, runtime)

    def query_gate_verify_billing_public_with_options(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyBillingPublicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.QueryGateVerifyBillingPublicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGateVerifyBillingPublic',
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
            dypnsapi_20170525_models.QueryGateVerifyBillingPublicResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gate_verify_billing_public_with_options_async(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyBillingPublicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.QueryGateVerifyBillingPublicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGateVerifyBillingPublic',
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
            dypnsapi_20170525_models.QueryGateVerifyBillingPublicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gate_verify_billing_public(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyBillingPublicRequest,
    ) -> dypnsapi_20170525_models.QueryGateVerifyBillingPublicResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_gate_verify_billing_public_with_options(request, runtime)

    async def query_gate_verify_billing_public_async(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyBillingPublicRequest,
    ) -> dypnsapi_20170525_models.QueryGateVerifyBillingPublicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_gate_verify_billing_public_with_options_async(request, runtime)

    def query_gate_verify_statistic_public_with_options(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyStatisticPublicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.QueryGateVerifyStatisticPublicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGateVerifyStatisticPublic',
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
            dypnsapi_20170525_models.QueryGateVerifyStatisticPublicResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gate_verify_statistic_public_with_options_async(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyStatisticPublicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.QueryGateVerifyStatisticPublicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGateVerifyStatisticPublic',
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
            dypnsapi_20170525_models.QueryGateVerifyStatisticPublicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gate_verify_statistic_public(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyStatisticPublicRequest,
    ) -> dypnsapi_20170525_models.QueryGateVerifyStatisticPublicResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_gate_verify_statistic_public_with_options(request, runtime)

    async def query_gate_verify_statistic_public_async(
        self,
        request: dypnsapi_20170525_models.QueryGateVerifyStatisticPublicRequest,
    ) -> dypnsapi_20170525_models.QueryGateVerifyStatisticPublicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_gate_verify_statistic_public_with_options_async(request, runtime)

    def verify_mobile_with_options(
        self,
        request: dypnsapi_20170525_models.VerifyMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifyMobileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_code):
            query['AccessCode'] = request.access_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyMobile',
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
            dypnsapi_20170525_models.VerifyMobileResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_mobile_with_options_async(
        self,
        request: dypnsapi_20170525_models.VerifyMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifyMobileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_code):
            query['AccessCode'] = request.access_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyMobile',
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
            dypnsapi_20170525_models.VerifyMobileResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sp_token):
            query['SpToken'] = request.sp_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyPhoneWithToken',
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
            dypnsapi_20170525_models.VerifyPhoneWithTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_phone_with_token_with_options_async(
        self,
        request: dypnsapi_20170525_models.VerifyPhoneWithTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifyPhoneWithTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sp_token):
            query['SpToken'] = request.sp_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyPhoneWithToken',
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
            dypnsapi_20170525_models.VerifyPhoneWithTokenResponse(),
            await self.call_api_async(params, req, runtime)
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

    def verify_sms_code_with_options(
        self,
        request: dypnsapi_20170525_models.VerifySmsCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifySmsCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.sms_code):
            query['SmsCode'] = request.sms_code
        if not UtilClient.is_unset(request.sms_token):
            query['SmsToken'] = request.sms_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySmsCode',
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
            dypnsapi_20170525_models.VerifySmsCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_sms_code_with_options_async(
        self,
        request: dypnsapi_20170525_models.VerifySmsCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypnsapi_20170525_models.VerifySmsCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.sms_code):
            query['SmsCode'] = request.sms_code
        if not UtilClient.is_unset(request.sms_token):
            query['SmsToken'] = request.sms_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySmsCode',
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
            dypnsapi_20170525_models.VerifySmsCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_sms_code(
        self,
        request: dypnsapi_20170525_models.VerifySmsCodeRequest,
    ) -> dypnsapi_20170525_models.VerifySmsCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_sms_code_with_options(request, runtime)

    async def verify_sms_code_async(
        self,
        request: dypnsapi_20170525_models.VerifySmsCodeRequest,
    ) -> dypnsapi_20170525_models.VerifySmsCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_sms_code_with_options_async(request, runtime)
