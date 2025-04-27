# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_appstream_center20210220 import models as appstream_center_20210220_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('appstream-center', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def find_idp_list_by_login_identifier_with_options(
        self,
        tmp_req: appstream_center_20210220_models.FindIdpListByLoginIdentifierRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.FindIdpListByLoginIdentifierResponse:
        """
        @summary 身份认证查询接口
        
        @param tmp_req: FindIdpListByLoginIdentifierRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindIdpListByLoginIdentifierResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210220_models.FindIdpListByLoginIdentifierShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_features):
            request.available_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not UtilClient.is_unset(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        body = {}
        if not UtilClient.is_unset(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.login_identifier):
            body['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.support_types):
            body['SupportTypes'] = request.support_types
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindIdpListByLoginIdentifier',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.FindIdpListByLoginIdentifierResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_idp_list_by_login_identifier_with_options_async(
        self,
        tmp_req: appstream_center_20210220_models.FindIdpListByLoginIdentifierRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.FindIdpListByLoginIdentifierResponse:
        """
        @summary 身份认证查询接口
        
        @param tmp_req: FindIdpListByLoginIdentifierRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindIdpListByLoginIdentifierResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210220_models.FindIdpListByLoginIdentifierShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_features):
            request.available_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not UtilClient.is_unset(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        body = {}
        if not UtilClient.is_unset(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.login_identifier):
            body['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.support_types):
            body['SupportTypes'] = request.support_types
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindIdpListByLoginIdentifier',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.FindIdpListByLoginIdentifierResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_idp_list_by_login_identifier(
        self,
        request: appstream_center_20210220_models.FindIdpListByLoginIdentifierRequest,
    ) -> appstream_center_20210220_models.FindIdpListByLoginIdentifierResponse:
        """
        @summary 身份认证查询接口
        
        @param request: FindIdpListByLoginIdentifierRequest
        @return: FindIdpListByLoginIdentifierResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_idp_list_by_login_identifier_with_options(request, runtime)

    async def find_idp_list_by_login_identifier_async(
        self,
        request: appstream_center_20210220_models.FindIdpListByLoginIdentifierRequest,
    ) -> appstream_center_20210220_models.FindIdpListByLoginIdentifierResponse:
        """
        @summary 身份认证查询接口
        
        @param request: FindIdpListByLoginIdentifierRequest
        @return: FindIdpListByLoginIdentifierResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_idp_list_by_login_identifier_with_options_async(request, runtime)

    def get_login_token_with_options(
        self,
        tmp_req: appstream_center_20210220_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.GetLoginTokenResponse:
        """
        @summary GetLoginToken
        
        @param tmp_req: GetLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210220_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_features):
            request.available_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not UtilClient.is_unset(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not UtilClient.is_unset(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_name):
            query['ClientName'] = request.client_name
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.encrypted_finger_print_data):
            query['EncryptedFingerPrintData'] = request.encrypted_finger_print_data
        if not UtilClient.is_unset(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not UtilClient.is_unset(request.encrypted_password):
            query['EncryptedPassword'] = request.encrypted_password
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.finger_print_data):
            query['FingerPrintData'] = request.finger_print_data
        if not UtilClient.is_unset(request.idp_id):
            query['IdpId'] = request.idp_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not UtilClient.is_unset(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.login_name):
            query['LoginName'] = request.login_name
        if not UtilClient.is_unset(request.mfa_type):
            query['MfaType'] = request.mfa_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.phone_verify_code):
            query['PhoneVerifyCode'] = request.phone_verify_code
        if not UtilClient.is_unset(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sso_extends_cookies):
            query['SsoExtendsCookies'] = request.sso_extends_cookies
        if not UtilClient.is_unset(request.sso_session_token):
            query['SsoSessionToken'] = request.sso_session_token
        if not UtilClient.is_unset(request.token_code):
            query['TokenCode'] = request.token_code
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.GetLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_token_with_options_async(
        self,
        tmp_req: appstream_center_20210220_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.GetLoginTokenResponse:
        """
        @summary GetLoginToken
        
        @param tmp_req: GetLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210220_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_features):
            request.available_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not UtilClient.is_unset(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not UtilClient.is_unset(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_name):
            query['ClientName'] = request.client_name
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.encrypted_finger_print_data):
            query['EncryptedFingerPrintData'] = request.encrypted_finger_print_data
        if not UtilClient.is_unset(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not UtilClient.is_unset(request.encrypted_password):
            query['EncryptedPassword'] = request.encrypted_password
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.finger_print_data):
            query['FingerPrintData'] = request.finger_print_data
        if not UtilClient.is_unset(request.idp_id):
            query['IdpId'] = request.idp_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not UtilClient.is_unset(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.login_name):
            query['LoginName'] = request.login_name
        if not UtilClient.is_unset(request.mfa_type):
            query['MfaType'] = request.mfa_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.phone_verify_code):
            query['PhoneVerifyCode'] = request.phone_verify_code
        if not UtilClient.is_unset(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sso_extends_cookies):
            query['SsoExtendsCookies'] = request.sso_extends_cookies
        if not UtilClient.is_unset(request.sso_session_token):
            query['SsoSessionToken'] = request.sso_session_token
        if not UtilClient.is_unset(request.token_code):
            query['TokenCode'] = request.token_code
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.GetLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_token(
        self,
        request: appstream_center_20210220_models.GetLoginTokenRequest,
    ) -> appstream_center_20210220_models.GetLoginTokenResponse:
        """
        @summary GetLoginToken
        
        @param request: GetLoginTokenRequest
        @return: GetLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    async def get_login_token_async(
        self,
        request: appstream_center_20210220_models.GetLoginTokenRequest,
    ) -> appstream_center_20210220_models.GetLoginTokenResponse:
        """
        @summary GetLoginToken
        
        @param request: GetLoginTokenRequest
        @return: GetLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_login_token_with_options_async(request, runtime)

    def get_sts_token_with_options(
        self,
        request: appstream_center_20210220_models.GetStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.GetStsTokenResponse:
        """
        @summary 获取无影StsToken
        
        @param request: GetStsTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStsTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_code):
            body['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStsToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.GetStsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sts_token_with_options_async(
        self,
        request: appstream_center_20210220_models.GetStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.GetStsTokenResponse:
        """
        @summary 获取无影StsToken
        
        @param request: GetStsTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStsTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_code):
            body['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStsToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.GetStsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sts_token(
        self,
        request: appstream_center_20210220_models.GetStsTokenRequest,
    ) -> appstream_center_20210220_models.GetStsTokenResponse:
        """
        @summary 获取无影StsToken
        
        @param request: GetStsTokenRequest
        @return: GetStsTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sts_token_with_options(request, runtime)

    async def get_sts_token_async(
        self,
        request: appstream_center_20210220_models.GetStsTokenRequest,
    ) -> appstream_center_20210220_models.GetStsTokenResponse:
        """
        @summary 获取无影StsToken
        
        @param request: GetStsTokenRequest
        @return: GetStsTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sts_token_with_options_async(request, runtime)

    def refresh_login_token_with_options(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLoginToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.RefreshLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_login_token_with_options_async(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLoginToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.RefreshLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_login_token(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @return: RefreshLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_login_token_with_options(request, runtime)

    async def refresh_login_token_async(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @return: RefreshLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_login_token_with_options_async(request, runtime)
