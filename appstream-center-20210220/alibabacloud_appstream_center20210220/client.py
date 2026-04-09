# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_appstream_center20210220 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def client_user_logout_with_options(
        self,
        request: main_models.ClientUserLogoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClientUserLogoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClientUserLogout',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClientUserLogoutResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def client_user_logout_with_options_async(
        self,
        request: main_models.ClientUserLogoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClientUserLogoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClientUserLogout',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClientUserLogoutResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def client_user_logout(
        self,
        request: main_models.ClientUserLogoutRequest,
    ) -> main_models.ClientUserLogoutResponse:
        runtime = RuntimeOptions()
        return self.client_user_logout_with_options(request, runtime)

    async def client_user_logout_async(
        self,
        request: main_models.ClientUserLogoutRequest,
    ) -> main_models.ClientUserLogoutResponse:
        runtime = RuntimeOptions()
        return await self.client_user_logout_with_options_async(request, runtime)

    def find_idp_list_by_login_identifier_with_options(
        self,
        tmp_req: main_models.FindIdpListByLoginIdentifierRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindIdpListByLoginIdentifierResponse:
        tmp_req.validate()
        request = main_models.FindIdpListByLoginIdentifierShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_features):
            request.available_features_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not DaraCore.is_null(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        body = {}
        if not DaraCore.is_null(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.login_identifier):
            body['LoginIdentifier'] = request.login_identifier
        if not DaraCore.is_null(request.support_types):
            body['SupportTypes'] = request.support_types
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FindIdpListByLoginIdentifier',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindIdpListByLoginIdentifierResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def find_idp_list_by_login_identifier_with_options_async(
        self,
        tmp_req: main_models.FindIdpListByLoginIdentifierRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindIdpListByLoginIdentifierResponse:
        tmp_req.validate()
        request = main_models.FindIdpListByLoginIdentifierShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_features):
            request.available_features_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not DaraCore.is_null(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        body = {}
        if not DaraCore.is_null(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.login_identifier):
            body['LoginIdentifier'] = request.login_identifier
        if not DaraCore.is_null(request.support_types):
            body['SupportTypes'] = request.support_types
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FindIdpListByLoginIdentifier',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindIdpListByLoginIdentifierResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def find_idp_list_by_login_identifier(
        self,
        request: main_models.FindIdpListByLoginIdentifierRequest,
    ) -> main_models.FindIdpListByLoginIdentifierResponse:
        runtime = RuntimeOptions()
        return self.find_idp_list_by_login_identifier_with_options(request, runtime)

    async def find_idp_list_by_login_identifier_async(
        self,
        request: main_models.FindIdpListByLoginIdentifierRequest,
    ) -> main_models.FindIdpListByLoginIdentifierResponse:
        runtime = RuntimeOptions()
        return await self.find_idp_list_by_login_identifier_with_options_async(request, runtime)

    def get_login_token_with_options(
        self,
        tmp_req: main_models.GetLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginTokenResponse:
        tmp_req.validate()
        request = main_models.GetLoginTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_features):
            request.available_features_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not DaraCore.is_null(request.area_site):
            query['AreaSite'] = request.area_site
        if not DaraCore.is_null(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not DaraCore.is_null(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            query['ClientName'] = request.client_name
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.encrypted_finger_print_data):
            query['EncryptedFingerPrintData'] = request.encrypted_finger_print_data
        if not DaraCore.is_null(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not DaraCore.is_null(request.encrypted_password):
            query['EncryptedPassword'] = request.encrypted_password
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.finger_print_data):
            query['FingerPrintData'] = request.finger_print_data
        if not DaraCore.is_null(request.idp_id):
            query['IdpId'] = request.idp_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not DaraCore.is_null(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not DaraCore.is_null(request.login_name):
            query['LoginName'] = request.login_name
        if not DaraCore.is_null(request.mfa_type):
            query['MfaType'] = request.mfa_type
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.phone_verify_code):
            query['PhoneVerifyCode'] = request.phone_verify_code
        if not DaraCore.is_null(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sso_extends_cookies):
            query['SsoExtendsCookies'] = request.sso_extends_cookies
        if not DaraCore.is_null(request.sso_session_token):
            query['SsoSessionToken'] = request.sso_session_token
        if not DaraCore.is_null(request.token_code):
            query['TokenCode'] = request.token_code
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginToken',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginTokenResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_login_token_with_options_async(
        self,
        tmp_req: main_models.GetLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginTokenResponse:
        tmp_req.validate()
        request = main_models.GetLoginTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_features):
            request.available_features_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not DaraCore.is_null(request.area_site):
            query['AreaSite'] = request.area_site
        if not DaraCore.is_null(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not DaraCore.is_null(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            query['ClientName'] = request.client_name
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.encrypted_finger_print_data):
            query['EncryptedFingerPrintData'] = request.encrypted_finger_print_data
        if not DaraCore.is_null(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not DaraCore.is_null(request.encrypted_password):
            query['EncryptedPassword'] = request.encrypted_password
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.finger_print_data):
            query['FingerPrintData'] = request.finger_print_data
        if not DaraCore.is_null(request.idp_id):
            query['IdpId'] = request.idp_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not DaraCore.is_null(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not DaraCore.is_null(request.login_name):
            query['LoginName'] = request.login_name
        if not DaraCore.is_null(request.mfa_type):
            query['MfaType'] = request.mfa_type
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.phone_verify_code):
            query['PhoneVerifyCode'] = request.phone_verify_code
        if not DaraCore.is_null(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sso_extends_cookies):
            query['SsoExtendsCookies'] = request.sso_extends_cookies
        if not DaraCore.is_null(request.sso_session_token):
            query['SsoSessionToken'] = request.sso_session_token
        if not DaraCore.is_null(request.token_code):
            query['TokenCode'] = request.token_code
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginToken',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginTokenResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_login_token(
        self,
        request: main_models.GetLoginTokenRequest,
    ) -> main_models.GetLoginTokenResponse:
        runtime = RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    async def get_login_token_async(
        self,
        request: main_models.GetLoginTokenRequest,
    ) -> main_models.GetLoginTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_login_token_with_options_async(request, runtime)

    def get_sts_token_with_options(
        self,
        request: main_models.GetStsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStsTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_code):
            body['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStsToken',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStsTokenResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_sts_token_with_options_async(
        self,
        request: main_models.GetStsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStsTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_code):
            body['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStsToken',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStsTokenResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_sts_token(
        self,
        request: main_models.GetStsTokenRequest,
    ) -> main_models.GetStsTokenResponse:
        runtime = RuntimeOptions()
        return self.get_sts_token_with_options(request, runtime)

    async def get_sts_token_async(
        self,
        request: main_models.GetStsTokenRequest,
    ) -> main_models.GetStsTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_sts_token_with_options_async(request, runtime)

    def refresh_login_token_with_options(
        self,
        request: main_models.RefreshLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshLoginToken',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshLoginTokenResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def refresh_login_token_with_options_async(
        self,
        request: main_models.RefreshLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.profile_region):
            query['ProfileRegion'] = request.profile_region
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshLoginToken',
            version = '2021-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshLoginTokenResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def refresh_login_token(
        self,
        request: main_models.RefreshLoginTokenRequest,
    ) -> main_models.RefreshLoginTokenResponse:
        runtime = RuntimeOptions()
        return self.refresh_login_token_with_options(request, runtime)

    async def refresh_login_token_async(
        self,
        request: main_models.RefreshLoginTokenRequest,
    ) -> main_models.RefreshLoginTokenResponse:
        runtime = RuntimeOptions()
        return await self.refresh_login_token_with_options_async(request, runtime)
