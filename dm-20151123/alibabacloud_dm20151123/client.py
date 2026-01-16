# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dm20151123 import models as main_models
from alibabacloud_tea_openapi import exceptions as open_api_exceptions
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore
from darabonba.core import DaraCore as DaraCore
from darabonba.exceptions import UnretryableException
from darabonba.policy.retry import RetryPolicyContext
from darabonba.request import DaraRequest
from darabonba.runtime import RuntimeOptions
from darabonba.utils.form import FileField
from darabonba.utils.form import Form as DaraForm
from darabonba.utils.stream import Stream as DaraStream
from darabonba.utils.xml import XML as DaraXML

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
        self._endpoint = self.get_endpoint('dm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def _post_ossobject(
        self,
        bucket_name: str,
        form: dict,
        runtime: RuntimeOptions,
    ) -> dict:
        _runtime = {
            'key': runtime.key or self._key,
            'cert': runtime.cert or self._cert,
            'ca': runtime.ca or self._ca,
            'readTimeout': DaraCore.to_number(runtime.read_timeout or self._read_timeout),
            'connectTimeout': DaraCore.to_number(runtime.connect_timeout or self._connect_timeout),
            'httpProxy': runtime.http_proxy or self._http_proxy,
            'httpsProxy': runtime.https_proxy or self._https_proxy,
            'noProxy': runtime.no_proxy or self._no_proxy,
            'socks5Proxy': runtime.socks_5proxy or self._socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work or self._socks_5net_work,
            'maxIdleConns': DaraCore.to_number(runtime.max_idle_conns or self._max_idle_conns),
            'retryOptions': self._retry_options,
            'ignoreSSL': bool(runtime.ignore_ssl or False),
            'tlsMinVersion': self._tls_min_version,
        }
        _last_request = None
        _last_response = None
        _retries_attempted = 0
        _context = RetryPolicyContext(
            retries_attempted= _retries_attempted
        )
        while DaraCore.should_retry(_runtime.get('retryOptions'), _context):
            if _retries_attempted > 0:
                _backoff_time = DaraCore.get_backoff_time(_runtime.get('retryOptions'), _context)
                if _backoff_time > 0:
                    DaraCore.sleep(_backoff_time)
            _retries_attempted = _retries_attempted + 1
            try:
                _request = DaraRequest()
                boundary = DaraForm.get_boundary()
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': str(form.get("host")),
                    'date': Utils.get_date_utcstring(),
                    'user-agent': Utils.get_user_agent('')
                }
                _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
                _request.body = DaraForm.to_file_form(form, boundary)
                _last_request = _request
                _response = DaraCore.do_action(_request, _runtime)
                _last_response = _response
                resp_map = None
                body_str = DaraStream.read_as_string(_response.body)
                if (_response.status_code >= 400) and (_response.status_code < 600):
                    resp_map = DaraXML.parse_xml(body_str, None)
                    err = resp_map.get("Error")
                    raise open_api_exceptions.ClientException(
                        code = str(err.get("Code")),
                        message = str(err.get("Message")),
                        data = {
                            'httpCode': _response.status_code,
                            'requestId': str(err.get("RequestId")),
                            'hostId': str(err.get("HostId"))
                        }
                    )
                resp_map = DaraXML.parse_xml(body_str, None)
                return DaraCore.merge({}, resp_map)
            except Exception as e:
                _context = RetryPolicyContext(
                    retries_attempted= _retries_attempted,
                    http_request = _last_request,
                    http_response = _last_response,
                    exception = e
                )
                continue
        raise UnretryableException(_context)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        form: dict,
        runtime: RuntimeOptions,
    ) -> dict:
        _runtime = {
            'key': runtime.key or self._key,
            'cert': runtime.cert or self._cert,
            'ca': runtime.ca or self._ca,
            'readTimeout': DaraCore.to_number(runtime.read_timeout or self._read_timeout),
            'connectTimeout': DaraCore.to_number(runtime.connect_timeout or self._connect_timeout),
            'httpProxy': runtime.http_proxy or self._http_proxy,
            'httpsProxy': runtime.https_proxy or self._https_proxy,
            'noProxy': runtime.no_proxy or self._no_proxy,
            'socks5Proxy': runtime.socks_5proxy or self._socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work or self._socks_5net_work,
            'maxIdleConns': DaraCore.to_number(runtime.max_idle_conns or self._max_idle_conns),
            'retryOptions': self._retry_options,
            'ignoreSSL': bool(runtime.ignore_ssl or False),
            'tlsMinVersion': self._tls_min_version,
        }
        _last_request = None
        _last_response = None
        _retries_attempted = 0
        _context = RetryPolicyContext(
            retries_attempted= _retries_attempted
        )
        while DaraCore.should_retry(_runtime.get('retryOptions'), _context):
            if _retries_attempted > 0:
                _backoff_time = DaraCore.get_backoff_time(_runtime.get('retryOptions'), _context)
                if _backoff_time > 0:
                    DaraCore.sleep(_backoff_time)
            _retries_attempted = _retries_attempted + 1
            try:
                _request = DaraRequest()
                boundary = DaraForm.get_boundary()
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': str(form.get("host")),
                    'date': Utils.get_date_utcstring(),
                    'user-agent': Utils.get_user_agent('')
                }
                _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
                _request.body = DaraForm.to_file_form(form, boundary)
                _last_request = _request
                _response = await DaraCore.async_do_action(_request, _runtime)
                _last_response = _response
                resp_map = None
                body_str = await DaraStream.read_as_string_async(_response.body)
                if (_response.status_code >= 400) and (_response.status_code < 600):
                    resp_map = DaraXML.parse_xml(body_str, None)
                    err = resp_map.get("Error")
                    raise open_api_exceptions.ClientException(
                        code = str(err.get("Code")),
                        message = str(err.get("Message")),
                        data = {
                            'httpCode': _response.status_code,
                            'requestId': str(err.get("RequestId")),
                            'hostId': str(err.get("HostId"))
                        }
                    )
                resp_map = DaraXML.parse_xml(body_str, None)
                return DaraCore.merge({}, resp_map)
            except Exception as e:
                _context = RetryPolicyContext(
                    retries_attempted= _retries_attempted,
                    http_request = _last_request,
                    http_response = _last_response,
                    exception = e
                )
                continue
        raise UnretryableException(_context)

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

    def add_ipfilter_with_options(
        self,
        request: main_models.AddIpfilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpfilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_address):
            query['IpAddress'] = request.ip_address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpfilter',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpfilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ipfilter_with_options_async(
        self,
        request: main_models.AddIpfilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpfilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_address):
            query['IpAddress'] = request.ip_address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpfilter',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpfilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ipfilter(
        self,
        request: main_models.AddIpfilterRequest,
    ) -> main_models.AddIpfilterResponse:
        runtime = RuntimeOptions()
        return self.add_ipfilter_with_options(request, runtime)

    async def add_ipfilter_async(
        self,
        request: main_models.AddIpfilterRequest,
    ) -> main_models.AddIpfilterResponse:
        runtime = RuntimeOptions()
        return await self.add_ipfilter_with_options_async(request, runtime)

    def approve_reply_mail_address_with_options(
        self,
        request: main_models.ApproveReplyMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveReplyMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApproveReplyMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveReplyMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_reply_mail_address_with_options_async(
        self,
        request: main_models.ApproveReplyMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveReplyMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApproveReplyMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveReplyMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_reply_mail_address(
        self,
        request: main_models.ApproveReplyMailAddressRequest,
    ) -> main_models.ApproveReplyMailAddressResponse:
        runtime = RuntimeOptions()
        return self.approve_reply_mail_address_with_options(request, runtime)

    async def approve_reply_mail_address_async(
        self,
        request: main_models.ApproveReplyMailAddressRequest,
    ) -> main_models.ApproveReplyMailAddressResponse:
        runtime = RuntimeOptions()
        return await self.approve_reply_mail_address_with_options_async(request, runtime)

    def batch_send_mail_with_options(
        self,
        request: main_models.BatchSendMailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSendMailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.click_trace):
            query['ClickTrace'] = request.click_trace
        if not DaraCore.is_null(request.domain_auth):
            query['DomainAuth'] = request.domain_auth
        if not DaraCore.is_null(request.headers):
            query['Headers'] = request.headers
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not DaraCore.is_null(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.reply_address_alias):
            query['ReplyAddressAlias'] = request.reply_address_alias
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.un_subscribe_filter_level):
            query['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not DaraCore.is_null(request.un_subscribe_link_type):
            query['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSendMail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSendMailResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_send_mail_with_options_async(
        self,
        request: main_models.BatchSendMailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSendMailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.click_trace):
            query['ClickTrace'] = request.click_trace
        if not DaraCore.is_null(request.domain_auth):
            query['DomainAuth'] = request.domain_auth
        if not DaraCore.is_null(request.headers):
            query['Headers'] = request.headers
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not DaraCore.is_null(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.reply_address_alias):
            query['ReplyAddressAlias'] = request.reply_address_alias
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.un_subscribe_filter_level):
            query['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not DaraCore.is_null(request.un_subscribe_link_type):
            query['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSendMail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSendMailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_send_mail(
        self,
        request: main_models.BatchSendMailRequest,
    ) -> main_models.BatchSendMailResponse:
        runtime = RuntimeOptions()
        return self.batch_send_mail_with_options(request, runtime)

    async def batch_send_mail_async(
        self,
        request: main_models.BatchSendMailRequest,
    ) -> main_models.BatchSendMailResponse:
        runtime = RuntimeOptions()
        return await self.batch_send_mail_with_options_async(request, runtime)

    def change_domain_dkim_record_with_options(
        self,
        request: main_models.ChangeDomainDkimRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDomainDkimRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dkim_rsa_length):
            query['DkimRsaLength'] = request.dkim_rsa_length
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDomainDkimRecord',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDomainDkimRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_domain_dkim_record_with_options_async(
        self,
        request: main_models.ChangeDomainDkimRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDomainDkimRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dkim_rsa_length):
            query['DkimRsaLength'] = request.dkim_rsa_length
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDomainDkimRecord',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDomainDkimRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_domain_dkim_record(
        self,
        request: main_models.ChangeDomainDkimRecordRequest,
    ) -> main_models.ChangeDomainDkimRecordResponse:
        runtime = RuntimeOptions()
        return self.change_domain_dkim_record_with_options(request, runtime)

    async def change_domain_dkim_record_async(
        self,
        request: main_models.ChangeDomainDkimRecordRequest,
    ) -> main_models.ChangeDomainDkimRecordResponse:
        runtime = RuntimeOptions()
        return await self.change_domain_dkim_record_with_options_async(request, runtime)

    def check_disposable_with_options(
        self,
        request: main_models.CheckDisposableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDisposableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDisposable',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDisposableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_disposable_with_options_async(
        self,
        request: main_models.CheckDisposableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDisposableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDisposable',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDisposableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_disposable(
        self,
        request: main_models.CheckDisposableRequest,
    ) -> main_models.CheckDisposableResponse:
        runtime = RuntimeOptions()
        return self.check_disposable_with_options(request, runtime)

    async def check_disposable_async(
        self,
        request: main_models.CheckDisposableRequest,
    ) -> main_models.CheckDisposableResponse:
        runtime = RuntimeOptions()
        return await self.check_disposable_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: main_models.CheckDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: main_models.CheckDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain(
        self,
        request: main_models.CheckDomainRequest,
    ) -> main_models.CheckDomainResponse:
        runtime = RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: main_models.CheckDomainRequest,
    ) -> main_models.CheckDomainResponse:
        runtime = RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def check_reply_to_mail_address_with_options(
        self,
        request: main_models.CheckReplyToMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckReplyToMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckReplyToMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckReplyToMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_reply_to_mail_address_with_options_async(
        self,
        request: main_models.CheckReplyToMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckReplyToMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckReplyToMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckReplyToMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_reply_to_mail_address(
        self,
        request: main_models.CheckReplyToMailAddressRequest,
    ) -> main_models.CheckReplyToMailAddressResponse:
        runtime = RuntimeOptions()
        return self.check_reply_to_mail_address_with_options(request, runtime)

    async def check_reply_to_mail_address_async(
        self,
        request: main_models.CheckReplyToMailAddressRequest,
    ) -> main_models.CheckReplyToMailAddressResponse:
        runtime = RuntimeOptions()
        return await self.check_reply_to_mail_address_with_options_async(request, runtime)

    def config_set_cancel_relation_from_address_with_options(
        self,
        request: main_models.ConfigSetCancelRelationFromAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetCancelRelationFromAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_address):
            query['FromAddress'] = request.from_address
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetCancelRelationFromAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetCancelRelationFromAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_cancel_relation_from_address_with_options_async(
        self,
        request: main_models.ConfigSetCancelRelationFromAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetCancelRelationFromAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_address):
            query['FromAddress'] = request.from_address
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetCancelRelationFromAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetCancelRelationFromAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_cancel_relation_from_address(
        self,
        request: main_models.ConfigSetCancelRelationFromAddressRequest,
    ) -> main_models.ConfigSetCancelRelationFromAddressResponse:
        runtime = RuntimeOptions()
        return self.config_set_cancel_relation_from_address_with_options(request, runtime)

    async def config_set_cancel_relation_from_address_async(
        self,
        request: main_models.ConfigSetCancelRelationFromAddressRequest,
    ) -> main_models.ConfigSetCancelRelationFromAddressResponse:
        runtime = RuntimeOptions()
        return await self.config_set_cancel_relation_from_address_with_options_async(request, runtime)

    def config_set_create_with_options(
        self,
        request: main_models.ConfigSetCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetCreate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_create_with_options_async(
        self,
        request: main_models.ConfigSetCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetCreate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_create(
        self,
        request: main_models.ConfigSetCreateRequest,
    ) -> main_models.ConfigSetCreateResponse:
        runtime = RuntimeOptions()
        return self.config_set_create_with_options(request, runtime)

    async def config_set_create_async(
        self,
        request: main_models.ConfigSetCreateRequest,
    ) -> main_models.ConfigSetCreateResponse:
        runtime = RuntimeOptions()
        return await self.config_set_create_with_options_async(request, runtime)

    def config_set_delete_with_options(
        self,
        request: main_models.ConfigSetDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.is_force):
            query['IsForce'] = request.is_force
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetDelete',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_delete_with_options_async(
        self,
        request: main_models.ConfigSetDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.is_force):
            query['IsForce'] = request.is_force
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetDelete',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_delete(
        self,
        request: main_models.ConfigSetDeleteRequest,
    ) -> main_models.ConfigSetDeleteResponse:
        runtime = RuntimeOptions()
        return self.config_set_delete_with_options(request, runtime)

    async def config_set_delete_async(
        self,
        request: main_models.ConfigSetDeleteRequest,
    ) -> main_models.ConfigSetDeleteResponse:
        runtime = RuntimeOptions()
        return await self.config_set_delete_with_options_async(request, runtime)

    def config_set_detail_with_options(
        self,
        request: main_models.ConfigSetDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_detail_with_options_async(
        self,
        request: main_models.ConfigSetDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_detail(
        self,
        request: main_models.ConfigSetDetailRequest,
    ) -> main_models.ConfigSetDetailResponse:
        runtime = RuntimeOptions()
        return self.config_set_detail_with_options(request, runtime)

    async def config_set_detail_async(
        self,
        request: main_models.ConfigSetDetailRequest,
    ) -> main_models.ConfigSetDetailResponse:
        runtime = RuntimeOptions()
        return await self.config_set_detail_with_options_async(request, runtime)

    def config_set_list_with_options(
        self,
        request: main_models.ConfigSetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_list_with_options_async(
        self,
        request: main_models.ConfigSetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_list(
        self,
        request: main_models.ConfigSetListRequest,
    ) -> main_models.ConfigSetListResponse:
        runtime = RuntimeOptions()
        return self.config_set_list_with_options(request, runtime)

    async def config_set_list_async(
        self,
        request: main_models.ConfigSetListRequest,
    ) -> main_models.ConfigSetListResponse:
        runtime = RuntimeOptions()
        return await self.config_set_list_with_options_async(request, runtime)

    def config_set_relation_from_address_with_options(
        self,
        request: main_models.ConfigSetRelationFromAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetRelationFromAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_address):
            query['FromAddress'] = request.from_address
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetRelationFromAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetRelationFromAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_relation_from_address_with_options_async(
        self,
        request: main_models.ConfigSetRelationFromAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetRelationFromAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_address):
            query['FromAddress'] = request.from_address
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetRelationFromAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetRelationFromAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_relation_from_address(
        self,
        request: main_models.ConfigSetRelationFromAddressRequest,
    ) -> main_models.ConfigSetRelationFromAddressResponse:
        runtime = RuntimeOptions()
        return self.config_set_relation_from_address_with_options(request, runtime)

    async def config_set_relation_from_address_async(
        self,
        request: main_models.ConfigSetRelationFromAddressRequest,
    ) -> main_models.ConfigSetRelationFromAddressResponse:
        runtime = RuntimeOptions()
        return await self.config_set_relation_from_address_with_options_async(request, runtime)

    def config_set_update_with_options(
        self,
        request: main_models.ConfigSetUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetUpdate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_set_update_with_options_async(
        self,
        request: main_models.ConfigSetUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigSetUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigSetUpdate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigSetUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_set_update(
        self,
        request: main_models.ConfigSetUpdateRequest,
    ) -> main_models.ConfigSetUpdateResponse:
        runtime = RuntimeOptions()
        return self.config_set_update_with_options(request, runtime)

    async def config_set_update_async(
        self,
        request: main_models.ConfigSetUpdateRequest,
    ) -> main_models.ConfigSetUpdateResponse:
        runtime = RuntimeOptions()
        return await self.config_set_update_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.dkim_selector):
            query['dkimSelector'] = request.dkim_selector
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.dkim_selector):
            query['dkimSelector'] = request.dkim_selector
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_mail_address_with_options(
        self,
        request: main_models.CreateMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mail_address_with_options_async(
        self,
        request: main_models.CreateMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mail_address(
        self,
        request: main_models.CreateMailAddressRequest,
    ) -> main_models.CreateMailAddressResponse:
        runtime = RuntimeOptions()
        return self.create_mail_address_with_options(request, runtime)

    async def create_mail_address_async(
        self,
        request: main_models.CreateMailAddressRequest,
    ) -> main_models.CreateMailAddressResponse:
        runtime = RuntimeOptions()
        return await self.create_mail_address_with_options_async(request, runtime)

    def create_receiver_with_options(
        self,
        request: main_models.CreateReceiverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReceiverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receivers_alias):
            query['ReceiversAlias'] = request.receivers_alias
        if not DaraCore.is_null(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateReceiver',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_receiver_with_options_async(
        self,
        request: main_models.CreateReceiverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReceiverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receivers_alias):
            query['ReceiversAlias'] = request.receivers_alias
        if not DaraCore.is_null(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateReceiver',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_receiver(
        self,
        request: main_models.CreateReceiverRequest,
    ) -> main_models.CreateReceiverResponse:
        runtime = RuntimeOptions()
        return self.create_receiver_with_options(request, runtime)

    async def create_receiver_async(
        self,
        request: main_models.CreateReceiverRequest,
    ) -> main_models.CreateReceiverResponse:
        runtime = RuntimeOptions()
        return await self.create_receiver_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: main_models.CreateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: main_models.CreateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_user_suppression_with_options(
        self,
        request: main_models.CreateUserSuppressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserSuppressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserSuppression',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserSuppressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_suppression_with_options_async(
        self,
        request: main_models.CreateUserSuppressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserSuppressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserSuppression',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserSuppressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_suppression(
        self,
        request: main_models.CreateUserSuppressionRequest,
    ) -> main_models.CreateUserSuppressionResponse:
        runtime = RuntimeOptions()
        return self.create_user_suppression_with_options(request, runtime)

    async def create_user_suppression_async(
        self,
        request: main_models.CreateUserSuppressionRequest,
    ) -> main_models.CreateUserSuppressionResponse:
        runtime = RuntimeOptions()
        return await self.create_user_suppression_with_options_async(request, runtime)

    def dedicated_ip_auto_renewal_with_options(
        self,
        request: main_models.DedicatedIpAutoRenewalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpAutoRenewalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpAutoRenewal',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpAutoRenewalResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_auto_renewal_with_options_async(
        self,
        request: main_models.DedicatedIpAutoRenewalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpAutoRenewalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renewal):
            query['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpAutoRenewal',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpAutoRenewalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_auto_renewal(
        self,
        request: main_models.DedicatedIpAutoRenewalRequest,
    ) -> main_models.DedicatedIpAutoRenewalResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_auto_renewal_with_options(request, runtime)

    async def dedicated_ip_auto_renewal_async(
        self,
        request: main_models.DedicatedIpAutoRenewalRequest,
    ) -> main_models.DedicatedIpAutoRenewalResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_auto_renewal_with_options_async(request, runtime)

    def dedicated_ip_change_warmup_type_with_options(
        self,
        request: main_models.DedicatedIpChangeWarmupTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpChangeWarmupTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.warmup_type):
            query['WarmupType'] = request.warmup_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpChangeWarmupType',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpChangeWarmupTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_change_warmup_type_with_options_async(
        self,
        request: main_models.DedicatedIpChangeWarmupTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpChangeWarmupTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.warmup_type):
            query['WarmupType'] = request.warmup_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpChangeWarmupType',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpChangeWarmupTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_change_warmup_type(
        self,
        request: main_models.DedicatedIpChangeWarmupTypeRequest,
    ) -> main_models.DedicatedIpChangeWarmupTypeResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_change_warmup_type_with_options(request, runtime)

    async def dedicated_ip_change_warmup_type_async(
        self,
        request: main_models.DedicatedIpChangeWarmupTypeRequest,
    ) -> main_models.DedicatedIpChangeWarmupTypeResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_change_warmup_type_with_options_async(request, runtime)

    def dedicated_ip_list_with_options(
        self,
        request: main_models.DedicatedIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_list_with_options_async(
        self,
        request: main_models.DedicatedIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_list(
        self,
        request: main_models.DedicatedIpListRequest,
    ) -> main_models.DedicatedIpListResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_list_with_options(request, runtime)

    async def dedicated_ip_list_async(
        self,
        request: main_models.DedicatedIpListRequest,
    ) -> main_models.DedicatedIpListResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_list_with_options_async(request, runtime)

    def dedicated_ip_none_pool_list_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpNonePoolListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DedicatedIpNonePoolList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpNonePoolListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_none_pool_list_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpNonePoolListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DedicatedIpNonePoolList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpNonePoolListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_none_pool_list(self) -> main_models.DedicatedIpNonePoolListResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_none_pool_list_with_options(runtime)

    async def dedicated_ip_none_pool_list_async(self) -> main_models.DedicatedIpNonePoolListResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_none_pool_list_with_options_async(runtime)

    def dedicated_ip_pool_create_with_options(
        self,
        request: main_models.DedicatedIpPoolCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolCreate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_create_with_options_async(
        self,
        request: main_models.DedicatedIpPoolCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolCreate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_create(
        self,
        request: main_models.DedicatedIpPoolCreateRequest,
    ) -> main_models.DedicatedIpPoolCreateResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_pool_create_with_options(request, runtime)

    async def dedicated_ip_pool_create_async(
        self,
        request: main_models.DedicatedIpPoolCreateRequest,
    ) -> main_models.DedicatedIpPoolCreateResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_pool_create_with_options_async(request, runtime)

    def dedicated_ip_pool_delete_with_options(
        self,
        request: main_models.DedicatedIpPoolDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolDelete',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_delete_with_options_async(
        self,
        request: main_models.DedicatedIpPoolDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolDelete',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_delete(
        self,
        request: main_models.DedicatedIpPoolDeleteRequest,
    ) -> main_models.DedicatedIpPoolDeleteResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_pool_delete_with_options(request, runtime)

    async def dedicated_ip_pool_delete_async(
        self,
        request: main_models.DedicatedIpPoolDeleteRequest,
    ) -> main_models.DedicatedIpPoolDeleteResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_pool_delete_with_options_async(request, runtime)

    def dedicated_ip_pool_list_with_options(
        self,
        request: main_models.DedicatedIpPoolListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_list_with_options_async(
        self,
        request: main_models.DedicatedIpPoolListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_list(
        self,
        request: main_models.DedicatedIpPoolListRequest,
    ) -> main_models.DedicatedIpPoolListResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_pool_list_with_options(request, runtime)

    async def dedicated_ip_pool_list_async(
        self,
        request: main_models.DedicatedIpPoolListRequest,
    ) -> main_models.DedicatedIpPoolListResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_pool_list_with_options_async(request, runtime)

    def dedicated_ip_pool_update_with_options(
        self,
        request: main_models.DedicatedIpPoolUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.update_resource):
            query['UpdateResource'] = request.update_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolUpdate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def dedicated_ip_pool_update_with_options_async(
        self,
        request: main_models.DedicatedIpPoolUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DedicatedIpPoolUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_resource_ids):
            query['BuyResourceIds'] = request.buy_resource_ids
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.update_resource):
            query['UpdateResource'] = request.update_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DedicatedIpPoolUpdate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DedicatedIpPoolUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dedicated_ip_pool_update(
        self,
        request: main_models.DedicatedIpPoolUpdateRequest,
    ) -> main_models.DedicatedIpPoolUpdateResponse:
        runtime = RuntimeOptions()
        return self.dedicated_ip_pool_update_with_options(request, runtime)

    async def dedicated_ip_pool_update_async(
        self,
        request: main_models.DedicatedIpPoolUpdateRequest,
    ) -> main_models.DedicatedIpPoolUpdateResponse:
        runtime = RuntimeOptions()
        return await self.dedicated_ip_pool_update_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_invalid_address_with_options(
        self,
        request: main_models.DeleteInvalidAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInvalidAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInvalidAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInvalidAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_invalid_address_with_options_async(
        self,
        request: main_models.DeleteInvalidAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInvalidAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInvalidAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInvalidAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_invalid_address(
        self,
        request: main_models.DeleteInvalidAddressRequest,
    ) -> main_models.DeleteInvalidAddressResponse:
        runtime = RuntimeOptions()
        return self.delete_invalid_address_with_options(request, runtime)

    async def delete_invalid_address_async(
        self,
        request: main_models.DeleteInvalidAddressRequest,
    ) -> main_models.DeleteInvalidAddressResponse:
        runtime = RuntimeOptions()
        return await self.delete_invalid_address_with_options_async(request, runtime)

    def delete_ipfilter_by_edm_id_with_options(
        self,
        request: main_models.DeleteIpfilterByEdmIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpfilterByEdmIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_type):
            query['FromType'] = request.from_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpfilterByEdmId',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpfilterByEdmIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipfilter_by_edm_id_with_options_async(
        self,
        request: main_models.DeleteIpfilterByEdmIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpfilterByEdmIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_type):
            query['FromType'] = request.from_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpfilterByEdmId',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpfilterByEdmIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipfilter_by_edm_id(
        self,
        request: main_models.DeleteIpfilterByEdmIdRequest,
    ) -> main_models.DeleteIpfilterByEdmIdResponse:
        runtime = RuntimeOptions()
        return self.delete_ipfilter_by_edm_id_with_options(request, runtime)

    async def delete_ipfilter_by_edm_id_async(
        self,
        request: main_models.DeleteIpfilterByEdmIdRequest,
    ) -> main_models.DeleteIpfilterByEdmIdResponse:
        runtime = RuntimeOptions()
        return await self.delete_ipfilter_by_edm_id_with_options_async(request, runtime)

    def delete_mail_address_with_options(
        self,
        request: main_models.DeleteMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mail_address_with_options_async(
        self,
        request: main_models.DeleteMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mail_address(
        self,
        request: main_models.DeleteMailAddressRequest,
    ) -> main_models.DeleteMailAddressResponse:
        runtime = RuntimeOptions()
        return self.delete_mail_address_with_options(request, runtime)

    async def delete_mail_address_async(
        self,
        request: main_models.DeleteMailAddressRequest,
    ) -> main_models.DeleteMailAddressResponse:
        runtime = RuntimeOptions()
        return await self.delete_mail_address_with_options_async(request, runtime)

    def delete_receiver_with_options(
        self,
        request: main_models.DeleteReceiverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReceiverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReceiver',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_receiver_with_options_async(
        self,
        request: main_models.DeleteReceiverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReceiverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReceiver',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_receiver(
        self,
        request: main_models.DeleteReceiverRequest,
    ) -> main_models.DeleteReceiverResponse:
        runtime = RuntimeOptions()
        return self.delete_receiver_with_options(request, runtime)

    async def delete_receiver_async(
        self,
        request: main_models.DeleteReceiverRequest,
    ) -> main_models.DeleteReceiverResponse:
        runtime = RuntimeOptions()
        return await self.delete_receiver_with_options_async(request, runtime)

    def delete_receiver_detail_with_options(
        self,
        request: main_models.DeleteReceiverDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReceiverDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReceiverDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_receiver_detail_with_options_async(
        self,
        request: main_models.DeleteReceiverDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReceiverDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReceiverDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReceiverDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_receiver_detail(
        self,
        request: main_models.DeleteReceiverDetailRequest,
    ) -> main_models.DeleteReceiverDetailResponse:
        runtime = RuntimeOptions()
        return self.delete_receiver_detail_with_options(request, runtime)

    async def delete_receiver_detail_async(
        self,
        request: main_models.DeleteReceiverDetailRequest,
    ) -> main_models.DeleteReceiverDetailResponse:
        runtime = RuntimeOptions()
        return await self.delete_receiver_detail_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: main_models.DeleteTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: main_models.DeleteTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def delete_validate_file_with_options(
        self,
        request: main_models.DeleteValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteValidateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_validate_file_with_options_async(
        self,
        request: main_models.DeleteValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteValidateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_validate_file(
        self,
        request: main_models.DeleteValidateFileRequest,
    ) -> main_models.DeleteValidateFileResponse:
        runtime = RuntimeOptions()
        return self.delete_validate_file_with_options(request, runtime)

    async def delete_validate_file_async(
        self,
        request: main_models.DeleteValidateFileRequest,
    ) -> main_models.DeleteValidateFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_validate_file_with_options_async(request, runtime)

    def desc_account_summary_with_options(
        self,
        request: main_models.DescAccountSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescAccountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescAccountSummary',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def desc_account_summary_with_options_async(
        self,
        request: main_models.DescAccountSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescAccountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescAccountSummary',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescAccountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def desc_account_summary(
        self,
        request: main_models.DescAccountSummaryRequest,
    ) -> main_models.DescAccountSummaryResponse:
        runtime = RuntimeOptions()
        return self.desc_account_summary_with_options(request, runtime)

    async def desc_account_summary_async(
        self,
        request: main_models.DescAccountSummaryRequest,
    ) -> main_models.DescAccountSummaryResponse:
        runtime = RuntimeOptions()
        return await self.desc_account_summary_with_options_async(request, runtime)

    def desc_domain_with_options(
        self,
        request: main_models.DescDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.require_real_time_dns_records):
            query['RequireRealTimeDnsRecords'] = request.require_real_time_dns_records
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def desc_domain_with_options_async(
        self,
        request: main_models.DescDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.require_real_time_dns_records):
            query['RequireRealTimeDnsRecords'] = request.require_real_time_dns_records
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def desc_domain(
        self,
        request: main_models.DescDomainRequest,
    ) -> main_models.DescDomainResponse:
        runtime = RuntimeOptions()
        return self.desc_domain_with_options(request, runtime)

    async def desc_domain_async(
        self,
        request: main_models.DescDomainRequest,
    ) -> main_models.DescDomainResponse:
        runtime = RuntimeOptions()
        return await self.desc_domain_with_options_async(request, runtime)

    def desc_template_with_options(
        self,
        request: main_models.DescTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_type):
            query['FromType'] = request.from_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescTemplate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def desc_template_with_options_async(
        self,
        request: main_models.DescTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_type):
            query['FromType'] = request.from_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescTemplate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def desc_template(
        self,
        request: main_models.DescTemplateRequest,
    ) -> main_models.DescTemplateResponse:
        runtime = RuntimeOptions()
        return self.desc_template_with_options(request, runtime)

    async def desc_template_async(
        self,
        request: main_models.DescTemplateRequest,
    ) -> main_models.DescTemplateResponse:
        runtime = RuntimeOptions()
        return await self.desc_template_with_options_async(request, runtime)

    def get_dedicated_ip_warm_up_detail_with_options(
        self,
        request: main_models.GetDedicatedIpWarmUpDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDedicatedIpWarmUpDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.end_day_mark):
            query['EndDayMark'] = request.end_day_mark
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.start_day_mark):
            query['StartDayMark'] = request.start_day_mark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDedicatedIpWarmUpDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDedicatedIpWarmUpDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dedicated_ip_warm_up_detail_with_options_async(
        self,
        request: main_models.GetDedicatedIpWarmUpDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDedicatedIpWarmUpDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.end_day_mark):
            query['EndDayMark'] = request.end_day_mark
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.start_day_mark):
            query['StartDayMark'] = request.start_day_mark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDedicatedIpWarmUpDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDedicatedIpWarmUpDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dedicated_ip_warm_up_detail(
        self,
        request: main_models.GetDedicatedIpWarmUpDetailRequest,
    ) -> main_models.GetDedicatedIpWarmUpDetailResponse:
        runtime = RuntimeOptions()
        return self.get_dedicated_ip_warm_up_detail_with_options(request, runtime)

    async def get_dedicated_ip_warm_up_detail_async(
        self,
        request: main_models.GetDedicatedIpWarmUpDetailRequest,
    ) -> main_models.GetDedicatedIpWarmUpDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_dedicated_ip_warm_up_detail_with_options_async(request, runtime)

    def get_dedicated_ip_warm_up_info_with_options(
        self,
        request: main_models.GetDedicatedIpWarmUpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDedicatedIpWarmUpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDedicatedIpWarmUpInfo',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDedicatedIpWarmUpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dedicated_ip_warm_up_info_with_options_async(
        self,
        request: main_models.GetDedicatedIpWarmUpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDedicatedIpWarmUpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDedicatedIpWarmUpInfo',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDedicatedIpWarmUpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dedicated_ip_warm_up_info(
        self,
        request: main_models.GetDedicatedIpWarmUpInfoRequest,
    ) -> main_models.GetDedicatedIpWarmUpInfoResponse:
        runtime = RuntimeOptions()
        return self.get_dedicated_ip_warm_up_info_with_options(request, runtime)

    async def get_dedicated_ip_warm_up_info_async(
        self,
        request: main_models.GetDedicatedIpWarmUpInfoRequest,
    ) -> main_models.GetDedicatedIpWarmUpInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_dedicated_ip_warm_up_info_with_options_async(request, runtime)

    def get_ip_protection_with_options(
        self,
        request: main_models.GetIpProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpProtection',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ip_protection_with_options_async(
        self,
        request: main_models.GetIpProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpProtection',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ip_protection(
        self,
        request: main_models.GetIpProtectionRequest,
    ) -> main_models.GetIpProtectionResponse:
        runtime = RuntimeOptions()
        return self.get_ip_protection_with_options(request, runtime)

    async def get_ip_protection_async(
        self,
        request: main_models.GetIpProtectionRequest,
    ) -> main_models.GetIpProtectionResponse:
        runtime = RuntimeOptions()
        return await self.get_ip_protection_with_options_async(request, runtime)

    def get_ipfilter_list_with_options(
        self,
        request: main_models.GetIpfilterListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpfilterListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpfilterList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpfilterListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ipfilter_list_with_options_async(
        self,
        request: main_models.GetIpfilterListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpfilterListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpfilterList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpfilterListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ipfilter_list(
        self,
        request: main_models.GetIpfilterListRequest,
    ) -> main_models.GetIpfilterListResponse:
        runtime = RuntimeOptions()
        return self.get_ipfilter_list_with_options(request, runtime)

    async def get_ipfilter_list_async(
        self,
        request: main_models.GetIpfilterListRequest,
    ) -> main_models.GetIpfilterListResponse:
        runtime = RuntimeOptions()
        return await self.get_ipfilter_list_with_options_async(request, runtime)

    def get_suppression_list_level_with_options(
        self,
        request: main_models.GetSuppressionListLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSuppressionListLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSuppressionListLevel',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSuppressionListLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_suppression_list_level_with_options_async(
        self,
        request: main_models.GetSuppressionListLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSuppressionListLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSuppressionListLevel',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSuppressionListLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_suppression_list_level(
        self,
        request: main_models.GetSuppressionListLevelRequest,
    ) -> main_models.GetSuppressionListLevelResponse:
        runtime = RuntimeOptions()
        return self.get_suppression_list_level_with_options(request, runtime)

    async def get_suppression_list_level_async(
        self,
        request: main_models.GetSuppressionListLevelRequest,
    ) -> main_models.GetSuppressionListLevelResponse:
        runtime = RuntimeOptions()
        return await self.get_suppression_list_level_with_options_async(request, runtime)

    def get_track_list_with_options(
        self,
        request: main_models.GetTrackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTrackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not DaraCore.is_null(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.total):
            query['Total'] = request.total
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrackList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_track_list_with_options_async(
        self,
        request: main_models.GetTrackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTrackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not DaraCore.is_null(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.total):
            query['Total'] = request.total
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrackList',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_track_list(
        self,
        request: main_models.GetTrackListRequest,
    ) -> main_models.GetTrackListResponse:
        runtime = RuntimeOptions()
        return self.get_track_list_with_options(request, runtime)

    async def get_track_list_async(
        self,
        request: main_models.GetTrackListRequest,
    ) -> main_models.GetTrackListResponse:
        runtime = RuntimeOptions()
        return await self.get_track_list_with_options_async(request, runtime)

    def get_track_list_by_mail_from_and_tag_name_with_options(
        self,
        request: main_models.GetTrackListByMailFromAndTagNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTrackListByMailFromAndTagNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not DaraCore.is_null(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.total):
            query['Total'] = request.total
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrackListByMailFromAndTagName',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrackListByMailFromAndTagNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_track_list_by_mail_from_and_tag_name_with_options_async(
        self,
        request: main_models.GetTrackListByMailFromAndTagNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTrackListByMailFromAndTagNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not DaraCore.is_null(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.total):
            query['Total'] = request.total
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrackListByMailFromAndTagName',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrackListByMailFromAndTagNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_track_list_by_mail_from_and_tag_name(
        self,
        request: main_models.GetTrackListByMailFromAndTagNameRequest,
    ) -> main_models.GetTrackListByMailFromAndTagNameResponse:
        runtime = RuntimeOptions()
        return self.get_track_list_by_mail_from_and_tag_name_with_options(request, runtime)

    async def get_track_list_by_mail_from_and_tag_name_async(
        self,
        request: main_models.GetTrackListByMailFromAndTagNameRequest,
    ) -> main_models.GetTrackListByMailFromAndTagNameResponse:
        runtime = RuntimeOptions()
        return await self.get_track_list_by_mail_from_and_tag_name_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(self) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return self.get_user_with_options(runtime)

    async def get_user_async(self) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return await self.get_user_with_options_async(runtime)

    def get_validate_file_with_options(
        self,
        request: main_models.GetValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_validate_file_with_options_async(
        self,
        request: main_models.GetValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_validate_file(
        self,
        request: main_models.GetValidateFileRequest,
    ) -> main_models.GetValidateFileResponse:
        runtime = RuntimeOptions()
        return self.get_validate_file_with_options(request, runtime)

    async def get_validate_file_async(
        self,
        request: main_models.GetValidateFileRequest,
    ) -> main_models.GetValidateFileResponse:
        runtime = RuntimeOptions()
        return await self.get_validate_file_with_options_async(request, runtime)

    def get_validate_file_status_with_options(
        self,
        request: main_models.GetValidateFileStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidateFileStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetValidateFileStatus',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidateFileStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_validate_file_status_with_options_async(
        self,
        request: main_models.GetValidateFileStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidateFileStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetValidateFileStatus',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidateFileStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_validate_file_status(
        self,
        request: main_models.GetValidateFileStatusRequest,
    ) -> main_models.GetValidateFileStatusResponse:
        runtime = RuntimeOptions()
        return self.get_validate_file_status_with_options(request, runtime)

    async def get_validate_file_status_async(
        self,
        request: main_models.GetValidateFileStatusRequest,
    ) -> main_models.GetValidateFileStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_validate_file_status_with_options_async(request, runtime)

    def get_validation_quota_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidationQuotaResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetValidationQuota',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidationQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_validation_quota_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidationQuotaResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetValidationQuota',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidationQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_validation_quota(self) -> main_models.GetValidationQuotaResponse:
        runtime = RuntimeOptions()
        return self.get_validation_quota_with_options(runtime)

    async def get_validation_quota_async(self) -> main_models.GetValidationQuotaResponse:
        runtime = RuntimeOptions()
        return await self.get_validation_quota_with_options_async(runtime)

    def list_block_sending_with_options(
        self,
        request: main_models.ListBlockSendingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBlockSendingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.block_email):
            query['BlockEmail'] = request.block_email
        if not DaraCore.is_null(request.block_type):
            query['BlockType'] = request.block_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBlockSending',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBlockSendingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_block_sending_with_options_async(
        self,
        request: main_models.ListBlockSendingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBlockSendingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.block_email):
            query['BlockEmail'] = request.block_email
        if not DaraCore.is_null(request.block_type):
            query['BlockType'] = request.block_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBlockSending',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBlockSendingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_block_sending(
        self,
        request: main_models.ListBlockSendingRequest,
    ) -> main_models.ListBlockSendingResponse:
        runtime = RuntimeOptions()
        return self.list_block_sending_with_options(request, runtime)

    async def list_block_sending_async(
        self,
        request: main_models.ListBlockSendingRequest,
    ) -> main_models.ListBlockSendingResponse:
        runtime = RuntimeOptions()
        return await self.list_block_sending_with_options_async(request, runtime)

    def list_user_suppression_with_options(
        self,
        request: main_models.ListUserSuppressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserSuppressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.end_bounce_time):
            query['EndBounceTime'] = request.end_bounce_time
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_bounce_time):
            query['StartBounceTime'] = request.start_bounce_time
        if not DaraCore.is_null(request.start_create_time):
            query['StartCreateTime'] = request.start_create_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserSuppression',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserSuppressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_suppression_with_options_async(
        self,
        request: main_models.ListUserSuppressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserSuppressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.end_bounce_time):
            query['EndBounceTime'] = request.end_bounce_time
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_bounce_time):
            query['StartBounceTime'] = request.start_bounce_time
        if not DaraCore.is_null(request.start_create_time):
            query['StartCreateTime'] = request.start_create_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserSuppression',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserSuppressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_suppression(
        self,
        request: main_models.ListUserSuppressionRequest,
    ) -> main_models.ListUserSuppressionResponse:
        runtime = RuntimeOptions()
        return self.list_user_suppression_with_options(request, runtime)

    async def list_user_suppression_async(
        self,
        request: main_models.ListUserSuppressionRequest,
    ) -> main_models.ListUserSuppressionResponse:
        runtime = RuntimeOptions()
        return await self.list_user_suppression_with_options_async(request, runtime)

    def list_validate_file_with_options(
        self,
        request: main_models.ListValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.file_keyword):
            query['FileKeyword'] = request.file_keyword
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListValidateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_validate_file_with_options_async(
        self,
        request: main_models.ListValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.file_keyword):
            query['FileKeyword'] = request.file_keyword
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListValidateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_validate_file(
        self,
        request: main_models.ListValidateFileRequest,
    ) -> main_models.ListValidateFileResponse:
        runtime = RuntimeOptions()
        return self.list_validate_file_with_options(request, runtime)

    async def list_validate_file_async(
        self,
        request: main_models.ListValidateFileRequest,
    ) -> main_models.ListValidateFileResponse:
        runtime = RuntimeOptions()
        return await self.list_validate_file_with_options_async(request, runtime)

    def modify_mail_address_with_options(
        self,
        request: main_models.ModifyMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mail_address_with_options_async(
        self,
        request: main_models.ModifyMailAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMailAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMailAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMailAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mail_address(
        self,
        request: main_models.ModifyMailAddressRequest,
    ) -> main_models.ModifyMailAddressResponse:
        runtime = RuntimeOptions()
        return self.modify_mail_address_with_options(request, runtime)

    async def modify_mail_address_async(
        self,
        request: main_models.ModifyMailAddressRequest,
    ) -> main_models.ModifyMailAddressResponse:
        runtime = RuntimeOptions()
        return await self.modify_mail_address_with_options_async(request, runtime)

    def modify_pwby_domain_with_options(
        self,
        request: main_models.ModifyPWByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPWByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPWByDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPWByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_pwby_domain_with_options_async(
        self,
        request: main_models.ModifyPWByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPWByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPWByDomain',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPWByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_pwby_domain(
        self,
        request: main_models.ModifyPWByDomainRequest,
    ) -> main_models.ModifyPWByDomainResponse:
        runtime = RuntimeOptions()
        return self.modify_pwby_domain_with_options(request, runtime)

    async def modify_pwby_domain_async(
        self,
        request: main_models.ModifyPWByDomainRequest,
    ) -> main_models.ModifyPWByDomainResponse:
        runtime = RuntimeOptions()
        return await self.modify_pwby_domain_with_options_async(request, runtime)

    def modify_tag_with_options(
        self,
        request: main_models.ModifyTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTag',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tag_with_options_async(
        self,
        request: main_models.ModifyTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTag',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tag(
        self,
        request: main_models.ModifyTagRequest,
    ) -> main_models.ModifyTagResponse:
        runtime = RuntimeOptions()
        return self.modify_tag_with_options(request, runtime)

    async def modify_tag_async(
        self,
        request: main_models.ModifyTagRequest,
    ) -> main_models.ModifyTagResponse:
        runtime = RuntimeOptions()
        return await self.modify_tag_with_options_async(request, runtime)

    def query_domain_by_param_with_options(
        self,
        request: main_models.QueryDomainByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_param_with_options_async(
        self,
        request: main_models.QueryDomainByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_param(
        self,
        request: main_models.QueryDomainByParamRequest,
    ) -> main_models.QueryDomainByParamResponse:
        runtime = RuntimeOptions()
        return self.query_domain_by_param_with_options(request, runtime)

    async def query_domain_by_param_async(
        self,
        request: main_models.QueryDomainByParamRequest,
    ) -> main_models.QueryDomainByParamResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_by_param_with_options_async(request, runtime)

    def query_invalid_address_with_options(
        self,
        request: main_models.QueryInvalidAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInvalidAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.next_start):
            query['NextStart'] = request.next_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInvalidAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInvalidAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_invalid_address_with_options_async(
        self,
        request: main_models.QueryInvalidAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInvalidAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.next_start):
            query['NextStart'] = request.next_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInvalidAddress',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInvalidAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_invalid_address(
        self,
        request: main_models.QueryInvalidAddressRequest,
    ) -> main_models.QueryInvalidAddressResponse:
        runtime = RuntimeOptions()
        return self.query_invalid_address_with_options(request, runtime)

    async def query_invalid_address_async(
        self,
        request: main_models.QueryInvalidAddressRequest,
    ) -> main_models.QueryInvalidAddressResponse:
        runtime = RuntimeOptions()
        return await self.query_invalid_address_with_options_async(request, runtime)

    def query_mail_address_by_param_with_options(
        self,
        request: main_models.QueryMailAddressByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMailAddressByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMailAddressByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMailAddressByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mail_address_by_param_with_options_async(
        self,
        request: main_models.QueryMailAddressByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMailAddressByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMailAddressByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMailAddressByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mail_address_by_param(
        self,
        request: main_models.QueryMailAddressByParamRequest,
    ) -> main_models.QueryMailAddressByParamResponse:
        runtime = RuntimeOptions()
        return self.query_mail_address_by_param_with_options(request, runtime)

    async def query_mail_address_by_param_async(
        self,
        request: main_models.QueryMailAddressByParamRequest,
    ) -> main_models.QueryMailAddressByParamResponse:
        runtime = RuntimeOptions()
        return await self.query_mail_address_by_param_with_options_async(request, runtime)

    def query_receiver_by_param_with_options(
        self,
        request: main_models.QueryReceiverByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReceiverByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReceiverByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReceiverByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_receiver_by_param_with_options_async(
        self,
        request: main_models.QueryReceiverByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReceiverByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReceiverByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReceiverByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_receiver_by_param(
        self,
        request: main_models.QueryReceiverByParamRequest,
    ) -> main_models.QueryReceiverByParamResponse:
        runtime = RuntimeOptions()
        return self.query_receiver_by_param_with_options(request, runtime)

    async def query_receiver_by_param_async(
        self,
        request: main_models.QueryReceiverByParamRequest,
    ) -> main_models.QueryReceiverByParamResponse:
        runtime = RuntimeOptions()
        return await self.query_receiver_by_param_with_options_async(request, runtime)

    def query_receiver_detail_with_options(
        self,
        request: main_models.QueryReceiverDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReceiverDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.next_start):
            query['NextStart'] = request.next_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReceiverDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_receiver_detail_with_options_async(
        self,
        request: main_models.QueryReceiverDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReceiverDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.next_start):
            query['NextStart'] = request.next_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReceiverDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReceiverDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_receiver_detail(
        self,
        request: main_models.QueryReceiverDetailRequest,
    ) -> main_models.QueryReceiverDetailResponse:
        runtime = RuntimeOptions()
        return self.query_receiver_detail_with_options(request, runtime)

    async def query_receiver_detail_async(
        self,
        request: main_models.QueryReceiverDetailRequest,
    ) -> main_models.QueryReceiverDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_receiver_detail_with_options_async(request, runtime)

    def query_tag_by_param_with_options(
        self,
        request: main_models.QueryTagByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_by_param_with_options_async(
        self,
        request: main_models.QueryTagByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_by_param(
        self,
        request: main_models.QueryTagByParamRequest,
    ) -> main_models.QueryTagByParamResponse:
        runtime = RuntimeOptions()
        return self.query_tag_by_param_with_options(request, runtime)

    async def query_tag_by_param_async(
        self,
        request: main_models.QueryTagByParamRequest,
    ) -> main_models.QueryTagByParamResponse:
        runtime = RuntimeOptions()
        return await self.query_tag_by_param_with_options_async(request, runtime)

    def query_task_by_param_with_options(
        self,
        request: main_models.QueryTaskByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_by_param_with_options_async(
        self,
        request: main_models.QueryTaskByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_by_param(
        self,
        request: main_models.QueryTaskByParamRequest,
    ) -> main_models.QueryTaskByParamResponse:
        runtime = RuntimeOptions()
        return self.query_task_by_param_with_options(request, runtime)

    async def query_task_by_param_async(
        self,
        request: main_models.QueryTaskByParamRequest,
    ) -> main_models.QueryTaskByParamResponse:
        runtime = RuntimeOptions()
        return await self.query_task_by_param_with_options_async(request, runtime)

    def query_template_by_param_with_options(
        self,
        request: main_models.QueryTemplateByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTemplateByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_type):
            query['FromType'] = request.from_type
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTemplateByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTemplateByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_template_by_param_with_options_async(
        self,
        request: main_models.QueryTemplateByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTemplateByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_type):
            query['FromType'] = request.from_type
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTemplateByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTemplateByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_template_by_param(
        self,
        request: main_models.QueryTemplateByParamRequest,
    ) -> main_models.QueryTemplateByParamResponse:
        runtime = RuntimeOptions()
        return self.query_template_by_param_with_options(request, runtime)

    async def query_template_by_param_async(
        self,
        request: main_models.QueryTemplateByParamRequest,
    ) -> main_models.QueryTemplateByParamResponse:
        runtime = RuntimeOptions()
        return await self.query_template_by_param_with_options_async(request, runtime)

    def remove_user_suppression_with_options(
        self,
        request: main_models.RemoveUserSuppressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserSuppressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.suppression_ids):
            query['SuppressionIds'] = request.suppression_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserSuppression',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserSuppressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_suppression_with_options_async(
        self,
        request: main_models.RemoveUserSuppressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserSuppressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.suppression_ids):
            query['SuppressionIds'] = request.suppression_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserSuppression',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserSuppressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_suppression(
        self,
        request: main_models.RemoveUserSuppressionRequest,
    ) -> main_models.RemoveUserSuppressionResponse:
        runtime = RuntimeOptions()
        return self.remove_user_suppression_with_options(request, runtime)

    async def remove_user_suppression_async(
        self,
        request: main_models.RemoveUserSuppressionRequest,
    ) -> main_models.RemoveUserSuppressionResponse:
        runtime = RuntimeOptions()
        return await self.remove_user_suppression_with_options_async(request, runtime)

    def save_receiver_detail_with_options(
        self,
        request: main_models.SaveReceiverDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveReceiverDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_detail):
            query['CustomDetail'] = request.custom_detail
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveReceiverDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_receiver_detail_with_options_async(
        self,
        request: main_models.SaveReceiverDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveReceiverDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_detail):
            query['CustomDetail'] = request.custom_detail
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveReceiverDetail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveReceiverDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_receiver_detail(
        self,
        request: main_models.SaveReceiverDetailRequest,
    ) -> main_models.SaveReceiverDetailResponse:
        runtime = RuntimeOptions()
        return self.save_receiver_detail_with_options(request, runtime)

    async def save_receiver_detail_async(
        self,
        request: main_models.SaveReceiverDetailRequest,
    ) -> main_models.SaveReceiverDetailResponse:
        runtime = RuntimeOptions()
        return await self.save_receiver_detail_with_options_async(request, runtime)

    def send_test_by_template_with_options(
        self,
        request: main_models.SendTestByTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendTestByTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.birthday):
            query['Birthday'] = request.birthday
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.gender):
            query['Gender'] = request.gender
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_params):
            query['TemplateParams'] = request.template_params
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendTestByTemplate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTestByTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_test_by_template_with_options_async(
        self,
        request: main_models.SendTestByTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendTestByTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.birthday):
            query['Birthday'] = request.birthday
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.gender):
            query['Gender'] = request.gender
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_params):
            query['TemplateParams'] = request.template_params
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendTestByTemplate',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTestByTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_test_by_template(
        self,
        request: main_models.SendTestByTemplateRequest,
    ) -> main_models.SendTestByTemplateResponse:
        runtime = RuntimeOptions()
        return self.send_test_by_template_with_options(request, runtime)

    async def send_test_by_template_async(
        self,
        request: main_models.SendTestByTemplateRequest,
    ) -> main_models.SendTestByTemplateResponse:
        runtime = RuntimeOptions()
        return await self.send_test_by_template_with_options_async(request, runtime)

    def send_validate_file_with_options(
        self,
        request: main_models.SendValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_column):
            query['AddressColumn'] = request.address_column
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.has_header_row):
            query['HasHeaderRow'] = request.has_header_row
        if not DaraCore.is_null(request.remove_duplicate):
            query['RemoveDuplicate'] = request.remove_duplicate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendValidateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_validate_file_with_options_async(
        self,
        request: main_models.SendValidateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendValidateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_column):
            query['AddressColumn'] = request.address_column
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.has_header_row):
            query['HasHeaderRow'] = request.has_header_row
        if not DaraCore.is_null(request.remove_duplicate):
            query['RemoveDuplicate'] = request.remove_duplicate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendValidateFile',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendValidateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_validate_file(
        self,
        request: main_models.SendValidateFileRequest,
    ) -> main_models.SendValidateFileResponse:
        runtime = RuntimeOptions()
        return self.send_validate_file_with_options(request, runtime)

    async def send_validate_file_async(
        self,
        request: main_models.SendValidateFileRequest,
    ) -> main_models.SendValidateFileResponse:
        runtime = RuntimeOptions()
        return await self.send_validate_file_with_options_async(request, runtime)

    def send_validate_file_advance(
        self,
        request: main_models.SendValidateFileAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendValidateFileResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        send_validate_file_req = main_models.SendValidateFileRequest()
        Utils.convert(request, send_validate_file_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            send_validate_file_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        send_validate_file_resp = self.send_validate_file_with_options(send_validate_file_req, runtime)
        return send_validate_file_resp

    async def send_validate_file_advance_async(
        self,
        request: main_models.SendValidateFileAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendValidateFileResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        send_validate_file_req = main_models.SendValidateFileRequest()
        Utils.convert(request, send_validate_file_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            send_validate_file_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        send_validate_file_resp = await self.send_validate_file_with_options_async(send_validate_file_req, runtime)
        return send_validate_file_resp

    def sender_statistics_by_tag_name_and_batch_idwith_options(
        self,
        request: main_models.SenderStatisticsByTagNameAndBatchIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SenderStatisticsByTagNameAndBatchIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SenderStatisticsByTagNameAndBatchID',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SenderStatisticsByTagNameAndBatchIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def sender_statistics_by_tag_name_and_batch_idwith_options_async(
        self,
        request: main_models.SenderStatisticsByTagNameAndBatchIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SenderStatisticsByTagNameAndBatchIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dedicated_ip):
            query['DedicatedIp'] = request.dedicated_ip
        if not DaraCore.is_null(request.dedicated_ip_pool_id):
            query['DedicatedIpPoolId'] = request.dedicated_ip_pool_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.esp):
            query['Esp'] = request.esp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SenderStatisticsByTagNameAndBatchID',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SenderStatisticsByTagNameAndBatchIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sender_statistics_by_tag_name_and_batch_id(
        self,
        request: main_models.SenderStatisticsByTagNameAndBatchIDRequest,
    ) -> main_models.SenderStatisticsByTagNameAndBatchIDResponse:
        runtime = RuntimeOptions()
        return self.sender_statistics_by_tag_name_and_batch_idwith_options(request, runtime)

    async def sender_statistics_by_tag_name_and_batch_id_async(
        self,
        request: main_models.SenderStatisticsByTagNameAndBatchIDRequest,
    ) -> main_models.SenderStatisticsByTagNameAndBatchIDResponse:
        runtime = RuntimeOptions()
        return await self.sender_statistics_by_tag_name_and_batch_idwith_options_async(request, runtime)

    def sender_statistics_detail_by_param_with_options(
        self,
        request: main_models.SenderStatisticsDetailByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SenderStatisticsDetailByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.next_start):
            query['NextStart'] = request.next_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SenderStatisticsDetailByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SenderStatisticsDetailByParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def sender_statistics_detail_by_param_with_options_async(
        self,
        request: main_models.SenderStatisticsDetailByParamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SenderStatisticsDetailByParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.config_set_id):
            query['ConfigSetId'] = request.config_set_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_pool_id):
            query['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.next_start):
            query['NextStart'] = request.next_start
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SenderStatisticsDetailByParam',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SenderStatisticsDetailByParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sender_statistics_detail_by_param(
        self,
        request: main_models.SenderStatisticsDetailByParamRequest,
    ) -> main_models.SenderStatisticsDetailByParamResponse:
        runtime = RuntimeOptions()
        return self.sender_statistics_detail_by_param_with_options(request, runtime)

    async def sender_statistics_detail_by_param_async(
        self,
        request: main_models.SenderStatisticsDetailByParamRequest,
    ) -> main_models.SenderStatisticsDetailByParamResponse:
        runtime = RuntimeOptions()
        return await self.sender_statistics_detail_by_param_with_options_async(request, runtime)

    def set_suppression_list_level_with_options(
        self,
        request: main_models.SetSuppressionListLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSuppressionListLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.suppression_list_level):
            query['SuppressionListLevel'] = request.suppression_list_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSuppressionListLevel',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSuppressionListLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_suppression_list_level_with_options_async(
        self,
        request: main_models.SetSuppressionListLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSuppressionListLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.suppression_list_level):
            query['SuppressionListLevel'] = request.suppression_list_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSuppressionListLevel',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSuppressionListLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_suppression_list_level(
        self,
        request: main_models.SetSuppressionListLevelRequest,
    ) -> main_models.SetSuppressionListLevelResponse:
        runtime = RuntimeOptions()
        return self.set_suppression_list_level_with_options(request, runtime)

    async def set_suppression_list_level_async(
        self,
        request: main_models.SetSuppressionListLevelRequest,
    ) -> main_models.SetSuppressionListLevelResponse:
        runtime = RuntimeOptions()
        return await self.set_suppression_list_level_with_options_async(request, runtime)

    def single_send_mail_with_options(
        self,
        tmp_req: main_models.SingleSendMailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleSendMailResponse:
        tmp_req.validate()
        request = main_models.SingleSendMailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.attachments):
            body['Attachments'] = request.attachments
        if not DaraCore.is_null(request.bcc_address):
            body['BccAddress'] = request.bcc_address
        if not DaraCore.is_null(request.click_trace):
            body['ClickTrace'] = request.click_trace
        if not DaraCore.is_null(request.domain_auth):
            body['DomainAuth'] = request.domain_auth
        if not DaraCore.is_null(request.from_alias):
            body['FromAlias'] = request.from_alias
        if not DaraCore.is_null(request.headers):
            body['Headers'] = request.headers
        if not DaraCore.is_null(request.html_body):
            body['HtmlBody'] = request.html_body
        if not DaraCore.is_null(request.ip_pool_id):
            body['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.reply_address):
            body['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.reply_address_alias):
            body['ReplyAddressAlias'] = request.reply_address_alias
        if not DaraCore.is_null(request.reply_to_address):
            body['ReplyToAddress'] = request.reply_to_address
        if not DaraCore.is_null(request.subject):
            body['Subject'] = request.subject
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        if not DaraCore.is_null(request.template_shrink):
            body['Template'] = request.template_shrink
        if not DaraCore.is_null(request.text_body):
            body['TextBody'] = request.text_body
        if not DaraCore.is_null(request.to_address):
            body['ToAddress'] = request.to_address
        if not DaraCore.is_null(request.un_subscribe_filter_level):
            body['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not DaraCore.is_null(request.un_subscribe_link_type):
            body['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SingleSendMail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleSendMailResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_send_mail_with_options_async(
        self,
        tmp_req: main_models.SingleSendMailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleSendMailResponse:
        tmp_req.validate()
        request = main_models.SingleSendMailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.template):
            request.template_shrink = Utils.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.attachments):
            body['Attachments'] = request.attachments
        if not DaraCore.is_null(request.bcc_address):
            body['BccAddress'] = request.bcc_address
        if not DaraCore.is_null(request.click_trace):
            body['ClickTrace'] = request.click_trace
        if not DaraCore.is_null(request.domain_auth):
            body['DomainAuth'] = request.domain_auth
        if not DaraCore.is_null(request.from_alias):
            body['FromAlias'] = request.from_alias
        if not DaraCore.is_null(request.headers):
            body['Headers'] = request.headers
        if not DaraCore.is_null(request.html_body):
            body['HtmlBody'] = request.html_body
        if not DaraCore.is_null(request.ip_pool_id):
            body['IpPoolId'] = request.ip_pool_id
        if not DaraCore.is_null(request.reply_address):
            body['ReplyAddress'] = request.reply_address
        if not DaraCore.is_null(request.reply_address_alias):
            body['ReplyAddressAlias'] = request.reply_address_alias
        if not DaraCore.is_null(request.reply_to_address):
            body['ReplyToAddress'] = request.reply_to_address
        if not DaraCore.is_null(request.subject):
            body['Subject'] = request.subject
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        if not DaraCore.is_null(request.template_shrink):
            body['Template'] = request.template_shrink
        if not DaraCore.is_null(request.text_body):
            body['TextBody'] = request.text_body
        if not DaraCore.is_null(request.to_address):
            body['ToAddress'] = request.to_address
        if not DaraCore.is_null(request.un_subscribe_filter_level):
            body['UnSubscribeFilterLevel'] = request.un_subscribe_filter_level
        if not DaraCore.is_null(request.un_subscribe_link_type):
            body['UnSubscribeLinkType'] = request.un_subscribe_link_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SingleSendMail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleSendMailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_send_mail(
        self,
        request: main_models.SingleSendMailRequest,
    ) -> main_models.SingleSendMailResponse:
        runtime = RuntimeOptions()
        return self.single_send_mail_with_options(request, runtime)

    async def single_send_mail_async(
        self,
        request: main_models.SingleSendMailRequest,
    ) -> main_models.SingleSendMailResponse:
        runtime = RuntimeOptions()
        return await self.single_send_mail_with_options_async(request, runtime)

    def single_send_mail_advance(
        self,
        request: main_models.SingleSendMailAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleSendMailResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        single_send_mail_req = main_models.SingleSendMailRequest()
        Utils.convert(request, single_send_mail_req)
        if not DaraCore.is_null(request.attachments):
            i_0 = 0
            for item_0 in request.attachments:
                if not DaraCore.is_null(item_0.attachment_url_object):
                    auth_response = auth_client.call_api(auth_params, auth_req, runtime)
                    tmp_body = auth_response.get('body')
                    use_accelerate = bool(tmp_body.get('UseAccelerate'))
                    auth_response_body = Utils.stringify_map_value(tmp_body)
                    file_obj = FileField(
                        filename = auth_response_body.get('ObjectKey'),
                        content = item_0.attachment_url_object,
                        content_type = ''
                    )
                    oss_header = {
                        'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                        'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                        'policy': auth_response_body.get('EncodedPolicy'),
                        'Signature': auth_response_body.get('Signature'),
                        'key': auth_response_body.get('ObjectKey'),
                        'file': file_obj,
                        'success_action_status': '201'
                    }
                    self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
                    tmp_obj = single_send_mail_req.attachments[i_0]
                    tmp_obj.attachment_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0+= 1
        single_send_mail_resp = self.single_send_mail_with_options(single_send_mail_req, runtime)
        return single_send_mail_resp

    async def single_send_mail_advance_async(
        self,
        request: main_models.SingleSendMailAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleSendMailResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Dm',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        single_send_mail_req = main_models.SingleSendMailRequest()
        Utils.convert(request, single_send_mail_req)
        if not DaraCore.is_null(request.attachments):
            i_0 = 0
            for item_0 in request.attachments:
                if not DaraCore.is_null(item_0.attachment_url_object):
                    auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    tmp_body = auth_response.get('body')
                    use_accelerate = bool(tmp_body.get('UseAccelerate'))
                    auth_response_body = Utils.stringify_map_value(tmp_body)
                    file_obj = FileField(
                        filename = auth_response_body.get('ObjectKey'),
                        content = item_0.attachment_url_object,
                        content_type = ''
                    )
                    oss_header = {
                        'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                        'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                        'policy': auth_response_body.get('EncodedPolicy'),
                        'Signature': auth_response_body.get('Signature'),
                        'key': auth_response_body.get('ObjectKey'),
                        'file': file_obj,
                        'success_action_status': '201'
                    }
                    await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
                    tmp_obj = single_send_mail_req.attachments[i_0]
                    tmp_obj.attachment_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0+= 1
        single_send_mail_resp = await self.single_send_mail_with_options_async(single_send_mail_req, runtime)
        return single_send_mail_resp

    def unblock_sending_with_options(
        self,
        request: main_models.UnblockSendingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnblockSendingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.block_email):
            query['BlockEmail'] = request.block_email
        if not DaraCore.is_null(request.block_type):
            query['BlockType'] = request.block_type
        if not DaraCore.is_null(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnblockSending',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnblockSendingResponse(),
            self.call_api(params, req, runtime)
        )

    async def unblock_sending_with_options_async(
        self,
        request: main_models.UnblockSendingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnblockSendingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.block_email):
            query['BlockEmail'] = request.block_email
        if not DaraCore.is_null(request.block_type):
            query['BlockType'] = request.block_type
        if not DaraCore.is_null(request.sender_email):
            query['SenderEmail'] = request.sender_email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnblockSending',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnblockSendingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unblock_sending(
        self,
        request: main_models.UnblockSendingRequest,
    ) -> main_models.UnblockSendingResponse:
        runtime = RuntimeOptions()
        return self.unblock_sending_with_options(request, runtime)

    async def unblock_sending_async(
        self,
        request: main_models.UnblockSendingRequest,
    ) -> main_models.UnblockSendingResponse:
        runtime = RuntimeOptions()
        return await self.unblock_sending_with_options_async(request, runtime)

    def update_ip_protection_with_options(
        self,
        request: main_models.UpdateIpProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_protection):
            query['IpProtection'] = request.ip_protection
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpProtection',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ip_protection_with_options_async(
        self,
        request: main_models.UpdateIpProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_protection):
            query['IpProtection'] = request.ip_protection
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpProtection',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ip_protection(
        self,
        request: main_models.UpdateIpProtectionRequest,
    ) -> main_models.UpdateIpProtectionResponse:
        runtime = RuntimeOptions()
        return self.update_ip_protection_with_options(request, runtime)

    async def update_ip_protection_async(
        self,
        request: main_models.UpdateIpProtectionRequest,
    ) -> main_models.UpdateIpProtectionResponse:
        runtime = RuntimeOptions()
        return await self.update_ip_protection_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        tmp_req: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        body = {}
        if not DaraCore.is_null(request.user_shrink):
            body['User'] = request.user_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        tmp_req: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        body = {}
        if not DaraCore.is_null(request.user_shrink):
            body['User'] = request.user_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def validate_email_with_options(
        self,
        request: main_models.ValidateEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_graylist):
            query['CheckGraylist'] = request.check_graylist
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateEmail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_email_with_options_async(
        self,
        request: main_models.ValidateEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_graylist):
            query['CheckGraylist'] = request.check_graylist
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateEmail',
            version = '2015-11-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_email(
        self,
        request: main_models.ValidateEmailRequest,
    ) -> main_models.ValidateEmailResponse:
        runtime = RuntimeOptions()
        return self.validate_email_with_options(request, runtime)

    async def validate_email_async(
        self,
        request: main_models.ValidateEmailRequest,
    ) -> main_models.ValidateEmailResponse:
        runtime = RuntimeOptions()
        return await self.validate_email_with_options_async(request, runtime)
