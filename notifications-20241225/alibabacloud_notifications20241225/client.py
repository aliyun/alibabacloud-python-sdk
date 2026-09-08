# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_notifications20241225 import models as main_models
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
        self._endpoint_map = {
            'ap-southeast-1': 'notifications-intl.aliyuncs.com',
            'cn-zhangjiakou': 'notifications.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('notifications', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_webhook_contact_with_options(
        self,
        request: main_models.CreateWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.bot_security_token):
            body['BotSecurityToken'] = request.bot_security_token
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.server_url):
            body['ServerUrl'] = request.server_url
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        if not DaraCore.is_null(request.verification_code):
            body['VerificationCode'] = request.verification_code
        if not DaraCore.is_null(request.webhook_type):
            body['WebhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_webhook_contact_with_options_async(
        self,
        request: main_models.CreateWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.bot_security_token):
            body['BotSecurityToken'] = request.bot_security_token
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.server_url):
            body['ServerUrl'] = request.server_url
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        if not DaraCore.is_null(request.verification_code):
            body['VerificationCode'] = request.verification_code
        if not DaraCore.is_null(request.webhook_type):
            body['WebhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_webhook_contact(
        self,
        request: main_models.CreateWebhookContactRequest,
    ) -> main_models.CreateWebhookContactResponse:
        runtime = RuntimeOptions()
        return self.create_webhook_contact_with_options(request, runtime)

    async def create_webhook_contact_async(
        self,
        request: main_models.CreateWebhookContactRequest,
    ) -> main_models.CreateWebhookContactResponse:
        runtime = RuntimeOptions()
        return await self.create_webhook_contact_with_options_async(request, runtime)

    def del_message_with_options(
        self,
        request: main_models.DelMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DelMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_message_with_options_async(
        self,
        request: main_models.DelMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DelMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_message(
        self,
        request: main_models.DelMessageRequest,
    ) -> main_models.DelMessageResponse:
        runtime = RuntimeOptions()
        return self.del_message_with_options(request, runtime)

    async def del_message_async(
        self,
        request: main_models.DelMessageRequest,
    ) -> main_models.DelMessageResponse:
        runtime = RuntimeOptions()
        return await self.del_message_with_options_async(request, runtime)

    def delete_all_message_with_options(
        self,
        request: main_models.DeleteAllMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAllMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_message_with_options_async(
        self,
        request: main_models.DeleteAllMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAllMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_message(
        self,
        request: main_models.DeleteAllMessageRequest,
    ) -> main_models.DeleteAllMessageResponse:
        runtime = RuntimeOptions()
        return self.delete_all_message_with_options(request, runtime)

    async def delete_all_message_async(
        self,
        request: main_models.DeleteAllMessageRequest,
    ) -> main_models.DeleteAllMessageResponse:
        runtime = RuntimeOptions()
        return await self.delete_all_message_with_options_async(request, runtime)

    def delete_webhook_contact_with_options(
        self,
        request: main_models.DeleteWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_webhook_contact_with_options_async(
        self,
        request: main_models.DeleteWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_webhook_contact(
        self,
        request: main_models.DeleteWebhookContactRequest,
    ) -> main_models.DeleteWebhookContactResponse:
        runtime = RuntimeOptions()
        return self.delete_webhook_contact_with_options(request, runtime)

    async def delete_webhook_contact_async(
        self,
        request: main_models.DeleteWebhookContactRequest,
    ) -> main_models.DeleteWebhookContactResponse:
        runtime = RuntimeOptions()
        return await self.delete_webhook_contact_with_options_async(request, runtime)

    def read_all_common_contacts_with_options(
        self,
        request: main_models.ReadAllCommonContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllCommonContactsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllCommonContacts',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllCommonContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_all_common_contacts_with_options_async(
        self,
        request: main_models.ReadAllCommonContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllCommonContactsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllCommonContacts',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllCommonContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_all_common_contacts(
        self,
        request: main_models.ReadAllCommonContactsRequest,
    ) -> main_models.ReadAllCommonContactsResponse:
        runtime = RuntimeOptions()
        return self.read_all_common_contacts_with_options(request, runtime)

    async def read_all_common_contacts_async(
        self,
        request: main_models.ReadAllCommonContactsRequest,
    ) -> main_models.ReadAllCommonContactsResponse:
        runtime = RuntimeOptions()
        return await self.read_all_common_contacts_with_options_async(request, runtime)

    def read_all_marketing_preferences_with_options(
        self,
        request: main_models.ReadAllMarketingPreferencesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllMarketingPreferencesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllMarketingPreferences',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllMarketingPreferencesResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_all_marketing_preferences_with_options_async(
        self,
        request: main_models.ReadAllMarketingPreferencesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllMarketingPreferencesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllMarketingPreferences',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllMarketingPreferencesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_all_marketing_preferences(
        self,
        request: main_models.ReadAllMarketingPreferencesRequest,
    ) -> main_models.ReadAllMarketingPreferencesResponse:
        runtime = RuntimeOptions()
        return self.read_all_marketing_preferences_with_options(request, runtime)

    async def read_all_marketing_preferences_async(
        self,
        request: main_models.ReadAllMarketingPreferencesRequest,
    ) -> main_models.ReadAllMarketingPreferencesResponse:
        runtime = RuntimeOptions()
        return await self.read_all_marketing_preferences_with_options_async(request, runtime)

    def read_all_message_with_options(
        self,
        request: main_models.ReadAllMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_all_message_with_options_async(
        self,
        request: main_models.ReadAllMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_all_message(
        self,
        request: main_models.ReadAllMessageRequest,
    ) -> main_models.ReadAllMessageResponse:
        runtime = RuntimeOptions()
        return self.read_all_message_with_options(request, runtime)

    async def read_all_message_async(
        self,
        request: main_models.ReadAllMessageRequest,
    ) -> main_models.ReadAllMessageResponse:
        runtime = RuntimeOptions()
        return await self.read_all_message_with_options_async(request, runtime)

    def read_all_webhook_contacts_with_options(
        self,
        request: main_models.ReadAllWebhookContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllWebhookContactsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllWebhookContacts',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllWebhookContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_all_webhook_contacts_with_options_async(
        self,
        request: main_models.ReadAllWebhookContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadAllWebhookContactsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadAllWebhookContacts',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadAllWebhookContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_all_webhook_contacts(
        self,
        request: main_models.ReadAllWebhookContactsRequest,
    ) -> main_models.ReadAllWebhookContactsResponse:
        runtime = RuntimeOptions()
        return self.read_all_webhook_contacts_with_options(request, runtime)

    async def read_all_webhook_contacts_async(
        self,
        request: main_models.ReadAllWebhookContactsRequest,
    ) -> main_models.ReadAllWebhookContactsResponse:
        runtime = RuntimeOptions()
        return await self.read_all_webhook_contacts_with_options_async(request, runtime)

    def read_category_group_list_with_options(
        self,
        request: main_models.ReadCategoryGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadCategoryGroupListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadCategoryGroupList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadCategoryGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_category_group_list_with_options_async(
        self,
        request: main_models.ReadCategoryGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadCategoryGroupListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadCategoryGroupList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadCategoryGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_category_group_list(
        self,
        request: main_models.ReadCategoryGroupListRequest,
    ) -> main_models.ReadCategoryGroupListResponse:
        runtime = RuntimeOptions()
        return self.read_category_group_list_with_options(request, runtime)

    async def read_category_group_list_async(
        self,
        request: main_models.ReadCategoryGroupListRequest,
    ) -> main_models.ReadCategoryGroupListResponse:
        runtime = RuntimeOptions()
        return await self.read_category_group_list_with_options_async(request, runtime)

    def read_class_name_with_options(
        self,
        request: main_models.ReadClassNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadClassNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadClassName',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadClassNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_class_name_with_options_async(
        self,
        request: main_models.ReadClassNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadClassNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadClassName',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadClassNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_class_name(
        self,
        request: main_models.ReadClassNameRequest,
    ) -> main_models.ReadClassNameResponse:
        runtime = RuntimeOptions()
        return self.read_class_name_with_options(request, runtime)

    async def read_class_name_async(
        self,
        request: main_models.ReadClassNameRequest,
    ) -> main_models.ReadClassNameResponse:
        runtime = RuntimeOptions()
        return await self.read_class_name_with_options_async(request, runtime)

    def read_common_contact_with_options(
        self,
        request: main_models.ReadCommonContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadCommonContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadCommonContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadCommonContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_common_contact_with_options_async(
        self,
        request: main_models.ReadCommonContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadCommonContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadCommonContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadCommonContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_common_contact(
        self,
        request: main_models.ReadCommonContactRequest,
    ) -> main_models.ReadCommonContactResponse:
        runtime = RuntimeOptions()
        return self.read_common_contact_with_options(request, runtime)

    async def read_common_contact_async(
        self,
        request: main_models.ReadCommonContactRequest,
    ) -> main_models.ReadCommonContactResponse:
        runtime = RuntimeOptions()
        return await self.read_common_contact_with_options_async(request, runtime)

    def read_marketing_preference_with_options(
        self,
        request: main_models.ReadMarketingPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMarketingPreferenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMarketingPreference',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMarketingPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_marketing_preference_with_options_async(
        self,
        request: main_models.ReadMarketingPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMarketingPreferenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMarketingPreference',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMarketingPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_marketing_preference(
        self,
        request: main_models.ReadMarketingPreferenceRequest,
    ) -> main_models.ReadMarketingPreferenceResponse:
        runtime = RuntimeOptions()
        return self.read_marketing_preference_with_options(request, runtime)

    async def read_marketing_preference_async(
        self,
        request: main_models.ReadMarketingPreferenceRequest,
    ) -> main_models.ReadMarketingPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.read_marketing_preference_with_options_async(request, runtime)

    def read_message_with_options(
        self,
        request: main_models.ReadMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_with_options_async(
        self,
        request: main_models.ReadMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.read_message_with_options(request, runtime)

    async def read_message_async(
        self,
        request: main_models.ReadMessageRequest,
    ) -> main_models.ReadMessageResponse:
        runtime = RuntimeOptions()
        return await self.read_message_with_options_async(request, runtime)

    def read_message_content_with_options(
        self,
        request: main_models.ReadMessageContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.history):
            body['History'] = request.history
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageContent',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_content_with_options_async(
        self,
        request: main_models.ReadMessageContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.history):
            body['History'] = request.history
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageContent',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message_content(
        self,
        request: main_models.ReadMessageContentRequest,
    ) -> main_models.ReadMessageContentResponse:
        runtime = RuntimeOptions()
        return self.read_message_content_with_options(request, runtime)

    async def read_message_content_async(
        self,
        request: main_models.ReadMessageContentRequest,
    ) -> main_models.ReadMessageContentResponse:
        runtime = RuntimeOptions()
        return await self.read_message_content_with_options_async(request, runtime)

    def read_message_language_with_options(
        self,
        request: main_models.ReadMessageLanguageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageLanguageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.return_default_lang):
            body['ReturnDefaultLang'] = request.return_default_lang
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageLanguage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageLanguageResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_language_with_options_async(
        self,
        request: main_models.ReadMessageLanguageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageLanguageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.return_default_lang):
            body['ReturnDefaultLang'] = request.return_default_lang
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageLanguage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageLanguageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message_language(
        self,
        request: main_models.ReadMessageLanguageRequest,
    ) -> main_models.ReadMessageLanguageResponse:
        runtime = RuntimeOptions()
        return self.read_message_language_with_options(request, runtime)

    async def read_message_language_async(
        self,
        request: main_models.ReadMessageLanguageRequest,
    ) -> main_models.ReadMessageLanguageResponse:
        runtime = RuntimeOptions()
        return await self.read_message_language_with_options_async(request, runtime)

    def read_message_list_with_options(
        self,
        request: main_models.ReadMessageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.history):
            body['History'] = request.history
        if not DaraCore.is_null(request.loc):
            body['Loc'] = request.loc
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_list_with_options_async(
        self,
        request: main_models.ReadMessageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.class_id):
            body['ClassId'] = request.class_id
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.history):
            body['History'] = request.history
        if not DaraCore.is_null(request.loc):
            body['Loc'] = request.loc
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message_list(
        self,
        request: main_models.ReadMessageListRequest,
    ) -> main_models.ReadMessageListResponse:
        runtime = RuntimeOptions()
        return self.read_message_list_with_options(request, runtime)

    async def read_message_list_async(
        self,
        request: main_models.ReadMessageListRequest,
    ) -> main_models.ReadMessageListResponse:
        runtime = RuntimeOptions()
        return await self.read_message_list_with_options_async(request, runtime)

    def read_message_new_total_with_options(
        self,
        request: main_models.ReadMessageNewTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageNewTotalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageNewTotal',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageNewTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_new_total_with_options_async(
        self,
        request: main_models.ReadMessageNewTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMessageNewTotalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMessageNewTotal',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMessageNewTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message_new_total(
        self,
        request: main_models.ReadMessageNewTotalRequest,
    ) -> main_models.ReadMessageNewTotalResponse:
        runtime = RuntimeOptions()
        return self.read_message_new_total_with_options(request, runtime)

    async def read_message_new_total_async(
        self,
        request: main_models.ReadMessageNewTotalRequest,
    ) -> main_models.ReadMessageNewTotalResponse:
        runtime = RuntimeOptions()
        return await self.read_message_new_total_with_options_async(request, runtime)

    def read_meta_config_with_options(
        self,
        request: main_models.ReadMetaConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMetaConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMetaConfig',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMetaConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_meta_config_with_options_async(
        self,
        request: main_models.ReadMetaConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadMetaConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadMetaConfig',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadMetaConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_meta_config(
        self,
        request: main_models.ReadMetaConfigRequest,
    ) -> main_models.ReadMetaConfigResponse:
        runtime = RuntimeOptions()
        return self.read_meta_config_with_options(request, runtime)

    async def read_meta_config_async(
        self,
        request: main_models.ReadMetaConfigRequest,
    ) -> main_models.ReadMetaConfigResponse:
        runtime = RuntimeOptions()
        return await self.read_meta_config_with_options_async(request, runtime)

    def read_num_group_by_class_with_options(
        self,
        request: main_models.ReadNumGroupByClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadNumGroupByClassResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadNumGroupByClass',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadNumGroupByClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_num_group_by_class_with_options_async(
        self,
        request: main_models.ReadNumGroupByClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadNumGroupByClassResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadNumGroupByClass',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadNumGroupByClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_num_group_by_class(
        self,
        request: main_models.ReadNumGroupByClassRequest,
    ) -> main_models.ReadNumGroupByClassResponse:
        runtime = RuntimeOptions()
        return self.read_num_group_by_class_with_options(request, runtime)

    async def read_num_group_by_class_async(
        self,
        request: main_models.ReadNumGroupByClassRequest,
    ) -> main_models.ReadNumGroupByClassResponse:
        runtime = RuntimeOptions()
        return await self.read_num_group_by_class_with_options_async(request, runtime)

    def read_num_group_total_with_options(
        self,
        request: main_models.ReadNumGroupTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadNumGroupTotalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadNumGroupTotal',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadNumGroupTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_num_group_total_with_options_async(
        self,
        request: main_models.ReadNumGroupTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadNumGroupTotalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadNumGroupTotal',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadNumGroupTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_num_group_total(
        self,
        request: main_models.ReadNumGroupTotalRequest,
    ) -> main_models.ReadNumGroupTotalResponse:
        runtime = RuntimeOptions()
        return self.read_num_group_total_with_options(request, runtime)

    async def read_num_group_total_async(
        self,
        request: main_models.ReadNumGroupTotalRequest,
    ) -> main_models.ReadNumGroupTotalResponse:
        runtime = RuntimeOptions()
        return await self.read_num_group_total_with_options_async(request, runtime)

    def read_revision_history_list_with_options(
        self,
        tmp_req: main_models.ReadRevisionHistoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadRevisionHistoryListResponse:
        tmp_req.validate()
        request = main_models.ReadRevisionHistoryListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page_info):
            request.page_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_info, 'PageInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.category_code):
            body['CategoryCode'] = request.category_code
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.page_info_shrink):
            body['PageInfo'] = request.page_info_shrink
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadRevisionHistoryList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadRevisionHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_revision_history_list_with_options_async(
        self,
        tmp_req: main_models.ReadRevisionHistoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadRevisionHistoryListResponse:
        tmp_req.validate()
        request = main_models.ReadRevisionHistoryListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page_info):
            request.page_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_info, 'PageInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.category_code):
            body['CategoryCode'] = request.category_code
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.page_info_shrink):
            body['PageInfo'] = request.page_info_shrink
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadRevisionHistoryList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadRevisionHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_revision_history_list(
        self,
        request: main_models.ReadRevisionHistoryListRequest,
    ) -> main_models.ReadRevisionHistoryListResponse:
        runtime = RuntimeOptions()
        return self.read_revision_history_list_with_options(request, runtime)

    async def read_revision_history_list_async(
        self,
        request: main_models.ReadRevisionHistoryListRequest,
    ) -> main_models.ReadRevisionHistoryListResponse:
        runtime = RuntimeOptions()
        return await self.read_revision_history_list_with_options_async(request, runtime)

    def read_user_subscription_list_with_options(
        self,
        request: main_models.ReadUserSubscriptionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadUserSubscriptionListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.category_group_code):
            body['CategoryGroupCode'] = request.category_group_code
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadUserSubscriptionList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadUserSubscriptionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_user_subscription_list_with_options_async(
        self,
        request: main_models.ReadUserSubscriptionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadUserSubscriptionListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.category_group_code):
            body['CategoryGroupCode'] = request.category_group_code
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadUserSubscriptionList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadUserSubscriptionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_user_subscription_list(
        self,
        request: main_models.ReadUserSubscriptionListRequest,
    ) -> main_models.ReadUserSubscriptionListResponse:
        runtime = RuntimeOptions()
        return self.read_user_subscription_list_with_options(request, runtime)

    async def read_user_subscription_list_async(
        self,
        request: main_models.ReadUserSubscriptionListRequest,
    ) -> main_models.ReadUserSubscriptionListResponse:
        runtime = RuntimeOptions()
        return await self.read_user_subscription_list_with_options_async(request, runtime)

    def read_webhook_contact_with_options(
        self,
        request: main_models.ReadWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_webhook_contact_with_options_async(
        self,
        request: main_models.ReadWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_webhook_contact(
        self,
        request: main_models.ReadWebhookContactRequest,
    ) -> main_models.ReadWebhookContactResponse:
        runtime = RuntimeOptions()
        return self.read_webhook_contact_with_options(request, runtime)

    async def read_webhook_contact_async(
        self,
        request: main_models.ReadWebhookContactRequest,
    ) -> main_models.ReadWebhookContactResponse:
        runtime = RuntimeOptions()
        return await self.read_webhook_contact_with_options_async(request, runtime)

    def read_webhook_contact_send_template_list_with_options(
        self,
        request: main_models.ReadWebhookContactSendTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadWebhookContactSendTemplateListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadWebhookContactSendTemplateList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadWebhookContactSendTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_webhook_contact_send_template_list_with_options_async(
        self,
        request: main_models.ReadWebhookContactSendTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadWebhookContactSendTemplateListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReadWebhookContactSendTemplateList',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadWebhookContactSendTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_webhook_contact_send_template_list(
        self,
        request: main_models.ReadWebhookContactSendTemplateListRequest,
    ) -> main_models.ReadWebhookContactSendTemplateListResponse:
        runtime = RuntimeOptions()
        return self.read_webhook_contact_send_template_list_with_options(request, runtime)

    async def read_webhook_contact_send_template_list_async(
        self,
        request: main_models.ReadWebhookContactSendTemplateListRequest,
    ) -> main_models.ReadWebhookContactSendTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.read_webhook_contact_send_template_list_with_options_async(request, runtime)

    def reset_user_subscription_with_options(
        self,
        tmp_req: main_models.ResetUserSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserSubscriptionResponse:
        tmp_req.validate()
        request = main_models.ResetUserSubscriptionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_codes):
            request.category_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_codes, 'CategoryCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.category_codes_shrink):
            body['CategoryCodes'] = request.category_codes_shrink
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.remarks):
            body['Remarks'] = request.remarks
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserSubscription',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_subscription_with_options_async(
        self,
        tmp_req: main_models.ResetUserSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserSubscriptionResponse:
        tmp_req.validate()
        request = main_models.ResetUserSubscriptionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_codes):
            request.category_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_codes, 'CategoryCodes', 'json')
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.category_codes_shrink):
            body['CategoryCodes'] = request.category_codes_shrink
        if not DaraCore.is_null(request.channel_group_code):
            body['ChannelGroupCode'] = request.channel_group_code
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.remarks):
            body['Remarks'] = request.remarks
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserSubscription',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_subscription(
        self,
        request: main_models.ResetUserSubscriptionRequest,
    ) -> main_models.ResetUserSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.reset_user_subscription_with_options(request, runtime)

    async def reset_user_subscription_async(
        self,
        request: main_models.ResetUserSubscriptionRequest,
    ) -> main_models.ResetUserSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.reset_user_subscription_with_options_async(request, runtime)

    def test_webhook_contact_with_options(
        self,
        request: main_models.TestWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.bot_security_token):
            body['BotSecurityToken'] = request.bot_security_token
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.server_url):
            body['ServerUrl'] = request.server_url
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        if not DaraCore.is_null(request.webhook_type):
            body['WebhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_webhook_contact_with_options_async(
        self,
        request: main_models.TestWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.bot_security_token):
            body['BotSecurityToken'] = request.bot_security_token
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.server_url):
            body['ServerUrl'] = request.server_url
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        if not DaraCore.is_null(request.webhook_type):
            body['WebhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_webhook_contact(
        self,
        request: main_models.TestWebhookContactRequest,
    ) -> main_models.TestWebhookContactResponse:
        runtime = RuntimeOptions()
        return self.test_webhook_contact_with_options(request, runtime)

    async def test_webhook_contact_async(
        self,
        request: main_models.TestWebhookContactRequest,
    ) -> main_models.TestWebhookContactResponse:
        runtime = RuntimeOptions()
        return await self.test_webhook_contact_with_options_async(request, runtime)

    def update_marketing_preference_with_options(
        self,
        request: main_models.UpdateMarketingPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMarketingPreferenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.allow_marketing):
            body['AllowMarketing'] = request.allow_marketing
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMarketingPreference',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMarketingPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_marketing_preference_with_options_async(
        self,
        request: main_models.UpdateMarketingPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMarketingPreferenceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.allow_marketing):
            body['AllowMarketing'] = request.allow_marketing
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMarketingPreference',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMarketingPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_marketing_preference(
        self,
        request: main_models.UpdateMarketingPreferenceRequest,
    ) -> main_models.UpdateMarketingPreferenceResponse:
        runtime = RuntimeOptions()
        return self.update_marketing_preference_with_options(request, runtime)

    async def update_marketing_preference_async(
        self,
        request: main_models.UpdateMarketingPreferenceRequest,
    ) -> main_models.UpdateMarketingPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.update_marketing_preference_with_options_async(request, runtime)

    def update_message_language_with_options(
        self,
        request: main_models.UpdateMessageLanguageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageLanguageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.prefer_lang):
            body['PreferLang'] = request.prefer_lang
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageLanguage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageLanguageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_message_language_with_options_async(
        self,
        request: main_models.UpdateMessageLanguageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageLanguageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.prefer_lang):
            body['PreferLang'] = request.prefer_lang
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageLanguage',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageLanguageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_message_language(
        self,
        request: main_models.UpdateMessageLanguageRequest,
    ) -> main_models.UpdateMessageLanguageResponse:
        runtime = RuntimeOptions()
        return self.update_message_language_with_options(request, runtime)

    async def update_message_language_async(
        self,
        request: main_models.UpdateMessageLanguageRequest,
    ) -> main_models.UpdateMessageLanguageResponse:
        runtime = RuntimeOptions()
        return await self.update_message_language_with_options_async(request, runtime)

    def update_webhook_contact_with_options(
        self,
        request: main_models.UpdateWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.bot_security_token):
            body['BotSecurityToken'] = request.bot_security_token
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.server_url):
            body['ServerUrl'] = request.server_url
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        if not DaraCore.is_null(request.verification_code):
            body['VerificationCode'] = request.verification_code
        if not DaraCore.is_null(request.webhook_type):
            body['WebhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_webhook_contact_with_options_async(
        self,
        request: main_models.UpdateWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_name):
            body['BizName'] = request.biz_name
        if not DaraCore.is_null(request.bot_security_token):
            body['BotSecurityToken'] = request.bot_security_token
        if not DaraCore.is_null(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not DaraCore.is_null(request.client_source):
            body['ClientSource'] = request.client_source
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.cookies):
            body['Cookies'] = request.cookies
        if not DaraCore.is_null(request.security_token):
            body['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.server_url):
            body['ServerUrl'] = request.server_url
        if not DaraCore.is_null(request.src_url):
            body['SrcUrl'] = request.src_url
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not DaraCore.is_null(request.uid_type):
            body['UidType'] = request.uid_type
        if not DaraCore.is_null(request.verification_code):
            body['VerificationCode'] = request.verification_code
        if not DaraCore.is_null(request.webhook_type):
            body['WebhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebhookContact',
            version = '2024-12-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_webhook_contact(
        self,
        request: main_models.UpdateWebhookContactRequest,
    ) -> main_models.UpdateWebhookContactResponse:
        runtime = RuntimeOptions()
        return self.update_webhook_contact_with_options(request, runtime)

    async def update_webhook_contact_async(
        self,
        request: main_models.UpdateWebhookContactRequest,
    ) -> main_models.UpdateWebhookContactResponse:
        runtime = RuntimeOptions()
        return await self.update_webhook_contact_with_options_async(request, runtime)
