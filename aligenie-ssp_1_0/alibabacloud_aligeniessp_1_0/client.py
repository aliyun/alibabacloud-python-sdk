# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligeniessp_1_0 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_and_remove_favorite_content_with_options(
        self,
        tmp_req: main_models.AddAndRemoveFavoriteContentRequest,
        headers: main_models.AddAndRemoveFavoriteContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddAndRemoveFavoriteContentResponse:
        tmp_req.validate()
        request = main_models.AddAndRemoveFavoriteContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_add_and_remove_favorite_content_request):
            request.open_add_and_remove_favorite_content_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_add_and_remove_favorite_content_request, 'OpenAddAndRemoveFavoriteContentRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_add_and_remove_favorite_content_request_shrink):
            body['OpenAddAndRemoveFavoriteContentRequest'] = request.open_add_and_remove_favorite_content_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddAndRemoveFavoriteContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/AddAndRemoveFavoriteContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAndRemoveFavoriteContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_and_remove_favorite_content_with_options_async(
        self,
        tmp_req: main_models.AddAndRemoveFavoriteContentRequest,
        headers: main_models.AddAndRemoveFavoriteContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddAndRemoveFavoriteContentResponse:
        tmp_req.validate()
        request = main_models.AddAndRemoveFavoriteContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_add_and_remove_favorite_content_request):
            request.open_add_and_remove_favorite_content_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_add_and_remove_favorite_content_request, 'OpenAddAndRemoveFavoriteContentRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_add_and_remove_favorite_content_request_shrink):
            body['OpenAddAndRemoveFavoriteContentRequest'] = request.open_add_and_remove_favorite_content_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddAndRemoveFavoriteContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/AddAndRemoveFavoriteContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAndRemoveFavoriteContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_and_remove_favorite_content(
        self,
        request: main_models.AddAndRemoveFavoriteContentRequest,
    ) -> main_models.AddAndRemoveFavoriteContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddAndRemoveFavoriteContentHeaders()
        return self.add_and_remove_favorite_content_with_options(request, headers, runtime)

    async def add_and_remove_favorite_content_async(
        self,
        request: main_models.AddAndRemoveFavoriteContentRequest,
    ) -> main_models.AddAndRemoveFavoriteContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddAndRemoveFavoriteContentHeaders()
        return await self.add_and_remove_favorite_content_with_options_async(request, headers, runtime)

    def add_sub_with_options(
        self,
        tmp_req: main_models.AddSubRequest,
        headers: main_models.AddSubHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddSubResponse:
        tmp_req.validate()
        request = main_models.AddSubShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_subscription_info_request):
            request.add_subscription_info_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_subscription_info_request, 'AddSubscriptionInfoRequest', 'json')
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.add_subscription_info_request_shrink):
            query['AddSubscriptionInfoRequest'] = request.add_subscription_info_request_shrink
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSub',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/addSub',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSubResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sub_with_options_async(
        self,
        tmp_req: main_models.AddSubRequest,
        headers: main_models.AddSubHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddSubResponse:
        tmp_req.validate()
        request = main_models.AddSubShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_subscription_info_request):
            request.add_subscription_info_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_subscription_info_request, 'AddSubscriptionInfoRequest', 'json')
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.add_subscription_info_request_shrink):
            query['AddSubscriptionInfoRequest'] = request.add_subscription_info_request_shrink
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSub',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/addSub',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sub(
        self,
        request: main_models.AddSubRequest,
    ) -> main_models.AddSubResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddSubHeaders()
        return self.add_sub_with_options(request, headers, runtime)

    async def add_sub_async(
        self,
        request: main_models.AddSubRequest,
    ) -> main_models.AddSubResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddSubHeaders()
        return await self.add_sub_with_options_async(request, headers, runtime)

    def auth_login_with_aligenie_user_info_with_options(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoRequest,
        headers: main_models.AuthLoginWithAligenieUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithAligenieUserInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encrypted_aligenie_user_identifier):
            body['EncryptedAligenieUserIdentifier'] = request.encrypted_aligenie_user_identifier
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithAligenieUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithAligenieUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithAligenieUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_login_with_aligenie_user_info_with_options_async(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoRequest,
        headers: main_models.AuthLoginWithAligenieUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithAligenieUserInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encrypted_aligenie_user_identifier):
            body['EncryptedAligenieUserIdentifier'] = request.encrypted_aligenie_user_identifier
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithAligenieUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithAligenieUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithAligenieUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_login_with_aligenie_user_info(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoRequest,
    ) -> main_models.AuthLoginWithAligenieUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithAligenieUserInfoHeaders()
        return self.auth_login_with_aligenie_user_info_with_options(request, headers, runtime)

    async def auth_login_with_aligenie_user_info_async(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoRequest,
    ) -> main_models.AuthLoginWithAligenieUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithAligenieUserInfoHeaders()
        return await self.auth_login_with_aligenie_user_info_with_options_async(request, headers, runtime)

    def auth_login_with_aligenie_user_info_generated_by_phone_number_with_options(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberRequest,
        headers: main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithAligenieUserInfoGeneratedByPhoneNumber',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithAligenieUserInfoGeneratedByPhoneNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_login_with_aligenie_user_info_generated_by_phone_number_with_options_async(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberRequest,
        headers: main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithAligenieUserInfoGeneratedByPhoneNumber',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithAligenieUserInfoGeneratedByPhoneNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_login_with_aligenie_user_info_generated_by_phone_number(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberRequest,
    ) -> main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders()
        return self.auth_login_with_aligenie_user_info_generated_by_phone_number_with_options(request, headers, runtime)

    async def auth_login_with_aligenie_user_info_generated_by_phone_number_async(
        self,
        request: main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberRequest,
    ) -> main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders()
        return await self.auth_login_with_aligenie_user_info_generated_by_phone_number_with_options_async(request, headers, runtime)

    def auth_login_with_taobao_user_info_with_options(
        self,
        request: main_models.AuthLoginWithTaobaoUserInfoRequest,
        headers: main_models.AuthLoginWithTaobaoUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithTaobaoUserInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encrypted_taobao_user_identifier):
            body['EncryptedTaobaoUserIdentifier'] = request.encrypted_taobao_user_identifier
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithTaobaoUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithTaobaoUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithTaobaoUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_login_with_taobao_user_info_with_options_async(
        self,
        request: main_models.AuthLoginWithTaobaoUserInfoRequest,
        headers: main_models.AuthLoginWithTaobaoUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithTaobaoUserInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encrypted_taobao_user_identifier):
            body['EncryptedTaobaoUserIdentifier'] = request.encrypted_taobao_user_identifier
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithTaobaoUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithTaobaoUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithTaobaoUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_login_with_taobao_user_info(
        self,
        request: main_models.AuthLoginWithTaobaoUserInfoRequest,
    ) -> main_models.AuthLoginWithTaobaoUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithTaobaoUserInfoHeaders()
        return self.auth_login_with_taobao_user_info_with_options(request, headers, runtime)

    async def auth_login_with_taobao_user_info_async(
        self,
        request: main_models.AuthLoginWithTaobaoUserInfoRequest,
    ) -> main_models.AuthLoginWithTaobaoUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithTaobaoUserInfoHeaders()
        return await self.auth_login_with_taobao_user_info_with_options_async(request, headers, runtime)

    def auth_login_with_third_user_info_with_options(
        self,
        tmp_req: main_models.AuthLoginWithThirdUserInfoRequest,
        headers: main_models.AuthLoginWithThirdUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithThirdUserInfoResponse:
        tmp_req.validate()
        request = main_models.AuthLoginWithThirdUserInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext_info):
            request.ext_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.third_user_identifier):
            body['ThirdUserIdentifier'] = request.third_user_identifier
        if not DaraCore.is_null(request.third_user_type):
            body['ThirdUserType'] = request.third_user_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithThirdUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithThirdUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithThirdUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_login_with_third_user_info_with_options_async(
        self,
        tmp_req: main_models.AuthLoginWithThirdUserInfoRequest,
        headers: main_models.AuthLoginWithThirdUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginWithThirdUserInfoResponse:
        tmp_req.validate()
        request = main_models.AuthLoginWithThirdUserInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext_info):
            request.ext_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.third_user_identifier):
            body['ThirdUserIdentifier'] = request.third_user_identifier
        if not DaraCore.is_null(request.third_user_type):
            body['ThirdUserType'] = request.third_user_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginWithThirdUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/authLoginWithThirdUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginWithThirdUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_login_with_third_user_info(
        self,
        request: main_models.AuthLoginWithThirdUserInfoRequest,
    ) -> main_models.AuthLoginWithThirdUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithThirdUserInfoHeaders()
        return self.auth_login_with_third_user_info_with_options(request, headers, runtime)

    async def auth_login_with_third_user_info_async(
        self,
        request: main_models.AuthLoginWithThirdUserInfoRequest,
    ) -> main_models.AuthLoginWithThirdUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.AuthLoginWithThirdUserInfoHeaders()
        return await self.auth_login_with_third_user_info_with_options_async(request, headers, runtime)

    def check_and_do_voip_call_for_hotel_with_options(
        self,
        tmp_req: main_models.CheckAndDoVoipCallForHotelRequest,
        headers: main_models.CheckAndDoVoipCallForHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAndDoVoipCallForHotelResponse:
        tmp_req.validate()
        request = main_models.CheckAndDoVoipCallForHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_data):
            body['BizData'] = request.biz_data
        if not DaraCore.is_null(request.callee_nick):
            body['CalleeNick'] = request.callee_nick
        if not DaraCore.is_null(request.callee_phone_num):
            body['CalleePhoneNum'] = request.callee_phone_num
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckAndDoVoipCallForHotel',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/checkAndDoVoipCallForHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAndDoVoipCallForHotelResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_and_do_voip_call_for_hotel_with_options_async(
        self,
        tmp_req: main_models.CheckAndDoVoipCallForHotelRequest,
        headers: main_models.CheckAndDoVoipCallForHotelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAndDoVoipCallForHotelResponse:
        tmp_req.validate()
        request = main_models.CheckAndDoVoipCallForHotelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_data):
            body['BizData'] = request.biz_data
        if not DaraCore.is_null(request.callee_nick):
            body['CalleeNick'] = request.callee_nick
        if not DaraCore.is_null(request.callee_phone_num):
            body['CalleePhoneNum'] = request.callee_phone_num
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckAndDoVoipCallForHotel',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/checkAndDoVoipCallForHotel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAndDoVoipCallForHotelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_and_do_voip_call_for_hotel(
        self,
        request: main_models.CheckAndDoVoipCallForHotelRequest,
    ) -> main_models.CheckAndDoVoipCallForHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckAndDoVoipCallForHotelHeaders()
        return self.check_and_do_voip_call_for_hotel_with_options(request, headers, runtime)

    async def check_and_do_voip_call_for_hotel_async(
        self,
        request: main_models.CheckAndDoVoipCallForHotelRequest,
    ) -> main_models.CheckAndDoVoipCallForHotelResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckAndDoVoipCallForHotelHeaders()
        return await self.check_and_do_voip_call_for_hotel_with_options_async(request, headers, runtime)

    def check_auth_code_bind_for_ext_with_options(
        self,
        tmp_req: main_models.CheckAuthCodeBindForExtRequest,
        headers: main_models.CheckAuthCodeBindForExtHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAuthCodeBindForExtResponse:
        tmp_req.validate()
        request = main_models.CheckAuthCodeBindForExtShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAuthCodeBindForExt',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/checkAuthCodeBindForExt',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAuthCodeBindForExtResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_auth_code_bind_for_ext_with_options_async(
        self,
        tmp_req: main_models.CheckAuthCodeBindForExtRequest,
        headers: main_models.CheckAuthCodeBindForExtHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAuthCodeBindForExtResponse:
        tmp_req.validate()
        request = main_models.CheckAuthCodeBindForExtShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAuthCodeBindForExt',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/checkAuthCodeBindForExt',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAuthCodeBindForExtResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_auth_code_bind_for_ext(
        self,
        request: main_models.CheckAuthCodeBindForExtRequest,
    ) -> main_models.CheckAuthCodeBindForExtResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckAuthCodeBindForExtHeaders()
        return self.check_auth_code_bind_for_ext_with_options(request, headers, runtime)

    async def check_auth_code_bind_for_ext_async(
        self,
        request: main_models.CheckAuthCodeBindForExtRequest,
    ) -> main_models.CheckAuthCodeBindForExtResponse:
        runtime = RuntimeOptions()
        headers = main_models.CheckAuthCodeBindForExtHeaders()
        return await self.check_auth_code_bind_for_ext_with_options_async(request, headers, runtime)

    def cloud_player_with_options(
        self,
        tmp_req: main_models.CloudPlayerRequest,
        headers: main_models.CloudPlayerHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CloudPlayerResponse:
        tmp_req.validate()
        request = main_models.CloudPlayerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.song_id_list):
            request.song_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.song_id_list, 'SongIdList', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.cur_play_index):
            query['CurPlayIndex'] = request.cur_play_index
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.play_mode):
            query['PlayMode'] = request.play_mode
        if not DaraCore.is_null(request.song_id):
            query['SongId'] = request.song_id
        if not DaraCore.is_null(request.song_id_list_shrink):
            query['SongIdList'] = request.song_id_list_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloudPlayer',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/cloud/player',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloudPlayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def cloud_player_with_options_async(
        self,
        tmp_req: main_models.CloudPlayerRequest,
        headers: main_models.CloudPlayerHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CloudPlayerResponse:
        tmp_req.validate()
        request = main_models.CloudPlayerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.song_id_list):
            request.song_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.song_id_list, 'SongIdList', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.cur_play_index):
            query['CurPlayIndex'] = request.cur_play_index
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.play_mode):
            query['PlayMode'] = request.play_mode
        if not DaraCore.is_null(request.song_id):
            query['SongId'] = request.song_id
        if not DaraCore.is_null(request.song_id_list_shrink):
            query['SongIdList'] = request.song_id_list_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloudPlayer',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/cloud/player',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloudPlayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cloud_player(
        self,
        request: main_models.CloudPlayerRequest,
    ) -> main_models.CloudPlayerResponse:
        runtime = RuntimeOptions()
        headers = main_models.CloudPlayerHeaders()
        return self.cloud_player_with_options(request, headers, runtime)

    async def cloud_player_async(
        self,
        request: main_models.CloudPlayerRequest,
    ) -> main_models.CloudPlayerResponse:
        runtime = RuntimeOptions()
        headers = main_models.CloudPlayerHeaders()
        return await self.cloud_player_with_options_async(request, headers, runtime)

    def create_alarm_with_options(
        self,
        tmp_req: main_models.CreateAlarmRequest,
        headers: main_models.CreateAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlarmResponse:
        tmp_req.validate()
        request = main_models.CreateAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlarm',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/createAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_with_options_async(
        self,
        tmp_req: main_models.CreateAlarmRequest,
        headers: main_models.CreateAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlarmResponse:
        tmp_req.validate()
        request = main_models.CreateAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlarm',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/createAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm(
        self,
        request: main_models.CreateAlarmRequest,
    ) -> main_models.CreateAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateAlarmHeaders()
        return self.create_alarm_with_options(request, headers, runtime)

    async def create_alarm_async(
        self,
        request: main_models.CreateAlarmRequest,
    ) -> main_models.CreateAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateAlarmHeaders()
        return await self.create_alarm_with_options_async(request, headers, runtime)

    def create_playing_list_with_options(
        self,
        tmp_req: main_models.CreatePlayingListRequest,
        headers: main_models.CreatePlayingListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePlayingListResponse:
        tmp_req.validate()
        request = main_models.CreatePlayingListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_create_playing_list_request, 'OpenCreatePlayingListRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlayingList',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/CreatePlayingList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_playing_list_with_options_async(
        self,
        tmp_req: main_models.CreatePlayingListRequest,
        headers: main_models.CreatePlayingListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePlayingListResponse:
        tmp_req.validate()
        request = main_models.CreatePlayingListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_create_playing_list_request, 'OpenCreatePlayingListRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlayingList',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/CreatePlayingList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePlayingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_playing_list(
        self,
        request: main_models.CreatePlayingListRequest,
    ) -> main_models.CreatePlayingListResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreatePlayingListHeaders()
        return self.create_playing_list_with_options(request, headers, runtime)

    async def create_playing_list_async(
        self,
        request: main_models.CreatePlayingListRequest,
    ) -> main_models.CreatePlayingListResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreatePlayingListHeaders()
        return await self.create_playing_list_with_options_async(request, headers, runtime)

    def create_playing_list_oauth_2with_options(
        self,
        tmp_req: main_models.CreatePlayingListOAuth2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePlayingListOAuth2Response:
        tmp_req.validate()
        request = main_models.CreatePlayingListOAuth2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_create_playing_list_request, 'OpenCreatePlayingListRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlayingListOAuth2',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/CreatePlayingListOAuth2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePlayingListOAuth2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_playing_list_oauth_2with_options_async(
        self,
        tmp_req: main_models.CreatePlayingListOAuth2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePlayingListOAuth2Response:
        tmp_req.validate()
        request = main_models.CreatePlayingListOAuth2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_create_playing_list_request, 'OpenCreatePlayingListRequest', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlayingListOAuth2',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/CreatePlayingListOAuth2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePlayingListOAuth2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_playing_list_oauth_2(
        self,
        request: main_models.CreatePlayingListOAuth2Request,
    ) -> main_models.CreatePlayingListOAuth2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_playing_list_oauth_2with_options(request, headers, runtime)

    async def create_playing_list_oauth_2_async(
        self,
        request: main_models.CreatePlayingListOAuth2Request,
    ) -> main_models.CreatePlayingListOAuth2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_playing_list_oauth_2with_options_async(request, headers, runtime)

    def create_schedule_task_with_options(
        self,
        tmp_req: main_models.CreateScheduleTaskRequest,
        headers: main_models.CreateScheduleTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduleTaskResponse:
        tmp_req.validate()
        request = main_models.CreateScheduleTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduleTask',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/CreateScheduleTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedule_task_with_options_async(
        self,
        tmp_req: main_models.CreateScheduleTaskRequest,
        headers: main_models.CreateScheduleTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduleTaskResponse:
        tmp_req.validate()
        request = main_models.CreateScheduleTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduleTask',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/CreateScheduleTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedule_task(
        self,
        request: main_models.CreateScheduleTaskRequest,
    ) -> main_models.CreateScheduleTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateScheduleTaskHeaders()
        return self.create_schedule_task_with_options(request, headers, runtime)

    async def create_schedule_task_async(
        self,
        request: main_models.CreateScheduleTaskRequest,
    ) -> main_models.CreateScheduleTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateScheduleTaskHeaders()
        return await self.create_schedule_task_with_options_async(request, headers, runtime)

    def delete_alarms_with_options(
        self,
        tmp_req: main_models.DeleteAlarmsRequest,
        headers: main_models.DeleteAlarmsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlarmsResponse:
        tmp_req.validate()
        request = main_models.DeleteAlarmsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlarms',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/deleteAlarms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alarms_with_options_async(
        self,
        tmp_req: main_models.DeleteAlarmsRequest,
        headers: main_models.DeleteAlarmsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlarmsResponse:
        tmp_req.validate()
        request = main_models.DeleteAlarmsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlarms',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/deleteAlarms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alarms(
        self,
        request: main_models.DeleteAlarmsRequest,
    ) -> main_models.DeleteAlarmsResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteAlarmsHeaders()
        return self.delete_alarms_with_options(request, headers, runtime)

    async def delete_alarms_async(
        self,
        request: main_models.DeleteAlarmsRequest,
    ) -> main_models.DeleteAlarmsResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteAlarmsHeaders()
        return await self.delete_alarms_with_options_async(request, headers, runtime)

    def delete_schedule_task_with_options(
        self,
        tmp_req: main_models.DeleteScheduleTaskRequest,
        headers: main_models.DeleteScheduleTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduleTaskResponse:
        tmp_req.validate()
        request = main_models.DeleteScheduleTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduleTask',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/DeleteScheduleTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedule_task_with_options_async(
        self,
        tmp_req: main_models.DeleteScheduleTaskRequest,
        headers: main_models.DeleteScheduleTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduleTaskResponse:
        tmp_req.validate()
        request = main_models.DeleteScheduleTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduleTask',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/DeleteScheduleTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedule_task(
        self,
        request: main_models.DeleteScheduleTaskRequest,
    ) -> main_models.DeleteScheduleTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteScheduleTaskHeaders()
        return self.delete_schedule_task_with_options(request, headers, runtime)

    async def delete_schedule_task_async(
        self,
        request: main_models.DeleteScheduleTaskRequest,
    ) -> main_models.DeleteScheduleTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteScheduleTaskHeaders()
        return await self.delete_schedule_task_with_options_async(request, headers, runtime)

    def delete_sub_with_options(
        self,
        request: main_models.DeleteSubRequest,
        headers: main_models.DeleteSubHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSub',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/deleteSub',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sub_with_options_async(
        self,
        request: main_models.DeleteSubRequest,
        headers: main_models.DeleteSubHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSub',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/deleteSub',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sub(
        self,
        request: main_models.DeleteSubRequest,
    ) -> main_models.DeleteSubResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteSubHeaders()
        return self.delete_sub_with_options(request, headers, runtime)

    async def delete_sub_async(
        self,
        request: main_models.DeleteSubRequest,
    ) -> main_models.DeleteSubResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteSubHeaders()
        return await self.delete_sub_with_options_async(request, headers, runtime)

    def device_control_with_options(
        self,
        tmp_req: main_models.DeviceControlRequest,
        headers: main_models.DeviceControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeviceControlResponse:
        tmp_req.validate()
        request = main_models.DeviceControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.control_request):
            request.control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.control_request, 'ControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not DaraCore.is_null(request.control_request_shrink):
            body['ControlRequest'] = request.control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeviceControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/control',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeviceControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def device_control_with_options_async(
        self,
        tmp_req: main_models.DeviceControlRequest,
        headers: main_models.DeviceControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeviceControlResponse:
        tmp_req.validate()
        request = main_models.DeviceControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.control_request):
            request.control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.control_request, 'ControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not DaraCore.is_null(request.control_request_shrink):
            body['ControlRequest'] = request.control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeviceControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/control',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeviceControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def device_control(
        self,
        request: main_models.DeviceControlRequest,
    ) -> main_models.DeviceControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeviceControlHeaders()
        return self.device_control_with_options(request, headers, runtime)

    async def device_control_async(
        self,
        request: main_models.DeviceControlRequest,
    ) -> main_models.DeviceControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeviceControlHeaders()
        return await self.device_control_with_options_async(request, headers, runtime)

    def ecology_openness_authenticate_with_options(
        self,
        request: main_models.EcologyOpennessAuthenticateRequest,
        headers: main_models.EcologyOpennessAuthenticateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EcologyOpennessAuthenticateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.login_state_access_token):
            body['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EcologyOpennessAuthenticate',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ecologyOpennessAuthenticate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EcologyOpennessAuthenticateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ecology_openness_authenticate_with_options_async(
        self,
        request: main_models.EcologyOpennessAuthenticateRequest,
        headers: main_models.EcologyOpennessAuthenticateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EcologyOpennessAuthenticateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.login_state_access_token):
            body['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EcologyOpennessAuthenticate',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ecologyOpennessAuthenticate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EcologyOpennessAuthenticateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ecology_openness_authenticate(
        self,
        request: main_models.EcologyOpennessAuthenticateRequest,
    ) -> main_models.EcologyOpennessAuthenticateResponse:
        runtime = RuntimeOptions()
        headers = main_models.EcologyOpennessAuthenticateHeaders()
        return self.ecology_openness_authenticate_with_options(request, headers, runtime)

    async def ecology_openness_authenticate_async(
        self,
        request: main_models.EcologyOpennessAuthenticateRequest,
    ) -> main_models.EcologyOpennessAuthenticateResponse:
        runtime = RuntimeOptions()
        headers = main_models.EcologyOpennessAuthenticateHeaders()
        return await self.ecology_openness_authenticate_with_options_async(request, headers, runtime)

    def ecology_openness_send_verification_code_with_options(
        self,
        request: main_models.EcologyOpennessSendVerificationCodeRequest,
        headers: main_models.EcologyOpennessSendVerificationCodeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EcologyOpennessSendVerificationCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EcologyOpennessSendVerificationCode',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ecologyOpennessSendVerificationCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EcologyOpennessSendVerificationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def ecology_openness_send_verification_code_with_options_async(
        self,
        request: main_models.EcologyOpennessSendVerificationCodeRequest,
        headers: main_models.EcologyOpennessSendVerificationCodeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EcologyOpennessSendVerificationCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EcologyOpennessSendVerificationCode',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ecologyOpennessSendVerificationCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EcologyOpennessSendVerificationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ecology_openness_send_verification_code(
        self,
        request: main_models.EcologyOpennessSendVerificationCodeRequest,
    ) -> main_models.EcologyOpennessSendVerificationCodeResponse:
        runtime = RuntimeOptions()
        headers = main_models.EcologyOpennessSendVerificationCodeHeaders()
        return self.ecology_openness_send_verification_code_with_options(request, headers, runtime)

    async def ecology_openness_send_verification_code_async(
        self,
        request: main_models.EcologyOpennessSendVerificationCodeRequest,
    ) -> main_models.EcologyOpennessSendVerificationCodeResponse:
        runtime = RuntimeOptions()
        headers = main_models.EcologyOpennessSendVerificationCodeHeaders()
        return await self.ecology_openness_send_verification_code_with_options_async(request, headers, runtime)

    def find_userlist_to_auth_login_with_phone_number_with_options(
        self,
        request: main_models.FindUserlistToAuthLoginWithPhoneNumberRequest,
        headers: main_models.FindUserlistToAuthLoginWithPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FindUserlistToAuthLoginWithPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindUserlistToAuthLoginWithPhoneNumber',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/findUserlistToAuthLoginWithPhoneNumber',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindUserlistToAuthLoginWithPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_userlist_to_auth_login_with_phone_number_with_options_async(
        self,
        request: main_models.FindUserlistToAuthLoginWithPhoneNumberRequest,
        headers: main_models.FindUserlistToAuthLoginWithPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FindUserlistToAuthLoginWithPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindUserlistToAuthLoginWithPhoneNumber',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/findUserlistToAuthLoginWithPhoneNumber',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindUserlistToAuthLoginWithPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_userlist_to_auth_login_with_phone_number(
        self,
        request: main_models.FindUserlistToAuthLoginWithPhoneNumberRequest,
    ) -> main_models.FindUserlistToAuthLoginWithPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.FindUserlistToAuthLoginWithPhoneNumberHeaders()
        return self.find_userlist_to_auth_login_with_phone_number_with_options(request, headers, runtime)

    async def find_userlist_to_auth_login_with_phone_number_async(
        self,
        request: main_models.FindUserlistToAuthLoginWithPhoneNumberRequest,
    ) -> main_models.FindUserlistToAuthLoginWithPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.FindUserlistToAuthLoginWithPhoneNumberHeaders()
        return await self.find_userlist_to_auth_login_with_phone_number_with_options_async(request, headers, runtime)

    def get_alarm_with_options(
        self,
        tmp_req: main_models.GetAlarmRequest,
        headers: main_models.GetAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlarmResponse:
        tmp_req.validate()
        request = main_models.GetAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAlarm',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alarm_with_options_async(
        self,
        tmp_req: main_models.GetAlarmRequest,
        headers: main_models.GetAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlarmResponse:
        tmp_req.validate()
        request = main_models.GetAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAlarm',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alarm(
        self,
        request: main_models.GetAlarmRequest,
    ) -> main_models.GetAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAlarmHeaders()
        return self.get_alarm_with_options(request, headers, runtime)

    async def get_alarm_async(
        self,
        request: main_models.GetAlarmRequest,
    ) -> main_models.GetAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAlarmHeaders()
        return await self.get_alarm_with_options_async(request, headers, runtime)

    def get_album_with_options(
        self,
        request: main_models.GetAlbumRequest,
        headers: main_models.GetAlbumHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlbumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlbum',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetAlbum',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlbumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_album_with_options_async(
        self,
        request: main_models.GetAlbumRequest,
        headers: main_models.GetAlbumHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlbumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlbum',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetAlbum',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlbumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_album(
        self,
        request: main_models.GetAlbumRequest,
    ) -> main_models.GetAlbumResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAlbumHeaders()
        return self.get_album_with_options(request, headers, runtime)

    async def get_album_async(
        self,
        request: main_models.GetAlbumRequest,
    ) -> main_models.GetAlbumResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAlbumHeaders()
        return await self.get_album_with_options_async(request, headers, runtime)

    def get_album_detail_by_id_with_options(
        self,
        request: main_models.GetAlbumDetailByIdRequest,
        headers: main_models.GetAlbumDetailByIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlbumDetailByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.album_id):
            query['AlbumId'] = request.album_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlbumDetailById',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getAlbumDetailById',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlbumDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_album_detail_by_id_with_options_async(
        self,
        request: main_models.GetAlbumDetailByIdRequest,
        headers: main_models.GetAlbumDetailByIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlbumDetailByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.album_id):
            query['AlbumId'] = request.album_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlbumDetailById',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getAlbumDetailById',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlbumDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_album_detail_by_id(
        self,
        request: main_models.GetAlbumDetailByIdRequest,
    ) -> main_models.GetAlbumDetailByIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAlbumDetailByIdHeaders()
        return self.get_album_detail_by_id_with_options(request, headers, runtime)

    async def get_album_detail_by_id_async(
        self,
        request: main_models.GetAlbumDetailByIdRequest,
    ) -> main_models.GetAlbumDetailByIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAlbumDetailByIdHeaders()
        return await self.get_album_detail_by_id_with_options_async(request, headers, runtime)

    def get_aligenie_user_info_with_options(
        self,
        request: main_models.GetAligenieUserInfoRequest,
        headers: main_models.GetAligenieUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAligenieUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.login_state_access_token):
            query['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAligenieUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getAligenieUserInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAligenieUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aligenie_user_info_with_options_async(
        self,
        request: main_models.GetAligenieUserInfoRequest,
        headers: main_models.GetAligenieUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAligenieUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.login_state_access_token):
            query['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAligenieUserInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getAligenieUserInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAligenieUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aligenie_user_info(
        self,
        request: main_models.GetAligenieUserInfoRequest,
    ) -> main_models.GetAligenieUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAligenieUserInfoHeaders()
        return self.get_aligenie_user_info_with_options(request, headers, runtime)

    async def get_aligenie_user_info_async(
        self,
        request: main_models.GetAligenieUserInfoRequest,
    ) -> main_models.GetAligenieUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAligenieUserInfoHeaders()
        return await self.get_aligenie_user_info_with_options_async(request, headers, runtime)

    def get_code_enhance_with_options(
        self,
        tmp_req: main_models.GetCodeEnhanceRequest,
        headers: main_models.GetCodeEnhanceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCodeEnhanceResponse:
        tmp_req.validate()
        request = main_models.GetCodeEnhanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channel_info):
            request.channel_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_info, 'ChannelInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCodeEnhance',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getCodeEnhance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCodeEnhanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_code_enhance_with_options_async(
        self,
        tmp_req: main_models.GetCodeEnhanceRequest,
        headers: main_models.GetCodeEnhanceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCodeEnhanceResponse:
        tmp_req.validate()
        request = main_models.GetCodeEnhanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channel_info):
            request.channel_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_info, 'ChannelInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCodeEnhance',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getCodeEnhance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCodeEnhanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_code_enhance(
        self,
        request: main_models.GetCodeEnhanceRequest,
    ) -> main_models.GetCodeEnhanceResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCodeEnhanceHeaders()
        return self.get_code_enhance_with_options(request, headers, runtime)

    async def get_code_enhance_async(
        self,
        request: main_models.GetCodeEnhanceRequest,
    ) -> main_models.GetCodeEnhanceResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCodeEnhanceHeaders()
        return await self.get_code_enhance_with_options_async(request, headers, runtime)

    def get_content_with_options(
        self,
        request: main_models.GetContentRequest,
        headers: main_models.GetContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_content_with_options_async(
        self,
        request: main_models.GetContentRequest,
        headers: main_models.GetContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_content(
        self,
        request: main_models.GetContentRequest,
    ) -> main_models.GetContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetContentHeaders()
        return self.get_content_with_options(request, headers, runtime)

    async def get_content_async(
        self,
        request: main_models.GetContentRequest,
    ) -> main_models.GetContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetContentHeaders()
        return await self.get_content_with_options_async(request, headers, runtime)

    def get_current_playing_item_with_options(
        self,
        tmp_req: main_models.GetCurrentPlayingItemRequest,
        headers: main_models.GetCurrentPlayingItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCurrentPlayingItemResponse:
        tmp_req.validate()
        request = main_models.GetCurrentPlayingItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCurrentPlayingItem',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetCurrentPlayingItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCurrentPlayingItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_current_playing_item_with_options_async(
        self,
        tmp_req: main_models.GetCurrentPlayingItemRequest,
        headers: main_models.GetCurrentPlayingItemHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCurrentPlayingItemResponse:
        tmp_req.validate()
        request = main_models.GetCurrentPlayingItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCurrentPlayingItem',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetCurrentPlayingItem',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCurrentPlayingItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_current_playing_item(
        self,
        request: main_models.GetCurrentPlayingItemRequest,
    ) -> main_models.GetCurrentPlayingItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCurrentPlayingItemHeaders()
        return self.get_current_playing_item_with_options(request, headers, runtime)

    async def get_current_playing_item_async(
        self,
        request: main_models.GetCurrentPlayingItemRequest,
    ) -> main_models.GetCurrentPlayingItemResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCurrentPlayingItemHeaders()
        return await self.get_current_playing_item_with_options_async(request, headers, runtime)

    def get_current_playing_list_with_options(
        self,
        tmp_req: main_models.GetCurrentPlayingListRequest,
        headers: main_models.GetCurrentPlayingListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCurrentPlayingListResponse:
        tmp_req.validate()
        request = main_models.GetCurrentPlayingListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_query_play_list_request):
            request.open_query_play_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_query_play_list_request, 'OpenQueryPlayListRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_query_play_list_request_shrink):
            body['OpenQueryPlayListRequest'] = request.open_query_play_list_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCurrentPlayingList',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetCurrentPlayingList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCurrentPlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_current_playing_list_with_options_async(
        self,
        tmp_req: main_models.GetCurrentPlayingListRequest,
        headers: main_models.GetCurrentPlayingListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCurrentPlayingListResponse:
        tmp_req.validate()
        request = main_models.GetCurrentPlayingListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_query_play_list_request):
            request.open_query_play_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_query_play_list_request, 'OpenQueryPlayListRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_query_play_list_request_shrink):
            body['OpenQueryPlayListRequest'] = request.open_query_play_list_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCurrentPlayingList',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetCurrentPlayingList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCurrentPlayingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_current_playing_list(
        self,
        request: main_models.GetCurrentPlayingListRequest,
    ) -> main_models.GetCurrentPlayingListResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCurrentPlayingListHeaders()
        return self.get_current_playing_list_with_options(request, headers, runtime)

    async def get_current_playing_list_async(
        self,
        request: main_models.GetCurrentPlayingListRequest,
    ) -> main_models.GetCurrentPlayingListResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCurrentPlayingListHeaders()
        return await self.get_current_playing_list_with_options_async(request, headers, runtime)

    def get_device_basic_info_with_options(
        self,
        tmp_req: main_models.GetDeviceBasicInfoRequest,
        headers: main_models.GetDeviceBasicInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceBasicInfoResponse:
        tmp_req.validate()
        request = main_models.GetDeviceBasicInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceBasicInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceBasicInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_basic_info_with_options_async(
        self,
        tmp_req: main_models.GetDeviceBasicInfoRequest,
        headers: main_models.GetDeviceBasicInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceBasicInfoResponse:
        tmp_req.validate()
        request = main_models.GetDeviceBasicInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceBasicInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceBasicInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_basic_info(
        self,
        request: main_models.GetDeviceBasicInfoRequest,
    ) -> main_models.GetDeviceBasicInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceBasicInfoHeaders()
        return self.get_device_basic_info_with_options(request, headers, runtime)

    async def get_device_basic_info_async(
        self,
        request: main_models.GetDeviceBasicInfoRequest,
    ) -> main_models.GetDeviceBasicInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceBasicInfoHeaders()
        return await self.get_device_basic_info_with_options_async(request, headers, runtime)

    def get_device_id_by_identity_with_options(
        self,
        request: main_models.GetDeviceIdByIdentityRequest,
        headers: main_models.GetDeviceIdByIdentityHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceIdByIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.identity_id):
            query['IdentityId'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceIdByIdentity',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceIdByIdentity',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceIdByIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_id_by_identity_with_options_async(
        self,
        request: main_models.GetDeviceIdByIdentityRequest,
        headers: main_models.GetDeviceIdByIdentityHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceIdByIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.identity_id):
            query['IdentityId'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceIdByIdentity',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceIdByIdentity',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceIdByIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_id_by_identity(
        self,
        request: main_models.GetDeviceIdByIdentityRequest,
    ) -> main_models.GetDeviceIdByIdentityResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceIdByIdentityHeaders()
        return self.get_device_id_by_identity_with_options(request, headers, runtime)

    async def get_device_id_by_identity_async(
        self,
        request: main_models.GetDeviceIdByIdentityRequest,
    ) -> main_models.GetDeviceIdByIdentityResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceIdByIdentityHeaders()
        return await self.get_device_id_by_identity_with_options_async(request, headers, runtime)

    def get_device_setting_with_options(
        self,
        tmp_req: main_models.GetDeviceSettingRequest,
        headers: main_models.GetDeviceSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceSettingResponse:
        tmp_req.validate()
        request = main_models.GetDeviceSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceSetting',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceSetting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_setting_with_options_async(
        self,
        tmp_req: main_models.GetDeviceSettingRequest,
        headers: main_models.GetDeviceSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceSettingResponse:
        tmp_req.validate()
        request = main_models.GetDeviceSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceSetting',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceSetting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_setting(
        self,
        request: main_models.GetDeviceSettingRequest,
    ) -> main_models.GetDeviceSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceSettingHeaders()
        return self.get_device_setting_with_options(request, headers, runtime)

    async def get_device_setting_async(
        self,
        request: main_models.GetDeviceSettingRequest,
    ) -> main_models.GetDeviceSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceSettingHeaders()
        return await self.get_device_setting_with_options_async(request, headers, runtime)

    def get_device_status_detail_with_options(
        self,
        tmp_req: main_models.GetDeviceStatusDetailRequest,
        headers: main_models.GetDeviceStatusDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceStatusDetailResponse:
        tmp_req.validate()
        request = main_models.GetDeviceStatusDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceStatusDetail',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceStatusDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceStatusDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_status_detail_with_options_async(
        self,
        tmp_req: main_models.GetDeviceStatusDetailRequest,
        headers: main_models.GetDeviceStatusDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceStatusDetailResponse:
        tmp_req.validate()
        request = main_models.GetDeviceStatusDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceStatusDetail',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceStatusDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceStatusDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_status_detail(
        self,
        request: main_models.GetDeviceStatusDetailRequest,
    ) -> main_models.GetDeviceStatusDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceStatusDetailHeaders()
        return self.get_device_status_detail_with_options(request, headers, runtime)

    async def get_device_status_detail_async(
        self,
        request: main_models.GetDeviceStatusDetailRequest,
    ) -> main_models.GetDeviceStatusDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceStatusDetailHeaders()
        return await self.get_device_status_detail_with_options_async(request, headers, runtime)

    def get_device_status_info_with_options(
        self,
        tmp_req: main_models.GetDeviceStatusInfoRequest,
        headers: main_models.GetDeviceStatusInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceStatusInfoResponse:
        tmp_req.validate()
        request = main_models.GetDeviceStatusInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceStatusInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceStatusInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceStatusInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_status_info_with_options_async(
        self,
        tmp_req: main_models.GetDeviceStatusInfoRequest,
        headers: main_models.GetDeviceStatusInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceStatusInfoResponse:
        tmp_req.validate()
        request = main_models.GetDeviceStatusInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceStatusInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceStatusInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceStatusInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_status_info(
        self,
        request: main_models.GetDeviceStatusInfoRequest,
    ) -> main_models.GetDeviceStatusInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceStatusInfoHeaders()
        return self.get_device_status_info_with_options(request, headers, runtime)

    async def get_device_status_info_async(
        self,
        request: main_models.GetDeviceStatusInfoRequest,
    ) -> main_models.GetDeviceStatusInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceStatusInfoHeaders()
        return await self.get_device_status_info_with_options_async(request, headers, runtime)

    def get_device_tag_with_options(
        self,
        tmp_req: main_models.GetDeviceTagRequest,
        headers: main_models.GetDeviceTagHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceTagResponse:
        tmp_req.validate()
        request = main_models.GetDeviceTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceTag',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceTag',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_tag_with_options_async(
        self,
        tmp_req: main_models.GetDeviceTagRequest,
        headers: main_models.GetDeviceTagHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceTagResponse:
        tmp_req.validate()
        request = main_models.GetDeviceTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceTag',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getDeviceTag',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_tag(
        self,
        request: main_models.GetDeviceTagRequest,
    ) -> main_models.GetDeviceTagResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceTagHeaders()
        return self.get_device_tag_with_options(request, headers, runtime)

    async def get_device_tag_async(
        self,
        request: main_models.GetDeviceTagRequest,
    ) -> main_models.GetDeviceTagResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeviceTagHeaders()
        return await self.get_device_tag_with_options_async(request, headers, runtime)

    def get_jiang_su_telecom_data_with_options(
        self,
        request: main_models.GetJiangSuTelecomDataRequest,
        headers: main_models.GetJiangSuTelecomDataHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetJiangSuTelecomDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJiangSuTelecomData',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetJiangSuTelecomData',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJiangSuTelecomDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_jiang_su_telecom_data_with_options_async(
        self,
        request: main_models.GetJiangSuTelecomDataRequest,
        headers: main_models.GetJiangSuTelecomDataHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetJiangSuTelecomDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJiangSuTelecomData',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetJiangSuTelecomData',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJiangSuTelecomDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_jiang_su_telecom_data(
        self,
        request: main_models.GetJiangSuTelecomDataRequest,
    ) -> main_models.GetJiangSuTelecomDataResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetJiangSuTelecomDataHeaders()
        return self.get_jiang_su_telecom_data_with_options(request, headers, runtime)

    async def get_jiang_su_telecom_data_async(
        self,
        request: main_models.GetJiangSuTelecomDataRequest,
    ) -> main_models.GetJiangSuTelecomDataResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetJiangSuTelecomDataHeaders()
        return await self.get_jiang_su_telecom_data_with_options_async(request, headers, runtime)

    def get_schedule_task_with_options(
        self,
        tmp_req: main_models.GetScheduleTaskRequest,
        headers: main_models.GetScheduleTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduleTaskResponse:
        tmp_req.validate()
        request = main_models.GetScheduleTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduleTask',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetScheduleTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schedule_task_with_options_async(
        self,
        tmp_req: main_models.GetScheduleTaskRequest,
        headers: main_models.GetScheduleTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduleTaskResponse:
        tmp_req.validate()
        request = main_models.GetScheduleTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduleTask',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetScheduleTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schedule_task(
        self,
        request: main_models.GetScheduleTaskRequest,
    ) -> main_models.GetScheduleTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetScheduleTaskHeaders()
        return self.get_schedule_task_with_options(request, headers, runtime)

    async def get_schedule_task_async(
        self,
        request: main_models.GetScheduleTaskRequest,
    ) -> main_models.GetScheduleTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetScheduleTaskHeaders()
        return await self.get_schedule_task_with_options_async(request, headers, runtime)

    def get_unread_message_count_with_options(
        self,
        tmp_req: main_models.GetUnreadMessageCountRequest,
        headers: main_models.GetUnreadMessageCountHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUnreadMessageCountResponse:
        tmp_req.validate()
        request = main_models.GetUnreadMessageCountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUnreadMessageCount',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getUnreadMessageCount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUnreadMessageCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_unread_message_count_with_options_async(
        self,
        tmp_req: main_models.GetUnreadMessageCountRequest,
        headers: main_models.GetUnreadMessageCountHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUnreadMessageCountResponse:
        tmp_req.validate()
        request = main_models.GetUnreadMessageCountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUnreadMessageCount',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getUnreadMessageCount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUnreadMessageCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_unread_message_count(
        self,
        request: main_models.GetUnreadMessageCountRequest,
    ) -> main_models.GetUnreadMessageCountResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUnreadMessageCountHeaders()
        return self.get_unread_message_count_with_options(request, headers, runtime)

    async def get_unread_message_count_async(
        self,
        request: main_models.GetUnreadMessageCountRequest,
    ) -> main_models.GetUnreadMessageCountResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUnreadMessageCountHeaders()
        return await self.get_unread_message_count_with_options_async(request, headers, runtime)

    def get_user_by_device_id_with_options(
        self,
        tmp_req: main_models.GetUserByDeviceIdRequest,
        headers: main_models.GetUserByDeviceIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserByDeviceIdResponse:
        tmp_req.validate()
        request = main_models.GetUserByDeviceIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserByDeviceId',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getUserByDeviceId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserByDeviceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_by_device_id_with_options_async(
        self,
        tmp_req: main_models.GetUserByDeviceIdRequest,
        headers: main_models.GetUserByDeviceIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserByDeviceIdResponse:
        tmp_req.validate()
        request = main_models.GetUserByDeviceIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserByDeviceId',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/getUserByDeviceId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserByDeviceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_by_device_id(
        self,
        request: main_models.GetUserByDeviceIdRequest,
    ) -> main_models.GetUserByDeviceIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserByDeviceIdHeaders()
        return self.get_user_by_device_id_with_options(request, headers, runtime)

    async def get_user_by_device_id_async(
        self,
        request: main_models.GetUserByDeviceIdRequest,
    ) -> main_models.GetUserByDeviceIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserByDeviceIdHeaders()
        return await self.get_user_by_device_id_with_options_async(request, headers, runtime)

    def get_weather_with_options(
        self,
        tmp_req: main_models.GetWeatherRequest,
        headers: main_models.GetWeatherHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetWeatherResponse:
        tmp_req.validate()
        request = main_models.GetWeatherShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWeather',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetWeather',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWeatherResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_weather_with_options_async(
        self,
        tmp_req: main_models.GetWeatherRequest,
        headers: main_models.GetWeatherHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetWeatherResponse:
        tmp_req.validate()
        request = main_models.GetWeatherShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWeather',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/GetWeather',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWeatherResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_weather(
        self,
        request: main_models.GetWeatherRequest,
    ) -> main_models.GetWeatherResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetWeatherHeaders()
        return self.get_weather_with_options(request, headers, runtime)

    async def get_weather_async(
        self,
        request: main_models.GetWeatherRequest,
    ) -> main_models.GetWeatherResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetWeatherHeaders()
        return await self.get_weather_with_options_async(request, headers, runtime)

    def index_control_playing_list_with_options(
        self,
        tmp_req: main_models.IndexControlPlayingListRequest,
        headers: main_models.IndexControlPlayingListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.IndexControlPlayingListResponse:
        tmp_req.validate()
        request = main_models.IndexControlPlayingListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_index_control_request):
            request.open_index_control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_index_control_request, 'OpenIndexControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_index_control_request_shrink):
            body['OpenIndexControlRequest'] = request.open_index_control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IndexControlPlayingList',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/IndexControlPlayingList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IndexControlPlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def index_control_playing_list_with_options_async(
        self,
        tmp_req: main_models.IndexControlPlayingListRequest,
        headers: main_models.IndexControlPlayingListHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.IndexControlPlayingListResponse:
        tmp_req.validate()
        request = main_models.IndexControlPlayingListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_index_control_request):
            request.open_index_control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_index_control_request, 'OpenIndexControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_index_control_request_shrink):
            body['OpenIndexControlRequest'] = request.open_index_control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IndexControlPlayingList',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/IndexControlPlayingList',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IndexControlPlayingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def index_control_playing_list(
        self,
        request: main_models.IndexControlPlayingListRequest,
    ) -> main_models.IndexControlPlayingListResponse:
        runtime = RuntimeOptions()
        headers = main_models.IndexControlPlayingListHeaders()
        return self.index_control_playing_list_with_options(request, headers, runtime)

    async def index_control_playing_list_async(
        self,
        request: main_models.IndexControlPlayingListRequest,
    ) -> main_models.IndexControlPlayingListResponse:
        runtime = RuntimeOptions()
        headers = main_models.IndexControlPlayingListHeaders()
        return await self.index_control_playing_list_with_options_async(request, headers, runtime)

    def invalidate_third_party_app_login_state_with_options(
        self,
        tmp_req: main_models.InvalidateThirdPartyAppLoginStateRequest,
        headers: main_models.InvalidateThirdPartyAppLoginStateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InvalidateThirdPartyAppLoginStateResponse:
        tmp_req.validate()
        request = main_models.InvalidateThirdPartyAppLoginStateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.third_party_app_id):
            body['ThirdPartyAppId'] = request.third_party_app_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvalidateThirdPartyAppLoginState',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/invalidateThirdPartyAppLoginState',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvalidateThirdPartyAppLoginStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def invalidate_third_party_app_login_state_with_options_async(
        self,
        tmp_req: main_models.InvalidateThirdPartyAppLoginStateRequest,
        headers: main_models.InvalidateThirdPartyAppLoginStateHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InvalidateThirdPartyAppLoginStateResponse:
        tmp_req.validate()
        request = main_models.InvalidateThirdPartyAppLoginStateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.third_party_app_id):
            body['ThirdPartyAppId'] = request.third_party_app_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvalidateThirdPartyAppLoginState',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/invalidateThirdPartyAppLoginState',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvalidateThirdPartyAppLoginStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invalidate_third_party_app_login_state(
        self,
        request: main_models.InvalidateThirdPartyAppLoginStateRequest,
    ) -> main_models.InvalidateThirdPartyAppLoginStateResponse:
        runtime = RuntimeOptions()
        headers = main_models.InvalidateThirdPartyAppLoginStateHeaders()
        return self.invalidate_third_party_app_login_state_with_options(request, headers, runtime)

    async def invalidate_third_party_app_login_state_async(
        self,
        request: main_models.InvalidateThirdPartyAppLoginStateRequest,
    ) -> main_models.InvalidateThirdPartyAppLoginStateResponse:
        runtime = RuntimeOptions()
        headers = main_models.InvalidateThirdPartyAppLoginStateHeaders()
        return await self.invalidate_third_party_app_login_state_with_options_async(request, headers, runtime)

    def list_alarms_with_options(
        self,
        tmp_req: main_models.ListAlarmsRequest,
        headers: main_models.ListAlarmsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlarmsResponse:
        tmp_req.validate()
        request = main_models.ListAlarmsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlarms',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarms_with_options_async(
        self,
        tmp_req: main_models.ListAlarmsRequest,
        headers: main_models.ListAlarmsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlarmsResponse:
        tmp_req.validate()
        request = main_models.ListAlarmsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlarms',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarms(
        self,
        request: main_models.ListAlarmsRequest,
    ) -> main_models.ListAlarmsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAlarmsHeaders()
        return self.list_alarms_with_options(request, headers, runtime)

    async def list_alarms_async(
        self,
        request: main_models.ListAlarmsRequest,
    ) -> main_models.ListAlarmsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAlarmsHeaders()
        return await self.list_alarms_with_options_async(request, headers, runtime)

    def list_album_detail_with_options(
        self,
        request: main_models.ListAlbumDetailRequest,
        headers: main_models.ListAlbumDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlbumDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlbumDetail',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListAlbumDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlbumDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_album_detail_with_options_async(
        self,
        request: main_models.ListAlbumDetailRequest,
        headers: main_models.ListAlbumDetailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlbumDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlbumDetail',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListAlbumDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlbumDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_album_detail(
        self,
        request: main_models.ListAlbumDetailRequest,
    ) -> main_models.ListAlbumDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAlbumDetailHeaders()
        return self.list_album_detail_with_options(request, headers, runtime)

    async def list_album_detail_async(
        self,
        request: main_models.ListAlbumDetailRequest,
    ) -> main_models.ListAlbumDetailResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAlbumDetailHeaders()
        return await self.list_album_detail_with_options_async(request, headers, runtime)

    def list_album_is_added_with_options(
        self,
        tmp_req: main_models.ListAlbumIsAddedRequest,
        headers: main_models.ListAlbumIsAddedHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlbumIsAddedResponse:
        tmp_req.validate()
        request = main_models.ListAlbumIsAddedShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.album_id_list):
            request.album_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.album_id_list, 'AlbumIdList', 'json')
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.album_id_list_shrink):
            query['AlbumIdList'] = request.album_id_list_shrink
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlbumIsAdded',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listAlbumIsAdded',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlbumIsAddedResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_album_is_added_with_options_async(
        self,
        tmp_req: main_models.ListAlbumIsAddedRequest,
        headers: main_models.ListAlbumIsAddedHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlbumIsAddedResponse:
        tmp_req.validate()
        request = main_models.ListAlbumIsAddedShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.album_id_list):
            request.album_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.album_id_list, 'AlbumIdList', 'json')
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.album_id_list_shrink):
            query['AlbumIdList'] = request.album_id_list_shrink
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlbumIsAdded',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listAlbumIsAdded',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlbumIsAddedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_album_is_added(
        self,
        request: main_models.ListAlbumIsAddedRequest,
    ) -> main_models.ListAlbumIsAddedResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAlbumIsAddedHeaders()
        return self.list_album_is_added_with_options(request, headers, runtime)

    async def list_album_is_added_async(
        self,
        request: main_models.ListAlbumIsAddedRequest,
    ) -> main_models.ListAlbumIsAddedResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListAlbumIsAddedHeaders()
        return await self.list_album_is_added_with_options_async(request, headers, runtime)

    def list_cate_content_with_options(
        self,
        tmp_req: main_models.ListCateContentRequest,
        headers: main_models.ListCateContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCateContentResponse:
        tmp_req.validate()
        request = main_models.ListCateContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCateContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCateContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCateContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cate_content_with_options_async(
        self,
        tmp_req: main_models.ListCateContentRequest,
        headers: main_models.ListCateContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCateContentResponse:
        tmp_req.validate()
        request = main_models.ListCateContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCateContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCateContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCateContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cate_content(
        self,
        request: main_models.ListCateContentRequest,
    ) -> main_models.ListCateContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCateContentHeaders()
        return self.list_cate_content_with_options(request, headers, runtime)

    async def list_cate_content_async(
        self,
        request: main_models.ListCateContentRequest,
    ) -> main_models.ListCateContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCateContentHeaders()
        return await self.list_cate_content_with_options_async(request, headers, runtime)

    def list_cate_info_with_options(
        self,
        request: main_models.ListCateInfoRequest,
        headers: main_models.ListCateInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCateInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCateInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cate_info_with_options_async(
        self,
        request: main_models.ListCateInfoRequest,
        headers: main_models.ListCateInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCateInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCateInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cate_info(
        self,
        request: main_models.ListCateInfoRequest,
    ) -> main_models.ListCateInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCateInfoHeaders()
        return self.list_cate_info_with_options(request, headers, runtime)

    async def list_cate_info_async(
        self,
        request: main_models.ListCateInfoRequest,
    ) -> main_models.ListCateInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCateInfoHeaders()
        return await self.list_cate_info_with_options_async(request, headers, runtime)

    def list_common_cate_first_floor_with_options(
        self,
        request: main_models.ListCommonCateFirstFloorRequest,
        headers: main_models.ListCommonCateFirstFloorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonCateFirstFloorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonCateFirstFloor',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCommonCateFirstFloor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonCateFirstFloorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_cate_first_floor_with_options_async(
        self,
        request: main_models.ListCommonCateFirstFloorRequest,
        headers: main_models.ListCommonCateFirstFloorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonCateFirstFloorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonCateFirstFloor',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCommonCateFirstFloor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonCateFirstFloorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_cate_first_floor(
        self,
        request: main_models.ListCommonCateFirstFloorRequest,
    ) -> main_models.ListCommonCateFirstFloorResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCommonCateFirstFloorHeaders()
        return self.list_common_cate_first_floor_with_options(request, headers, runtime)

    async def list_common_cate_first_floor_async(
        self,
        request: main_models.ListCommonCateFirstFloorRequest,
    ) -> main_models.ListCommonCateFirstFloorResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCommonCateFirstFloorHeaders()
        return await self.list_common_cate_first_floor_with_options_async(request, headers, runtime)

    def list_common_cate_second_floor_with_options(
        self,
        request: main_models.ListCommonCateSecondFloorRequest,
        headers: main_models.ListCommonCateSecondFloorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonCateSecondFloorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parent_cate_id):
            query['ParentCateId'] = request.parent_cate_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonCateSecondFloor',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCommonCateSecondFloor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonCateSecondFloorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_cate_second_floor_with_options_async(
        self,
        request: main_models.ListCommonCateSecondFloorRequest,
        headers: main_models.ListCommonCateSecondFloorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonCateSecondFloorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parent_cate_id):
            query['ParentCateId'] = request.parent_cate_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonCateSecondFloor',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListCommonCateSecondFloor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonCateSecondFloorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_cate_second_floor(
        self,
        request: main_models.ListCommonCateSecondFloorRequest,
    ) -> main_models.ListCommonCateSecondFloorResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCommonCateSecondFloorHeaders()
        return self.list_common_cate_second_floor_with_options(request, headers, runtime)

    async def list_common_cate_second_floor_async(
        self,
        request: main_models.ListCommonCateSecondFloorRequest,
    ) -> main_models.ListCommonCateSecondFloorResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCommonCateSecondFloorHeaders()
        return await self.list_common_cate_second_floor_with_options_async(request, headers, runtime)

    def list_device_basic_info_with_options(
        self,
        tmp_req: main_models.ListDeviceBasicInfoRequest,
        headers: main_models.ListDeviceBasicInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceBasicInfoResponse:
        tmp_req.validate()
        request = main_models.ListDeviceBasicInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_infos):
            request.device_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_infos, 'DeviceInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.device_infos_shrink):
            query['DeviceInfos'] = request.device_infos_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceBasicInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceBasicInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_basic_info_with_options_async(
        self,
        tmp_req: main_models.ListDeviceBasicInfoRequest,
        headers: main_models.ListDeviceBasicInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceBasicInfoResponse:
        tmp_req.validate()
        request = main_models.ListDeviceBasicInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_infos):
            request.device_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_infos, 'DeviceInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.device_infos_shrink):
            query['DeviceInfos'] = request.device_infos_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceBasicInfo',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceBasicInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_basic_info(
        self,
        request: main_models.ListDeviceBasicInfoRequest,
    ) -> main_models.ListDeviceBasicInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceBasicInfoHeaders()
        return self.list_device_basic_info_with_options(request, headers, runtime)

    async def list_device_basic_info_async(
        self,
        request: main_models.ListDeviceBasicInfoRequest,
    ) -> main_models.ListDeviceBasicInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceBasicInfoHeaders()
        return await self.list_device_basic_info_with_options_async(request, headers, runtime)

    def list_device_by_user_id_with_options(
        self,
        tmp_req: main_models.ListDeviceByUserIdRequest,
        headers: main_models.ListDeviceByUserIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceByUserIdResponse:
        tmp_req.validate()
        request = main_models.ListDeviceByUserIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceByUserId',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceByUserId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_by_user_id_with_options_async(
        self,
        tmp_req: main_models.ListDeviceByUserIdRequest,
        headers: main_models.ListDeviceByUserIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceByUserIdResponse:
        tmp_req.validate()
        request = main_models.ListDeviceByUserIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceByUserId',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceByUserId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_by_user_id(
        self,
        request: main_models.ListDeviceByUserIdRequest,
    ) -> main_models.ListDeviceByUserIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceByUserIdHeaders()
        return self.list_device_by_user_id_with_options(request, headers, runtime)

    async def list_device_by_user_id_async(
        self,
        request: main_models.ListDeviceByUserIdRequest,
    ) -> main_models.ListDeviceByUserIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceByUserIdHeaders()
        return await self.list_device_by_user_id_with_options_async(request, headers, runtime)

    def list_device_by_user_id_and_chanel_with_options(
        self,
        tmp_req: main_models.ListDeviceByUserIdAndChanelRequest,
        headers: main_models.ListDeviceByUserIdAndChanelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceByUserIdAndChanelResponse:
        tmp_req.validate()
        request = main_models.ListDeviceByUserIdAndChanelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channel_info):
            request.channel_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_info, 'ChannelInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceByUserIdAndChanel',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceByUserIdAndChanel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceByUserIdAndChanelResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_by_user_id_and_chanel_with_options_async(
        self,
        tmp_req: main_models.ListDeviceByUserIdAndChanelRequest,
        headers: main_models.ListDeviceByUserIdAndChanelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceByUserIdAndChanelResponse:
        tmp_req.validate()
        request = main_models.ListDeviceByUserIdAndChanelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.channel_info):
            request.channel_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_info, 'ChannelInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceByUserIdAndChanel',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceByUserIdAndChanel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceByUserIdAndChanelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_by_user_id_and_chanel(
        self,
        request: main_models.ListDeviceByUserIdAndChanelRequest,
    ) -> main_models.ListDeviceByUserIdAndChanelResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceByUserIdAndChanelHeaders()
        return self.list_device_by_user_id_and_chanel_with_options(request, headers, runtime)

    async def list_device_by_user_id_and_chanel_async(
        self,
        request: main_models.ListDeviceByUserIdAndChanelRequest,
    ) -> main_models.ListDeviceByUserIdAndChanelResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceByUserIdAndChanelHeaders()
        return await self.list_device_by_user_id_and_chanel_with_options_async(request, headers, runtime)

    def list_device_id_by_identities_with_options(
        self,
        tmp_req: main_models.ListDeviceIdByIdentitiesRequest,
        headers: main_models.ListDeviceIdByIdentitiesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceIdByIdentitiesResponse:
        tmp_req.validate()
        request = main_models.ListDeviceIdByIdentitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.identity_ids):
            request.identity_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.identity_ids, 'IdentityIds', 'json')
        query = {}
        if not DaraCore.is_null(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.identity_ids_shrink):
            query['IdentityIds'] = request.identity_ids_shrink
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceIdByIdentities',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceIdByIdentities',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceIdByIdentitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_id_by_identities_with_options_async(
        self,
        tmp_req: main_models.ListDeviceIdByIdentitiesRequest,
        headers: main_models.ListDeviceIdByIdentitiesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceIdByIdentitiesResponse:
        tmp_req.validate()
        request = main_models.ListDeviceIdByIdentitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.identity_ids):
            request.identity_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.identity_ids, 'IdentityIds', 'json')
        query = {}
        if not DaraCore.is_null(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.identity_ids_shrink):
            query['IdentityIds'] = request.identity_ids_shrink
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceIdByIdentities',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listDeviceIdByIdentities',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceIdByIdentitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_id_by_identities(
        self,
        request: main_models.ListDeviceIdByIdentitiesRequest,
    ) -> main_models.ListDeviceIdByIdentitiesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceIdByIdentitiesHeaders()
        return self.list_device_id_by_identities_with_options(request, headers, runtime)

    async def list_device_id_by_identities_async(
        self,
        request: main_models.ListDeviceIdByIdentitiesRequest,
    ) -> main_models.ListDeviceIdByIdentitiesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeviceIdByIdentitiesHeaders()
        return await self.list_device_id_by_identities_with_options_async(request, headers, runtime)

    def list_music_with_options(
        self,
        tmp_req: main_models.ListMusicRequest,
        headers: main_models.ListMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListMusicResponse:
        tmp_req.validate()
        request = main_models.ListMusicShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMusic',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMusicResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_music_with_options_async(
        self,
        tmp_req: main_models.ListMusicRequest,
        headers: main_models.ListMusicHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListMusicResponse:
        tmp_req.validate()
        request = main_models.ListMusicShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMusic',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listMusic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMusicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_music(
        self,
        request: main_models.ListMusicRequest,
    ) -> main_models.ListMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListMusicHeaders()
        return self.list_music_with_options(request, headers, runtime)

    async def list_music_async(
        self,
        request: main_models.ListMusicRequest,
    ) -> main_models.ListMusicResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListMusicHeaders()
        return await self.list_music_with_options_async(request, headers, runtime)

    def list_play_history_with_options(
        self,
        tmp_req: main_models.ListPlayHistoryRequest,
        headers: main_models.ListPlayHistoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlayHistoryResponse:
        tmp_req.validate()
        request = main_models.ListPlayHistoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPlayHistory',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListPlayHistory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlayHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_play_history_with_options_async(
        self,
        tmp_req: main_models.ListPlayHistoryRequest,
        headers: main_models.ListPlayHistoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlayHistoryResponse:
        tmp_req.validate()
        request = main_models.ListPlayHistoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPlayHistory',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListPlayHistory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlayHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_play_history(
        self,
        request: main_models.ListPlayHistoryRequest,
    ) -> main_models.ListPlayHistoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListPlayHistoryHeaders()
        return self.list_play_history_with_options(request, headers, runtime)

    async def list_play_history_async(
        self,
        request: main_models.ListPlayHistoryRequest,
    ) -> main_models.ListPlayHistoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListPlayHistoryHeaders()
        return await self.list_play_history_with_options_async(request, headers, runtime)

    def list_recommend_content_with_options(
        self,
        tmp_req: main_models.ListRecommendContentRequest,
        headers: main_models.ListRecommendContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecommendContentResponse:
        tmp_req.validate()
        request = main_models.ListRecommendContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRecommendContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListRecommendContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecommendContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recommend_content_with_options_async(
        self,
        tmp_req: main_models.ListRecommendContentRequest,
        headers: main_models.ListRecommendContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecommendContentResponse:
        tmp_req.validate()
        request = main_models.ListRecommendContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRecommendContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ListRecommendContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecommendContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recommend_content(
        self,
        request: main_models.ListRecommendContentRequest,
    ) -> main_models.ListRecommendContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListRecommendContentHeaders()
        return self.list_recommend_content_with_options(request, headers, runtime)

    async def list_recommend_content_async(
        self,
        request: main_models.ListRecommendContentRequest,
    ) -> main_models.ListRecommendContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListRecommendContentHeaders()
        return await self.list_recommend_content_with_options_async(request, headers, runtime)

    def list_sub_with_options(
        self,
        tmp_req: main_models.ListSubRequest,
        headers: main_models.ListSubHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubResponse:
        tmp_req.validate()
        request = main_models.ListSubShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSub',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listSub',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_with_options_async(
        self,
        tmp_req: main_models.ListSubRequest,
        headers: main_models.ListSubHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubResponse:
        tmp_req.validate()
        request = main_models.ListSubShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSub',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listSub',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub(
        self,
        request: main_models.ListSubRequest,
    ) -> main_models.ListSubResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSubHeaders()
        return self.list_sub_with_options(request, headers, runtime)

    async def list_sub_async(
        self,
        request: main_models.ListSubRequest,
    ) -> main_models.ListSubResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSubHeaders()
        return await self.list_sub_with_options_async(request, headers, runtime)

    def list_sub_album_with_options(
        self,
        tmp_req: main_models.ListSubAlbumRequest,
        headers: main_models.ListSubAlbumHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubAlbumResponse:
        tmp_req.validate()
        request = main_models.ListSubAlbumShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.query_subscription_album_request):
            request.query_subscription_album_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_subscription_album_request, 'QuerySubscriptionAlbumRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.query_subscription_album_request_shrink):
            query['QuerySubscriptionAlbumRequest'] = request.query_subscription_album_request_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubAlbum',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listSubAlbum',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubAlbumResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_album_with_options_async(
        self,
        tmp_req: main_models.ListSubAlbumRequest,
        headers: main_models.ListSubAlbumHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubAlbumResponse:
        tmp_req.validate()
        request = main_models.ListSubAlbumShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.query_subscription_album_request):
            request.query_subscription_album_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_subscription_album_request, 'QuerySubscriptionAlbumRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.query_subscription_album_request_shrink):
            query['QuerySubscriptionAlbumRequest'] = request.query_subscription_album_request_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubAlbum',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listSubAlbum',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubAlbumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_album(
        self,
        request: main_models.ListSubAlbumRequest,
    ) -> main_models.ListSubAlbumResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSubAlbumHeaders()
        return self.list_sub_album_with_options(request, headers, runtime)

    async def list_sub_album_async(
        self,
        request: main_models.ListSubAlbumRequest,
    ) -> main_models.ListSubAlbumResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSubAlbumHeaders()
        return await self.list_sub_album_with_options_async(request, headers, runtime)

    def list_subscription_album_category_with_options(
        self,
        request: main_models.ListSubscriptionAlbumCategoryRequest,
        headers: main_models.ListSubscriptionAlbumCategoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionAlbumCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptionAlbumCategory',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listSubscriptionAlbumCategory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionAlbumCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscription_album_category_with_options_async(
        self,
        request: main_models.ListSubscriptionAlbumCategoryRequest,
        headers: main_models.ListSubscriptionAlbumCategoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionAlbumCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptionAlbumCategory',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listSubscriptionAlbumCategory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionAlbumCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscription_album_category(
        self,
        request: main_models.ListSubscriptionAlbumCategoryRequest,
    ) -> main_models.ListSubscriptionAlbumCategoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSubscriptionAlbumCategoryHeaders()
        return self.list_subscription_album_category_with_options(request, headers, runtime)

    async def list_subscription_album_category_async(
        self,
        request: main_models.ListSubscriptionAlbumCategoryRequest,
    ) -> main_models.ListSubscriptionAlbumCategoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSubscriptionAlbumCategoryHeaders()
        return await self.list_subscription_album_category_with_options_async(request, headers, runtime)

    def list_user_message_with_options(
        self,
        tmp_req: main_models.ListUserMessageRequest,
        headers: main_models.ListUserMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserMessageResponse:
        tmp_req.validate()
        request = main_models.ListUserMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserMessage',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listUserMessage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_message_with_options_async(
        self,
        tmp_req: main_models.ListUserMessageRequest,
        headers: main_models.ListUserMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserMessageResponse:
        tmp_req.validate()
        request = main_models.ListUserMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserMessage',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/listUserMessage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_message(
        self,
        request: main_models.ListUserMessageRequest,
    ) -> main_models.ListUserMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListUserMessageHeaders()
        return self.list_user_message_with_options(request, headers, runtime)

    async def list_user_message_async(
        self,
        request: main_models.ListUserMessageRequest,
    ) -> main_models.ListUserMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListUserMessageHeaders()
        return await self.list_user_message_with_options_async(request, headers, runtime)

    def mobile_recommend_with_options(
        self,
        tmp_req: main_models.MobileRecommendRequest,
        headers: main_models.MobileRecommendHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.MobileRecommendResponse:
        tmp_req.validate()
        request = main_models.MobileRecommendShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.style):
            query['Style'] = request.style
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MobileRecommend',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/mobile/recommend/music',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_recommend_with_options_async(
        self,
        tmp_req: main_models.MobileRecommendRequest,
        headers: main_models.MobileRecommendHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.MobileRecommendResponse:
        tmp_req.validate()
        request = main_models.MobileRecommendShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.bot_id):
            query['BotId'] = request.bot_id
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.style):
            query['Style'] = request.style
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MobileRecommend',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/mobile/recommend/music',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_recommend(
        self,
        request: main_models.MobileRecommendRequest,
    ) -> main_models.MobileRecommendResponse:
        runtime = RuntimeOptions()
        headers = main_models.MobileRecommendHeaders()
        return self.mobile_recommend_with_options(request, headers, runtime)

    async def mobile_recommend_async(
        self,
        request: main_models.MobileRecommendRequest,
    ) -> main_models.MobileRecommendResponse:
        runtime = RuntimeOptions()
        headers = main_models.MobileRecommendHeaders()
        return await self.mobile_recommend_with_options_async(request, headers, runtime)

    def play_and_pause_control_with_options(
        self,
        tmp_req: main_models.PlayAndPauseControlRequest,
        headers: main_models.PlayAndPauseControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PlayAndPauseControlResponse:
        tmp_req.validate()
        request = main_models.PlayAndPauseControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_play_and_pause_control_param):
            request.open_play_and_pause_control_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_play_and_pause_control_param, 'OpenPlayAndPauseControlParam', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_play_and_pause_control_param_shrink):
            body['OpenPlayAndPauseControlParam'] = request.open_play_and_pause_control_param_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PlayAndPauseControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/PlayAndPauseControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PlayAndPauseControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def play_and_pause_control_with_options_async(
        self,
        tmp_req: main_models.PlayAndPauseControlRequest,
        headers: main_models.PlayAndPauseControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PlayAndPauseControlResponse:
        tmp_req.validate()
        request = main_models.PlayAndPauseControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_play_and_pause_control_param):
            request.open_play_and_pause_control_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_play_and_pause_control_param, 'OpenPlayAndPauseControlParam', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_play_and_pause_control_param_shrink):
            body['OpenPlayAndPauseControlParam'] = request.open_play_and_pause_control_param_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PlayAndPauseControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/PlayAndPauseControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PlayAndPauseControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def play_and_pause_control(
        self,
        request: main_models.PlayAndPauseControlRequest,
    ) -> main_models.PlayAndPauseControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.PlayAndPauseControlHeaders()
        return self.play_and_pause_control_with_options(request, headers, runtime)

    async def play_and_pause_control_async(
        self,
        request: main_models.PlayAndPauseControlRequest,
    ) -> main_models.PlayAndPauseControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.PlayAndPauseControlHeaders()
        return await self.play_and_pause_control_with_options_async(request, headers, runtime)

    def play_mode_control_with_options(
        self,
        tmp_req: main_models.PlayModeControlRequest,
        headers: main_models.PlayModeControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PlayModeControlResponse:
        tmp_req.validate()
        request = main_models.PlayModeControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_play_mode_control_request):
            request.open_play_mode_control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_play_mode_control_request, 'OpenPlayModeControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_play_mode_control_request_shrink):
            body['OpenPlayModeControlRequest'] = request.open_play_mode_control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PlayModeControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/PlayModeControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PlayModeControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def play_mode_control_with_options_async(
        self,
        tmp_req: main_models.PlayModeControlRequest,
        headers: main_models.PlayModeControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PlayModeControlResponse:
        tmp_req.validate()
        request = main_models.PlayModeControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_play_mode_control_request):
            request.open_play_mode_control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_play_mode_control_request, 'OpenPlayModeControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_play_mode_control_request_shrink):
            body['OpenPlayModeControlRequest'] = request.open_play_mode_control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PlayModeControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/PlayModeControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PlayModeControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def play_mode_control(
        self,
        request: main_models.PlayModeControlRequest,
    ) -> main_models.PlayModeControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.PlayModeControlHeaders()
        return self.play_mode_control_with_options(request, headers, runtime)

    async def play_mode_control_async(
        self,
        request: main_models.PlayModeControlRequest,
    ) -> main_models.PlayModeControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.PlayModeControlHeaders()
        return await self.play_mode_control_with_options_async(request, headers, runtime)

    def previous_and_next_control_with_options(
        self,
        tmp_req: main_models.PreviousAndNextControlRequest,
        headers: main_models.PreviousAndNextControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PreviousAndNextControlResponse:
        tmp_req.validate()
        request = main_models.PreviousAndNextControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_control_playing_list_request):
            request.open_control_playing_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_control_playing_list_request, 'OpenControlPlayingListRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_control_playing_list_request_shrink):
            body['OpenControlPlayingListRequest'] = request.open_control_playing_list_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviousAndNextControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/PreviousAndNextControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviousAndNextControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def previous_and_next_control_with_options_async(
        self,
        tmp_req: main_models.PreviousAndNextControlRequest,
        headers: main_models.PreviousAndNextControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PreviousAndNextControlResponse:
        tmp_req.validate()
        request = main_models.PreviousAndNextControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_control_playing_list_request):
            request.open_control_playing_list_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_control_playing_list_request, 'OpenControlPlayingListRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_control_playing_list_request_shrink):
            body['OpenControlPlayingListRequest'] = request.open_control_playing_list_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviousAndNextControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/PreviousAndNextControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviousAndNextControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def previous_and_next_control(
        self,
        request: main_models.PreviousAndNextControlRequest,
    ) -> main_models.PreviousAndNextControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.PreviousAndNextControlHeaders()
        return self.previous_and_next_control_with_options(request, headers, runtime)

    async def previous_and_next_control_async(
        self,
        request: main_models.PreviousAndNextControlRequest,
    ) -> main_models.PreviousAndNextControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.PreviousAndNextControlHeaders()
        return await self.previous_and_next_control_with_options_async(request, headers, runtime)

    def progress_control_with_options(
        self,
        tmp_req: main_models.ProgressControlRequest,
        headers: main_models.ProgressControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ProgressControlResponse:
        tmp_req.validate()
        request = main_models.ProgressControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_progress_control_request):
            request.open_progress_control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_progress_control_request, 'OpenProgressControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_progress_control_request_shrink):
            body['OpenProgressControlRequest'] = request.open_progress_control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ProgressControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ProgressControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProgressControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def progress_control_with_options_async(
        self,
        tmp_req: main_models.ProgressControlRequest,
        headers: main_models.ProgressControlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ProgressControlResponse:
        tmp_req.validate()
        request = main_models.ProgressControlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.open_progress_control_request):
            request.open_progress_control_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.open_progress_control_request, 'OpenProgressControlRequest', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.open_progress_control_request_shrink):
            body['OpenProgressControlRequest'] = request.open_progress_control_request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ProgressControl',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/ProgressControl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProgressControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def progress_control(
        self,
        request: main_models.ProgressControlRequest,
    ) -> main_models.ProgressControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.ProgressControlHeaders()
        return self.progress_control_with_options(request, headers, runtime)

    async def progress_control_async(
        self,
        request: main_models.ProgressControlRequest,
    ) -> main_models.ProgressControlResponse:
        runtime = RuntimeOptions()
        headers = main_models.ProgressControlHeaders()
        return await self.progress_control_with_options_async(request, headers, runtime)

    def query_music_type_with_options(
        self,
        tmp_req: main_models.QueryMusicTypeRequest,
        headers: main_models.QueryMusicTypeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMusicTypeResponse:
        tmp_req.validate()
        request = main_models.QueryMusicTypeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMusicType',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/queryMusicType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMusicTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_music_type_with_options_async(
        self,
        tmp_req: main_models.QueryMusicTypeRequest,
        headers: main_models.QueryMusicTypeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMusicTypeResponse:
        tmp_req.validate()
        request = main_models.QueryMusicTypeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMusicType',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/queryMusicType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMusicTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_music_type(
        self,
        request: main_models.QueryMusicTypeRequest,
    ) -> main_models.QueryMusicTypeResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryMusicTypeHeaders()
        return self.query_music_type_with_options(request, headers, runtime)

    async def query_music_type_async(
        self,
        request: main_models.QueryMusicTypeRequest,
    ) -> main_models.QueryMusicTypeResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryMusicTypeHeaders()
        return await self.query_music_type_with_options_async(request, headers, runtime)

    def query_user_device_list_by_tme_user_id_with_options(
        self,
        request: main_models.QueryUserDeviceListByTmeUserIdRequest,
        headers: main_models.QueryUserDeviceListByTmeUserIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserDeviceListByTmeUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sp):
            query['Sp'] = request.sp
        if not DaraCore.is_null(request.tme_user_id):
            query['TmeUserId'] = request.tme_user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserDeviceListByTmeUserId',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/queryUserDeviceListByTmeUserId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserDeviceListByTmeUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_device_list_by_tme_user_id_with_options_async(
        self,
        request: main_models.QueryUserDeviceListByTmeUserIdRequest,
        headers: main_models.QueryUserDeviceListByTmeUserIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserDeviceListByTmeUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sp):
            query['Sp'] = request.sp
        if not DaraCore.is_null(request.tme_user_id):
            query['TmeUserId'] = request.tme_user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserDeviceListByTmeUserId',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/queryUserDeviceListByTmeUserId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserDeviceListByTmeUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_device_list_by_tme_user_id(
        self,
        request: main_models.QueryUserDeviceListByTmeUserIdRequest,
    ) -> main_models.QueryUserDeviceListByTmeUserIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryUserDeviceListByTmeUserIdHeaders()
        return self.query_user_device_list_by_tme_user_id_with_options(request, headers, runtime)

    async def query_user_device_list_by_tme_user_id_async(
        self,
        request: main_models.QueryUserDeviceListByTmeUserIdRequest,
    ) -> main_models.QueryUserDeviceListByTmeUserIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.QueryUserDeviceListByTmeUserIdHeaders()
        return await self.query_user_device_list_by_tme_user_id_with_options_async(request, headers, runtime)

    def read_message_with_options(
        self,
        tmp_req: main_models.ReadMessageRequest,
        headers: main_models.ReadMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageResponse:
        tmp_req.validate()
        request = main_models.ReadMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessage',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/readMessage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_with_options_async(
        self,
        tmp_req: main_models.ReadMessageRequest,
        headers: main_models.ReadMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageResponse:
        tmp_req.validate()
        request = main_models.ReadMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessage',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/readMessage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message(
        self,
        request: main_models.ReadMessageRequest,
    ) -> main_models.ReadMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.ReadMessageHeaders()
        return self.read_message_with_options(request, headers, runtime)

    async def read_message_async(
        self,
        request: main_models.ReadMessageRequest,
    ) -> main_models.ReadMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.ReadMessageHeaders()
        return await self.read_message_with_options_async(request, headers, runtime)

    def scan_code_bind_with_options(
        self,
        tmp_req: main_models.ScanCodeBindRequest,
        headers: main_models.ScanCodeBindHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ScanCodeBindResponse:
        tmp_req.validate()
        request = main_models.ScanCodeBindShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.bind_req):
            request.bind_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.bind_req, 'BindReq', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.bind_req_shrink):
            body['BindReq'] = request.bind_req_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScanCodeBind',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/scanCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanCodeBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_code_bind_with_options_async(
        self,
        tmp_req: main_models.ScanCodeBindRequest,
        headers: main_models.ScanCodeBindHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ScanCodeBindResponse:
        tmp_req.validate()
        request = main_models.ScanCodeBindShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.bind_req):
            request.bind_req_shrink = Utils.array_to_string_with_specified_style(tmp_req.bind_req, 'BindReq', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.bind_req_shrink):
            body['BindReq'] = request.bind_req_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScanCodeBind',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/scanCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanCodeBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_code_bind(
        self,
        request: main_models.ScanCodeBindRequest,
    ) -> main_models.ScanCodeBindResponse:
        runtime = RuntimeOptions()
        headers = main_models.ScanCodeBindHeaders()
        return self.scan_code_bind_with_options(request, headers, runtime)

    async def scan_code_bind_async(
        self,
        request: main_models.ScanCodeBindRequest,
    ) -> main_models.ScanCodeBindResponse:
        runtime = RuntimeOptions()
        headers = main_models.ScanCodeBindHeaders()
        return await self.scan_code_bind_with_options_async(request, headers, runtime)

    def scg_search_with_options(
        self,
        tmp_req: main_models.ScgSearchRequest,
        headers: main_models.ScgSearchHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ScgSearchResponse:
        tmp_req.validate()
        request = main_models.ScgSearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scg_filter):
            request.scg_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.scg_filter, 'ScgFilter', 'json')
        query = {}
        if not DaraCore.is_null(request.scg_filter_shrink):
            query['ScgFilter'] = request.scg_filter_shrink
        if not DaraCore.is_null(request.topic_id):
            query['TopicId'] = request.topic_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScgSearch',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/scgSearch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScgSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def scg_search_with_options_async(
        self,
        tmp_req: main_models.ScgSearchRequest,
        headers: main_models.ScgSearchHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ScgSearchResponse:
        tmp_req.validate()
        request = main_models.ScgSearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scg_filter):
            request.scg_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.scg_filter, 'ScgFilter', 'json')
        query = {}
        if not DaraCore.is_null(request.scg_filter_shrink):
            query['ScgFilter'] = request.scg_filter_shrink
        if not DaraCore.is_null(request.topic_id):
            query['TopicId'] = request.topic_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScgSearch',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/scgSearch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScgSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scg_search(
        self,
        request: main_models.ScgSearchRequest,
    ) -> main_models.ScgSearchResponse:
        runtime = RuntimeOptions()
        headers = main_models.ScgSearchHeaders()
        return self.scg_search_with_options(request, headers, runtime)

    async def scg_search_async(
        self,
        request: main_models.ScgSearchRequest,
    ) -> main_models.ScgSearchResponse:
        runtime = RuntimeOptions()
        headers = main_models.ScgSearchHeaders()
        return await self.scg_search_with_options_async(request, headers, runtime)

    def search_content_with_options(
        self,
        tmp_req: main_models.SearchContentRequest,
        headers: main_models.SearchContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SearchContentResponse:
        tmp_req.validate()
        request = main_models.SearchContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/SearchContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_content_with_options_async(
        self,
        tmp_req: main_models.SearchContentRequest,
        headers: main_models.SearchContentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SearchContentResponse:
        tmp_req.validate()
        request = main_models.SearchContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.request):
            request.request_shrink = Utils.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not DaraCore.is_null(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchContent',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/SearchContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_content(
        self,
        request: main_models.SearchContentRequest,
    ) -> main_models.SearchContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.SearchContentHeaders()
        return self.search_content_with_options(request, headers, runtime)

    async def search_content_async(
        self,
        request: main_models.SearchContentRequest,
    ) -> main_models.SearchContentResponse:
        runtime = RuntimeOptions()
        headers = main_models.SearchContentHeaders()
        return await self.search_content_with_options_async(request, headers, runtime)

    def send_message_with_options(
        self,
        tmp_req: main_models.SendMessageRequest,
        headers: main_models.SendMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        tmp_req.validate()
        request = main_models.SendMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        tmp_req: main_models.SendMessageRequest,
        headers: main_models.SendMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        tmp_req.validate()
        request = main_models.SendMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.SendMessageHeaders()
        return self.send_message_with_options(request, headers, runtime)

    async def send_message_async(
        self,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.SendMessageHeaders()
        return await self.send_message_with_options_async(request, headers, runtime)

    def set_device_setting_with_options(
        self,
        tmp_req: main_models.SetDeviceSettingRequest,
        headers: main_models.SetDeviceSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeviceSettingResponse:
        tmp_req.validate()
        request = main_models.SetDeviceSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDeviceSetting',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/setDeviceSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeviceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_setting_with_options_async(
        self,
        tmp_req: main_models.SetDeviceSettingRequest,
        headers: main_models.SetDeviceSettingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeviceSettingResponse:
        tmp_req.validate()
        request = main_models.SetDeviceSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDeviceSetting',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/setDeviceSetting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeviceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_device_setting(
        self,
        request: main_models.SetDeviceSettingRequest,
    ) -> main_models.SetDeviceSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.SetDeviceSettingHeaders()
        return self.set_device_setting_with_options(request, headers, runtime)

    async def set_device_setting_async(
        self,
        request: main_models.SetDeviceSettingRequest,
    ) -> main_models.SetDeviceSettingResponse:
        runtime = RuntimeOptions()
        headers = main_models.SetDeviceSettingHeaders()
        return await self.set_device_setting_with_options_async(request, headers, runtime)

    def third_immediate_msg_push_with_options(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
        headers: main_models.ThirdImmediateMsgPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.change_detail):
            query['ChangeDetail'] = request.change_detail
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.psg_ids):
            query['PsgIds'] = request.psg_ids
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.traffic_change_type):
            query['TrafficChangeType'] = request.traffic_change_type
        if not DaraCore.is_null(request.traffic_change_type_desc):
            query['TrafficChangeTypeDesc'] = request.traffic_change_type_desc
        if not DaraCore.is_null(request.traffic_journey_ids):
            query['TrafficJourneyIds'] = request.traffic_journey_ids
        if not DaraCore.is_null(request.traffic_sub_order_ids):
            query['TrafficSubOrderIds'] = request.traffic_sub_order_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ThirdImmediateMsgPush',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/thirdImmediateMsgPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ThirdImmediateMsgPushResponse(),
            self.call_api(params, req, runtime)
        )

    async def third_immediate_msg_push_with_options_async(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
        headers: main_models.ThirdImmediateMsgPushHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.change_detail):
            query['ChangeDetail'] = request.change_detail
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.psg_ids):
            query['PsgIds'] = request.psg_ids
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.traffic_change_type):
            query['TrafficChangeType'] = request.traffic_change_type
        if not DaraCore.is_null(request.traffic_change_type_desc):
            query['TrafficChangeTypeDesc'] = request.traffic_change_type_desc
        if not DaraCore.is_null(request.traffic_journey_ids):
            query['TrafficJourneyIds'] = request.traffic_journey_ids
        if not DaraCore.is_null(request.traffic_sub_order_ids):
            query['TrafficSubOrderIds'] = request.traffic_sub_order_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ThirdImmediateMsgPush',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/thirdImmediateMsgPush',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ThirdImmediateMsgPushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def third_immediate_msg_push(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.ThirdImmediateMsgPushHeaders()
        return self.third_immediate_msg_push_with_options(request, headers, runtime)

    async def third_immediate_msg_push_async(
        self,
        request: main_models.ThirdImmediateMsgPushRequest,
    ) -> main_models.ThirdImmediateMsgPushResponse:
        runtime = RuntimeOptions()
        headers = main_models.ThirdImmediateMsgPushHeaders()
        return await self.third_immediate_msg_push_with_options_async(request, headers, runtime)

    def unbind_aligenie_user_with_options(
        self,
        request: main_models.UnbindAligenieUserRequest,
        headers: main_models.UnbindAligenieUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAligenieUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.login_state_access_token):
            body['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAligenieUser',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/unbindAligenieUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAligenieUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_aligenie_user_with_options_async(
        self,
        request: main_models.UnbindAligenieUserRequest,
        headers: main_models.UnbindAligenieUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAligenieUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.login_state_access_token):
            body['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAligenieUser',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/unbindAligenieUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAligenieUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_aligenie_user(
        self,
        request: main_models.UnbindAligenieUserRequest,
    ) -> main_models.UnbindAligenieUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.UnbindAligenieUserHeaders()
        return self.unbind_aligenie_user_with_options(request, headers, runtime)

    async def unbind_aligenie_user_async(
        self,
        request: main_models.UnbindAligenieUserRequest,
    ) -> main_models.UnbindAligenieUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.UnbindAligenieUserHeaders()
        return await self.unbind_aligenie_user_with_options_async(request, headers, runtime)

    def unbind_device_with_options(
        self,
        tmp_req: main_models.UnbindDeviceRequest,
        headers: main_models.UnbindDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDeviceResponse:
        tmp_req.validate()
        request = main_models.UnbindDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDevice',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/unbindDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_device_with_options_async(
        self,
        tmp_req: main_models.UnbindDeviceRequest,
        headers: main_models.UnbindDeviceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDeviceResponse:
        tmp_req.validate()
        request = main_models.UnbindDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDevice',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/unbindDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_device(
        self,
        request: main_models.UnbindDeviceRequest,
    ) -> main_models.UnbindDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.UnbindDeviceHeaders()
        return self.unbind_device_with_options(request, headers, runtime)

    async def unbind_device_async(
        self,
        request: main_models.UnbindDeviceRequest,
    ) -> main_models.UnbindDeviceResponse:
        runtime = RuntimeOptions()
        headers = main_models.UnbindDeviceHeaders()
        return await self.unbind_device_with_options_async(request, headers, runtime)

    def update_alarm_with_options(
        self,
        tmp_req: main_models.UpdateAlarmRequest,
        headers: main_models.UpdateAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlarmResponse:
        tmp_req.validate()
        request = main_models.UpdateAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlarm',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/updateAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alarm_with_options_async(
        self,
        tmp_req: main_models.UpdateAlarmRequest,
        headers: main_models.UpdateAlarmHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlarmResponse:
        tmp_req.validate()
        request = main_models.UpdateAlarmShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.device_info):
            request.device_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not DaraCore.is_null(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = str(headers.x_acs_aligenie_access_token)
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlarm',
            version = 'ssp_1.0',
            protocol = 'HTTPS',
            pathname = f'/v1.0/ssp/updateAlarm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alarm(
        self,
        request: main_models.UpdateAlarmRequest,
    ) -> main_models.UpdateAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateAlarmHeaders()
        return self.update_alarm_with_options(request, headers, runtime)

    async def update_alarm_async(
        self,
        request: main_models.UpdateAlarmRequest,
    ) -> main_models.UpdateAlarmResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateAlarmHeaders()
        return await self.update_alarm_with_options_async(request, headers, runtime)
