# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_account_crm20160606 import models as main_models
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
        self._endpoint = self.get_endpoint('account-crm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def account_one_key_delete_with_options(
        self,
        request: main_models.AccountOneKeyDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountOneKeyDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AccountOneKeyDelete',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountOneKeyDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def account_one_key_delete_with_options_async(
        self,
        request: main_models.AccountOneKeyDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AccountOneKeyDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AccountOneKeyDelete',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AccountOneKeyDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def account_one_key_delete(
        self,
        request: main_models.AccountOneKeyDeleteRequest,
    ) -> main_models.AccountOneKeyDeleteResponse:
        runtime = RuntimeOptions()
        return self.account_one_key_delete_with_options(request, runtime)

    async def account_one_key_delete_async(
        self,
        request: main_models.AccountOneKeyDeleteRequest,
    ) -> main_models.AccountOneKeyDeleteResponse:
        runtime = RuntimeOptions()
        return await self.account_one_key_delete_with_options_async(request, runtime)

    def add_customer_label_with_options(
        self,
        request: main_models.AddCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endtime):
            query['Endtime'] = request.endtime
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomerLabel',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomerLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_customer_label_with_options_async(
        self,
        request: main_models.AddCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endtime):
            query['Endtime'] = request.endtime
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomerLabel',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomerLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_customer_label(
        self,
        request: main_models.AddCustomerLabelRequest,
    ) -> main_models.AddCustomerLabelResponse:
        runtime = RuntimeOptions()
        return self.add_customer_label_with_options(request, runtime)

    async def add_customer_label_async(
        self,
        request: main_models.AddCustomerLabelRequest,
    ) -> main_models.AddCustomerLabelResponse:
        runtime = RuntimeOptions()
        return await self.add_customer_label_with_options_async(request, runtime)

    def allow_ag_account_login_with_options(
        self,
        request: main_models.AllowAgAccountLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllowAgAccountLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllowAgAccountLogin',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllowAgAccountLoginResponse(),
            self.call_api(params, req, runtime)
        )

    async def allow_ag_account_login_with_options_async(
        self,
        request: main_models.AllowAgAccountLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllowAgAccountLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllowAgAccountLogin',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllowAgAccountLoginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allow_ag_account_login(
        self,
        request: main_models.AllowAgAccountLoginRequest,
    ) -> main_models.AllowAgAccountLoginResponse:
        runtime = RuntimeOptions()
        return self.allow_ag_account_login_with_options(request, runtime)

    async def allow_ag_account_login_async(
        self,
        request: main_models.AllowAgAccountLoginRequest,
    ) -> main_models.AllowAgAccountLoginResponse:
        runtime = RuntimeOptions()
        return await self.allow_ag_account_login_with_options_async(request, runtime)

    def apply_ag_one_key_delete_task_with_options(
        self,
        request: main_models.ApplyAgOneKeyDeleteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAgOneKeyDeleteTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abandoned_dependency):
            query['AbandonedDependency'] = request.abandoned_dependency
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAgOneKeyDeleteTask',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAgOneKeyDeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ag_one_key_delete_task_with_options_async(
        self,
        request: main_models.ApplyAgOneKeyDeleteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAgOneKeyDeleteTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abandoned_dependency):
            query['AbandonedDependency'] = request.abandoned_dependency
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAgOneKeyDeleteTask',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAgOneKeyDeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ag_one_key_delete_task(
        self,
        request: main_models.ApplyAgOneKeyDeleteTaskRequest,
    ) -> main_models.ApplyAgOneKeyDeleteTaskResponse:
        runtime = RuntimeOptions()
        return self.apply_ag_one_key_delete_task_with_options(request, runtime)

    async def apply_ag_one_key_delete_task_async(
        self,
        request: main_models.ApplyAgOneKeyDeleteTaskRequest,
    ) -> main_models.ApplyAgOneKeyDeleteTaskResponse:
        runtime = RuntimeOptions()
        return await self.apply_ag_one_key_delete_task_with_options_async(request, runtime)

    def apply_ag_one_key_only_checker_task_with_options(
        self,
        request: main_models.ApplyAgOneKeyOnlyCheckerTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAgOneKeyOnlyCheckerTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAgOneKeyOnlyCheckerTask',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAgOneKeyOnlyCheckerTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ag_one_key_only_checker_task_with_options_async(
        self,
        request: main_models.ApplyAgOneKeyOnlyCheckerTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAgOneKeyOnlyCheckerTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAgOneKeyOnlyCheckerTask',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAgOneKeyOnlyCheckerTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ag_one_key_only_checker_task(
        self,
        request: main_models.ApplyAgOneKeyOnlyCheckerTaskRequest,
    ) -> main_models.ApplyAgOneKeyOnlyCheckerTaskResponse:
        runtime = RuntimeOptions()
        return self.apply_ag_one_key_only_checker_task_with_options(request, runtime)

    async def apply_ag_one_key_only_checker_task_async(
        self,
        request: main_models.ApplyAgOneKeyOnlyCheckerTaskRequest,
    ) -> main_models.ApplyAgOneKeyOnlyCheckerTaskResponse:
        runtime = RuntimeOptions()
        return await self.apply_ag_one_key_only_checker_task_with_options_async(request, runtime)

    def apply_identity_registration_with_options(
        self,
        request: main_models.ApplyIdentityRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyIdentityRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.doc_back_pic):
            query['DocBackPic'] = request.doc_back_pic
        if not DaraCore.is_null(request.doc_front_pic):
            query['DocFrontPic'] = request.doc_front_pic
        if not DaraCore.is_null(request.doc_num):
            query['DocNum'] = request.doc_num
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.full_name):
            query['FullName'] = request.full_name
        if not DaraCore.is_null(request.registered_address):
            query['RegisteredAddress'] = request.registered_address
        if not DaraCore.is_null(request.registered_country):
            query['RegisteredCountry'] = request.registered_country
        if not DaraCore.is_null(request.registered_num):
            query['RegisteredNum'] = request.registered_num
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tel):
            query['Tel'] = request.tel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyIdentityRegistration',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyIdentityRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_identity_registration_with_options_async(
        self,
        request: main_models.ApplyIdentityRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyIdentityRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.doc_back_pic):
            query['DocBackPic'] = request.doc_back_pic
        if not DaraCore.is_null(request.doc_front_pic):
            query['DocFrontPic'] = request.doc_front_pic
        if not DaraCore.is_null(request.doc_num):
            query['DocNum'] = request.doc_num
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.full_name):
            query['FullName'] = request.full_name
        if not DaraCore.is_null(request.registered_address):
            query['RegisteredAddress'] = request.registered_address
        if not DaraCore.is_null(request.registered_country):
            query['RegisteredCountry'] = request.registered_country
        if not DaraCore.is_null(request.registered_num):
            query['RegisteredNum'] = request.registered_num
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tel):
            query['Tel'] = request.tel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyIdentityRegistration',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyIdentityRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_identity_registration(
        self,
        request: main_models.ApplyIdentityRegistrationRequest,
    ) -> main_models.ApplyIdentityRegistrationResponse:
        runtime = RuntimeOptions()
        return self.apply_identity_registration_with_options(request, runtime)

    async def apply_identity_registration_async(
        self,
        request: main_models.ApplyIdentityRegistrationRequest,
    ) -> main_models.ApplyIdentityRegistrationResponse:
        runtime = RuntimeOptions()
        return await self.apply_identity_registration_with_options_async(request, runtime)

    def async_create_ag_account_with_options(
        self,
        request: main_models.AsyncCreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncCreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.maser_account_info):
            query['MaserAccountInfo'] = request.maser_account_info
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsyncCreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncCreateAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_create_ag_account_with_options_async(
        self,
        request: main_models.AsyncCreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncCreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.maser_account_info):
            query['MaserAccountInfo'] = request.maser_account_info
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsyncCreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncCreateAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_create_ag_account(
        self,
        request: main_models.AsyncCreateAgAccountRequest,
    ) -> main_models.AsyncCreateAgAccountResponse:
        runtime = RuntimeOptions()
        return self.async_create_ag_account_with_options(request, runtime)

    async def async_create_ag_account_async(
        self,
        request: main_models.AsyncCreateAgAccountRequest,
    ) -> main_models.AsyncCreateAgAccountResponse:
        runtime = RuntimeOptions()
        return await self.async_create_ag_account_with_options_async(request, runtime)

    def async_modify_ag_login_email_with_options(
        self,
        request: main_models.AsyncModifyAgLoginEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncModifyAgLoginEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.new_login_email):
            query['NewLoginEmail'] = request.new_login_email
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsyncModifyAgLoginEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncModifyAgLoginEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_modify_ag_login_email_with_options_async(
        self,
        request: main_models.AsyncModifyAgLoginEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncModifyAgLoginEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.new_login_email):
            query['NewLoginEmail'] = request.new_login_email
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsyncModifyAgLoginEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncModifyAgLoginEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_modify_ag_login_email(
        self,
        request: main_models.AsyncModifyAgLoginEmailRequest,
    ) -> main_models.AsyncModifyAgLoginEmailResponse:
        runtime = RuntimeOptions()
        return self.async_modify_ag_login_email_with_options(request, runtime)

    async def async_modify_ag_login_email_async(
        self,
        request: main_models.AsyncModifyAgLoginEmailRequest,
    ) -> main_models.AsyncModifyAgLoginEmailResponse:
        runtime = RuntimeOptions()
        return await self.async_modify_ag_login_email_with_options_async(request, runtime)

    def auth_and_active_with_hid_with_options(
        self,
        request: main_models.AuthAndActiveWithHidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthAndActiveWithHidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthAndActiveWithHid',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthAndActiveWithHidResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_and_active_with_hid_with_options_async(
        self,
        request: main_models.AuthAndActiveWithHidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthAndActiveWithHidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthAndActiveWithHid',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthAndActiveWithHidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_and_active_with_hid(
        self,
        request: main_models.AuthAndActiveWithHidRequest,
    ) -> main_models.AuthAndActiveWithHidResponse:
        runtime = RuntimeOptions()
        return self.auth_and_active_with_hid_with_options(request, runtime)

    async def auth_and_active_with_hid_async(
        self,
        request: main_models.AuthAndActiveWithHidRequest,
    ) -> main_models.AuthAndActiveWithHidResponse:
        runtime = RuntimeOptions()
        return await self.auth_and_active_with_hid_with_options_async(request, runtime)

    def auth_and_refresh_login_ticket_with_options(
        self,
        request: main_models.AuthAndRefreshLoginTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthAndRefreshLoginTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthAndRefreshLoginTicket',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthAndRefreshLoginTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_and_refresh_login_ticket_with_options_async(
        self,
        request: main_models.AuthAndRefreshLoginTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthAndRefreshLoginTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthAndRefreshLoginTicket',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthAndRefreshLoginTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_and_refresh_login_ticket(
        self,
        request: main_models.AuthAndRefreshLoginTicketRequest,
    ) -> main_models.AuthAndRefreshLoginTicketResponse:
        runtime = RuntimeOptions()
        return self.auth_and_refresh_login_ticket_with_options(request, runtime)

    async def auth_and_refresh_login_ticket_async(
        self,
        request: main_models.AuthAndRefreshLoginTicketRequest,
    ) -> main_models.AuthAndRefreshLoginTicketResponse:
        runtime = RuntimeOptions()
        return await self.auth_and_refresh_login_ticket_with_options_async(request, runtime)

    def auth_login_ticket_with_options(
        self,
        request: main_models.AuthLoginTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.minor_auth_code):
            query['MinorAuthCode'] = request.minor_auth_code
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginTicket',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_login_ticket_with_options_async(
        self,
        request: main_models.AuthLoginTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthLoginTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.minor_auth_code):
            query['MinorAuthCode'] = request.minor_auth_code
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthLoginTicket',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthLoginTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_login_ticket(
        self,
        request: main_models.AuthLoginTicketRequest,
    ) -> main_models.AuthLoginTicketResponse:
        runtime = RuntimeOptions()
        return self.auth_login_ticket_with_options(request, runtime)

    async def auth_login_ticket_async(
        self,
        request: main_models.AuthLoginTicketRequest,
    ) -> main_models.AuthLoginTicketResponse:
        runtime = RuntimeOptions()
        return await self.auth_login_ticket_with_options_async(request, runtime)

    def batch_query_ag_account_with_options(
        self,
        request: main_models.BatchQueryAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk_list):
            query['PkList'] = request.pk_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_ag_account_with_options_async(
        self,
        request: main_models.BatchQueryAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk_list):
            query['PkList'] = request.pk_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_ag_account(
        self,
        request: main_models.BatchQueryAgAccountRequest,
    ) -> main_models.BatchQueryAgAccountResponse:
        runtime = RuntimeOptions()
        return self.batch_query_ag_account_with_options(request, runtime)

    async def batch_query_ag_account_async(
        self,
        request: main_models.BatchQueryAgAccountRequest,
    ) -> main_models.BatchQueryAgAccountResponse:
        runtime = RuntimeOptions()
        return await self.batch_query_ag_account_with_options_async(request, runtime)

    def batch_query_create_account_trace_with_options(
        self,
        request: main_models.BatchQueryCreateAccountTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryCreateAccountTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no_list):
            query['TraceNoList'] = request.trace_no_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryCreateAccountTrace',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryCreateAccountTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_create_account_trace_with_options_async(
        self,
        request: main_models.BatchQueryCreateAccountTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryCreateAccountTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no_list):
            query['TraceNoList'] = request.trace_no_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryCreateAccountTrace',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryCreateAccountTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_create_account_trace(
        self,
        request: main_models.BatchQueryCreateAccountTraceRequest,
    ) -> main_models.BatchQueryCreateAccountTraceResponse:
        runtime = RuntimeOptions()
        return self.batch_query_create_account_trace_with_options(request, runtime)

    async def batch_query_create_account_trace_async(
        self,
        request: main_models.BatchQueryCreateAccountTraceRequest,
    ) -> main_models.BatchQueryCreateAccountTraceResponse:
        runtime = RuntimeOptions()
        return await self.batch_query_create_account_trace_with_options_async(request, runtime)

    def batch_query_modify_login_email_trace_with_options(
        self,
        request: main_models.BatchQueryModifyLoginEmailTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryModifyLoginEmailTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no_list):
            query['TraceNoList'] = request.trace_no_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryModifyLoginEmailTrace',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryModifyLoginEmailTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_modify_login_email_trace_with_options_async(
        self,
        request: main_models.BatchQueryModifyLoginEmailTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryModifyLoginEmailTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no_list):
            query['TraceNoList'] = request.trace_no_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryModifyLoginEmailTrace',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryModifyLoginEmailTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_modify_login_email_trace(
        self,
        request: main_models.BatchQueryModifyLoginEmailTraceRequest,
    ) -> main_models.BatchQueryModifyLoginEmailTraceResponse:
        runtime = RuntimeOptions()
        return self.batch_query_modify_login_email_trace_with_options(request, runtime)

    async def batch_query_modify_login_email_trace_async(
        self,
        request: main_models.BatchQueryModifyLoginEmailTraceRequest,
    ) -> main_models.BatchQueryModifyLoginEmailTraceResponse:
        runtime = RuntimeOptions()
        return await self.batch_query_modify_login_email_trace_with_options_async(request, runtime)

    def cancel_async_create_ag_account_with_options(
        self,
        request: main_models.CancelAsyncCreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncCreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncCreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncCreateAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_async_create_ag_account_with_options_async(
        self,
        request: main_models.CancelAsyncCreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncCreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncCreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncCreateAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_async_create_ag_account(
        self,
        request: main_models.CancelAsyncCreateAgAccountRequest,
    ) -> main_models.CancelAsyncCreateAgAccountResponse:
        runtime = RuntimeOptions()
        return self.cancel_async_create_ag_account_with_options(request, runtime)

    async def cancel_async_create_ag_account_async(
        self,
        request: main_models.CancelAsyncCreateAgAccountRequest,
    ) -> main_models.CancelAsyncCreateAgAccountResponse:
        runtime = RuntimeOptions()
        return await self.cancel_async_create_ag_account_with_options_async(request, runtime)

    def cancel_async_modify_login_email_with_options(
        self,
        request: main_models.CancelAsyncModifyLoginEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncModifyLoginEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncModifyLoginEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncModifyLoginEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_async_modify_login_email_with_options_async(
        self,
        request: main_models.CancelAsyncModifyLoginEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncModifyLoginEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncModifyLoginEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncModifyLoginEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_async_modify_login_email(
        self,
        request: main_models.CancelAsyncModifyLoginEmailRequest,
    ) -> main_models.CancelAsyncModifyLoginEmailResponse:
        runtime = RuntimeOptions()
        return self.cancel_async_modify_login_email_with_options(request, runtime)

    async def cancel_async_modify_login_email_async(
        self,
        request: main_models.CancelAsyncModifyLoginEmailRequest,
    ) -> main_models.CancelAsyncModifyLoginEmailResponse:
        runtime = RuntimeOptions()
        return await self.cancel_async_modify_login_email_with_options_async(request, runtime)

    def change_ag_account_nationality_code_with_options(
        self,
        request: main_models.ChangeAgAccountNationalityCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAgAccountNationalityCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.nationality_code):
            query['NationalityCode'] = request.nationality_code
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAgAccountNationalityCode',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAgAccountNationalityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_ag_account_nationality_code_with_options_async(
        self,
        request: main_models.ChangeAgAccountNationalityCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAgAccountNationalityCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.nationality_code):
            query['NationalityCode'] = request.nationality_code
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAgAccountNationalityCode',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAgAccountNationalityCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_ag_account_nationality_code(
        self,
        request: main_models.ChangeAgAccountNationalityCodeRequest,
    ) -> main_models.ChangeAgAccountNationalityCodeResponse:
        runtime = RuntimeOptions()
        return self.change_ag_account_nationality_code_with_options(request, runtime)

    async def change_ag_account_nationality_code_async(
        self,
        request: main_models.ChangeAgAccountNationalityCodeRequest,
    ) -> main_models.ChangeAgAccountNationalityCodeResponse:
        runtime = RuntimeOptions()
        return await self.change_ag_account_nationality_code_with_options_async(request, runtime)

    def change_ag_security_email_with_options(
        self,
        request: main_models.ChangeAgSecurityEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAgSecurityEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.security_email):
            query['SecurityEmail'] = request.security_email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAgSecurityEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAgSecurityEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_ag_security_email_with_options_async(
        self,
        request: main_models.ChangeAgSecurityEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAgSecurityEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.security_email):
            query['SecurityEmail'] = request.security_email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAgSecurityEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAgSecurityEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_ag_security_email(
        self,
        request: main_models.ChangeAgSecurityEmailRequest,
    ) -> main_models.ChangeAgSecurityEmailResponse:
        runtime = RuntimeOptions()
        return self.change_ag_security_email_with_options(request, runtime)

    async def change_ag_security_email_async(
        self,
        request: main_models.ChangeAgSecurityEmailRequest,
    ) -> main_models.ChangeAgSecurityEmailResponse:
        runtime = RuntimeOptions()
        return await self.change_ag_security_email_with_options_async(request, runtime)

    def change_ag_security_mobile_with_options(
        self,
        request: main_models.ChangeAgSecurityMobileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAgSecurityMobileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.security_mobile):
            query['SecurityMobile'] = request.security_mobile
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAgSecurityMobile',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAgSecurityMobileResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_ag_security_mobile_with_options_async(
        self,
        request: main_models.ChangeAgSecurityMobileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAgSecurityMobileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.security_mobile):
            query['SecurityMobile'] = request.security_mobile
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAgSecurityMobile',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAgSecurityMobileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_ag_security_mobile(
        self,
        request: main_models.ChangeAgSecurityMobileRequest,
    ) -> main_models.ChangeAgSecurityMobileResponse:
        runtime = RuntimeOptions()
        return self.change_ag_security_mobile_with_options(request, runtime)

    async def change_ag_security_mobile_async(
        self,
        request: main_models.ChangeAgSecurityMobileRequest,
    ) -> main_models.ChangeAgSecurityMobileResponse:
        runtime = RuntimeOptions()
        return await self.change_ag_security_mobile_with_options_async(request, runtime)

    def create_account_profile_info_with_options(
        self,
        request: main_models.CreateAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountProfileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_json):
            query['AccountJson'] = request.account_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountProfileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_profile_info_with_options_async(
        self,
        request: main_models.CreateAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountProfileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_json):
            query['AccountJson'] = request.account_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountProfileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account_profile_info(
        self,
        request: main_models.CreateAccountProfileInfoRequest,
    ) -> main_models.CreateAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return self.create_account_profile_info_with_options(request, runtime)

    async def create_account_profile_info_async(
        self,
        request: main_models.CreateAccountProfileInfoRequest,
    ) -> main_models.CreateAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return await self.create_account_profile_info_with_options_async(request, runtime)

    def create_ag_account_with_options(
        self,
        request: main_models.CreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.nation_code):
            query['NationCode'] = request.nation_code
        if not DaraCore.is_null(request.own):
            query['Own'] = request.own
        if not DaraCore.is_null(request.real_parent_pk):
            query['RealParentPk'] = request.real_parent_pk
        if not DaraCore.is_null(request.security_mobile):
            query['SecurityMobile'] = request.security_mobile
        if not DaraCore.is_null(request.show_nick_name):
            query['ShowNickName'] = request.show_nick_name
        if not DaraCore.is_null(request.site_nick):
            query['SiteNick'] = request.site_nick
        if not DaraCore.is_null(request.src_account_info):
            query['srcAccountInfo'] = request.src_account_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ag_account_with_options_async(
        self,
        request: main_models.CreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.nation_code):
            query['NationCode'] = request.nation_code
        if not DaraCore.is_null(request.own):
            query['Own'] = request.own
        if not DaraCore.is_null(request.real_parent_pk):
            query['RealParentPk'] = request.real_parent_pk
        if not DaraCore.is_null(request.security_mobile):
            query['SecurityMobile'] = request.security_mobile
        if not DaraCore.is_null(request.show_nick_name):
            query['ShowNickName'] = request.show_nick_name
        if not DaraCore.is_null(request.site_nick):
            query['SiteNick'] = request.site_nick
        if not DaraCore.is_null(request.src_account_info):
            query['srcAccountInfo'] = request.src_account_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ag_account(
        self,
        request: main_models.CreateAgAccountRequest,
    ) -> main_models.CreateAgAccountResponse:
        runtime = RuntimeOptions()
        return self.create_ag_account_with_options(request, runtime)

    async def create_ag_account_async(
        self,
        request: main_models.CreateAgAccountRequest,
    ) -> main_models.CreateAgAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_ag_account_with_options_async(request, runtime)

    def create_contacter_with_options(
        self,
        request: main_models.CreateContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_address):
            query['ContacterAddress'] = request.contacter_address
        if not DaraCore.is_null(request.contacter_dingding):
            query['ContacterDingding'] = request.contacter_dingding
        if not DaraCore.is_null(request.contacter_email):
            query['ContacterEmail'] = request.contacter_email
        if not DaraCore.is_null(request.contacter_mobile):
            query['ContacterMobile'] = request.contacter_mobile
        if not DaraCore.is_null(request.contacter_name):
            query['ContacterName'] = request.contacter_name
        if not DaraCore.is_null(request.contacter_position):
            query['ContacterPosition'] = request.contacter_position
        if not DaraCore.is_null(request.contacter_staff_no):
            query['ContacterStaffNo'] = request.contacter_staff_no
        if not DaraCore.is_null(request.contacter_type):
            query['ContacterType'] = request.contacter_type
        if not DaraCore.is_null(request.contacter_wangwang):
            query['ContacterWangwang'] = request.contacter_wangwang
        if not DaraCore.is_null(request.email_confirmed):
            query['EmailConfirmed'] = request.email_confirmed
        if not DaraCore.is_null(request.mobile_confirmed):
            query['MobileConfirmed'] = request.mobile_confirmed
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContacterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_contacter_with_options_async(
        self,
        request: main_models.CreateContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_address):
            query['ContacterAddress'] = request.contacter_address
        if not DaraCore.is_null(request.contacter_dingding):
            query['ContacterDingding'] = request.contacter_dingding
        if not DaraCore.is_null(request.contacter_email):
            query['ContacterEmail'] = request.contacter_email
        if not DaraCore.is_null(request.contacter_mobile):
            query['ContacterMobile'] = request.contacter_mobile
        if not DaraCore.is_null(request.contacter_name):
            query['ContacterName'] = request.contacter_name
        if not DaraCore.is_null(request.contacter_position):
            query['ContacterPosition'] = request.contacter_position
        if not DaraCore.is_null(request.contacter_staff_no):
            query['ContacterStaffNo'] = request.contacter_staff_no
        if not DaraCore.is_null(request.contacter_type):
            query['ContacterType'] = request.contacter_type
        if not DaraCore.is_null(request.contacter_wangwang):
            query['ContacterWangwang'] = request.contacter_wangwang
        if not DaraCore.is_null(request.email_confirmed):
            query['EmailConfirmed'] = request.email_confirmed
        if not DaraCore.is_null(request.mobile_confirmed):
            query['MobileConfirmed'] = request.mobile_confirmed
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContacterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_contacter(
        self,
        request: main_models.CreateContacterRequest,
    ) -> main_models.CreateContacterResponse:
        runtime = RuntimeOptions()
        return self.create_contacter_with_options(request, runtime)

    async def create_contacter_async(
        self,
        request: main_models.CreateContacterRequest,
    ) -> main_models.CreateContacterResponse:
        runtime = RuntimeOptions()
        return await self.create_contacter_with_options_async(request, runtime)

    def create_real_name_certification_with_options(
        self,
        request: main_models.CreateRealNameCertificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRealNameCertificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_certify_type):
            query['AccountCertifyType'] = request.account_certify_type
        if not DaraCore.is_null(request.corporate_license_number):
            query['CorporateLicenseNumber'] = request.corporate_license_number
        if not DaraCore.is_null(request.corporate_name):
            query['CorporateName'] = request.corporate_name
        if not DaraCore.is_null(request.license_number):
            query['LicenseNumber'] = request.license_number
        if not DaraCore.is_null(request.license_type):
            query['LicenseType'] = request.license_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRealNameCertification',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRealNameCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_real_name_certification_with_options_async(
        self,
        request: main_models.CreateRealNameCertificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRealNameCertificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_certify_type):
            query['AccountCertifyType'] = request.account_certify_type
        if not DaraCore.is_null(request.corporate_license_number):
            query['CorporateLicenseNumber'] = request.corporate_license_number
        if not DaraCore.is_null(request.corporate_name):
            query['CorporateName'] = request.corporate_name
        if not DaraCore.is_null(request.license_number):
            query['LicenseNumber'] = request.license_number
        if not DaraCore.is_null(request.license_type):
            query['LicenseType'] = request.license_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRealNameCertification',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRealNameCertificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_real_name_certification(
        self,
        request: main_models.CreateRealNameCertificationRequest,
    ) -> main_models.CreateRealNameCertificationResponse:
        runtime = RuntimeOptions()
        return self.create_real_name_certification_with_options(request, runtime)

    async def create_real_name_certification_async(
        self,
        request: main_models.CreateRealNameCertificationRequest,
    ) -> main_models.CreateRealNameCertificationResponse:
        runtime = RuntimeOptions()
        return await self.create_real_name_certification_with_options_async(request, runtime)

    def customer_sensitive_info_logical_delete_with_options(
        self,
        request: main_models.CustomerSensitiveInfoLogicalDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CustomerSensitiveInfoLogicalDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CustomerSensitiveInfoLogicalDelete',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CustomerSensitiveInfoLogicalDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def customer_sensitive_info_logical_delete_with_options_async(
        self,
        request: main_models.CustomerSensitiveInfoLogicalDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CustomerSensitiveInfoLogicalDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CustomerSensitiveInfoLogicalDelete',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CustomerSensitiveInfoLogicalDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def customer_sensitive_info_logical_delete(
        self,
        request: main_models.CustomerSensitiveInfoLogicalDeleteRequest,
    ) -> main_models.CustomerSensitiveInfoLogicalDeleteResponse:
        runtime = RuntimeOptions()
        return self.customer_sensitive_info_logical_delete_with_options(request, runtime)

    async def customer_sensitive_info_logical_delete_async(
        self,
        request: main_models.CustomerSensitiveInfoLogicalDeleteRequest,
    ) -> main_models.CustomerSensitiveInfoLogicalDeleteResponse:
        runtime = RuntimeOptions()
        return await self.customer_sensitive_info_logical_delete_with_options_async(request, runtime)

    def customer_sensitive_info_physical_delete_with_options(
        self,
        request: main_models.CustomerSensitiveInfoPhysicalDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CustomerSensitiveInfoPhysicalDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CustomerSensitiveInfoPhysicalDelete',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CustomerSensitiveInfoPhysicalDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def customer_sensitive_info_physical_delete_with_options_async(
        self,
        request: main_models.CustomerSensitiveInfoPhysicalDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CustomerSensitiveInfoPhysicalDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CustomerSensitiveInfoPhysicalDelete',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CustomerSensitiveInfoPhysicalDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def customer_sensitive_info_physical_delete(
        self,
        request: main_models.CustomerSensitiveInfoPhysicalDeleteRequest,
    ) -> main_models.CustomerSensitiveInfoPhysicalDeleteResponse:
        runtime = RuntimeOptions()
        return self.customer_sensitive_info_physical_delete_with_options(request, runtime)

    async def customer_sensitive_info_physical_delete_async(
        self,
        request: main_models.CustomerSensitiveInfoPhysicalDeleteRequest,
    ) -> main_models.CustomerSensitiveInfoPhysicalDeleteResponse:
        runtime = RuntimeOptions()
        return await self.customer_sensitive_info_physical_delete_with_options_async(request, runtime)

    def del_cache_operate_sync_with_options(
        self,
        request: main_models.DelCacheOperateSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelCacheOperateSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelCacheOperateSync',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelCacheOperateSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_cache_operate_sync_with_options_async(
        self,
        request: main_models.DelCacheOperateSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelCacheOperateSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelCacheOperateSync',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelCacheOperateSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_cache_operate_sync(
        self,
        request: main_models.DelCacheOperateSyncRequest,
    ) -> main_models.DelCacheOperateSyncResponse:
        runtime = RuntimeOptions()
        return self.del_cache_operate_sync_with_options(request, runtime)

    async def del_cache_operate_sync_async(
        self,
        request: main_models.DelCacheOperateSyncRequest,
    ) -> main_models.DelCacheOperateSyncResponse:
        runtime = RuntimeOptions()
        return await self.del_cache_operate_sync_with_options_async(request, runtime)

    def delete_contacter_with_options(
        self,
        request: main_models.DeleteContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_id):
            query['ContacterId'] = request.contacter_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContacterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contacter_with_options_async(
        self,
        request: main_models.DeleteContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_id):
            query['ContacterId'] = request.contacter_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContacterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contacter(
        self,
        request: main_models.DeleteContacterRequest,
    ) -> main_models.DeleteContacterResponse:
        runtime = RuntimeOptions()
        return self.delete_contacter_with_options(request, runtime)

    async def delete_contacter_async(
        self,
        request: main_models.DeleteContacterRequest,
    ) -> main_models.DeleteContacterResponse:
        runtime = RuntimeOptions()
        return await self.delete_contacter_with_options_async(request, runtime)

    def delete_customer_label_with_options(
        self,
        request: main_models.DeleteCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomerLabel',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomerLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_customer_label_with_options_async(
        self,
        request: main_models.DeleteCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomerLabel',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomerLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_customer_label(
        self,
        request: main_models.DeleteCustomerLabelRequest,
    ) -> main_models.DeleteCustomerLabelResponse:
        runtime = RuntimeOptions()
        return self.delete_customer_label_with_options(request, runtime)

    async def delete_customer_label_async(
        self,
        request: main_models.DeleteCustomerLabelRequest,
    ) -> main_models.DeleteCustomerLabelResponse:
        runtime = RuntimeOptions()
        return await self.delete_customer_label_with_options_async(request, runtime)

    def exist_binds_by_outer_id_with_options(
        self,
        request: main_models.ExistBindsByOuterIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExistBindsByOuterIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExistBindsByOuterId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExistBindsByOuterIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def exist_binds_by_outer_id_with_options_async(
        self,
        request: main_models.ExistBindsByOuterIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExistBindsByOuterIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExistBindsByOuterId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExistBindsByOuterIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exist_binds_by_outer_id(
        self,
        request: main_models.ExistBindsByOuterIdRequest,
    ) -> main_models.ExistBindsByOuterIdResponse:
        runtime = RuntimeOptions()
        return self.exist_binds_by_outer_id_with_options(request, runtime)

    async def exist_binds_by_outer_id_async(
        self,
        request: main_models.ExistBindsByOuterIdRequest,
    ) -> main_models.ExistBindsByOuterIdResponse:
        runtime = RuntimeOptions()
        return await self.exist_binds_by_outer_id_with_options_async(request, runtime)

    def find_all_contacter_with_options(
        self,
        request: main_models.FindAllContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindAllContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindAllContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindAllContacterResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_all_contacter_with_options_async(
        self,
        request: main_models.FindAllContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindAllContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindAllContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindAllContacterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_all_contacter(
        self,
        request: main_models.FindAllContacterRequest,
    ) -> main_models.FindAllContacterResponse:
        runtime = RuntimeOptions()
        return self.find_all_contacter_with_options(request, runtime)

    async def find_all_contacter_async(
        self,
        request: main_models.FindAllContacterRequest,
    ) -> main_models.FindAllContacterResponse:
        runtime = RuntimeOptions()
        return await self.find_all_contacter_with_options_async(request, runtime)

    def find_biz_category_config_with_options(
        self,
        request: main_models.FindBizCategoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindBizCategoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindBizCategoryConfig',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindBizCategoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_biz_category_config_with_options_async(
        self,
        request: main_models.FindBizCategoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindBizCategoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindBizCategoryConfig',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindBizCategoryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_biz_category_config(
        self,
        request: main_models.FindBizCategoryConfigRequest,
    ) -> main_models.FindBizCategoryConfigResponse:
        runtime = RuntimeOptions()
        return self.find_biz_category_config_with_options(request, runtime)

    async def find_biz_category_config_async(
        self,
        request: main_models.FindBizCategoryConfigRequest,
    ) -> main_models.FindBizCategoryConfigResponse:
        runtime = RuntimeOptions()
        return await self.find_biz_category_config_with_options_async(request, runtime)

    def find_contacter_with_options(
        self,
        request: main_models.FindContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_id):
            query['ContacterId'] = request.contacter_id
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindContacterResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_contacter_with_options_async(
        self,
        request: main_models.FindContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_id):
            query['ContacterId'] = request.contacter_id
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindContacterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_contacter(
        self,
        request: main_models.FindContacterRequest,
    ) -> main_models.FindContacterResponse:
        runtime = RuntimeOptions()
        return self.find_contacter_with_options(request, runtime)

    async def find_contacter_async(
        self,
        request: main_models.FindContacterRequest,
    ) -> main_models.FindContacterResponse:
        runtime = RuntimeOptions()
        return await self.find_contacter_with_options_async(request, runtime)

    def find_customer_info_with_options(
        self,
        request: main_models.FindCustomerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindCustomerInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindCustomerInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindCustomerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_customer_info_with_options_async(
        self,
        request: main_models.FindCustomerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindCustomerInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindCustomerInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindCustomerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_customer_info(
        self,
        request: main_models.FindCustomerInfoRequest,
    ) -> main_models.FindCustomerInfoResponse:
        runtime = RuntimeOptions()
        return self.find_customer_info_with_options(request, runtime)

    async def find_customer_info_async(
        self,
        request: main_models.FindCustomerInfoRequest,
    ) -> main_models.FindCustomerInfoResponse:
        runtime = RuntimeOptions()
        return await self.find_customer_info_with_options_async(request, runtime)

    def find_customer_snapshot_with_options(
        self,
        request: main_models.FindCustomerSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindCustomerSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.info_type):
            query['InfoType'] = request.info_type
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindCustomerSnapshot',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindCustomerSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_customer_snapshot_with_options_async(
        self,
        request: main_models.FindCustomerSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindCustomerSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.info_type):
            query['InfoType'] = request.info_type
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindCustomerSnapshot',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindCustomerSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_customer_snapshot(
        self,
        request: main_models.FindCustomerSnapshotRequest,
    ) -> main_models.FindCustomerSnapshotResponse:
        runtime = RuntimeOptions()
        return self.find_customer_snapshot_with_options(request, runtime)

    async def find_customer_snapshot_async(
        self,
        request: main_models.FindCustomerSnapshotRequest,
    ) -> main_models.FindCustomerSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.find_customer_snapshot_with_options_async(request, runtime)

    def find_finance_tax_with_options(
        self,
        request: main_models.FindFinanceTaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindFinanceTaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hid):
            query['HId'] = request.hid
        if not DaraCore.is_null(request.tax_version):
            query['TaxVersion'] = request.tax_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindFinanceTax',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindFinanceTaxResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_finance_tax_with_options_async(
        self,
        request: main_models.FindFinanceTaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindFinanceTaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hid):
            query['HId'] = request.hid
        if not DaraCore.is_null(request.tax_version):
            query['TaxVersion'] = request.tax_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindFinanceTax',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindFinanceTaxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_finance_tax(
        self,
        request: main_models.FindFinanceTaxRequest,
    ) -> main_models.FindFinanceTaxResponse:
        runtime = RuntimeOptions()
        return self.find_finance_tax_with_options(request, runtime)

    async def find_finance_tax_async(
        self,
        request: main_models.FindFinanceTaxRequest,
    ) -> main_models.FindFinanceTaxResponse:
        runtime = RuntimeOptions()
        return await self.find_finance_tax_with_options_async(request, runtime)

    def find_finance_tax_detail_with_options(
        self,
        request: main_models.FindFinanceTaxDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindFinanceTaxDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kp_id):
            query['KpId'] = request.kp_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindFinanceTaxDetail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindFinanceTaxDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_finance_tax_detail_with_options_async(
        self,
        request: main_models.FindFinanceTaxDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindFinanceTaxDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kp_id):
            query['KpId'] = request.kp_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindFinanceTaxDetail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindFinanceTaxDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_finance_tax_detail(
        self,
        request: main_models.FindFinanceTaxDetailRequest,
    ) -> main_models.FindFinanceTaxDetailResponse:
        runtime = RuntimeOptions()
        return self.find_finance_tax_detail_with_options(request, runtime)

    async def find_finance_tax_detail_async(
        self,
        request: main_models.FindFinanceTaxDetailRequest,
    ) -> main_models.FindFinanceTaxDetailResponse:
        runtime = RuntimeOptions()
        return await self.find_finance_tax_detail_with_options_async(request, runtime)

    def find_pk_by_hid_for_login_with_legacy_with_options(
        self,
        request: main_models.FindPkByHidForLoginWithLegacyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindPkByHidForLoginWithLegacyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindPkByHidForLoginWithLegacy',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindPkByHidForLoginWithLegacyResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_pk_by_hid_for_login_with_legacy_with_options_async(
        self,
        request: main_models.FindPkByHidForLoginWithLegacyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FindPkByHidForLoginWithLegacyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FindPkByHidForLoginWithLegacy',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FindPkByHidForLoginWithLegacyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_pk_by_hid_for_login_with_legacy(
        self,
        request: main_models.FindPkByHidForLoginWithLegacyRequest,
    ) -> main_models.FindPkByHidForLoginWithLegacyResponse:
        runtime = RuntimeOptions()
        return self.find_pk_by_hid_for_login_with_legacy_with_options(request, runtime)

    async def find_pk_by_hid_for_login_with_legacy_async(
        self,
        request: main_models.FindPkByHidForLoginWithLegacyRequest,
    ) -> main_models.FindPkByHidForLoginWithLegacyResponse:
        runtime = RuntimeOptions()
        return await self.find_pk_by_hid_for_login_with_legacy_with_options_async(request, runtime)

    def forbidden_ag_account_login_with_options(
        self,
        request: main_models.ForbiddenAgAccountLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForbiddenAgAccountLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ForbiddenAgAccountLogin',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForbiddenAgAccountLoginResponse(),
            self.call_api(params, req, runtime)
        )

    async def forbidden_ag_account_login_with_options_async(
        self,
        request: main_models.ForbiddenAgAccountLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForbiddenAgAccountLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ForbiddenAgAccountLogin',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForbiddenAgAccountLoginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def forbidden_ag_account_login(
        self,
        request: main_models.ForbiddenAgAccountLoginRequest,
    ) -> main_models.ForbiddenAgAccountLoginResponse:
        runtime = RuntimeOptions()
        return self.forbidden_ag_account_login_with_options(request, runtime)

    async def forbidden_ag_account_login_async(
        self,
        request: main_models.ForbiddenAgAccountLoginRequest,
    ) -> main_models.ForbiddenAgAccountLoginResponse:
        runtime = RuntimeOptions()
        return await self.forbidden_ag_account_login_with_options_async(request, runtime)

    def generate_aliyun_cert_url_with_options(
        self,
        request: main_models.GenerateAliyunCertUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAliyunCertUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_pk):
            query['AliyunPk'] = request.aliyun_pk
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.apply_channel):
            query['ApplyChannel'] = request.apply_channel
        if not DaraCore.is_null(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.cert_way):
            query['CertWay'] = request.cert_way
        if not DaraCore.is_null(request.ignore_already_cert):
            query['IgnoreAlreadyCert'] = request.ignore_already_cert
        if not DaraCore.is_null(request.is_mobile):
            query['IsMobile'] = request.is_mobile
        if not DaraCore.is_null(request.is_open_app):
            query['IsOpenApp'] = request.is_open_app
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.subject_type):
            query['SubjectType'] = request.subject_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAliyunCertUrl',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAliyunCertUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aliyun_cert_url_with_options_async(
        self,
        request: main_models.GenerateAliyunCertUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAliyunCertUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_pk):
            query['AliyunPk'] = request.aliyun_pk
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.apply_channel):
            query['ApplyChannel'] = request.apply_channel
        if not DaraCore.is_null(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.cert_way):
            query['CertWay'] = request.cert_way
        if not DaraCore.is_null(request.ignore_already_cert):
            query['IgnoreAlreadyCert'] = request.ignore_already_cert
        if not DaraCore.is_null(request.is_mobile):
            query['IsMobile'] = request.is_mobile
        if not DaraCore.is_null(request.is_open_app):
            query['IsOpenApp'] = request.is_open_app
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.subject_type):
            query['SubjectType'] = request.subject_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAliyunCertUrl',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAliyunCertUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aliyun_cert_url(
        self,
        request: main_models.GenerateAliyunCertUrlRequest,
    ) -> main_models.GenerateAliyunCertUrlResponse:
        runtime = RuntimeOptions()
        return self.generate_aliyun_cert_url_with_options(request, runtime)

    async def generate_aliyun_cert_url_async(
        self,
        request: main_models.GenerateAliyunCertUrlRequest,
    ) -> main_models.GenerateAliyunCertUrlResponse:
        runtime = RuntimeOptions()
        return await self.generate_aliyun_cert_url_with_options_async(request, runtime)

    def get_ag_account_ak_with_options(
        self,
        request: main_models.GetAgAccountAkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgAccountAkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgAccountAk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgAccountAkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ag_account_ak_with_options_async(
        self,
        request: main_models.GetAgAccountAkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgAccountAkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgAccountAk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgAccountAkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ag_account_ak(
        self,
        request: main_models.GetAgAccountAkRequest,
    ) -> main_models.GetAgAccountAkResponse:
        runtime = RuntimeOptions()
        return self.get_ag_account_ak_with_options(request, runtime)

    async def get_ag_account_ak_async(
        self,
        request: main_models.GetAgAccountAkRequest,
    ) -> main_models.GetAgAccountAkResponse:
        runtime = RuntimeOptions()
        return await self.get_ag_account_ak_with_options_async(request, runtime)

    def get_ag_one_key_delete_task_with_options(
        self,
        request: main_models.GetAgOneKeyDeleteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgOneKeyDeleteTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgOneKeyDeleteTask',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgOneKeyDeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ag_one_key_delete_task_with_options_async(
        self,
        request: main_models.GetAgOneKeyDeleteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgOneKeyDeleteTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgOneKeyDeleteTask',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgOneKeyDeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ag_one_key_delete_task(
        self,
        request: main_models.GetAgOneKeyDeleteTaskRequest,
    ) -> main_models.GetAgOneKeyDeleteTaskResponse:
        runtime = RuntimeOptions()
        return self.get_ag_one_key_delete_task_with_options(request, runtime)

    async def get_ag_one_key_delete_task_async(
        self,
        request: main_models.GetAgOneKeyDeleteTaskRequest,
    ) -> main_models.GetAgOneKeyDeleteTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_ag_one_key_delete_task_with_options_async(request, runtime)

    def get_ag_relation_with_options(
        self,
        request: main_models.GetAgRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgRelation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ag_relation_with_options_async(
        self,
        request: main_models.GetAgRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgRelation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ag_relation(
        self,
        request: main_models.GetAgRelationRequest,
    ) -> main_models.GetAgRelationResponse:
        runtime = RuntimeOptions()
        return self.get_ag_relation_with_options(request, runtime)

    async def get_ag_relation_async(
        self,
        request: main_models.GetAgRelationRequest,
    ) -> main_models.GetAgRelationResponse:
        runtime = RuntimeOptions()
        return await self.get_ag_relation_with_options_async(request, runtime)

    def get_aliyun_id_by_pk_with_options(
        self,
        request: main_models.GetAliyunIdByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAliyunIdByPkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAliyunIdByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliyunIdByPkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aliyun_id_by_pk_with_options_async(
        self,
        request: main_models.GetAliyunIdByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAliyunIdByPkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAliyunIdByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliyunIdByPkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aliyun_id_by_pk(
        self,
        request: main_models.GetAliyunIdByPkRequest,
    ) -> main_models.GetAliyunIdByPkResponse:
        runtime = RuntimeOptions()
        return self.get_aliyun_id_by_pk_with_options(request, runtime)

    async def get_aliyun_id_by_pk_async(
        self,
        request: main_models.GetAliyunIdByPkRequest,
    ) -> main_models.GetAliyunIdByPkResponse:
        runtime = RuntimeOptions()
        return await self.get_aliyun_id_by_pk_with_options_async(request, runtime)

    def get_aliyun_pkby_aliyun_idwith_options(
        self,
        request: main_models.GetAliyunPKByAliyunIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAliyunPKByAliyunIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_id):
            query['AliyunId'] = request.aliyun_id
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAliyunPKByAliyunID',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliyunPKByAliyunIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aliyun_pkby_aliyun_idwith_options_async(
        self,
        request: main_models.GetAliyunPKByAliyunIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAliyunPKByAliyunIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_id):
            query['AliyunId'] = request.aliyun_id
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAliyunPKByAliyunID',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliyunPKByAliyunIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aliyun_pkby_aliyun_id(
        self,
        request: main_models.GetAliyunPKByAliyunIDRequest,
    ) -> main_models.GetAliyunPKByAliyunIDResponse:
        runtime = RuntimeOptions()
        return self.get_aliyun_pkby_aliyun_idwith_options(request, runtime)

    async def get_aliyun_pkby_aliyun_id_async(
        self,
        request: main_models.GetAliyunPKByAliyunIDRequest,
    ) -> main_models.GetAliyunPKByAliyunIDResponse:
        runtime = RuntimeOptions()
        return await self.get_aliyun_pkby_aliyun_idwith_options_async(request, runtime)

    def get_customer_category_with_options(
        self,
        request: main_models.GetCustomerCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerCategory',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_category_with_options_async(
        self,
        request: main_models.GetCustomerCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locale_string):
            query['LocaleString'] = request.locale_string
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerCategory',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_category(
        self,
        request: main_models.GetCustomerCategoryRequest,
    ) -> main_models.GetCustomerCategoryResponse:
        runtime = RuntimeOptions()
        return self.get_customer_category_with_options(request, runtime)

    async def get_customer_category_async(
        self,
        request: main_models.GetCustomerCategoryRequest,
    ) -> main_models.GetCustomerCategoryResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_category_with_options_async(request, runtime)

    def get_customer_category_dictionary_with_options(
        self,
        request: main_models.GetCustomerCategoryDictionaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerCategoryDictionaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerCategoryDictionary',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerCategoryDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_category_dictionary_with_options_async(
        self,
        request: main_models.GetCustomerCategoryDictionaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerCategoryDictionaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerCategoryDictionary',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerCategoryDictionaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_category_dictionary(
        self,
        request: main_models.GetCustomerCategoryDictionaryRequest,
    ) -> main_models.GetCustomerCategoryDictionaryResponse:
        runtime = RuntimeOptions()
        return self.get_customer_category_dictionary_with_options(request, runtime)

    async def get_customer_category_dictionary_async(
        self,
        request: main_models.GetCustomerCategoryDictionaryRequest,
    ) -> main_models.GetCustomerCategoryDictionaryResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_category_dictionary_with_options_async(request, runtime)

    def get_customer_information_with_options(
        self,
        request: main_models.GetCustomerInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerInformation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_information_with_options_async(
        self,
        request: main_models.GetCustomerInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerInformation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_information(
        self,
        request: main_models.GetCustomerInformationRequest,
    ) -> main_models.GetCustomerInformationResponse:
        runtime = RuntimeOptions()
        return self.get_customer_information_with_options(request, runtime)

    async def get_customer_information_async(
        self,
        request: main_models.GetCustomerInformationRequest,
    ) -> main_models.GetCustomerInformationResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_information_with_options_async(request, runtime)

    def get_ding_talk_user_org_by_aliyun_tmp_code_with_options(
        self,
        request: main_models.GetDingTalkUserOrgByAliyunTmpCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDingTalkUserOrgByAliyunTmpCodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDingTalkUserOrgByAliyunTmpCode',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDingTalkUserOrgByAliyunTmpCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ding_talk_user_org_by_aliyun_tmp_code_with_options_async(
        self,
        request: main_models.GetDingTalkUserOrgByAliyunTmpCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDingTalkUserOrgByAliyunTmpCodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDingTalkUserOrgByAliyunTmpCode',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDingTalkUserOrgByAliyunTmpCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ding_talk_user_org_by_aliyun_tmp_code(
        self,
        request: main_models.GetDingTalkUserOrgByAliyunTmpCodeRequest,
    ) -> main_models.GetDingTalkUserOrgByAliyunTmpCodeResponse:
        runtime = RuntimeOptions()
        return self.get_ding_talk_user_org_by_aliyun_tmp_code_with_options(request, runtime)

    async def get_ding_talk_user_org_by_aliyun_tmp_code_async(
        self,
        request: main_models.GetDingTalkUserOrgByAliyunTmpCodeRequest,
    ) -> main_models.GetDingTalkUserOrgByAliyunTmpCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_ding_talk_user_org_by_aliyun_tmp_code_with_options_async(request, runtime)

    def get_identity_registration_by_customer_with_options(
        self,
        request: main_models.GetIdentityRegistrationByCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityRegistrationByCustomerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityRegistrationByCustomer',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityRegistrationByCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_registration_by_customer_with_options_async(
        self,
        request: main_models.GetIdentityRegistrationByCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityRegistrationByCustomerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityRegistrationByCustomer',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityRegistrationByCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_registration_by_customer(
        self,
        request: main_models.GetIdentityRegistrationByCustomerRequest,
    ) -> main_models.GetIdentityRegistrationByCustomerResponse:
        runtime = RuntimeOptions()
        return self.get_identity_registration_by_customer_with_options(request, runtime)

    async def get_identity_registration_by_customer_async(
        self,
        request: main_models.GetIdentityRegistrationByCustomerRequest,
    ) -> main_models.GetIdentityRegistrationByCustomerResponse:
        runtime = RuntimeOptions()
        return await self.get_identity_registration_by_customer_with_options_async(request, runtime)

    def get_profile_type_by_pk_with_options(
        self,
        request: main_models.GetProfileTypeByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProfileTypeByPkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProfileTypeByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProfileTypeByPkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_profile_type_by_pk_with_options_async(
        self,
        request: main_models.GetProfileTypeByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProfileTypeByPkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProfileTypeByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProfileTypeByPkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_profile_type_by_pk(
        self,
        request: main_models.GetProfileTypeByPkRequest,
    ) -> main_models.GetProfileTypeByPkResponse:
        runtime = RuntimeOptions()
        return self.get_profile_type_by_pk_with_options(request, runtime)

    async def get_profile_type_by_pk_async(
        self,
        request: main_models.GetProfileTypeByPkRequest,
    ) -> main_models.GetProfileTypeByPkResponse:
        runtime = RuntimeOptions()
        return await self.get_profile_type_by_pk_with_options_async(request, runtime)

    def get_upload_identity_registration_doc_config_with_options(
        self,
        request: main_models.GetUploadIdentityRegistrationDocConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadIdentityRegistrationDocConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadIdentityRegistrationDocConfig',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadIdentityRegistrationDocConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_identity_registration_doc_config_with_options_async(
        self,
        request: main_models.GetUploadIdentityRegistrationDocConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadIdentityRegistrationDocConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadIdentityRegistrationDocConfig',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadIdentityRegistrationDocConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_identity_registration_doc_config(
        self,
        request: main_models.GetUploadIdentityRegistrationDocConfigRequest,
    ) -> main_models.GetUploadIdentityRegistrationDocConfigResponse:
        runtime = RuntimeOptions()
        return self.get_upload_identity_registration_doc_config_with_options(request, runtime)

    async def get_upload_identity_registration_doc_config_async(
        self,
        request: main_models.GetUploadIdentityRegistrationDocConfigRequest,
    ) -> main_models.GetUploadIdentityRegistrationDocConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_upload_identity_registration_doc_config_with_options_async(request, runtime)

    def incr_by_cache_operate_sync_with_options(
        self,
        request: main_models.IncrByCacheOperateSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncrByCacheOperateSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_value):
            query['DefaultValue'] = request.default_value
        if not DaraCore.is_null(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.step):
            query['Step'] = request.step
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncrByCacheOperateSync',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncrByCacheOperateSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def incr_by_cache_operate_sync_with_options_async(
        self,
        request: main_models.IncrByCacheOperateSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncrByCacheOperateSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_value):
            query['DefaultValue'] = request.default_value
        if not DaraCore.is_null(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.step):
            query['Step'] = request.step
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncrByCacheOperateSync',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncrByCacheOperateSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def incr_by_cache_operate_sync(
        self,
        request: main_models.IncrByCacheOperateSyncRequest,
    ) -> main_models.IncrByCacheOperateSyncResponse:
        runtime = RuntimeOptions()
        return self.incr_by_cache_operate_sync_with_options(request, runtime)

    async def incr_by_cache_operate_sync_async(
        self,
        request: main_models.IncrByCacheOperateSyncRequest,
    ) -> main_models.IncrByCacheOperateSyncResponse:
        runtime = RuntimeOptions()
        return await self.incr_by_cache_operate_sync_with_options_async(request, runtime)

    def judge_ag_exist_quiet_period_with_options(
        self,
        request: main_models.JudgeAgExistQuietPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JudgeAgExistQuietPeriodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JudgeAgExistQuietPeriod',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JudgeAgExistQuietPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def judge_ag_exist_quiet_period_with_options_async(
        self,
        request: main_models.JudgeAgExistQuietPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JudgeAgExistQuietPeriodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JudgeAgExistQuietPeriod',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JudgeAgExistQuietPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def judge_ag_exist_quiet_period(
        self,
        request: main_models.JudgeAgExistQuietPeriodRequest,
    ) -> main_models.JudgeAgExistQuietPeriodResponse:
        runtime = RuntimeOptions()
        return self.judge_ag_exist_quiet_period_with_options(request, runtime)

    async def judge_ag_exist_quiet_period_async(
        self,
        request: main_models.JudgeAgExistQuietPeriodRequest,
    ) -> main_models.JudgeAgExistQuietPeriodResponse:
        runtime = RuntimeOptions()
        return await self.judge_ag_exist_quiet_period_with_options_async(request, runtime)

    def load_real_name_info_by_pk_with_options(
        self,
        request: main_models.LoadRealNameInfoByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadRealNameInfoByPkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadRealNameInfoByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadRealNameInfoByPkResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_real_name_info_by_pk_with_options_async(
        self,
        request: main_models.LoadRealNameInfoByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadRealNameInfoByPkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadRealNameInfoByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadRealNameInfoByPkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_real_name_info_by_pk(
        self,
        request: main_models.LoadRealNameInfoByPkRequest,
    ) -> main_models.LoadRealNameInfoByPkResponse:
        runtime = RuntimeOptions()
        return self.load_real_name_info_by_pk_with_options(request, runtime)

    async def load_real_name_info_by_pk_async(
        self,
        request: main_models.LoadRealNameInfoByPkRequest,
    ) -> main_models.LoadRealNameInfoByPkResponse:
        runtime = RuntimeOptions()
        return await self.load_real_name_info_by_pk_with_options_async(request, runtime)

    def map_from_havana_bind_id_with_options(
        self,
        tmp_req: main_models.MapFromHavanaBindIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapFromHavanaBindIdResponse:
        tmp_req.validate()
        request = main_models.MapFromHavanaBindIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.havana_bind_stations):
            request.havana_bind_stations_shrink = Utils.array_to_string_with_specified_style(tmp_req.havana_bind_stations, 'HavanaBindStations', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_bind_id):
            query['HavanaBindId'] = request.havana_bind_id
        if not DaraCore.is_null(request.havana_bind_stations_shrink):
            query['HavanaBindStations'] = request.havana_bind_stations_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapFromHavanaBindId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapFromHavanaBindIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def map_from_havana_bind_id_with_options_async(
        self,
        tmp_req: main_models.MapFromHavanaBindIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapFromHavanaBindIdResponse:
        tmp_req.validate()
        request = main_models.MapFromHavanaBindIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.havana_bind_stations):
            request.havana_bind_stations_shrink = Utils.array_to_string_with_specified_style(tmp_req.havana_bind_stations, 'HavanaBindStations', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_bind_id):
            query['HavanaBindId'] = request.havana_bind_id
        if not DaraCore.is_null(request.havana_bind_stations_shrink):
            query['HavanaBindStations'] = request.havana_bind_stations_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapFromHavanaBindId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapFromHavanaBindIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def map_from_havana_bind_id(
        self,
        request: main_models.MapFromHavanaBindIdRequest,
    ) -> main_models.MapFromHavanaBindIdResponse:
        runtime = RuntimeOptions()
        return self.map_from_havana_bind_id_with_options(request, runtime)

    async def map_from_havana_bind_id_async(
        self,
        request: main_models.MapFromHavanaBindIdRequest,
    ) -> main_models.MapFromHavanaBindIdResponse:
        runtime = RuntimeOptions()
        return await self.map_from_havana_bind_id_with_options_async(request, runtime)

    def map_pk_from_hid_with_options(
        self,
        request: main_models.MapPkFromHidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapPkFromHidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.bid):
            query['Bid'] = request.bid
        if not DaraCore.is_null(request.hid):
            query['Hid'] = request.hid
        if not DaraCore.is_null(request.mapping_scenes):
            query['MappingScenes'] = request.mapping_scenes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapPkFromHid',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapPkFromHidResponse(),
            self.call_api(params, req, runtime)
        )

    async def map_pk_from_hid_with_options_async(
        self,
        request: main_models.MapPkFromHidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapPkFromHidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.bid):
            query['Bid'] = request.bid
        if not DaraCore.is_null(request.hid):
            query['Hid'] = request.hid
        if not DaraCore.is_null(request.mapping_scenes):
            query['MappingScenes'] = request.mapping_scenes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapPkFromHid',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapPkFromHidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def map_pk_from_hid(
        self,
        request: main_models.MapPkFromHidRequest,
    ) -> main_models.MapPkFromHidResponse:
        runtime = RuntimeOptions()
        return self.map_pk_from_hid_with_options(request, runtime)

    async def map_pk_from_hid_async(
        self,
        request: main_models.MapPkFromHidRequest,
    ) -> main_models.MapPkFromHidResponse:
        runtime = RuntimeOptions()
        return await self.map_pk_from_hid_with_options_async(request, runtime)

    def map_pk_to_hid_with_options(
        self,
        request: main_models.MapPkToHidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapPkToHidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mapping_scenes):
            query['MappingScenes'] = request.mapping_scenes
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapPkToHid',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapPkToHidResponse(),
            self.call_api(params, req, runtime)
        )

    async def map_pk_to_hid_with_options_async(
        self,
        request: main_models.MapPkToHidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapPkToHidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mapping_scenes):
            query['MappingScenes'] = request.mapping_scenes
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapPkToHid',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapPkToHidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def map_pk_to_hid(
        self,
        request: main_models.MapPkToHidRequest,
    ) -> main_models.MapPkToHidResponse:
        runtime = RuntimeOptions()
        return self.map_pk_to_hid_with_options(request, runtime)

    async def map_pk_to_hid_async(
        self,
        request: main_models.MapPkToHidRequest,
    ) -> main_models.MapPkToHidResponse:
        runtime = RuntimeOptions()
        return await self.map_pk_to_hid_with_options_async(request, runtime)

    def map_to_havana_bind_id_with_options(
        self,
        tmp_req: main_models.MapToHavanaBindIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapToHavanaBindIdResponse:
        tmp_req.validate()
        request = main_models.MapToHavanaBindIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.havana_bind_stations):
            request.havana_bind_stations_shrink = Utils.array_to_string_with_specified_style(tmp_req.havana_bind_stations, 'HavanaBindStations', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_bind_stations_shrink):
            query['HavanaBindStations'] = request.havana_bind_stations_shrink
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapToHavanaBindId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapToHavanaBindIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def map_to_havana_bind_id_with_options_async(
        self,
        tmp_req: main_models.MapToHavanaBindIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MapToHavanaBindIdResponse:
        tmp_req.validate()
        request = main_models.MapToHavanaBindIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.havana_bind_stations):
            request.havana_bind_stations_shrink = Utils.array_to_string_with_specified_style(tmp_req.havana_bind_stations, 'HavanaBindStations', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.havana_bind_stations_shrink):
            query['HavanaBindStations'] = request.havana_bind_stations_shrink
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MapToHavanaBindId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MapToHavanaBindIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def map_to_havana_bind_id(
        self,
        request: main_models.MapToHavanaBindIdRequest,
    ) -> main_models.MapToHavanaBindIdResponse:
        runtime = RuntimeOptions()
        return self.map_to_havana_bind_id_with_options(request, runtime)

    async def map_to_havana_bind_id_async(
        self,
        request: main_models.MapToHavanaBindIdRequest,
    ) -> main_models.MapToHavanaBindIdResponse:
        runtime = RuntimeOptions()
        return await self.map_to_havana_bind_id_with_options_async(request, runtime)

    def modify_biz_category_with_options(
        self,
        request: main_models.ModifyBizCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBizCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_list):
            query['ParamList'] = request.param_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBizCategory',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBizCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_biz_category_with_options_async(
        self,
        request: main_models.ModifyBizCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBizCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_list):
            query['ParamList'] = request.param_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBizCategory',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBizCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_biz_category(
        self,
        request: main_models.ModifyBizCategoryRequest,
    ) -> main_models.ModifyBizCategoryResponse:
        runtime = RuntimeOptions()
        return self.modify_biz_category_with_options(request, runtime)

    async def modify_biz_category_async(
        self,
        request: main_models.ModifyBizCategoryRequest,
    ) -> main_models.ModifyBizCategoryResponse:
        runtime = RuntimeOptions()
        return await self.modify_biz_category_with_options_async(request, runtime)

    def modify_contacter_with_options(
        self,
        request: main_models.ModifyContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_address):
            query['ContacterAddress'] = request.contacter_address
        if not DaraCore.is_null(request.contacter_dingding):
            query['ContacterDingding'] = request.contacter_dingding
        if not DaraCore.is_null(request.contacter_email):
            query['ContacterEmail'] = request.contacter_email
        if not DaraCore.is_null(request.contacter_id):
            query['ContacterId'] = request.contacter_id
        if not DaraCore.is_null(request.contacter_mobile):
            query['ContacterMobile'] = request.contacter_mobile
        if not DaraCore.is_null(request.contacter_name):
            query['ContacterName'] = request.contacter_name
        if not DaraCore.is_null(request.contacter_position):
            query['ContacterPosition'] = request.contacter_position
        if not DaraCore.is_null(request.contacter_staff_no):
            query['ContacterStaffNo'] = request.contacter_staff_no
        if not DaraCore.is_null(request.contacter_type):
            query['ContacterType'] = request.contacter_type
        if not DaraCore.is_null(request.contacter_wangwang):
            query['ContacterWangwang'] = request.contacter_wangwang
        if not DaraCore.is_null(request.email_confirmed):
            query['EmailConfirmed'] = request.email_confirmed
        if not DaraCore.is_null(request.mobile_confirmed):
            query['MobileConfirmed'] = request.mobile_confirmed
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyContacterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_contacter_with_options_async(
        self,
        request: main_models.ModifyContacterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyContacterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacter_address):
            query['ContacterAddress'] = request.contacter_address
        if not DaraCore.is_null(request.contacter_dingding):
            query['ContacterDingding'] = request.contacter_dingding
        if not DaraCore.is_null(request.contacter_email):
            query['ContacterEmail'] = request.contacter_email
        if not DaraCore.is_null(request.contacter_id):
            query['ContacterId'] = request.contacter_id
        if not DaraCore.is_null(request.contacter_mobile):
            query['ContacterMobile'] = request.contacter_mobile
        if not DaraCore.is_null(request.contacter_name):
            query['ContacterName'] = request.contacter_name
        if not DaraCore.is_null(request.contacter_position):
            query['ContacterPosition'] = request.contacter_position
        if not DaraCore.is_null(request.contacter_staff_no):
            query['ContacterStaffNo'] = request.contacter_staff_no
        if not DaraCore.is_null(request.contacter_type):
            query['ContacterType'] = request.contacter_type
        if not DaraCore.is_null(request.contacter_wangwang):
            query['ContacterWangwang'] = request.contacter_wangwang
        if not DaraCore.is_null(request.email_confirmed):
            query['EmailConfirmed'] = request.email_confirmed
        if not DaraCore.is_null(request.mobile_confirmed):
            query['MobileConfirmed'] = request.mobile_confirmed
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyContacter',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyContacterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_contacter(
        self,
        request: main_models.ModifyContacterRequest,
    ) -> main_models.ModifyContacterResponse:
        runtime = RuntimeOptions()
        return self.modify_contacter_with_options(request, runtime)

    async def modify_contacter_async(
        self,
        request: main_models.ModifyContacterRequest,
    ) -> main_models.ModifyContacterResponse:
        runtime = RuntimeOptions()
        return await self.modify_contacter_with_options_async(request, runtime)

    def modify_customer_info_with_options(
        self,
        request: main_models.ModifyCustomerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomerInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz):
            query['Biz'] = request.biz
        if not DaraCore.is_null(request.customer_category):
            query['CustomerCategory'] = request.customer_category
        if not DaraCore.is_null(request.customer_sub_category):
            query['CustomerSubCategory'] = request.customer_sub_category
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.website):
            query['Website'] = request.website
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomerInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_customer_info_with_options_async(
        self,
        request: main_models.ModifyCustomerInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomerInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz):
            query['Biz'] = request.biz
        if not DaraCore.is_null(request.customer_category):
            query['CustomerCategory'] = request.customer_category
        if not DaraCore.is_null(request.customer_sub_category):
            query['CustomerSubCategory'] = request.customer_sub_category
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.website):
            query['Website'] = request.website
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomerInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_customer_info(
        self,
        request: main_models.ModifyCustomerInfoRequest,
    ) -> main_models.ModifyCustomerInfoResponse:
        runtime = RuntimeOptions()
        return self.modify_customer_info_with_options(request, runtime)

    async def modify_customer_info_async(
        self,
        request: main_models.ModifyCustomerInfoRequest,
    ) -> main_models.ModifyCustomerInfoResponse:
        runtime = RuntimeOptions()
        return await self.modify_customer_info_with_options_async(request, runtime)

    def operate_finance_tax_with_options(
        self,
        request: main_models.OperateFinanceTaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateFinanceTaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.finance_tax):
            query['FinanceTax'] = request.finance_tax
        if not DaraCore.is_null(request.finance_tax_certificate_img_name):
            query['FinanceTaxCertificateImgName'] = request.finance_tax_certificate_img_name
        if not DaraCore.is_null(request.hid):
            query['HId'] = request.hid
        if not DaraCore.is_null(request.second_finance_tax):
            query['SecondFinanceTax'] = request.second_finance_tax
        if not DaraCore.is_null(request.second_finance_tax_certificate_img_name):
            query['SecondFinanceTaxCertificateImgName'] = request.second_finance_tax_certificate_img_name
        if not DaraCore.is_null(request.second_finance_tax_certificate_img_url):
            query['SecondFinanceTaxCertificateImgUrl'] = request.second_finance_tax_certificate_img_url
        if not DaraCore.is_null(request.finance_tax_certificate_img_url):
            query['financeTaxCertificateImgUrl'] = request.finance_tax_certificate_img_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateFinanceTax',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateFinanceTaxResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_finance_tax_with_options_async(
        self,
        request: main_models.OperateFinanceTaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateFinanceTaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.finance_tax):
            query['FinanceTax'] = request.finance_tax
        if not DaraCore.is_null(request.finance_tax_certificate_img_name):
            query['FinanceTaxCertificateImgName'] = request.finance_tax_certificate_img_name
        if not DaraCore.is_null(request.hid):
            query['HId'] = request.hid
        if not DaraCore.is_null(request.second_finance_tax):
            query['SecondFinanceTax'] = request.second_finance_tax
        if not DaraCore.is_null(request.second_finance_tax_certificate_img_name):
            query['SecondFinanceTaxCertificateImgName'] = request.second_finance_tax_certificate_img_name
        if not DaraCore.is_null(request.second_finance_tax_certificate_img_url):
            query['SecondFinanceTaxCertificateImgUrl'] = request.second_finance_tax_certificate_img_url
        if not DaraCore.is_null(request.finance_tax_certificate_img_url):
            query['financeTaxCertificateImgUrl'] = request.finance_tax_certificate_img_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateFinanceTax',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateFinanceTaxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_finance_tax(
        self,
        request: main_models.OperateFinanceTaxRequest,
    ) -> main_models.OperateFinanceTaxResponse:
        runtime = RuntimeOptions()
        return self.operate_finance_tax_with_options(request, runtime)

    async def operate_finance_tax_async(
        self,
        request: main_models.OperateFinanceTaxRequest,
    ) -> main_models.OperateFinanceTaxResponse:
        runtime = RuntimeOptions()
        return await self.operate_finance_tax_with_options_async(request, runtime)

    def query_account_address_info_with_options(
        self,
        request: main_models.QueryAccountAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountAddressInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_version):
            query['AddressVersion'] = request.address_version
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountAddressInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_address_info_with_options_async(
        self,
        request: main_models.QueryAccountAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountAddressInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_version):
            query['AddressVersion'] = request.address_version
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountAddressInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_address_info(
        self,
        request: main_models.QueryAccountAddressInfoRequest,
    ) -> main_models.QueryAccountAddressInfoResponse:
        runtime = RuntimeOptions()
        return self.query_account_address_info_with_options(request, runtime)

    async def query_account_address_info_async(
        self,
        request: main_models.QueryAccountAddressInfoRequest,
    ) -> main_models.QueryAccountAddressInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_account_address_info_with_options_async(request, runtime)

    def query_account_address_info_without_havana_with_options(
        self,
        request: main_models.QueryAccountAddressInfoWithoutHavanaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountAddressInfoWithoutHavanaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_version):
            query['AddressVersion'] = request.address_version
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountAddressInfoWithoutHavana',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountAddressInfoWithoutHavanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_address_info_without_havana_with_options_async(
        self,
        request: main_models.QueryAccountAddressInfoWithoutHavanaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountAddressInfoWithoutHavanaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_version):
            query['AddressVersion'] = request.address_version
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountAddressInfoWithoutHavana',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountAddressInfoWithoutHavanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_address_info_without_havana(
        self,
        request: main_models.QueryAccountAddressInfoWithoutHavanaRequest,
    ) -> main_models.QueryAccountAddressInfoWithoutHavanaResponse:
        runtime = RuntimeOptions()
        return self.query_account_address_info_without_havana_with_options(request, runtime)

    async def query_account_address_info_without_havana_async(
        self,
        request: main_models.QueryAccountAddressInfoWithoutHavanaRequest,
    ) -> main_models.QueryAccountAddressInfoWithoutHavanaResponse:
        runtime = RuntimeOptions()
        return await self.query_account_address_info_without_havana_with_options_async(request, runtime)

    def query_account_delivery_address_info_with_options(
        self,
        request: main_models.QueryAccountDeliveryAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountDeliveryAddressInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountDeliveryAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountDeliveryAddressInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_delivery_address_info_with_options_async(
        self,
        request: main_models.QueryAccountDeliveryAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountDeliveryAddressInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountDeliveryAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountDeliveryAddressInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_delivery_address_info(
        self,
        request: main_models.QueryAccountDeliveryAddressInfoRequest,
    ) -> main_models.QueryAccountDeliveryAddressInfoResponse:
        runtime = RuntimeOptions()
        return self.query_account_delivery_address_info_with_options(request, runtime)

    async def query_account_delivery_address_info_async(
        self,
        request: main_models.QueryAccountDeliveryAddressInfoRequest,
    ) -> main_models.QueryAccountDeliveryAddressInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_account_delivery_address_info_with_options_async(request, runtime)

    def query_account_profile_info_with_options(
        self,
        request: main_models.QueryAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountProfileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountProfileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_profile_info_with_options_async(
        self,
        request: main_models.QueryAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountProfileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountProfileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_profile_info(
        self,
        request: main_models.QueryAccountProfileInfoRequest,
    ) -> main_models.QueryAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return self.query_account_profile_info_with_options(request, runtime)

    async def query_account_profile_info_async(
        self,
        request: main_models.QueryAccountProfileInfoRequest,
    ) -> main_models.QueryAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_account_profile_info_with_options_async(request, runtime)

    def query_account_real_name_info_with_options(
        self,
        request: main_models.QueryAccountRealNameInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountRealNameInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountRealNameInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountRealNameInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_real_name_info_with_options_async(
        self,
        request: main_models.QueryAccountRealNameInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountRealNameInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountRealNameInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountRealNameInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_real_name_info(
        self,
        request: main_models.QueryAccountRealNameInfoRequest,
    ) -> main_models.QueryAccountRealNameInfoResponse:
        runtime = RuntimeOptions()
        return self.query_account_real_name_info_with_options(request, runtime)

    async def query_account_real_name_info_async(
        self,
        request: main_models.QueryAccountRealNameInfoRequest,
    ) -> main_models.QueryAccountRealNameInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_account_real_name_info_with_options_async(request, runtime)

    def query_account_site_with_options(
        self,
        request: main_models.QueryAccountSiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountSiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountSite',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_site_with_options_async(
        self,
        request: main_models.QueryAccountSiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountSiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountSite',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_site(
        self,
        request: main_models.QueryAccountSiteRequest,
    ) -> main_models.QueryAccountSiteResponse:
        runtime = RuntimeOptions()
        return self.query_account_site_with_options(request, runtime)

    async def query_account_site_async(
        self,
        request: main_models.QueryAccountSiteRequest,
    ) -> main_models.QueryAccountSiteResponse:
        runtime = RuntimeOptions()
        return await self.query_account_site_with_options_async(request, runtime)

    def query_account_true_name_with_options(
        self,
        request: main_models.QueryAccountTrueNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountTrueNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountTrueName',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountTrueNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_true_name_with_options_async(
        self,
        request: main_models.QueryAccountTrueNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountTrueNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountTrueName',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountTrueNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_true_name(
        self,
        request: main_models.QueryAccountTrueNameRequest,
    ) -> main_models.QueryAccountTrueNameResponse:
        runtime = RuntimeOptions()
        return self.query_account_true_name_with_options(request, runtime)

    async def query_account_true_name_async(
        self,
        request: main_models.QueryAccountTrueNameRequest,
    ) -> main_models.QueryAccountTrueNameResponse:
        runtime = RuntimeOptions()
        return await self.query_account_true_name_with_options_async(request, runtime)

    def query_ag_account_login_permission_with_options(
        self,
        request: main_models.QueryAgAccountLoginPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgAccountLoginPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgAccountLoginPermission',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgAccountLoginPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ag_account_login_permission_with_options_async(
        self,
        request: main_models.QueryAgAccountLoginPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgAccountLoginPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgAccountLoginPermission',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgAccountLoginPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ag_account_login_permission(
        self,
        request: main_models.QueryAgAccountLoginPermissionRequest,
    ) -> main_models.QueryAgAccountLoginPermissionResponse:
        runtime = RuntimeOptions()
        return self.query_ag_account_login_permission_with_options(request, runtime)

    async def query_ag_account_login_permission_async(
        self,
        request: main_models.QueryAgAccountLoginPermissionRequest,
    ) -> main_models.QueryAgAccountLoginPermissionResponse:
        runtime = RuntimeOptions()
        return await self.query_ag_account_login_permission_with_options_async(request, runtime)

    def query_ag_relation_count_and_quota_with_options(
        self,
        request: main_models.QueryAgRelationCountAndQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgRelationCountAndQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not DaraCore.is_null(request.caller_parent_id):
            body['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.caller_type):
            body['CallerType'] = request.caller_type
        if not DaraCore.is_null(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not DaraCore.is_null(request.mpk):
            body['Mpk'] = request.mpk
        if not DaraCore.is_null(request.null_object):
            body['NullObject'] = request.null_object
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.source_ip):
            body['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.sts_token_caller_bid):
            body['StsTokenCallerBid'] = request.sts_token_caller_bid
        if not DaraCore.is_null(request.sts_token_caller_uid):
            body['StsTokenCallerUid'] = request.sts_token_caller_uid
        if not DaraCore.is_null(request.sts_token_role_id):
            body['StsTokenRoleId'] = request.sts_token_role_id
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgRelationCountAndQuota',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgRelationCountAndQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ag_relation_count_and_quota_with_options_async(
        self,
        request: main_models.QueryAgRelationCountAndQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgRelationCountAndQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not DaraCore.is_null(request.caller_parent_id):
            body['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.caller_type):
            body['CallerType'] = request.caller_type
        if not DaraCore.is_null(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not DaraCore.is_null(request.mpk):
            body['Mpk'] = request.mpk
        if not DaraCore.is_null(request.null_object):
            body['NullObject'] = request.null_object
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.source_ip):
            body['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.sts_token_caller_bid):
            body['StsTokenCallerBid'] = request.sts_token_caller_bid
        if not DaraCore.is_null(request.sts_token_caller_uid):
            body['StsTokenCallerUid'] = request.sts_token_caller_uid
        if not DaraCore.is_null(request.sts_token_role_id):
            body['StsTokenRoleId'] = request.sts_token_role_id
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgRelationCountAndQuota',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgRelationCountAndQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ag_relation_count_and_quota(
        self,
        request: main_models.QueryAgRelationCountAndQuotaRequest,
    ) -> main_models.QueryAgRelationCountAndQuotaResponse:
        runtime = RuntimeOptions()
        return self.query_ag_relation_count_and_quota_with_options(request, runtime)

    async def query_ag_relation_count_and_quota_async(
        self,
        request: main_models.QueryAgRelationCountAndQuotaRequest,
    ) -> main_models.QueryAgRelationCountAndQuotaResponse:
        runtime = RuntimeOptions()
        return await self.query_ag_relation_count_and_quota_with_options_async(request, runtime)

    def query_ag_security_mobile_with_options(
        self,
        request: main_models.QueryAgSecurityMobileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgSecurityMobileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgSecurityMobile',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgSecurityMobileResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ag_security_mobile_with_options_async(
        self,
        request: main_models.QueryAgSecurityMobileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAgSecurityMobileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAgSecurityMobile',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAgSecurityMobileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ag_security_mobile(
        self,
        request: main_models.QueryAgSecurityMobileRequest,
    ) -> main_models.QueryAgSecurityMobileResponse:
        runtime = RuntimeOptions()
        return self.query_ag_security_mobile_with_options(request, runtime)

    async def query_ag_security_mobile_async(
        self,
        request: main_models.QueryAgSecurityMobileRequest,
    ) -> main_models.QueryAgSecurityMobileResponse:
        runtime = RuntimeOptions()
        return await self.query_ag_security_mobile_with_options_async(request, runtime)

    def query_binds_by_outer_id_with_options(
        self,
        request: main_models.QueryBindsByOuterIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBindsByOuterIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.minor_outer_id):
            query['MinorOuterId'] = request.minor_outer_id
        if not DaraCore.is_null(request.outer_id):
            query['OuterId'] = request.outer_id
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBindsByOuterId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBindsByOuterIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_binds_by_outer_id_with_options_async(
        self,
        request: main_models.QueryBindsByOuterIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBindsByOuterIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.minor_outer_id):
            query['MinorOuterId'] = request.minor_outer_id
        if not DaraCore.is_null(request.outer_id):
            query['OuterId'] = request.outer_id
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBindsByOuterId',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBindsByOuterIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_binds_by_outer_id(
        self,
        request: main_models.QueryBindsByOuterIdRequest,
    ) -> main_models.QueryBindsByOuterIdResponse:
        runtime = RuntimeOptions()
        return self.query_binds_by_outer_id_with_options(request, runtime)

    async def query_binds_by_outer_id_async(
        self,
        request: main_models.QueryBindsByOuterIdRequest,
    ) -> main_models.QueryBindsByOuterIdResponse:
        runtime = RuntimeOptions()
        return await self.query_binds_by_outer_id_with_options_async(request, runtime)

    def query_binds_by_pk_with_options(
        self,
        tmp_req: main_models.QueryBindsByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBindsByPkResponse:
        tmp_req.validate()
        request = main_models.QueryBindsByPkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tenant_ids):
            request.tenant_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_ids, 'TenantIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.tenant_ids_shrink):
            query['TenantIds'] = request.tenant_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBindsByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBindsByPkResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_binds_by_pk_with_options_async(
        self,
        tmp_req: main_models.QueryBindsByPkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBindsByPkResponse:
        tmp_req.validate()
        request = main_models.QueryBindsByPkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tenant_ids):
            request.tenant_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_ids, 'TenantIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.tenant_ids_shrink):
            query['TenantIds'] = request.tenant_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBindsByPk',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBindsByPkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_binds_by_pk(
        self,
        request: main_models.QueryBindsByPkRequest,
    ) -> main_models.QueryBindsByPkResponse:
        runtime = RuntimeOptions()
        return self.query_binds_by_pk_with_options(request, runtime)

    async def query_binds_by_pk_async(
        self,
        request: main_models.QueryBindsByPkRequest,
    ) -> main_models.QueryBindsByPkResponse:
        runtime = RuntimeOptions()
        return await self.query_binds_by_pk_with_options_async(request, runtime)

    def query_customer_label_with_options(
        self,
        request: main_models.QueryCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerLabel',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_customer_label_with_options_async(
        self,
        request: main_models.QueryCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerLabel',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_customer_label(
        self,
        request: main_models.QueryCustomerLabelRequest,
    ) -> main_models.QueryCustomerLabelResponse:
        runtime = RuntimeOptions()
        return self.query_customer_label_with_options(request, runtime)

    async def query_customer_label_async(
        self,
        request: main_models.QueryCustomerLabelRequest,
    ) -> main_models.QueryCustomerLabelResponse:
        runtime = RuntimeOptions()
        return await self.query_customer_label_with_options_async(request, runtime)

    def query_delete_task_check_data_with_options(
        self,
        request: main_models.QueryDeleteTaskCheckDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeleteTaskCheckDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.long_lang):
            query['LongLang'] = request.long_lang
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeleteTaskCheckData',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeleteTaskCheckDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_delete_task_check_data_with_options_async(
        self,
        request: main_models.QueryDeleteTaskCheckDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeleteTaskCheckDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.long_lang):
            query['LongLang'] = request.long_lang
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeleteTaskCheckData',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeleteTaskCheckDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_delete_task_check_data(
        self,
        request: main_models.QueryDeleteTaskCheckDataRequest,
    ) -> main_models.QueryDeleteTaskCheckDataResponse:
        runtime = RuntimeOptions()
        return self.query_delete_task_check_data_with_options(request, runtime)

    async def query_delete_task_check_data_async(
        self,
        request: main_models.QueryDeleteTaskCheckDataRequest,
    ) -> main_models.QueryDeleteTaskCheckDataResponse:
        runtime = RuntimeOptions()
        return await self.query_delete_task_check_data_with_options_async(request, runtime)

    def query_encrypted_account_profile_info_with_options(
        self,
        request: main_models.QueryEncryptedAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEncryptedAccountProfileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEncryptedAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEncryptedAccountProfileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_encrypted_account_profile_info_with_options_async(
        self,
        request: main_models.QueryEncryptedAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEncryptedAccountProfileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEncryptedAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEncryptedAccountProfileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_encrypted_account_profile_info(
        self,
        request: main_models.QueryEncryptedAccountProfileInfoRequest,
    ) -> main_models.QueryEncryptedAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return self.query_encrypted_account_profile_info_with_options(request, runtime)

    async def query_encrypted_account_profile_info_async(
        self,
        request: main_models.QueryEncryptedAccountProfileInfoRequest,
    ) -> main_models.QueryEncryptedAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_encrypted_account_profile_info_with_options_async(request, runtime)

    def query_enterprise_info_with_options(
        self,
        request: main_models.QueryEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_version):
            query['EnterpriseVersion'] = request.enterprise_version
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnterpriseInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnterpriseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_enterprise_info_with_options_async(
        self,
        request: main_models.QueryEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_version):
            query['EnterpriseVersion'] = request.enterprise_version
        if not DaraCore.is_null(request.havana_id):
            query['HavanaId'] = request.havana_id
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnterpriseInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnterpriseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_enterprise_info(
        self,
        request: main_models.QueryEnterpriseInfoRequest,
    ) -> main_models.QueryEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return self.query_enterprise_info_with_options(request, runtime)

    async def query_enterprise_info_async(
        self,
        request: main_models.QueryEnterpriseInfoRequest,
    ) -> main_models.QueryEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_enterprise_info_with_options_async(request, runtime)

    def query_enum_config_by_type_with_options(
        self,
        request: main_models.QueryEnumConfigByTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnumConfigByTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnumConfigByType',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnumConfigByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_enum_config_by_type_with_options_async(
        self,
        request: main_models.QueryEnumConfigByTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnumConfigByTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnumConfigByType',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnumConfigByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_enum_config_by_type(
        self,
        request: main_models.QueryEnumConfigByTypeRequest,
    ) -> main_models.QueryEnumConfigByTypeResponse:
        runtime = RuntimeOptions()
        return self.query_enum_config_by_type_with_options(request, runtime)

    async def query_enum_config_by_type_async(
        self,
        request: main_models.QueryEnumConfigByTypeRequest,
    ) -> main_models.QueryEnumConfigByTypeResponse:
        runtime = RuntimeOptions()
        return await self.query_enum_config_by_type_with_options_async(request, runtime)

    def query_one_key_delete_block_list_with_options(
        self,
        request: main_models.QueryOneKeyDeleteBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOneKeyDeleteBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOneKeyDeleteBlockList',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOneKeyDeleteBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_one_key_delete_block_list_with_options_async(
        self,
        request: main_models.QueryOneKeyDeleteBlockListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOneKeyDeleteBlockListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOneKeyDeleteBlockList',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOneKeyDeleteBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_one_key_delete_block_list(
        self,
        request: main_models.QueryOneKeyDeleteBlockListRequest,
    ) -> main_models.QueryOneKeyDeleteBlockListResponse:
        runtime = RuntimeOptions()
        return self.query_one_key_delete_block_list_with_options(request, runtime)

    async def query_one_key_delete_block_list_async(
        self,
        request: main_models.QueryOneKeyDeleteBlockListRequest,
    ) -> main_models.QueryOneKeyDeleteBlockListResponse:
        runtime = RuntimeOptions()
        return await self.query_one_key_delete_block_list_with_options_async(request, runtime)

    def query_security_info_with_options(
        self,
        request: main_models.QuerySecurityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecurityInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecurityInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecurityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_security_info_with_options_async(
        self,
        request: main_models.QuerySecurityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecurityInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecurityInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecurityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_security_info(
        self,
        request: main_models.QuerySecurityInfoRequest,
    ) -> main_models.QuerySecurityInfoResponse:
        runtime = RuntimeOptions()
        return self.query_security_info_with_options(request, runtime)

    async def query_security_info_async(
        self,
        request: main_models.QuerySecurityInfoRequest,
    ) -> main_models.QuerySecurityInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_security_info_with_options_async(request, runtime)

    def register_internal_account_for_buc_with_options(
        self,
        request: main_models.RegisterInternalAccountForBucRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterInternalAccountForBucResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bid):
            query['Bid'] = request.bid
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.is_email_confirmed):
            query['IsEmailConfirmed'] = request.is_email_confirmed
        if not DaraCore.is_null(request.is_mobile_confirmed):
            query['IsMobileConfirmed'] = request.is_mobile_confirmed
        if not DaraCore.is_null(request.is_mobile_login):
            query['IsMobileLogin'] = request.is_mobile_login
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.nationality_code):
            query['NationalityCode'] = request.nationality_code
        if not DaraCore.is_null(request.plain_password):
            query['PlainPassword'] = request.plain_password
        if not DaraCore.is_null(request.preferred_language):
            query['PreferredLanguage'] = request.preferred_language
        if not DaraCore.is_null(request.account_type_code):
            query['accountTypeCode'] = request.account_type_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterInternalAccountForBuc',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterInternalAccountForBucResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_internal_account_for_buc_with_options_async(
        self,
        request: main_models.RegisterInternalAccountForBucRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterInternalAccountForBucResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bid):
            query['Bid'] = request.bid
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.is_email_confirmed):
            query['IsEmailConfirmed'] = request.is_email_confirmed
        if not DaraCore.is_null(request.is_mobile_confirmed):
            query['IsMobileConfirmed'] = request.is_mobile_confirmed
        if not DaraCore.is_null(request.is_mobile_login):
            query['IsMobileLogin'] = request.is_mobile_login
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.nationality_code):
            query['NationalityCode'] = request.nationality_code
        if not DaraCore.is_null(request.plain_password):
            query['PlainPassword'] = request.plain_password
        if not DaraCore.is_null(request.preferred_language):
            query['PreferredLanguage'] = request.preferred_language
        if not DaraCore.is_null(request.account_type_code):
            query['accountTypeCode'] = request.account_type_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterInternalAccountForBuc',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterInternalAccountForBucResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_internal_account_for_buc(
        self,
        request: main_models.RegisterInternalAccountForBucRequest,
    ) -> main_models.RegisterInternalAccountForBucResponse:
        runtime = RuntimeOptions()
        return self.register_internal_account_for_buc_with_options(request, runtime)

    async def register_internal_account_for_buc_async(
        self,
        request: main_models.RegisterInternalAccountForBucRequest,
    ) -> main_models.RegisterInternalAccountForBucResponse:
        runtime = RuntimeOptions()
        return await self.register_internal_account_for_buc_with_options_async(request, runtime)

    def release_ag_account_with_options(
        self,
        request: main_models.ReleaseAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.release_reason):
            query['ReleaseReason'] = request.release_reason
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_ag_account_with_options_async(
        self,
        request: main_models.ReleaseAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.release_reason):
            query['ReleaseReason'] = request.release_reason
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_ag_account(
        self,
        request: main_models.ReleaseAgAccountRequest,
    ) -> main_models.ReleaseAgAccountResponse:
        runtime = RuntimeOptions()
        return self.release_ag_account_with_options(request, runtime)

    async def release_ag_account_async(
        self,
        request: main_models.ReleaseAgAccountRequest,
    ) -> main_models.ReleaseAgAccountResponse:
        runtime = RuntimeOptions()
        return await self.release_ag_account_with_options_async(request, runtime)

    def resend_async_create_ag_account_with_options(
        self,
        request: main_models.ResendAsyncCreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendAsyncCreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendAsyncCreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendAsyncCreateAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_async_create_ag_account_with_options_async(
        self,
        request: main_models.ResendAsyncCreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendAsyncCreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendAsyncCreateAgAccount',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendAsyncCreateAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_async_create_ag_account(
        self,
        request: main_models.ResendAsyncCreateAgAccountRequest,
    ) -> main_models.ResendAsyncCreateAgAccountResponse:
        runtime = RuntimeOptions()
        return self.resend_async_create_ag_account_with_options(request, runtime)

    async def resend_async_create_ag_account_async(
        self,
        request: main_models.ResendAsyncCreateAgAccountRequest,
    ) -> main_models.ResendAsyncCreateAgAccountResponse:
        runtime = RuntimeOptions()
        return await self.resend_async_create_ag_account_with_options_async(request, runtime)

    def resend_async_modify_login_email_with_options(
        self,
        request: main_models.ResendAsyncModifyLoginEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendAsyncModifyLoginEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendAsyncModifyLoginEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendAsyncModifyLoginEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_async_modify_login_email_with_options_async(
        self,
        request: main_models.ResendAsyncModifyLoginEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendAsyncModifyLoginEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.trace_no):
            query['TraceNo'] = request.trace_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendAsyncModifyLoginEmail',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendAsyncModifyLoginEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_async_modify_login_email(
        self,
        request: main_models.ResendAsyncModifyLoginEmailRequest,
    ) -> main_models.ResendAsyncModifyLoginEmailResponse:
        runtime = RuntimeOptions()
        return self.resend_async_modify_login_email_with_options(request, runtime)

    async def resend_async_modify_login_email_async(
        self,
        request: main_models.ResendAsyncModifyLoginEmailRequest,
    ) -> main_models.ResendAsyncModifyLoginEmailResponse:
        runtime = RuntimeOptions()
        return await self.resend_async_modify_login_email_with_options_async(request, runtime)

    def separate_ag_relation_with_options(
        self,
        request: main_models.SeparateAgRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SeparateAgRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SeparateAgRelation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SeparateAgRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def separate_ag_relation_with_options_async(
        self,
        request: main_models.SeparateAgRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SeparateAgRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SeparateAgRelation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SeparateAgRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def separate_ag_relation(
        self,
        request: main_models.SeparateAgRelationRequest,
    ) -> main_models.SeparateAgRelationResponse:
        runtime = RuntimeOptions()
        return self.separate_ag_relation_with_options(request, runtime)

    async def separate_ag_relation_async(
        self,
        request: main_models.SeparateAgRelationRequest,
    ) -> main_models.SeparateAgRelationResponse:
        runtime = RuntimeOptions()
        return await self.separate_ag_relation_with_options_async(request, runtime)

    def set_cache_operate_sync_with_options(
        self,
        request: main_models.SetCacheOperateSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCacheOperateSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.except_version):
            query['ExceptVersion'] = request.except_version
        if not DaraCore.is_null(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.set_type):
            query['SetType'] = request.set_type
        if not DaraCore.is_null(request.value_clazz):
            query['ValueClazz'] = request.value_clazz
        if not DaraCore.is_null(request.value_string):
            query['ValueString'] = request.value_string
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCacheOperateSync',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCacheOperateSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cache_operate_sync_with_options_async(
        self,
        request: main_models.SetCacheOperateSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCacheOperateSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.except_version):
            query['ExceptVersion'] = request.except_version
        if not DaraCore.is_null(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.set_type):
            query['SetType'] = request.set_type
        if not DaraCore.is_null(request.value_clazz):
            query['ValueClazz'] = request.value_clazz
        if not DaraCore.is_null(request.value_string):
            query['ValueString'] = request.value_string
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCacheOperateSync',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCacheOperateSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cache_operate_sync(
        self,
        request: main_models.SetCacheOperateSyncRequest,
    ) -> main_models.SetCacheOperateSyncResponse:
        runtime = RuntimeOptions()
        return self.set_cache_operate_sync_with_options(request, runtime)

    async def set_cache_operate_sync_async(
        self,
        request: main_models.SetCacheOperateSyncRequest,
    ) -> main_models.SetCacheOperateSyncResponse:
        runtime = RuntimeOptions()
        return await self.set_cache_operate_sync_with_options_async(request, runtime)

    def update_account_address_info_with_options(
        self,
        tmp_req: main_models.UpdateAccountAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountAddressInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateAccountAddressInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.city_json_string):
            request.city_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.city_json_string, 'CityJsonString', 'json')
        if not DaraCore.is_null(tmp_req.district_json_string):
            request.district_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.district_json_string, 'DistrictJsonString', 'json')
        if not DaraCore.is_null(tmp_req.province_json_string):
            request.province_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.province_json_string, 'ProvinceJsonString', 'json')
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_2):
            query['Address2'] = request.address_2
        if not DaraCore.is_null(request.city_json_string_shrink):
            query['CityJsonString'] = request.city_json_string_shrink
        if not DaraCore.is_null(request.district_json_string_shrink):
            query['DistrictJsonString'] = request.district_json_string_shrink
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.post_code):
            query['PostCode'] = request.post_code
        if not DaraCore.is_null(request.province_json_string_shrink):
            query['ProvinceJsonString'] = request.province_json_string_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountAddressInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_address_info_with_options_async(
        self,
        tmp_req: main_models.UpdateAccountAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountAddressInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateAccountAddressInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.city_json_string):
            request.city_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.city_json_string, 'CityJsonString', 'json')
        if not DaraCore.is_null(tmp_req.district_json_string):
            request.district_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.district_json_string, 'DistrictJsonString', 'json')
        if not DaraCore.is_null(tmp_req.province_json_string):
            request.province_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.province_json_string, 'ProvinceJsonString', 'json')
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_2):
            query['Address2'] = request.address_2
        if not DaraCore.is_null(request.city_json_string_shrink):
            query['CityJsonString'] = request.city_json_string_shrink
        if not DaraCore.is_null(request.district_json_string_shrink):
            query['DistrictJsonString'] = request.district_json_string_shrink
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.post_code):
            query['PostCode'] = request.post_code
        if not DaraCore.is_null(request.province_json_string_shrink):
            query['ProvinceJsonString'] = request.province_json_string_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountAddressInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_address_info(
        self,
        request: main_models.UpdateAccountAddressInfoRequest,
    ) -> main_models.UpdateAccountAddressInfoResponse:
        runtime = RuntimeOptions()
        return self.update_account_address_info_with_options(request, runtime)

    async def update_account_address_info_async(
        self,
        request: main_models.UpdateAccountAddressInfoRequest,
    ) -> main_models.UpdateAccountAddressInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_account_address_info_with_options_async(request, runtime)

    def update_account_profile_info_with_options(
        self,
        tmp_req: main_models.UpdateAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountProfileInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateAccountProfileInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.city_json_string):
            request.city_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.city_json_string, 'CityJsonString', 'json')
        if not DaraCore.is_null(tmp_req.district_json_string):
            request.district_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.district_json_string, 'DistrictJsonString', 'json')
        if not DaraCore.is_null(tmp_req.province_json_string):
            request.province_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.province_json_string, 'ProvinceJsonString', 'json')
        query = {}
        if not DaraCore.is_null(request.account_attribute):
            query['AccountAttribute'] = request.account_attribute
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_2):
            query['Address2'] = request.address_2
        if not DaraCore.is_null(request.bind_alipay_no):
            query['BindAlipayNo'] = request.bind_alipay_no
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.city_json_string_shrink):
            query['CityJsonString'] = request.city_json_string_shrink
        if not DaraCore.is_null(request.contact_method):
            query['ContactMethod'] = request.contact_method
        if not DaraCore.is_null(request.district_json_string_shrink):
            query['DistrictJsonString'] = request.district_json_string_shrink
        if not DaraCore.is_null(request.fax):
            query['Fax'] = request.fax
        if not DaraCore.is_null(request.first_name):
            query['FirstName'] = request.first_name
        if not DaraCore.is_null(request.head):
            query['Head'] = request.head
        if not DaraCore.is_null(request.head_color):
            query['HeadColor'] = request.head_color
        if not DaraCore.is_null(request.last_name):
            query['LastName'] = request.last_name
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.post_code):
            query['PostCode'] = request.post_code
        if not DaraCore.is_null(request.province_json_string_shrink):
            query['ProvinceJsonString'] = request.province_json_string_shrink
        if not DaraCore.is_null(request.self_servicing_business_reg_num):
            query['SelfServicingBusinessRegNum'] = request.self_servicing_business_reg_num
        if not DaraCore.is_null(request.self_servicing_identification_num):
            query['SelfServicingIdentificationNum'] = request.self_servicing_identification_num
        if not DaraCore.is_null(request.true_name):
            query['TrueName'] = request.true_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountProfileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_profile_info_with_options_async(
        self,
        tmp_req: main_models.UpdateAccountProfileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountProfileInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateAccountProfileInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.city_json_string):
            request.city_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.city_json_string, 'CityJsonString', 'json')
        if not DaraCore.is_null(tmp_req.district_json_string):
            request.district_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.district_json_string, 'DistrictJsonString', 'json')
        if not DaraCore.is_null(tmp_req.province_json_string):
            request.province_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.province_json_string, 'ProvinceJsonString', 'json')
        query = {}
        if not DaraCore.is_null(request.account_attribute):
            query['AccountAttribute'] = request.account_attribute
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_2):
            query['Address2'] = request.address_2
        if not DaraCore.is_null(request.bind_alipay_no):
            query['BindAlipayNo'] = request.bind_alipay_no
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.city_json_string_shrink):
            query['CityJsonString'] = request.city_json_string_shrink
        if not DaraCore.is_null(request.contact_method):
            query['ContactMethod'] = request.contact_method
        if not DaraCore.is_null(request.district_json_string_shrink):
            query['DistrictJsonString'] = request.district_json_string_shrink
        if not DaraCore.is_null(request.fax):
            query['Fax'] = request.fax
        if not DaraCore.is_null(request.first_name):
            query['FirstName'] = request.first_name
        if not DaraCore.is_null(request.head):
            query['Head'] = request.head
        if not DaraCore.is_null(request.head_color):
            query['HeadColor'] = request.head_color
        if not DaraCore.is_null(request.last_name):
            query['LastName'] = request.last_name
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.post_code):
            query['PostCode'] = request.post_code
        if not DaraCore.is_null(request.province_json_string_shrink):
            query['ProvinceJsonString'] = request.province_json_string_shrink
        if not DaraCore.is_null(request.self_servicing_business_reg_num):
            query['SelfServicingBusinessRegNum'] = request.self_servicing_business_reg_num
        if not DaraCore.is_null(request.self_servicing_identification_num):
            query['SelfServicingIdentificationNum'] = request.self_servicing_identification_num
        if not DaraCore.is_null(request.true_name):
            query['TrueName'] = request.true_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountProfileInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountProfileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_profile_info(
        self,
        request: main_models.UpdateAccountProfileInfoRequest,
    ) -> main_models.UpdateAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return self.update_account_profile_info_with_options(request, runtime)

    async def update_account_profile_info_async(
        self,
        request: main_models.UpdateAccountProfileInfoRequest,
    ) -> main_models.UpdateAccountProfileInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_account_profile_info_with_options_async(request, runtime)

    def update_ag_account_address_info_with_options(
        self,
        request: main_models.UpdateAgAccountAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgAccountAddressInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_2):
            query['Address2'] = request.address_2
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.post_code):
            query['PostCode'] = request.post_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgAccountAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgAccountAddressInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ag_account_address_info_with_options_async(
        self,
        request: main_models.UpdateAgAccountAddressInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgAccountAddressInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_2):
            query['Address2'] = request.address_2
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.post_code):
            query['PostCode'] = request.post_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgAccountAddressInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgAccountAddressInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ag_account_address_info(
        self,
        request: main_models.UpdateAgAccountAddressInfoRequest,
    ) -> main_models.UpdateAgAccountAddressInfoResponse:
        runtime = RuntimeOptions()
        return self.update_ag_account_address_info_with_options(request, runtime)

    async def update_ag_account_address_info_async(
        self,
        request: main_models.UpdateAgAccountAddressInfoRequest,
    ) -> main_models.UpdateAgAccountAddressInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_ag_account_address_info_with_options_async(request, runtime)

    def update_ag_service_status_with_options(
        self,
        request: main_models.UpdateAgServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgServiceStatus',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ag_service_status_with_options_async(
        self,
        request: main_models.UpdateAgServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ag_account_type):
            query['AgAccountType'] = request.ag_account_type
        if not DaraCore.is_null(request.mpk):
            query['Mpk'] = request.mpk
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgServiceStatus',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ag_service_status(
        self,
        request: main_models.UpdateAgServiceStatusRequest,
    ) -> main_models.UpdateAgServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.update_ag_service_status_with_options(request, runtime)

    async def update_ag_service_status_async(
        self,
        request: main_models.UpdateAgServiceStatusRequest,
    ) -> main_models.UpdateAgServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_ag_service_status_with_options_async(request, runtime)

    def update_customer_category_with_options(
        self,
        request: main_models.UpdateCustomerCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomerCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_list):
            query['ParamList'] = request.param_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomerCategory',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomerCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_customer_category_with_options_async(
        self,
        request: main_models.UpdateCustomerCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomerCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_list):
            query['ParamList'] = request.param_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomerCategory',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomerCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_customer_category(
        self,
        request: main_models.UpdateCustomerCategoryRequest,
    ) -> main_models.UpdateCustomerCategoryResponse:
        runtime = RuntimeOptions()
        return self.update_customer_category_with_options(request, runtime)

    async def update_customer_category_async(
        self,
        request: main_models.UpdateCustomerCategoryRequest,
    ) -> main_models.UpdateCustomerCategoryResponse:
        runtime = RuntimeOptions()
        return await self.update_customer_category_with_options_async(request, runtime)

    def update_customer_information_with_options(
        self,
        request: main_models.UpdateCustomerInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomerInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz):
            query['Biz'] = request.biz
        if not DaraCore.is_null(request.customer_category):
            query['CustomerCategory'] = request.customer_category
        if not DaraCore.is_null(request.customer_sub_category):
            query['CustomerSubCategory'] = request.customer_sub_category
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.website):
            query['Website'] = request.website
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomerInformation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomerInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_customer_information_with_options_async(
        self,
        request: main_models.UpdateCustomerInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomerInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz):
            query['Biz'] = request.biz
        if not DaraCore.is_null(request.customer_category):
            query['CustomerCategory'] = request.customer_category
        if not DaraCore.is_null(request.customer_sub_category):
            query['CustomerSubCategory'] = request.customer_sub_category
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.website):
            query['Website'] = request.website
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomerInformation',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomerInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_customer_information(
        self,
        request: main_models.UpdateCustomerInformationRequest,
    ) -> main_models.UpdateCustomerInformationResponse:
        runtime = RuntimeOptions()
        return self.update_customer_information_with_options(request, runtime)

    async def update_customer_information_async(
        self,
        request: main_models.UpdateCustomerInformationRequest,
    ) -> main_models.UpdateCustomerInformationResponse:
        runtime = RuntimeOptions()
        return await self.update_customer_information_with_options_async(request, runtime)

    def update_or_insert_enterprise_info_with_options(
        self,
        tmp_req: main_models.UpdateOrInsertEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrInsertEnterpriseInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateOrInsertEnterpriseInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.city_json_string):
            request.city_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.city_json_string, 'CityJsonString', 'json')
        if not DaraCore.is_null(tmp_req.province_json_string):
            request.province_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.province_json_string, 'ProvinceJsonString', 'json')
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.city_json_string_shrink):
            query['CityJsonString'] = request.city_json_string_shrink
        if not DaraCore.is_null(request.enterprise_size):
            query['EnterpriseSize'] = request.enterprise_size
        if not DaraCore.is_null(request.fax):
            query['Fax'] = request.fax
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.province_json_string_shrink):
            query['ProvinceJsonString'] = request.province_json_string_shrink
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrInsertEnterpriseInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrInsertEnterpriseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_or_insert_enterprise_info_with_options_async(
        self,
        tmp_req: main_models.UpdateOrInsertEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrInsertEnterpriseInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateOrInsertEnterpriseInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.city_json_string):
            request.city_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.city_json_string, 'CityJsonString', 'json')
        if not DaraCore.is_null(tmp_req.province_json_string):
            request.province_json_string_shrink = Utils.array_to_string_with_specified_style(tmp_req.province_json_string, 'ProvinceJsonString', 'json')
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.alias):
            query['Alias'] = request.alias
        if not DaraCore.is_null(request.city_json_string_shrink):
            query['CityJsonString'] = request.city_json_string_shrink
        if not DaraCore.is_null(request.enterprise_size):
            query['EnterpriseSize'] = request.enterprise_size
        if not DaraCore.is_null(request.fax):
            query['Fax'] = request.fax
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.province_json_string_shrink):
            query['ProvinceJsonString'] = request.province_json_string_shrink
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrInsertEnterpriseInfo',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrInsertEnterpriseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_or_insert_enterprise_info(
        self,
        request: main_models.UpdateOrInsertEnterpriseInfoRequest,
    ) -> main_models.UpdateOrInsertEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return self.update_or_insert_enterprise_info_with_options(request, runtime)

    async def update_or_insert_enterprise_info_async(
        self,
        request: main_models.UpdateOrInsertEnterpriseInfoRequest,
    ) -> main_models.UpdateOrInsertEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_or_insert_enterprise_info_with_options_async(request, runtime)

    def do_logical_delete_resource_with_options(
        self,
        request: main_models.DoLogicalDeleteResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DoLogicalDeleteResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bid):
            query['Bid'] = request.bid
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not DaraCore.is_null(request.hid):
            query['Hid'] = request.hid
        if not DaraCore.is_null(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not DaraCore.is_null(request.invoker):
            query['Invoker'] = request.invoker
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.success):
            query['Success'] = request.success
        if not DaraCore.is_null(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not DaraCore.is_null(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'doLogicalDeleteResource',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DoLogicalDeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_logical_delete_resource_with_options_async(
        self,
        request: main_models.DoLogicalDeleteResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DoLogicalDeleteResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bid):
            query['Bid'] = request.bid
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not DaraCore.is_null(request.hid):
            query['Hid'] = request.hid
        if not DaraCore.is_null(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not DaraCore.is_null(request.invoker):
            query['Invoker'] = request.invoker
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.success):
            query['Success'] = request.success
        if not DaraCore.is_null(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not DaraCore.is_null(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'doLogicalDeleteResource',
            version = '2016-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DoLogicalDeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_logical_delete_resource(
        self,
        request: main_models.DoLogicalDeleteResourceRequest,
    ) -> main_models.DoLogicalDeleteResourceResponse:
        runtime = RuntimeOptions()
        return self.do_logical_delete_resource_with_options(request, runtime)

    async def do_logical_delete_resource_async(
        self,
        request: main_models.DoLogicalDeleteResourceRequest,
    ) -> main_models.DoLogicalDeleteResourceResponse:
        runtime = RuntimeOptions()
        return await self.do_logical_delete_resource_with_options_async(request, runtime)
