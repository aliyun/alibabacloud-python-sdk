# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_accountcenter20241209 import models as main_models
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
        self._endpoint = self.get_endpoint('accountcenter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def account_contact_add_with_options(
        self,
        request: main_models.AccountContactAddRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactAddResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactAdd',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_contact_add_with_options_async(
        self,
        request: main_models.AccountContactAddRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactAddResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactAdd',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_contact_add(
        self,
        request: main_models.AccountContactAddRequest,
    ) -> main_models.AccountContactAddResponse:
        runtime = RuntimeOptions()
        return self.account_contact_add_with_options(request, runtime)

    async def account_contact_add_async(
        self,
        request: main_models.AccountContactAddRequest,
    ) -> main_models.AccountContactAddResponse:
        runtime = RuntimeOptions()
        return await self.account_contact_add_with_options_async(request, runtime)

    def account_contact_delete_with_options(
        self,
        request: main_models.AccountContactDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactDeleteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactDelete',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_contact_delete_with_options_async(
        self,
        request: main_models.AccountContactDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactDeleteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactDelete',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_contact_delete(
        self,
        request: main_models.AccountContactDeleteRequest,
    ) -> main_models.AccountContactDeleteResponse:
        runtime = RuntimeOptions()
        return self.account_contact_delete_with_options(request, runtime)

    async def account_contact_delete_async(
        self,
        request: main_models.AccountContactDeleteRequest,
    ) -> main_models.AccountContactDeleteResponse:
        runtime = RuntimeOptions()
        return await self.account_contact_delete_with_options_async(request, runtime)

    def account_contact_edit_with_options(
        self,
        request: main_models.AccountContactEditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactEditResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactEdit',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactEditResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_contact_edit_with_options_async(
        self,
        request: main_models.AccountContactEditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactEditResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactEdit',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactEditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_contact_edit(
        self,
        request: main_models.AccountContactEditRequest,
    ) -> main_models.AccountContactEditResponse:
        runtime = RuntimeOptions()
        return self.account_contact_edit_with_options(request, runtime)

    async def account_contact_edit_async(
        self,
        request: main_models.AccountContactEditRequest,
    ) -> main_models.AccountContactEditResponse:
        runtime = RuntimeOptions()
        return await self.account_contact_edit_with_options_async(request, runtime)

    def account_contact_query_detail_with_options(
        self,
        request: main_models.AccountContactQueryDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactQueryDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactQueryDetail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactQueryDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_contact_query_detail_with_options_async(
        self,
        request: main_models.AccountContactQueryDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactQueryDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactQueryDetail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactQueryDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_contact_query_detail(
        self,
        request: main_models.AccountContactQueryDetailRequest,
    ) -> main_models.AccountContactQueryDetailResponse:
        runtime = RuntimeOptions()
        return self.account_contact_query_detail_with_options(request, runtime)

    async def account_contact_query_detail_async(
        self,
        request: main_models.AccountContactQueryDetailRequest,
    ) -> main_models.AccountContactQueryDetailResponse:
        runtime = RuntimeOptions()
        return await self.account_contact_query_detail_with_options_async(request, runtime)

    def account_contact_query_page_list_with_options(
        self,
        request: main_models.AccountContactQueryPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactQueryPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_contact):
            body['PrivateContact'] = request.private_contact
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactQueryPageList',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactQueryPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_contact_query_page_list_with_options_async(
        self,
        request: main_models.AccountContactQueryPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountContactQueryPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_contact):
            body['PrivateContact'] = request.private_contact
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AccountContactQueryPageList',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountContactQueryPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_contact_query_page_list(
        self,
        request: main_models.AccountContactQueryPageListRequest,
    ) -> main_models.AccountContactQueryPageListResponse:
        runtime = RuntimeOptions()
        return self.account_contact_query_page_list_with_options(request, runtime)

    async def account_contact_query_page_list_async(
        self,
        request: main_models.AccountContactQueryPageListRequest,
    ) -> main_models.AccountContactQueryPageListResponse:
        runtime = RuntimeOptions()
        return await self.account_contact_query_page_list_with_options_async(request, runtime)

    def enterprise_account_change_login_password_with_options(
        self,
        request: main_models.EnterpriseAccountChangeLoginPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountChangeLoginPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountChangeLoginPassword',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountChangeLoginPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_change_login_password_with_options_async(
        self,
        request: main_models.EnterpriseAccountChangeLoginPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountChangeLoginPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountChangeLoginPassword',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountChangeLoginPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_change_login_password(
        self,
        request: main_models.EnterpriseAccountChangeLoginPasswordRequest,
    ) -> main_models.EnterpriseAccountChangeLoginPasswordResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_change_login_password_with_options(request, runtime)

    async def enterprise_account_change_login_password_async(
        self,
        request: main_models.EnterpriseAccountChangeLoginPasswordRequest,
    ) -> main_models.EnterpriseAccountChangeLoginPasswordResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_change_login_password_with_options_async(request, runtime)

    def enterprise_account_change_security_email_with_options(
        self,
        request: main_models.EnterpriseAccountChangeSecurityEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountChangeSecurityEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.security_email):
            query['SecurityEmail'] = request.security_email
        if not DaraCore.is_null(request.verify_code):
            query['VerifyCode'] = request.verify_code
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountChangeSecurityEmail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountChangeSecurityEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_change_security_email_with_options_async(
        self,
        request: main_models.EnterpriseAccountChangeSecurityEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountChangeSecurityEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.security_email):
            query['SecurityEmail'] = request.security_email
        if not DaraCore.is_null(request.verify_code):
            query['VerifyCode'] = request.verify_code
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountChangeSecurityEmail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountChangeSecurityEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_change_security_email(
        self,
        request: main_models.EnterpriseAccountChangeSecurityEmailRequest,
    ) -> main_models.EnterpriseAccountChangeSecurityEmailResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_change_security_email_with_options(request, runtime)

    async def enterprise_account_change_security_email_async(
        self,
        request: main_models.EnterpriseAccountChangeSecurityEmailRequest,
    ) -> main_models.EnterpriseAccountChangeSecurityEmailResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_change_security_email_with_options_async(request, runtime)

    def enterprise_account_change_security_mobile_with_options(
        self,
        request: main_models.EnterpriseAccountChangeSecurityMobileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountChangeSecurityMobileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.new_mobile):
            query['NewMobile'] = request.new_mobile
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.verification_code):
            query['VerificationCode'] = request.verification_code
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountChangeSecurityMobile',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountChangeSecurityMobileResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_change_security_mobile_with_options_async(
        self,
        request: main_models.EnterpriseAccountChangeSecurityMobileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountChangeSecurityMobileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.new_mobile):
            query['NewMobile'] = request.new_mobile
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.verification_code):
            query['VerificationCode'] = request.verification_code
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountChangeSecurityMobile',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountChangeSecurityMobileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_change_security_mobile(
        self,
        request: main_models.EnterpriseAccountChangeSecurityMobileRequest,
    ) -> main_models.EnterpriseAccountChangeSecurityMobileResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_change_security_mobile_with_options(request, runtime)

    async def enterprise_account_change_security_mobile_async(
        self,
        request: main_models.EnterpriseAccountChangeSecurityMobileRequest,
    ) -> main_models.EnterpriseAccountChangeSecurityMobileResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_change_security_mobile_with_options_async(request, runtime)

    def enterprise_account_query_account_granted_roles_with_options(
        self,
        request: main_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.pk):
            body['Pk'] = request.pk
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountQueryAccountGrantedRoles',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountQueryAccountGrantedRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_query_account_granted_roles_with_options_async(
        self,
        request: main_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.pk):
            body['Pk'] = request.pk
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountQueryAccountGrantedRoles',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountQueryAccountGrantedRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_query_account_granted_roles(
        self,
        request: main_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
    ) -> main_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_query_account_granted_roles_with_options(request, runtime)

    async def enterprise_account_query_account_granted_roles_async(
        self,
        request: main_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
    ) -> main_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_query_account_granted_roles_with_options_async(request, runtime)

    def enterprise_account_query_accounts_info_with_options(
        self,
        request: main_models.EnterpriseAccountQueryAccountsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountQueryAccountsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.pks_json):
            query['PksJson'] = request.pks_json
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountQueryAccountsInfo',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountQueryAccountsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_query_accounts_info_with_options_async(
        self,
        request: main_models.EnterpriseAccountQueryAccountsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountQueryAccountsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.pks_json):
            query['PksJson'] = request.pks_json
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountQueryAccountsInfo',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountQueryAccountsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_query_accounts_info(
        self,
        request: main_models.EnterpriseAccountQueryAccountsInfoRequest,
    ) -> main_models.EnterpriseAccountQueryAccountsInfoResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_query_accounts_info_with_options(request, runtime)

    async def enterprise_account_query_accounts_info_async(
        self,
        request: main_models.EnterpriseAccountQueryAccountsInfoRequest,
    ) -> main_models.EnterpriseAccountQueryAccountsInfoResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_query_accounts_info_with_options_async(request, runtime)

    def enterprise_account_query_login_settings_with_options(
        self,
        request: main_models.EnterpriseAccountQueryLoginSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountQueryLoginSettingsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.pk):
            body['Pk'] = request.pk
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountQueryLoginSettings',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountQueryLoginSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_query_login_settings_with_options_async(
        self,
        request: main_models.EnterpriseAccountQueryLoginSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountQueryLoginSettingsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.pk):
            body['Pk'] = request.pk
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountQueryLoginSettings',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountQueryLoginSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_query_login_settings(
        self,
        request: main_models.EnterpriseAccountQueryLoginSettingsRequest,
    ) -> main_models.EnterpriseAccountQueryLoginSettingsResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_query_login_settings_with_options(request, runtime)

    async def enterprise_account_query_login_settings_async(
        self,
        request: main_models.EnterpriseAccountQueryLoginSettingsRequest,
    ) -> main_models.EnterpriseAccountQueryLoginSettingsResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_query_login_settings_with_options_async(request, runtime)

    def enterprise_account_remove_mfa_with_options(
        self,
        request: main_models.EnterpriseAccountRemoveMfaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountRemoveMfaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountRemoveMfa',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountRemoveMfaResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_remove_mfa_with_options_async(
        self,
        request: main_models.EnterpriseAccountRemoveMfaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountRemoveMfaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountRemoveMfa',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountRemoveMfaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_remove_mfa(
        self,
        request: main_models.EnterpriseAccountRemoveMfaRequest,
    ) -> main_models.EnterpriseAccountRemoveMfaResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_remove_mfa_with_options(request, runtime)

    async def enterprise_account_remove_mfa_async(
        self,
        request: main_models.EnterpriseAccountRemoveMfaRequest,
    ) -> main_models.EnterpriseAccountRemoveMfaResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_remove_mfa_with_options_async(request, runtime)

    def enterprise_account_separate_ea_with_options(
        self,
        request: main_models.EnterpriseAccountSeparateEaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountSeparateEaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountSeparateEa',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountSeparateEaResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_separate_ea_with_options_async(
        self,
        request: main_models.EnterpriseAccountSeparateEaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountSeparateEaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountSeparateEa',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountSeparateEaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_separate_ea(
        self,
        request: main_models.EnterpriseAccountSeparateEaRequest,
    ) -> main_models.EnterpriseAccountSeparateEaResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_separate_ea_with_options(request, runtime)

    async def enterprise_account_separate_ea_async(
        self,
        request: main_models.EnterpriseAccountSeparateEaRequest,
    ) -> main_models.EnterpriseAccountSeparateEaResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_separate_ea_with_options_async(request, runtime)

    def enterprise_account_update_account_alias_with_options(
        self,
        request: main_models.EnterpriseAccountUpdateAccountAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateAccountAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateAccountAlias',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_account_alias_with_options_async(
        self,
        request: main_models.EnterpriseAccountUpdateAccountAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateAccountAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateAccountAlias',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_account_alias(
        self,
        request: main_models.EnterpriseAccountUpdateAccountAliasRequest,
    ) -> main_models.EnterpriseAccountUpdateAccountAliasResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_update_account_alias_with_options(request, runtime)

    async def enterprise_account_update_account_alias_async(
        self,
        request: main_models.EnterpriseAccountUpdateAccountAliasRequest,
    ) -> main_models.EnterpriseAccountUpdateAccountAliasResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_update_account_alias_with_options_async(request, runtime)

    def enterprise_account_update_account_biz_role_grant_with_options(
        self,
        request: main_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code_list_json):
            query['BizRoleCodeListJson'] = request.biz_role_code_list_json
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateAccountBizRoleGrant',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_account_biz_role_grant_with_options_async(
        self,
        request: main_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code_list_json):
            query['BizRoleCodeListJson'] = request.biz_role_code_list_json
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateAccountBizRoleGrant',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_account_biz_role_grant(
        self,
        request: main_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
    ) -> main_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_update_account_biz_role_grant_with_options(request, runtime)

    async def enterprise_account_update_account_biz_role_grant_async(
        self,
        request: main_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
    ) -> main_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_update_account_biz_role_grant_with_options_async(request, runtime)

    def enterprise_account_update_ip_mask_with_options(
        self,
        request: main_models.EnterpriseAccountUpdateIpMaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateIpMaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_masks_json):
            query['IpMasksJson'] = request.ip_masks_json
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateIpMask',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateIpMaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_ip_mask_with_options_async(
        self,
        request: main_models.EnterpriseAccountUpdateIpMaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateIpMaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_masks_json):
            query['IpMasksJson'] = request.ip_masks_json
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateIpMask',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateIpMaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_ip_mask(
        self,
        request: main_models.EnterpriseAccountUpdateIpMaskRequest,
    ) -> main_models.EnterpriseAccountUpdateIpMaskResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_update_ip_mask_with_options(request, runtime)

    async def enterprise_account_update_ip_mask_async(
        self,
        request: main_models.EnterpriseAccountUpdateIpMaskRequest,
    ) -> main_models.EnterpriseAccountUpdateIpMaskResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_update_ip_mask_with_options_async(request, runtime)

    def enterprise_account_update_operate_risk_control_with_options(
        self,
        request: main_models.EnterpriseAccountUpdateOperateRiskControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.product_level):
            query['ProductLevel'] = request.product_level
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateOperateRiskControl',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateOperateRiskControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_operate_risk_control_with_options_async(
        self,
        request: main_models.EnterpriseAccountUpdateOperateRiskControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.product_level):
            query['ProductLevel'] = request.product_level
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateOperateRiskControl',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateOperateRiskControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_operate_risk_control(
        self,
        request: main_models.EnterpriseAccountUpdateOperateRiskControlRequest,
    ) -> main_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_update_operate_risk_control_with_options(request, runtime)

    async def enterprise_account_update_operate_risk_control_async(
        self,
        request: main_models.EnterpriseAccountUpdateOperateRiskControlRequest,
    ) -> main_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_update_operate_risk_control_with_options_async(request, runtime)

    def enterprise_account_update_security_mobile_login_status_with_options(
        self,
        request: main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateSecurityMobileLoginStatus',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_security_mobile_login_status_with_options_async(
        self,
        request: main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateSecurityMobileLoginStatus',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_security_mobile_login_status(
        self,
        request: main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
    ) -> main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_update_security_mobile_login_status_with_options(request, runtime)

    async def enterprise_account_update_security_mobile_login_status_async(
        self,
        request: main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
    ) -> main_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_update_security_mobile_login_status_with_options_async(request, runtime)

    def enterprise_account_update_session_expire_time_with_options(
        self,
        request: main_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.session_expire_time):
            query['SessionExpireTime'] = request.session_expire_time
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateSessionExpireTime',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateSessionExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_session_expire_time_with_options_async(
        self,
        request: main_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.session_expire_time):
            query['SessionExpireTime'] = request.session_expire_time
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseAccountUpdateSessionExpireTime',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseAccountUpdateSessionExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_session_expire_time(
        self,
        request: main_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
    ) -> main_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        runtime = RuntimeOptions()
        return self.enterprise_account_update_session_expire_time_with_options(request, runtime)

    async def enterprise_account_update_session_expire_time_async(
        self,
        request: main_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
    ) -> main_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_account_update_session_expire_time_with_options_async(request, runtime)

    def enterprise_contact_add_with_options(
        self,
        request: main_models.EnterpriseContactAddRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactAddResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactAdd',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactAddResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_contact_add_with_options_async(
        self,
        request: main_models.EnterpriseContactAddRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactAddResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactAdd',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactAddResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_contact_add(
        self,
        request: main_models.EnterpriseContactAddRequest,
    ) -> main_models.EnterpriseContactAddResponse:
        runtime = RuntimeOptions()
        return self.enterprise_contact_add_with_options(request, runtime)

    async def enterprise_contact_add_async(
        self,
        request: main_models.EnterpriseContactAddRequest,
    ) -> main_models.EnterpriseContactAddResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_contact_add_with_options_async(request, runtime)

    def enterprise_contact_delete_with_options(
        self,
        request: main_models.EnterpriseContactDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactDeleteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactDelete',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_contact_delete_with_options_async(
        self,
        request: main_models.EnterpriseContactDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactDeleteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactDelete',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_contact_delete(
        self,
        request: main_models.EnterpriseContactDeleteRequest,
    ) -> main_models.EnterpriseContactDeleteResponse:
        runtime = RuntimeOptions()
        return self.enterprise_contact_delete_with_options(request, runtime)

    async def enterprise_contact_delete_async(
        self,
        request: main_models.EnterpriseContactDeleteRequest,
    ) -> main_models.EnterpriseContactDeleteResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_contact_delete_with_options_async(request, runtime)

    def enterprise_contact_edit_with_options(
        self,
        request: main_models.EnterpriseContactEditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactEditResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactEdit',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactEditResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_contact_edit_with_options_async(
        self,
        request: main_models.EnterpriseContactEditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactEditResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.async_email_verify):
            body['AsyncEmailVerify'] = request.async_email_verify
        if not DaraCore.is_null(request.async_mobile_verify):
            body['AsyncMobileVerify'] = request.async_mobile_verify
        if not DaraCore.is_null(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_position):
            body['ContactPosition'] = request.contact_position
        if not DaraCore.is_null(request.email_code):
            body['EmailCode'] = request.email_code
        if not DaraCore.is_null(request.mobile_code):
            body['MobileCode'] = request.mobile_code
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactEdit',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactEditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_contact_edit(
        self,
        request: main_models.EnterpriseContactEditRequest,
    ) -> main_models.EnterpriseContactEditResponse:
        runtime = RuntimeOptions()
        return self.enterprise_contact_edit_with_options(request, runtime)

    async def enterprise_contact_edit_async(
        self,
        request: main_models.EnterpriseContactEditRequest,
    ) -> main_models.EnterpriseContactEditResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_contact_edit_with_options_async(request, runtime)

    def enterprise_contact_query_detail_with_options(
        self,
        request: main_models.EnterpriseContactQueryDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactQueryDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactQueryDetail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactQueryDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_contact_query_detail_with_options_async(
        self,
        request: main_models.EnterpriseContactQueryDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactQueryDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactQueryDetail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactQueryDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_contact_query_detail(
        self,
        request: main_models.EnterpriseContactQueryDetailRequest,
    ) -> main_models.EnterpriseContactQueryDetailResponse:
        runtime = RuntimeOptions()
        return self.enterprise_contact_query_detail_with_options(request, runtime)

    async def enterprise_contact_query_detail_async(
        self,
        request: main_models.EnterpriseContactQueryDetailRequest,
    ) -> main_models.EnterpriseContactQueryDetailResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_contact_query_detail_with_options_async(request, runtime)

    def enterprise_contact_query_page_list_with_options(
        self,
        request: main_models.EnterpriseContactQueryPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactQueryPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_contact):
            body['PrivateContact'] = request.private_contact
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactQueryPageList',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactQueryPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_contact_query_page_list_with_options_async(
        self,
        request: main_models.EnterpriseContactQueryPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseContactQueryPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_contact):
            body['PrivateContact'] = request.private_contact
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.shared_contact):
            body['SharedContact'] = request.shared_contact
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseContactQueryPageList',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseContactQueryPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_contact_query_page_list(
        self,
        request: main_models.EnterpriseContactQueryPageListRequest,
    ) -> main_models.EnterpriseContactQueryPageListResponse:
        runtime = RuntimeOptions()
        return self.enterprise_contact_query_page_list_with_options(request, runtime)

    async def enterprise_contact_query_page_list_async(
        self,
        request: main_models.EnterpriseContactQueryPageListRequest,
    ) -> main_models.EnterpriseContactQueryPageListResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_contact_query_page_list_with_options_async(request, runtime)

    def enterprise_org_query_load_tree_with_options(
        self,
        request: main_models.EnterpriseOrgQueryLoadTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseOrgQueryLoadTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.load_org_only):
            query['LoadOrgOnly'] = request.load_org_only
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseOrgQueryLoadTree',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseOrgQueryLoadTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_org_query_load_tree_with_options_async(
        self,
        request: main_models.EnterpriseOrgQueryLoadTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseOrgQueryLoadTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.load_org_only):
            query['LoadOrgOnly'] = request.load_org_only
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseOrgQueryLoadTree',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseOrgQueryLoadTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_org_query_load_tree(
        self,
        request: main_models.EnterpriseOrgQueryLoadTreeRequest,
    ) -> main_models.EnterpriseOrgQueryLoadTreeResponse:
        runtime = RuntimeOptions()
        return self.enterprise_org_query_load_tree_with_options(request, runtime)

    async def enterprise_org_query_load_tree_async(
        self,
        request: main_models.EnterpriseOrgQueryLoadTreeRequest,
    ) -> main_models.EnterpriseOrgQueryLoadTreeResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_org_query_load_tree_with_options_async(request, runtime)

    def enterprise_register_account_with_options(
        self,
        request: main_models.EnterpriseRegisterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRegisterAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        if not DaraCore.is_null(request.site_nick):
            query['SiteNick'] = request.site_nick
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRegisterAccount',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRegisterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_register_account_with_options_async(
        self,
        request: main_models.EnterpriseRegisterAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRegisterAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        if not DaraCore.is_null(request.site_nick):
            query['SiteNick'] = request.site_nick
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRegisterAccount',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRegisterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_register_account(
        self,
        request: main_models.EnterpriseRegisterAccountRequest,
    ) -> main_models.EnterpriseRegisterAccountResponse:
        runtime = RuntimeOptions()
        return self.enterprise_register_account_with_options(request, runtime)

    async def enterprise_register_account_async(
        self,
        request: main_models.EnterpriseRegisterAccountRequest,
    ) -> main_models.EnterpriseRegisterAccountResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_register_account_with_options_async(request, runtime)

    def enterprise_role_create_biz_role_with_options(
        self,
        request: main_models.EnterpriseRoleCreateBizRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleCreateBizRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not DaraCore.is_null(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not DaraCore.is_null(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleCreateBizRole',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleCreateBizRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_create_biz_role_with_options_async(
        self,
        request: main_models.EnterpriseRoleCreateBizRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleCreateBizRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not DaraCore.is_null(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not DaraCore.is_null(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleCreateBizRole',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleCreateBizRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_create_biz_role(
        self,
        request: main_models.EnterpriseRoleCreateBizRoleRequest,
    ) -> main_models.EnterpriseRoleCreateBizRoleResponse:
        runtime = RuntimeOptions()
        return self.enterprise_role_create_biz_role_with_options(request, runtime)

    async def enterprise_role_create_biz_role_async(
        self,
        request: main_models.EnterpriseRoleCreateBizRoleRequest,
    ) -> main_models.EnterpriseRoleCreateBizRoleResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_role_create_biz_role_with_options_async(request, runtime)

    def enterprise_role_delete_biz_role_with_options(
        self,
        request: main_models.EnterpriseRoleDeleteBizRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleDeleteBizRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleDeleteBizRole',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleDeleteBizRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_delete_biz_role_with_options_async(
        self,
        request: main_models.EnterpriseRoleDeleteBizRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleDeleteBizRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleDeleteBizRole',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleDeleteBizRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_delete_biz_role(
        self,
        request: main_models.EnterpriseRoleDeleteBizRoleRequest,
    ) -> main_models.EnterpriseRoleDeleteBizRoleResponse:
        runtime = RuntimeOptions()
        return self.enterprise_role_delete_biz_role_with_options(request, runtime)

    async def enterprise_role_delete_biz_role_async(
        self,
        request: main_models.EnterpriseRoleDeleteBizRoleRequest,
    ) -> main_models.EnterpriseRoleDeleteBizRoleResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_role_delete_biz_role_with_options_async(request, runtime)

    def enterprise_role_query_account_for_role_grant_by_page_with_options(
        self,
        request: main_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleQueryAccountForRoleGrantByPage',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_query_account_for_role_grant_by_page_with_options_async(
        self,
        request: main_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleQueryAccountForRoleGrantByPage',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_query_account_for_role_grant_by_page(
        self,
        request: main_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
    ) -> main_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        runtime = RuntimeOptions()
        return self.enterprise_role_query_account_for_role_grant_by_page_with_options(request, runtime)

    async def enterprise_role_query_account_for_role_grant_by_page_async(
        self,
        request: main_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
    ) -> main_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_role_query_account_for_role_grant_by_page_with_options_async(request, runtime)

    def enterprise_role_query_biz_role_by_page_with_options(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleQueryBizRoleByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.src_type):
            query['SrcType'] = request.src_type
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleQueryBizRoleByPage',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleQueryBizRoleByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_query_biz_role_by_page_with_options_async(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleQueryBizRoleByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.src_type):
            query['SrcType'] = request.src_type
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleQueryBizRoleByPage',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleQueryBizRoleByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_query_biz_role_by_page(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleByPageRequest,
    ) -> main_models.EnterpriseRoleQueryBizRoleByPageResponse:
        runtime = RuntimeOptions()
        return self.enterprise_role_query_biz_role_by_page_with_options(request, runtime)

    async def enterprise_role_query_biz_role_by_page_async(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleByPageRequest,
    ) -> main_models.EnterpriseRoleQueryBizRoleByPageResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_role_query_biz_role_by_page_with_options_async(request, runtime)

    def enterprise_role_query_biz_role_detail_with_options(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleQueryBizRoleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleQueryBizRoleDetail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleQueryBizRoleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_query_biz_role_detail_with_options_async(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleQueryBizRoleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleQueryBizRoleDetail',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleQueryBizRoleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_query_biz_role_detail(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleDetailRequest,
    ) -> main_models.EnterpriseRoleQueryBizRoleDetailResponse:
        runtime = RuntimeOptions()
        return self.enterprise_role_query_biz_role_detail_with_options(request, runtime)

    async def enterprise_role_query_biz_role_detail_async(
        self,
        request: main_models.EnterpriseRoleQueryBizRoleDetailRequest,
    ) -> main_models.EnterpriseRoleQueryBizRoleDetailResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_role_query_biz_role_detail_with_options_async(request, runtime)

    def enterprise_role_update_biz_role_with_options(
        self,
        request: main_models.EnterpriseRoleUpdateBizRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleUpdateBizRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not DaraCore.is_null(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleUpdateBizRole',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleUpdateBizRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_update_biz_role_with_options_async(
        self,
        request: main_models.EnterpriseRoleUpdateBizRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseRoleUpdateBizRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not DaraCore.is_null(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not DaraCore.is_null(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not DaraCore.is_null(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        body = {}
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseRoleUpdateBizRole',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseRoleUpdateBizRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_update_biz_role(
        self,
        request: main_models.EnterpriseRoleUpdateBizRoleRequest,
    ) -> main_models.EnterpriseRoleUpdateBizRoleResponse:
        runtime = RuntimeOptions()
        return self.enterprise_role_update_biz_role_with_options(request, runtime)

    async def enterprise_role_update_biz_role_async(
        self,
        request: main_models.EnterpriseRoleUpdateBizRoleRequest,
    ) -> main_models.EnterpriseRoleUpdateBizRoleResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_role_update_biz_role_with_options_async(request, runtime)

    def enterprise_todo_deal_account_todo_with_options(
        self,
        request: main_models.EnterpriseTodoDealAccountTodoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseTodoDealAccountTodoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.todo_id):
            body['TodoId'] = request.todo_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseTodoDealAccountTodo',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseTodoDealAccountTodoResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_todo_deal_account_todo_with_options_async(
        self,
        request: main_models.EnterpriseTodoDealAccountTodoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseTodoDealAccountTodoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.todo_id):
            body['TodoId'] = request.todo_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseTodoDealAccountTodo',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseTodoDealAccountTodoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_todo_deal_account_todo(
        self,
        request: main_models.EnterpriseTodoDealAccountTodoRequest,
    ) -> main_models.EnterpriseTodoDealAccountTodoResponse:
        runtime = RuntimeOptions()
        return self.enterprise_todo_deal_account_todo_with_options(request, runtime)

    async def enterprise_todo_deal_account_todo_async(
        self,
        request: main_models.EnterpriseTodoDealAccountTodoRequest,
    ) -> main_models.EnterpriseTodoDealAccountTodoResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_todo_deal_account_todo_with_options_async(request, runtime)

    def enterprise_todo_query_account_todo_list_with_options(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseTodoQueryAccountTodoList',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseTodoQueryAccountTodoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_todo_query_account_todo_list_with_options_async(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseTodoQueryAccountTodoList',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseTodoQueryAccountTodoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_todo_query_account_todo_list(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListRequest,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListResponse:
        runtime = RuntimeOptions()
        return self.enterprise_todo_query_account_todo_list_with_options(request, runtime)

    async def enterprise_todo_query_account_todo_list_async(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListRequest,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_todo_query_account_todo_list_with_options_async(request, runtime)

    def enterprise_todo_query_account_todo_list_by_applicant_with_options(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseTodoQueryAccountTodoListByApplicant',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_todo_query_account_todo_list_by_applicant_with_options_async(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not DaraCore.is_null(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not DaraCore.is_null(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not DaraCore.is_null(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseTodoQueryAccountTodoListByApplicant',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_todo_query_account_todo_list_by_applicant(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        runtime = RuntimeOptions()
        return self.enterprise_todo_query_account_todo_list_by_applicant_with_options(request, runtime)

    async def enterprise_todo_query_account_todo_list_by_applicant_async(
        self,
        request: main_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
    ) -> main_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_todo_query_account_todo_list_by_applicant_with_options_async(request, runtime)

    def enterprise_uninvited_admin_invite_join_enterprise_with_options(
        self,
        request: main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id):
            query['EcId'] = request.ec_id
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.invitee_pk):
            query['InviteePk'] = request.invitee_pk
        if not DaraCore.is_null(request.le_id):
            query['LeId'] = request.le_id
        if not DaraCore.is_null(request.nb_id):
            query['NbId'] = request.nb_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseUninvitedAdminInviteJoinEnterprise',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_uninvited_admin_invite_join_enterprise_with_options_async(
        self,
        request: main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id):
            query['EcId'] = request.ec_id
        if not DaraCore.is_null(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not DaraCore.is_null(request.invitee_pk):
            query['InviteePk'] = request.invitee_pk
        if not DaraCore.is_null(request.le_id):
            query['LeId'] = request.le_id
        if not DaraCore.is_null(request.nb_id):
            query['NbId'] = request.nb_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnterpriseUninvitedAdminInviteJoinEnterprise',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_uninvited_admin_invite_join_enterprise(
        self,
        request: main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
    ) -> main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        runtime = RuntimeOptions()
        return self.enterprise_uninvited_admin_invite_join_enterprise_with_options(request, runtime)

    async def enterprise_uninvited_admin_invite_join_enterprise_async(
        self,
        request: main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
    ) -> main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        runtime = RuntimeOptions()
        return await self.enterprise_uninvited_admin_invite_join_enterprise_with_options_async(request, runtime)

    def send_async_email_captcha_with_options(
        self,
        request: main_models.SendAsyncEmailCaptchaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendAsyncEmailCaptchaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.contactor_id):
            body['ContactorId'] = request.contactor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendAsyncEmailCaptcha',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendAsyncEmailCaptchaResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_async_email_captcha_with_options_async(
        self,
        request: main_models.SendAsyncEmailCaptchaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendAsyncEmailCaptchaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.contactor_id):
            body['ContactorId'] = request.contactor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendAsyncEmailCaptcha',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendAsyncEmailCaptchaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_async_email_captcha(
        self,
        request: main_models.SendAsyncEmailCaptchaRequest,
    ) -> main_models.SendAsyncEmailCaptchaResponse:
        runtime = RuntimeOptions()
        return self.send_async_email_captcha_with_options(request, runtime)

    async def send_async_email_captcha_async(
        self,
        request: main_models.SendAsyncEmailCaptchaRequest,
    ) -> main_models.SendAsyncEmailCaptchaResponse:
        runtime = RuntimeOptions()
        return await self.send_async_email_captcha_with_options_async(request, runtime)

    def send_async_mobile_captcha_with_options(
        self,
        request: main_models.SendAsyncMobileCaptchaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendAsyncMobileCaptchaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.contactor_id):
            body['ContactorId'] = request.contactor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendAsyncMobileCaptcha',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendAsyncMobileCaptchaResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_async_mobile_captcha_with_options_async(
        self,
        request: main_models.SendAsyncMobileCaptchaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendAsyncMobileCaptchaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.contactor_id):
            body['ContactorId'] = request.contactor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendAsyncMobileCaptcha',
            version = '2024-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendAsyncMobileCaptchaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_async_mobile_captcha(
        self,
        request: main_models.SendAsyncMobileCaptchaRequest,
    ) -> main_models.SendAsyncMobileCaptchaResponse:
        runtime = RuntimeOptions()
        return self.send_async_mobile_captcha_with_options(request, runtime)

    async def send_async_mobile_captcha_async(
        self,
        request: main_models.SendAsyncMobileCaptchaRequest,
    ) -> main_models.SendAsyncMobileCaptchaResponse:
        runtime = RuntimeOptions()
        return await self.send_async_mobile_captcha_with_options_async(request, runtime)
