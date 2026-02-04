# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dcdn20180115 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'dcdn.aliyuncs.com',
            'ap-northeast-2-pop': 'dcdn.aliyuncs.com',
            'ap-south-1': 'dcdn.aliyuncs.com',
            'ap-southeast-1': 'dcdn.aliyuncs.com',
            'ap-southeast-2': 'dcdn.aliyuncs.com',
            'ap-southeast-3': 'dcdn.aliyuncs.com',
            'ap-southeast-5': 'dcdn.aliyuncs.com',
            'cn-beijing': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-1': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'dcdn.aliyuncs.com',
            'cn-beijing-gov-1': 'dcdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dcdn.aliyuncs.com',
            'cn-chengdu': 'dcdn.aliyuncs.com',
            'cn-edge-1': 'dcdn.aliyuncs.com',
            'cn-fujian': 'dcdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dcdn.aliyuncs.com',
            'cn-hangzhou': 'dcdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dcdn.aliyuncs.com',
            'cn-hangzhou-finance': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dcdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'dcdn.aliyuncs.com',
            'cn-hongkong': 'dcdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dcdn.aliyuncs.com',
            'cn-huhehaote': 'dcdn.aliyuncs.com',
            'cn-north-2-gov-1': 'dcdn.aliyuncs.com',
            'cn-qingdao': 'dcdn.aliyuncs.com',
            'cn-qingdao-nebula': 'dcdn.aliyuncs.com',
            'cn-shanghai': 'dcdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'dcdn.aliyuncs.com',
            'cn-shanghai-inner': 'dcdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen': 'dcdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen-inner': 'dcdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dcdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dcdn.aliyuncs.com',
            'cn-wuhan': 'dcdn.aliyuncs.com',
            'cn-yushanfang': 'dcdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dcdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dcdn.aliyuncs.com',
            'eu-central-1': 'dcdn.aliyuncs.com',
            'eu-west-1': 'dcdn.aliyuncs.com',
            'eu-west-1-oxs': 'dcdn.aliyuncs.com',
            'me-east-1': 'dcdn.aliyuncs.com',
            'rus-west-1-pop': 'dcdn.aliyuncs.com',
            'us-east-1': 'dcdn.aliyuncs.com',
            'us-west-1': 'dcdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dcdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_dcdn_domain_with_options(
        self,
        request: main_models.AddDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_type):
            query['FunctionType'] = request.function_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dcdn_domain_with_options_async(
        self,
        request: main_models.AddDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_type):
            query['FunctionType'] = request.function_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dcdn_domain(
        self,
        request: main_models.AddDcdnDomainRequest,
    ) -> main_models.AddDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.add_dcdn_domain_with_options(request, runtime)

    async def add_dcdn_domain_async(
        self,
        request: main_models.AddDcdnDomainRequest,
    ) -> main_models.AddDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.add_dcdn_domain_with_options_async(request, runtime)

    def add_dcdn_ipa_domain_with_options(
        self,
        request: main_models.AddDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dcdn_ipa_domain_with_options_async(
        self,
        request: main_models.AddDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dcdn_ipa_domain(
        self,
        request: main_models.AddDcdnIpaDomainRequest,
    ) -> main_models.AddDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return self.add_dcdn_ipa_domain_with_options(request, runtime)

    async def add_dcdn_ipa_domain_async(
        self,
        request: main_models.AddDcdnIpaDomainRequest,
    ) -> main_models.AddDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return await self.add_dcdn_ipa_domain_with_options_async(request, runtime)

    def batch_add_dcdn_domain_with_options(
        self,
        request: main_models.BatchAddDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_dcdn_domain_with_options_async(
        self,
        request: main_models.BatchAddDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_dcdn_domain(
        self,
        request: main_models.BatchAddDcdnDomainRequest,
    ) -> main_models.BatchAddDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_add_dcdn_domain_with_options(request, runtime)

    async def batch_add_dcdn_domain_async(
        self,
        request: main_models.BatchAddDcdnDomainRequest,
    ) -> main_models.BatchAddDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_add_dcdn_domain_with_options_async(request, runtime)

    def batch_create_dcdn_waf_rules_with_options(
        self,
        request: main_models.BatchCreateDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateDcdnWafRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_dcdn_waf_rules_with_options_async(
        self,
        request: main_models.BatchCreateDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateDcdnWafRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_dcdn_waf_rules(
        self,
        request: main_models.BatchCreateDcdnWafRulesRequest,
    ) -> main_models.BatchCreateDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return self.batch_create_dcdn_waf_rules_with_options(request, runtime)

    async def batch_create_dcdn_waf_rules_async(
        self,
        request: main_models.BatchCreateDcdnWafRulesRequest,
    ) -> main_models.BatchCreateDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return await self.batch_create_dcdn_waf_rules_with_options_async(request, runtime)

    def batch_delete_dcdn_domain_configs_with_options(
        self,
        request: main_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_dcdn_domain_configs_with_options_async(
        self,
        request: main_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_dcdn_domain_configs(
        self,
        request: main_models.BatchDeleteDcdnDomainConfigsRequest,
    ) -> main_models.BatchDeleteDcdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_dcdn_domain_configs_with_options(request, runtime)

    async def batch_delete_dcdn_domain_configs_async(
        self,
        request: main_models.BatchDeleteDcdnDomainConfigsRequest,
    ) -> main_models.BatchDeleteDcdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_delete_dcdn_kv_with_options(
        self,
        tmp_req: main_models.BatchDeleteDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnKvResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteDcdnKvShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.keys_shrink):
            body['Keys'] = request.keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_dcdn_kv_with_options_async(
        self,
        tmp_req: main_models.BatchDeleteDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnKvResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteDcdnKvShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.keys_shrink):
            body['Keys'] = request.keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_dcdn_kv(
        self,
        request: main_models.BatchDeleteDcdnKvRequest,
    ) -> main_models.BatchDeleteDcdnKvResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_dcdn_kv_with_options(request, runtime)

    async def batch_delete_dcdn_kv_async(
        self,
        request: main_models.BatchDeleteDcdnKvRequest,
    ) -> main_models.BatchDeleteDcdnKvResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_dcdn_kv_with_options_async(request, runtime)

    def batch_delete_dcdn_kv_with_high_capacity_with_options(
        self,
        request: main_models.BatchDeleteDcdnKvWithHighCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnKvWithHighCapacityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnKvWithHighCapacity',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnKvWithHighCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_dcdn_kv_with_high_capacity_with_options_async(
        self,
        request: main_models.BatchDeleteDcdnKvWithHighCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnKvWithHighCapacityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnKvWithHighCapacity',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnKvWithHighCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_dcdn_kv_with_high_capacity(
        self,
        request: main_models.BatchDeleteDcdnKvWithHighCapacityRequest,
    ) -> main_models.BatchDeleteDcdnKvWithHighCapacityResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_dcdn_kv_with_high_capacity_with_options(request, runtime)

    async def batch_delete_dcdn_kv_with_high_capacity_async(
        self,
        request: main_models.BatchDeleteDcdnKvWithHighCapacityRequest,
    ) -> main_models.BatchDeleteDcdnKvWithHighCapacityResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_dcdn_kv_with_high_capacity_with_options_async(request, runtime)

    def batch_delete_dcdn_kv_with_high_capacity_advance(
        self,
        request: main_models.BatchDeleteDcdnKvWithHighCapacityAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnKvWithHighCapacityResponse:
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
            'Product': 'dcdn',
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
        batch_delete_dcdn_kv_with_high_capacity_req = main_models.BatchDeleteDcdnKvWithHighCapacityRequest()
        Utils.convert(request, batch_delete_dcdn_kv_with_high_capacity_req)
        if not DaraCore.is_null(request.url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.url_object,
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
            batch_delete_dcdn_kv_with_high_capacity_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        batch_delete_dcdn_kv_with_high_capacity_resp = self.batch_delete_dcdn_kv_with_high_capacity_with_options(batch_delete_dcdn_kv_with_high_capacity_req, runtime)
        return batch_delete_dcdn_kv_with_high_capacity_resp

    async def batch_delete_dcdn_kv_with_high_capacity_advance_async(
        self,
        request: main_models.BatchDeleteDcdnKvWithHighCapacityAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnKvWithHighCapacityResponse:
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
            'Product': 'dcdn',
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
        batch_delete_dcdn_kv_with_high_capacity_req = main_models.BatchDeleteDcdnKvWithHighCapacityRequest()
        Utils.convert(request, batch_delete_dcdn_kv_with_high_capacity_req)
        if not DaraCore.is_null(request.url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.url_object,
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
            batch_delete_dcdn_kv_with_high_capacity_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        batch_delete_dcdn_kv_with_high_capacity_resp = await self.batch_delete_dcdn_kv_with_high_capacity_with_options_async(batch_delete_dcdn_kv_with_high_capacity_req, runtime)
        return batch_delete_dcdn_kv_with_high_capacity_resp

    def batch_delete_dcdn_waf_rules_with_options(
        self,
        request: main_models.BatchDeleteDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnWafRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.rule_ids):
            body['RuleIds'] = request.rule_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_dcdn_waf_rules_with_options_async(
        self,
        request: main_models.BatchDeleteDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDcdnWafRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.rule_ids):
            body['RuleIds'] = request.rule_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_dcdn_waf_rules(
        self,
        request: main_models.BatchDeleteDcdnWafRulesRequest,
    ) -> main_models.BatchDeleteDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_dcdn_waf_rules_with_options(request, runtime)

    async def batch_delete_dcdn_waf_rules_async(
        self,
        request: main_models.BatchDeleteDcdnWafRulesRequest,
    ) -> main_models.BatchDeleteDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_dcdn_waf_rules_with_options_async(request, runtime)

    def batch_modify_dcdn_waf_rules_with_options(
        self,
        request: main_models.BatchModifyDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchModifyDcdnWafRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchModifyDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchModifyDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_modify_dcdn_waf_rules_with_options_async(
        self,
        request: main_models.BatchModifyDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchModifyDcdnWafRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchModifyDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchModifyDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_modify_dcdn_waf_rules(
        self,
        request: main_models.BatchModifyDcdnWafRulesRequest,
    ) -> main_models.BatchModifyDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return self.batch_modify_dcdn_waf_rules_with_options(request, runtime)

    async def batch_modify_dcdn_waf_rules_async(
        self,
        request: main_models.BatchModifyDcdnWafRulesRequest,
    ) -> main_models.BatchModifyDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return await self.batch_modify_dcdn_waf_rules_with_options_async(request, runtime)

    def batch_put_dcdn_kv_with_options(
        self,
        tmp_req: main_models.BatchPutDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchPutDcdnKvResponse:
        tmp_req.validate()
        request = main_models.BatchPutDcdnKvShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.kv_list):
            request.kv_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.kv_list, 'KvList', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.kv_list_shrink):
            body['KvList'] = request.kv_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchPutDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchPutDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_put_dcdn_kv_with_options_async(
        self,
        tmp_req: main_models.BatchPutDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchPutDcdnKvResponse:
        tmp_req.validate()
        request = main_models.BatchPutDcdnKvShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.kv_list):
            request.kv_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.kv_list, 'KvList', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.kv_list_shrink):
            body['KvList'] = request.kv_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchPutDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchPutDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_put_dcdn_kv(
        self,
        request: main_models.BatchPutDcdnKvRequest,
    ) -> main_models.BatchPutDcdnKvResponse:
        runtime = RuntimeOptions()
        return self.batch_put_dcdn_kv_with_options(request, runtime)

    async def batch_put_dcdn_kv_async(
        self,
        request: main_models.BatchPutDcdnKvRequest,
    ) -> main_models.BatchPutDcdnKvResponse:
        runtime = RuntimeOptions()
        return await self.batch_put_dcdn_kv_with_options_async(request, runtime)

    def batch_put_dcdn_kv_with_high_capacity_with_options(
        self,
        request: main_models.BatchPutDcdnKvWithHighCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchPutDcdnKvWithHighCapacityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchPutDcdnKvWithHighCapacity',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchPutDcdnKvWithHighCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_put_dcdn_kv_with_high_capacity_with_options_async(
        self,
        request: main_models.BatchPutDcdnKvWithHighCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchPutDcdnKvWithHighCapacityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchPutDcdnKvWithHighCapacity',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchPutDcdnKvWithHighCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_put_dcdn_kv_with_high_capacity(
        self,
        request: main_models.BatchPutDcdnKvWithHighCapacityRequest,
    ) -> main_models.BatchPutDcdnKvWithHighCapacityResponse:
        runtime = RuntimeOptions()
        return self.batch_put_dcdn_kv_with_high_capacity_with_options(request, runtime)

    async def batch_put_dcdn_kv_with_high_capacity_async(
        self,
        request: main_models.BatchPutDcdnKvWithHighCapacityRequest,
    ) -> main_models.BatchPutDcdnKvWithHighCapacityResponse:
        runtime = RuntimeOptions()
        return await self.batch_put_dcdn_kv_with_high_capacity_with_options_async(request, runtime)

    def batch_put_dcdn_kv_with_high_capacity_advance(
        self,
        request: main_models.BatchPutDcdnKvWithHighCapacityAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchPutDcdnKvWithHighCapacityResponse:
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
            'Product': 'dcdn',
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
        batch_put_dcdn_kv_with_high_capacity_req = main_models.BatchPutDcdnKvWithHighCapacityRequest()
        Utils.convert(request, batch_put_dcdn_kv_with_high_capacity_req)
        if not DaraCore.is_null(request.url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.url_object,
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
            batch_put_dcdn_kv_with_high_capacity_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        batch_put_dcdn_kv_with_high_capacity_resp = self.batch_put_dcdn_kv_with_high_capacity_with_options(batch_put_dcdn_kv_with_high_capacity_req, runtime)
        return batch_put_dcdn_kv_with_high_capacity_resp

    async def batch_put_dcdn_kv_with_high_capacity_advance_async(
        self,
        request: main_models.BatchPutDcdnKvWithHighCapacityAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchPutDcdnKvWithHighCapacityResponse:
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
            'Product': 'dcdn',
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
        batch_put_dcdn_kv_with_high_capacity_req = main_models.BatchPutDcdnKvWithHighCapacityRequest()
        Utils.convert(request, batch_put_dcdn_kv_with_high_capacity_req)
        if not DaraCore.is_null(request.url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.url_object,
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
            batch_put_dcdn_kv_with_high_capacity_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        batch_put_dcdn_kv_with_high_capacity_resp = await self.batch_put_dcdn_kv_with_high_capacity_with_options_async(batch_put_dcdn_kv_with_high_capacity_req, runtime)
        return batch_put_dcdn_kv_with_high_capacity_resp

    def batch_set_dcdn_domain_configs_with_options(
        self,
        request: main_models.BatchSetDcdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDcdnDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDcdnDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_dcdn_domain_configs_with_options_async(
        self,
        request: main_models.BatchSetDcdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDcdnDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDcdnDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDcdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_dcdn_domain_configs(
        self,
        request: main_models.BatchSetDcdnDomainConfigsRequest,
    ) -> main_models.BatchSetDcdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.batch_set_dcdn_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_domain_configs_async(
        self,
        request: main_models.BatchSetDcdnDomainConfigsRequest,
    ) -> main_models.BatchSetDcdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_ipa_domain_configs_with_options(
        self,
        request: main_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDcdnIpaDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDcdnIpaDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDcdnIpaDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: main_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDcdnIpaDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDcdnIpaDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDcdnIpaDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_dcdn_ipa_domain_configs(
        self,
        request: main_models.BatchSetDcdnIpaDomainConfigsRequest,
    ) -> main_models.BatchSetDcdnIpaDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.batch_set_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_ipa_domain_configs_async(
        self,
        request: main_models.BatchSetDcdnIpaDomainConfigsRequest,
    ) -> main_models.BatchSetDcdnIpaDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_waf_domain_configs_with_options(
        self,
        request: main_models.BatchSetDcdnWafDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDcdnWafDomainConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_ip_tag):
            body['ClientIpTag'] = request.client_ip_tag
        if not DaraCore.is_null(request.defense_status):
            body['DefenseStatus'] = request.defense_status
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDcdnWafDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDcdnWafDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_dcdn_waf_domain_configs_with_options_async(
        self,
        request: main_models.BatchSetDcdnWafDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDcdnWafDomainConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_ip_tag):
            body['ClientIpTag'] = request.client_ip_tag
        if not DaraCore.is_null(request.defense_status):
            body['DefenseStatus'] = request.defense_status
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDcdnWafDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDcdnWafDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_dcdn_waf_domain_configs(
        self,
        request: main_models.BatchSetDcdnWafDomainConfigsRequest,
    ) -> main_models.BatchSetDcdnWafDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.batch_set_dcdn_waf_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_waf_domain_configs_async(
        self,
        request: main_models.BatchSetDcdnWafDomainConfigsRequest,
    ) -> main_models.BatchSetDcdnWafDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_dcdn_waf_domain_configs_with_options_async(request, runtime)

    def batch_start_dcdn_domain_with_options(
        self,
        request: main_models.BatchStartDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_dcdn_domain_with_options_async(
        self,
        request: main_models.BatchStartDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_dcdn_domain(
        self,
        request: main_models.BatchStartDcdnDomainRequest,
    ) -> main_models.BatchStartDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_start_dcdn_domain_with_options(request, runtime)

    async def batch_start_dcdn_domain_async(
        self,
        request: main_models.BatchStartDcdnDomainRequest,
    ) -> main_models.BatchStartDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_start_dcdn_domain_with_options_async(request, runtime)

    def batch_stop_dcdn_domain_with_options(
        self,
        request: main_models.BatchStopDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_dcdn_domain_with_options_async(
        self,
        request: main_models.BatchStopDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_dcdn_domain(
        self,
        request: main_models.BatchStopDcdnDomainRequest,
    ) -> main_models.BatchStopDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_stop_dcdn_domain_with_options(request, runtime)

    async def batch_stop_dcdn_domain_async(
        self,
        request: main_models.BatchStopDcdnDomainRequest,
    ) -> main_models.BatchStopDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_stop_dcdn_domain_with_options_async(request, runtime)

    def check_dcdn_project_exist_with_options(
        self,
        request: main_models.CheckDcdnProjectExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDcdnProjectExistResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDcdnProjectExist',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDcdnProjectExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_dcdn_project_exist_with_options_async(
        self,
        request: main_models.CheckDcdnProjectExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDcdnProjectExistResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDcdnProjectExist',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDcdnProjectExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_dcdn_project_exist(
        self,
        request: main_models.CheckDcdnProjectExistRequest,
    ) -> main_models.CheckDcdnProjectExistResponse:
        runtime = RuntimeOptions()
        return self.check_dcdn_project_exist_with_options(request, runtime)

    async def check_dcdn_project_exist_async(
        self,
        request: main_models.CheckDcdnProjectExistRequest,
    ) -> main_models.CheckDcdnProjectExistResponse:
        runtime = RuntimeOptions()
        return await self.check_dcdn_project_exist_with_options_async(request, runtime)

    def commit_staging_routine_code_with_options(
        self,
        request: main_models.CommitStagingRoutineCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CommitStagingRoutineCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_description):
            body['CodeDescription'] = request.code_description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CommitStagingRoutineCode',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CommitStagingRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_staging_routine_code_with_options_async(
        self,
        request: main_models.CommitStagingRoutineCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CommitStagingRoutineCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_description):
            body['CodeDescription'] = request.code_description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CommitStagingRoutineCode',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CommitStagingRoutineCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_staging_routine_code(
        self,
        request: main_models.CommitStagingRoutineCodeRequest,
    ) -> main_models.CommitStagingRoutineCodeResponse:
        runtime = RuntimeOptions()
        return self.commit_staging_routine_code_with_options(request, runtime)

    async def commit_staging_routine_code_async(
        self,
        request: main_models.CommitStagingRoutineCodeRequest,
    ) -> main_models.CommitStagingRoutineCodeResponse:
        runtime = RuntimeOptions()
        return await self.commit_staging_routine_code_with_options_async(request, runtime)

    def create_dcdn_certificate_signing_request_with_options(
        self,
        request: main_models.CreateDcdnCertificateSigningRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnCertificateSigningRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.sans):
            query['SANs'] = request.sans
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnCertificateSigningRequest',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnCertificateSigningRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_certificate_signing_request_with_options_async(
        self,
        request: main_models.CreateDcdnCertificateSigningRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnCertificateSigningRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.sans):
            query['SANs'] = request.sans
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnCertificateSigningRequest',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnCertificateSigningRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_certificate_signing_request(
        self,
        request: main_models.CreateDcdnCertificateSigningRequestRequest,
    ) -> main_models.CreateDcdnCertificateSigningRequestResponse:
        runtime = RuntimeOptions()
        return self.create_dcdn_certificate_signing_request_with_options(request, runtime)

    async def create_dcdn_certificate_signing_request_async(
        self,
        request: main_models.CreateDcdnCertificateSigningRequestRequest,
    ) -> main_models.CreateDcdnCertificateSigningRequestResponse:
        runtime = RuntimeOptions()
        return await self.create_dcdn_certificate_signing_request_with_options_async(request, runtime)

    def create_dcdn_deliver_task_with_options(
        self,
        request: main_models.CreateDcdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnDeliverTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deliver):
            body['Deliver'] = request.deliver
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.reports):
            body['Reports'] = request.reports
        if not DaraCore.is_null(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnDeliverTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_deliver_task_with_options_async(
        self,
        request: main_models.CreateDcdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnDeliverTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deliver):
            body['Deliver'] = request.deliver
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.reports):
            body['Reports'] = request.reports
        if not DaraCore.is_null(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnDeliverTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_deliver_task(
        self,
        request: main_models.CreateDcdnDeliverTaskRequest,
    ) -> main_models.CreateDcdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return self.create_dcdn_deliver_task_with_options(request, runtime)

    async def create_dcdn_deliver_task_async(
        self,
        request: main_models.CreateDcdnDeliverTaskRequest,
    ) -> main_models.CreateDcdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_dcdn_deliver_task_with_options_async(request, runtime)

    def create_dcdn_slsreal_time_log_delivery_with_options(
        self,
        request: main_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.data_center):
            body['DataCenter'] = request.data_center
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not DaraCore.is_null(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not DaraCore.is_null(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not DaraCore.is_null(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnSLSRealTimeLogDelivery',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnSLSRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_slsreal_time_log_delivery_with_options_async(
        self,
        request: main_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.data_center):
            body['DataCenter'] = request.data_center
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not DaraCore.is_null(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not DaraCore.is_null(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not DaraCore.is_null(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnSLSRealTimeLogDelivery',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnSLSRealTimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_slsreal_time_log_delivery(
        self,
        request: main_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
    ) -> main_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.create_dcdn_slsreal_time_log_delivery_with_options(request, runtime)

    async def create_dcdn_slsreal_time_log_delivery_async(
        self,
        request: main_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
    ) -> main_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.create_dcdn_slsreal_time_log_delivery_with_options_async(request, runtime)

    def create_dcdn_sub_task_with_options(
        self,
        request: main_models.CreateDcdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnSubTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.report_ids):
            body['ReportIds'] = request.report_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnSubTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_sub_task_with_options_async(
        self,
        request: main_models.CreateDcdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnSubTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.report_ids):
            body['ReportIds'] = request.report_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnSubTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_sub_task(
        self,
        request: main_models.CreateDcdnSubTaskRequest,
    ) -> main_models.CreateDcdnSubTaskResponse:
        runtime = RuntimeOptions()
        return self.create_dcdn_sub_task_with_options(request, runtime)

    async def create_dcdn_sub_task_async(
        self,
        request: main_models.CreateDcdnSubTaskRequest,
    ) -> main_models.CreateDcdnSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_dcdn_sub_task_with_options_async(request, runtime)

    def create_dcdn_waf_group_with_options(
        self,
        request: main_models.CreateDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnWafGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.subscribe):
            body['Subscribe'] = request.subscribe
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnWafGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_waf_group_with_options_async(
        self,
        request: main_models.CreateDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnWafGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.subscribe):
            body['Subscribe'] = request.subscribe
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnWafGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_waf_group(
        self,
        request: main_models.CreateDcdnWafGroupRequest,
    ) -> main_models.CreateDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return self.create_dcdn_waf_group_with_options(request, runtime)

    async def create_dcdn_waf_group_async(
        self,
        request: main_models.CreateDcdnWafGroupRequest,
    ) -> main_models.CreateDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_dcdn_waf_group_with_options_async(request, runtime)

    def create_dcdn_waf_policy_with_options(
        self,
        request: main_models.CreateDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnWafPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.defense_scene):
            body['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_waf_policy_with_options_async(
        self,
        request: main_models.CreateDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDcdnWafPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.defense_scene):
            body['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_waf_policy(
        self,
        request: main_models.CreateDcdnWafPolicyRequest,
    ) -> main_models.CreateDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_dcdn_waf_policy_with_options(request, runtime)

    async def create_dcdn_waf_policy_async(
        self,
        request: main_models.CreateDcdnWafPolicyRequest,
    ) -> main_models.CreateDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_dcdn_waf_policy_with_options_async(request, runtime)

    def create_routine_with_options(
        self,
        tmp_req: main_models.CreateRoutineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoutineResponse:
        tmp_req.validate()
        request = main_models.CreateRoutineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.env_conf):
            request.env_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRoutine',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_routine_with_options_async(
        self,
        tmp_req: main_models.CreateRoutineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoutineResponse:
        tmp_req.validate()
        request = main_models.CreateRoutineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.env_conf):
            request.env_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRoutine',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_routine(
        self,
        request: main_models.CreateRoutineRequest,
    ) -> main_models.CreateRoutineResponse:
        runtime = RuntimeOptions()
        return self.create_routine_with_options(request, runtime)

    async def create_routine_async(
        self,
        request: main_models.CreateRoutineRequest,
    ) -> main_models.CreateRoutineResponse:
        runtime = RuntimeOptions()
        return await self.create_routine_with_options_async(request, runtime)

    def create_slr_and_sls_project_with_options(
        self,
        request: main_models.CreateSlrAndSlsProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlrAndSlsProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlrAndSlsProject',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlrAndSlsProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slr_and_sls_project_with_options_async(
        self,
        request: main_models.CreateSlrAndSlsProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlrAndSlsProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlrAndSlsProject',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlrAndSlsProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slr_and_sls_project(
        self,
        request: main_models.CreateSlrAndSlsProjectRequest,
    ) -> main_models.CreateSlrAndSlsProjectResponse:
        runtime = RuntimeOptions()
        return self.create_slr_and_sls_project_with_options(request, runtime)

    async def create_slr_and_sls_project_async(
        self,
        request: main_models.CreateSlrAndSlsProjectRequest,
    ) -> main_models.CreateSlrAndSlsProjectResponse:
        runtime = RuntimeOptions()
        return await self.create_slr_and_sls_project_with_options_async(request, runtime)

    def delete_custom_domain_sample_rate_with_options(
        self,
        request: main_models.DeleteCustomDomainSampleRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomDomainSampleRateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomDomainSampleRate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomDomainSampleRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_domain_sample_rate_with_options_async(
        self,
        request: main_models.DeleteCustomDomainSampleRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomDomainSampleRateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomDomainSampleRate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomDomainSampleRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_domain_sample_rate(
        self,
        request: main_models.DeleteCustomDomainSampleRateRequest,
    ) -> main_models.DeleteCustomDomainSampleRateResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_domain_sample_rate_with_options(request, runtime)

    async def delete_custom_domain_sample_rate_async(
        self,
        request: main_models.DeleteCustomDomainSampleRateRequest,
    ) -> main_models.DeleteCustomDomainSampleRateResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_domain_sample_rate_with_options_async(request, runtime)

    def delete_dcdn_deliver_task_with_options(
        self,
        request: main_models.DeleteDcdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnDeliverTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnDeliverTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_deliver_task_with_options_async(
        self,
        request: main_models.DeleteDcdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnDeliverTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnDeliverTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_deliver_task(
        self,
        request: main_models.DeleteDcdnDeliverTaskRequest,
    ) -> main_models.DeleteDcdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_deliver_task_with_options(request, runtime)

    async def delete_dcdn_deliver_task_async(
        self,
        request: main_models.DeleteDcdnDeliverTaskRequest,
    ) -> main_models.DeleteDcdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_deliver_task_with_options_async(request, runtime)

    def delete_dcdn_domain_with_options(
        self,
        request: main_models.DeleteDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_domain_with_options_async(
        self,
        request: main_models.DeleteDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_domain(
        self,
        request: main_models.DeleteDcdnDomainRequest,
    ) -> main_models.DeleteDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_domain_with_options(request, runtime)

    async def delete_dcdn_domain_async(
        self,
        request: main_models.DeleteDcdnDomainRequest,
    ) -> main_models.DeleteDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_domain_with_options(
        self,
        request: main_models.DeleteDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_ipa_domain_with_options_async(
        self,
        request: main_models.DeleteDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_ipa_domain(
        self,
        request: main_models.DeleteDcdnIpaDomainRequest,
    ) -> main_models.DeleteDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_ipa_domain_with_options(request, runtime)

    async def delete_dcdn_ipa_domain_async(
        self,
        request: main_models.DeleteDcdnIpaDomainRequest,
    ) -> main_models.DeleteDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_ipa_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_specific_config_with_options(
        self,
        request: main_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnIpaSpecificConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnIpaSpecificConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnIpaSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_ipa_specific_config_with_options_async(
        self,
        request: main_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnIpaSpecificConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnIpaSpecificConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnIpaSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_ipa_specific_config(
        self,
        request: main_models.DeleteDcdnIpaSpecificConfigRequest,
    ) -> main_models.DeleteDcdnIpaSpecificConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_ipa_specific_config_with_options(request, runtime)

    async def delete_dcdn_ipa_specific_config_async(
        self,
        request: main_models.DeleteDcdnIpaSpecificConfigRequest,
    ) -> main_models.DeleteDcdnIpaSpecificConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_ipa_specific_config_with_options_async(request, runtime)

    def delete_dcdn_kv_with_options(
        self,
        request: main_models.DeleteDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnKvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_kv_with_options_async(
        self,
        request: main_models.DeleteDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnKvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_kv(
        self,
        request: main_models.DeleteDcdnKvRequest,
    ) -> main_models.DeleteDcdnKvResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_kv_with_options(request, runtime)

    async def delete_dcdn_kv_async(
        self,
        request: main_models.DeleteDcdnKvRequest,
    ) -> main_models.DeleteDcdnKvResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_kv_with_options_async(request, runtime)

    def delete_dcdn_kv_namespace_with_options(
        self,
        request: main_models.DeleteDcdnKvNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnKvNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnKvNamespace',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_kv_namespace_with_options_async(
        self,
        request: main_models.DeleteDcdnKvNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnKvNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnKvNamespace',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_kv_namespace(
        self,
        request: main_models.DeleteDcdnKvNamespaceRequest,
    ) -> main_models.DeleteDcdnKvNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_kv_namespace_with_options(request, runtime)

    async def delete_dcdn_kv_namespace_async(
        self,
        request: main_models.DeleteDcdnKvNamespaceRequest,
    ) -> main_models.DeleteDcdnKvNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_kv_namespace_with_options_async(request, runtime)

    def delete_dcdn_real_time_log_project_with_options(
        self,
        request: main_models.DeleteDcdnRealTimeLogProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnRealTimeLogProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnRealTimeLogProject',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnRealTimeLogProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_real_time_log_project_with_options_async(
        self,
        request: main_models.DeleteDcdnRealTimeLogProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnRealTimeLogProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnRealTimeLogProject',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnRealTimeLogProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_real_time_log_project(
        self,
        request: main_models.DeleteDcdnRealTimeLogProjectRequest,
    ) -> main_models.DeleteDcdnRealTimeLogProjectResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_real_time_log_project_with_options(request, runtime)

    async def delete_dcdn_real_time_log_project_async(
        self,
        request: main_models.DeleteDcdnRealTimeLogProjectRequest,
    ) -> main_models.DeleteDcdnRealTimeLogProjectResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_real_time_log_project_with_options_async(request, runtime)

    def delete_dcdn_specific_config_with_options(
        self,
        request: main_models.DeleteDcdnSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnSpecificConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnSpecificConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_specific_config_with_options_async(
        self,
        request: main_models.DeleteDcdnSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnSpecificConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnSpecificConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_specific_config(
        self,
        request: main_models.DeleteDcdnSpecificConfigRequest,
    ) -> main_models.DeleteDcdnSpecificConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_specific_config_with_options(request, runtime)

    async def delete_dcdn_specific_config_async(
        self,
        request: main_models.DeleteDcdnSpecificConfigRequest,
    ) -> main_models.DeleteDcdnSpecificConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_specific_config_with_options_async(request, runtime)

    def delete_dcdn_specific_staging_config_with_options(
        self,
        request: main_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnSpecificStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnSpecificStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_specific_staging_config_with_options_async(
        self,
        request: main_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnSpecificStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnSpecificStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnSpecificStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_specific_staging_config(
        self,
        request: main_models.DeleteDcdnSpecificStagingConfigRequest,
    ) -> main_models.DeleteDcdnSpecificStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_specific_staging_config_with_options(request, runtime)

    async def delete_dcdn_specific_staging_config_async(
        self,
        request: main_models.DeleteDcdnSpecificStagingConfigRequest,
    ) -> main_models.DeleteDcdnSpecificStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_specific_staging_config_with_options_async(request, runtime)

    def delete_dcdn_sub_task_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnSubTaskResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DeleteDcdnSubTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_sub_task_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnSubTaskResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DeleteDcdnSubTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_sub_task(self) -> main_models.DeleteDcdnSubTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_sub_task_with_options(runtime)

    async def delete_dcdn_sub_task_async(self) -> main_models.DeleteDcdnSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_sub_task_with_options_async(runtime)

    def delete_dcdn_user_config_with_options(
        self,
        request: main_models.DeleteDcdnUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnUserConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_user_config_with_options_async(
        self,
        request: main_models.DeleteDcdnUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnUserConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_user_config(
        self,
        request: main_models.DeleteDcdnUserConfigRequest,
    ) -> main_models.DeleteDcdnUserConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_user_config_with_options(request, runtime)

    async def delete_dcdn_user_config_async(
        self,
        request: main_models.DeleteDcdnUserConfigRequest,
    ) -> main_models.DeleteDcdnUserConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_user_config_with_options_async(request, runtime)

    def delete_dcdn_waf_group_with_options(
        self,
        request: main_models.DeleteDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnWafGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnWafGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_waf_group_with_options_async(
        self,
        request: main_models.DeleteDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnWafGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnWafGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_waf_group(
        self,
        request: main_models.DeleteDcdnWafGroupRequest,
    ) -> main_models.DeleteDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_waf_group_with_options(request, runtime)

    async def delete_dcdn_waf_group_async(
        self,
        request: main_models.DeleteDcdnWafGroupRequest,
    ) -> main_models.DeleteDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_waf_group_with_options_async(request, runtime)

    def delete_dcdn_waf_policy_with_options(
        self,
        request: main_models.DeleteDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnWafPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_waf_policy_with_options_async(
        self,
        request: main_models.DeleteDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDcdnWafPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_waf_policy(
        self,
        request: main_models.DeleteDcdnWafPolicyRequest,
    ) -> main_models.DeleteDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_dcdn_waf_policy_with_options(request, runtime)

    async def delete_dcdn_waf_policy_async(
        self,
        request: main_models.DeleteDcdnWafPolicyRequest,
    ) -> main_models.DeleteDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_dcdn_waf_policy_with_options_async(request, runtime)

    def delete_routine_with_options(
        self,
        request: main_models.DeleteRoutineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoutineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoutine',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_with_options_async(
        self,
        request: main_models.DeleteRoutineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoutineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoutine',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine(
        self,
        request: main_models.DeleteRoutineRequest,
    ) -> main_models.DeleteRoutineResponse:
        runtime = RuntimeOptions()
        return self.delete_routine_with_options(request, runtime)

    async def delete_routine_async(
        self,
        request: main_models.DeleteRoutineRequest,
    ) -> main_models.DeleteRoutineResponse:
        runtime = RuntimeOptions()
        return await self.delete_routine_with_options_async(request, runtime)

    def delete_routine_code_revision_with_options(
        self,
        request: main_models.DeleteRoutineCodeRevisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoutineCodeRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoutineCodeRevision',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_code_revision_with_options_async(
        self,
        request: main_models.DeleteRoutineCodeRevisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoutineCodeRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoutineCodeRevision',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoutineCodeRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine_code_revision(
        self,
        request: main_models.DeleteRoutineCodeRevisionRequest,
    ) -> main_models.DeleteRoutineCodeRevisionResponse:
        runtime = RuntimeOptions()
        return self.delete_routine_code_revision_with_options(request, runtime)

    async def delete_routine_code_revision_async(
        self,
        request: main_models.DeleteRoutineCodeRevisionRequest,
    ) -> main_models.DeleteRoutineCodeRevisionResponse:
        runtime = RuntimeOptions()
        return await self.delete_routine_code_revision_with_options_async(request, runtime)

    def delete_routine_conf_envs_with_options(
        self,
        tmp_req: main_models.DeleteRoutineConfEnvsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoutineConfEnvsResponse:
        tmp_req.validate()
        request = main_models.DeleteRoutineConfEnvsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.envs):
            request.envs_shrink = Utils.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not DaraCore.is_null(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoutineConfEnvs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoutineConfEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_conf_envs_with_options_async(
        self,
        tmp_req: main_models.DeleteRoutineConfEnvsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoutineConfEnvsResponse:
        tmp_req.validate()
        request = main_models.DeleteRoutineConfEnvsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.envs):
            request.envs_shrink = Utils.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not DaraCore.is_null(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRoutineConfEnvs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoutineConfEnvsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine_conf_envs(
        self,
        request: main_models.DeleteRoutineConfEnvsRequest,
    ) -> main_models.DeleteRoutineConfEnvsResponse:
        runtime = RuntimeOptions()
        return self.delete_routine_conf_envs_with_options(request, runtime)

    async def delete_routine_conf_envs_async(
        self,
        request: main_models.DeleteRoutineConfEnvsRequest,
    ) -> main_models.DeleteRoutineConfEnvsResponse:
        runtime = RuntimeOptions()
        return await self.delete_routine_conf_envs_with_options_async(request, runtime)

    def describe_custom_domain_sample_rate_with_options(
        self,
        request: main_models.DescribeCustomDomainSampleRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomDomainSampleRateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomDomainSampleRate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomDomainSampleRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_domain_sample_rate_with_options_async(
        self,
        request: main_models.DescribeCustomDomainSampleRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomDomainSampleRateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomDomainSampleRate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomDomainSampleRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_domain_sample_rate(
        self,
        request: main_models.DescribeCustomDomainSampleRateRequest,
    ) -> main_models.DescribeCustomDomainSampleRateResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_domain_sample_rate_with_options(request, runtime)

    async def describe_custom_domain_sample_rate_async(
        self,
        request: main_models.DescribeCustomDomainSampleRateRequest,
    ) -> main_models.DescribeCustomDomainSampleRateResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_domain_sample_rate_with_options_async(request, runtime)

    def describe_dcdn_acl_fields_with_options(
        self,
        request: main_models.DescribeDcdnAclFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnAclFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnAclFields',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnAclFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_acl_fields_with_options_async(
        self,
        request: main_models.DescribeDcdnAclFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnAclFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnAclFields',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnAclFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_acl_fields(
        self,
        request: main_models.DescribeDcdnAclFieldsRequest,
    ) -> main_models.DescribeDcdnAclFieldsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_acl_fields_with_options(request, runtime)

    async def describe_dcdn_acl_fields_async(
        self,
        request: main_models.DescribeDcdnAclFieldsRequest,
    ) -> main_models.DescribeDcdnAclFieldsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_acl_fields_with_options_async(request, runtime)

    def describe_dcdn_bgp_bps_data_with_options(
        self,
        request: main_models.DescribeDcdnBgpBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnBgpBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.device_port):
            query['DevicePort'] = request.device_port
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnBgpBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnBgpBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_bgp_bps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnBgpBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnBgpBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.device_port):
            query['DevicePort'] = request.device_port
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnBgpBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnBgpBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_bgp_bps_data(
        self,
        request: main_models.DescribeDcdnBgpBpsDataRequest,
    ) -> main_models.DescribeDcdnBgpBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_bgp_bps_data_with_options(request, runtime)

    async def describe_dcdn_bgp_bps_data_async(
        self,
        request: main_models.DescribeDcdnBgpBpsDataRequest,
    ) -> main_models.DescribeDcdnBgpBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_bgp_bps_data_with_options_async(request, runtime)

    def describe_dcdn_bgp_traffic_data_with_options(
        self,
        request: main_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnBgpTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnBgpTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnBgpTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_bgp_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnBgpTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnBgpTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnBgpTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_bgp_traffic_data(
        self,
        request: main_models.DescribeDcdnBgpTrafficDataRequest,
    ) -> main_models.DescribeDcdnBgpTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_bgp_traffic_data_with_options(request, runtime)

    async def describe_dcdn_bgp_traffic_data_async(
        self,
        request: main_models.DescribeDcdnBgpTrafficDataRequest,
    ) -> main_models.DescribeDcdnBgpTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_bgp_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_blocked_regions_with_options(
        self,
        request: main_models.DescribeDcdnBlockedRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnBlockedRegionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnBlockedRegions',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnBlockedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_blocked_regions_with_options_async(
        self,
        request: main_models.DescribeDcdnBlockedRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnBlockedRegionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnBlockedRegions',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnBlockedRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_blocked_regions(
        self,
        request: main_models.DescribeDcdnBlockedRegionsRequest,
    ) -> main_models.DescribeDcdnBlockedRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_blocked_regions_with_options(request, runtime)

    async def describe_dcdn_blocked_regions_async(
        self,
        request: main_models.DescribeDcdnBlockedRegionsRequest,
    ) -> main_models.DescribeDcdnBlockedRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_blocked_regions_with_options_async(request, runtime)

    def describe_dcdn_certificate_detail_with_options(
        self,
        request: main_models.DescribeDcdnCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnCertificateDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_certificate_detail_with_options_async(
        self,
        request: main_models.DescribeDcdnCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnCertificateDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_certificate_detail(
        self,
        request: main_models.DescribeDcdnCertificateDetailRequest,
    ) -> main_models.DescribeDcdnCertificateDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_certificate_detail_with_options(request, runtime)

    async def describe_dcdn_certificate_detail_async(
        self,
        request: main_models.DescribeDcdnCertificateDetailRequest,
    ) -> main_models.DescribeDcdnCertificateDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_certificate_detail_with_options_async(request, runtime)

    def describe_dcdn_certificate_list_with_options(
        self,
        request: main_models.DescribeDcdnCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnCertificateList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_certificate_list_with_options_async(
        self,
        request: main_models.DescribeDcdnCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnCertificateList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_certificate_list(
        self,
        request: main_models.DescribeDcdnCertificateListRequest,
    ) -> main_models.DescribeDcdnCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_certificate_list_with_options(request, runtime)

    async def describe_dcdn_certificate_list_async(
        self,
        request: main_models.DescribeDcdnCertificateListRequest,
    ) -> main_models.DescribeDcdnCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_certificate_list_with_options_async(request, runtime)

    def describe_dcdn_ddos_service_with_options(
        self,
        request: main_models.DescribeDcdnDdosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDdosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDdosService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDdosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ddos_service_with_options_async(
        self,
        request: main_models.DescribeDcdnDdosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDdosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDdosService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDdosServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ddos_service(
        self,
        request: main_models.DescribeDcdnDdosServiceRequest,
    ) -> main_models.DescribeDcdnDdosServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ddos_service_with_options(request, runtime)

    async def describe_dcdn_ddos_service_async(
        self,
        request: main_models.DescribeDcdnDdosServiceRequest,
    ) -> main_models.DescribeDcdnDdosServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ddos_service_with_options_async(request, runtime)

    def describe_dcdn_ddos_spec_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDdosSpecInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDdosSpecInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDdosSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ddos_spec_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDdosSpecInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDdosSpecInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDdosSpecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ddos_spec_info(self) -> main_models.DescribeDcdnDdosSpecInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ddos_spec_info_with_options(runtime)

    async def describe_dcdn_ddos_spec_info_async(self) -> main_models.DescribeDcdnDdosSpecInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ddos_spec_info_with_options_async(runtime)

    def describe_dcdn_deleted_domains_with_options(
        self,
        request: main_models.DescribeDcdnDeletedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDeletedDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDeletedDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDeletedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_deleted_domains_with_options_async(
        self,
        request: main_models.DescribeDcdnDeletedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDeletedDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDeletedDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDeletedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_deleted_domains(
        self,
        request: main_models.DescribeDcdnDeletedDomainsRequest,
    ) -> main_models.DescribeDcdnDeletedDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_deleted_domains_with_options(request, runtime)

    async def describe_dcdn_deleted_domains_async(
        self,
        request: main_models.DescribeDcdnDeletedDomainsRequest,
    ) -> main_models.DescribeDcdnDeletedDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_deleted_domains_with_options_async(request, runtime)

    def describe_dcdn_deliver_list_with_options(
        self,
        request: main_models.DescribeDcdnDeliverListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDeliverListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDeliverList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDeliverListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_deliver_list_with_options_async(
        self,
        request: main_models.DescribeDcdnDeliverListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDeliverListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDeliverList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDeliverListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_deliver_list(
        self,
        request: main_models.DescribeDcdnDeliverListRequest,
    ) -> main_models.DescribeDcdnDeliverListResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_deliver_list_with_options(request, runtime)

    async def describe_dcdn_deliver_list_async(
        self,
        request: main_models.DescribeDcdnDeliverListRequest,
    ) -> main_models.DescribeDcdnDeliverListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_deliver_list_with_options_async(request, runtime)

    def describe_dcdn_domain_bps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_bps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_bps_data(
        self,
        request: main_models.DescribeDcdnDomainBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_bps_data_async(
        self,
        request: main_models.DescribeDcdnDomainBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_bps_data_by_layer_with_options(
        self,
        request: main_models.DescribeDcdnDomainBpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainBpsDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainBpsDataByLayer',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_bps_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainBpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainBpsDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainBpsDataByLayer',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainBpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_bps_data_by_layer(
        self,
        request: main_models.DescribeDcdnDomainBpsDataByLayerRequest,
    ) -> main_models.DescribeDcdnDomainBpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_by_layer_with_options(request, runtime)

    async def describe_dcdn_domain_bps_data_by_layer_async(
        self,
        request: main_models.DescribeDcdnDomainBpsDataByLayerRequest,
    ) -> main_models.DescribeDcdnDomainBpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_bps_data_by_layer_with_options_async(request, runtime)

    def describe_dcdn_domain_by_certificate_with_options(
        self,
        request: main_models.DescribeDcdnDomainByCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainByCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exact):
            query['Exact'] = request.exact
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.sslstatus):
            query['SSLStatus'] = request.sslstatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainByCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainByCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_by_certificate_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainByCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainByCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exact):
            query['Exact'] = request.exact
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.sslstatus):
            query['SSLStatus'] = request.sslstatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainByCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainByCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_by_certificate(
        self,
        request: main_models.DescribeDcdnDomainByCertificateRequest,
    ) -> main_models.DescribeDcdnDomainByCertificateResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_by_certificate_with_options(request, runtime)

    async def describe_dcdn_domain_by_certificate_async(
        self,
        request: main_models.DescribeDcdnDomainByCertificateRequest,
    ) -> main_models.DescribeDcdnDomainByCertificateResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_by_certificate_with_options_async(request, runtime)

    def describe_dcdn_domain_cc_activity_log_with_options(
        self,
        request: main_models.DescribeDcdnDomainCcActivityLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainCcActivityLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trigger_object):
            query['TriggerObject'] = request.trigger_object
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainCcActivityLog',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainCcActivityLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_cc_activity_log_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainCcActivityLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainCcActivityLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trigger_object):
            query['TriggerObject'] = request.trigger_object
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainCcActivityLog',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainCcActivityLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_cc_activity_log(
        self,
        request: main_models.DescribeDcdnDomainCcActivityLogRequest,
    ) -> main_models.DescribeDcdnDomainCcActivityLogResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_cc_activity_log_with_options(request, runtime)

    async def describe_dcdn_domain_cc_activity_log_async(
        self,
        request: main_models.DescribeDcdnDomainCcActivityLogRequest,
    ) -> main_models.DescribeDcdnDomainCcActivityLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_cc_activity_log_with_options_async(request, runtime)

    def describe_dcdn_domain_certificate_info_with_options(
        self,
        request: main_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainCertificateInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_certificate_info_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainCertificateInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_certificate_info(
        self,
        request: main_models.DescribeDcdnDomainCertificateInfoRequest,
    ) -> main_models.DescribeDcdnDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_certificate_info_with_options(request, runtime)

    async def describe_dcdn_domain_certificate_info_async(
        self,
        request: main_models.DescribeDcdnDomainCertificateInfoRequest,
    ) -> main_models.DescribeDcdnDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_certificate_info_with_options_async(request, runtime)

    def describe_dcdn_domain_cname_with_options(
        self,
        request: main_models.DescribeDcdnDomainCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainCnameResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainCname',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_cname_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainCnameResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainCname',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_cname(
        self,
        request: main_models.DescribeDcdnDomainCnameRequest,
    ) -> main_models.DescribeDcdnDomainCnameResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_cname_with_options(request, runtime)

    async def describe_dcdn_domain_cname_async(
        self,
        request: main_models.DescribeDcdnDomainCnameRequest,
    ) -> main_models.DescribeDcdnDomainCnameResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_cname_with_options_async(request, runtime)

    def describe_dcdn_domain_configs_with_options(
        self,
        request: main_models.DescribeDcdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_configs_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_configs(
        self,
        request: main_models.DescribeDcdnDomainConfigsRequest,
    ) -> main_models.DescribeDcdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_configs_with_options(request, runtime)

    async def describe_dcdn_domain_configs_async(
        self,
        request: main_models.DescribeDcdnDomainConfigsRequest,
    ) -> main_models.DescribeDcdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_domain_detail_with_options(
        self,
        request: main_models.DescribeDcdnDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_detail_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_detail(
        self,
        request: main_models.DescribeDcdnDomainDetailRequest,
    ) -> main_models.DescribeDcdnDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_detail_with_options(request, runtime)

    async def describe_dcdn_domain_detail_async(
        self,
        request: main_models.DescribeDcdnDomainDetailRequest,
    ) -> main_models.DescribeDcdnDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_domain_hit_rate_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainHitRateDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainHitRateData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainHitRateDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainHitRateData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_hit_rate_data(
        self,
        request: main_models.DescribeDcdnDomainHitRateDataRequest,
    ) -> main_models.DescribeDcdnDomainHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_hit_rate_data_async(
        self,
        request: main_models.DescribeDcdnDomainHitRateDataRequest,
    ) -> main_models.DescribeDcdnDomainHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_http_code_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_http_code_data(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_http_code_data_async(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_http_code_data_by_layer_with_options(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainHttpCodeDataByLayer',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainHttpCodeDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_http_code_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainHttpCodeDataByLayer',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainHttpCodeDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_http_code_data_by_layer(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_by_layer_with_options(request, runtime)

    async def describe_dcdn_domain_http_code_data_by_layer_async(
        self,
        request: main_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
    ) -> main_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_http_code_data_by_layer_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_bps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIpaBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIpaBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIpaBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_ipa_bps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIpaBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIpaBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIpaBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_bps_data(
        self,
        request: main_models.DescribeDcdnDomainIpaBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainIpaBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_ipa_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_bps_data_async(
        self,
        request: main_models.DescribeDcdnDomainIpaBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainIpaBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_conn_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainIpaConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIpaConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIpaConnData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIpaConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_ipa_conn_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainIpaConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIpaConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIpaConnData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIpaConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_conn_data(
        self,
        request: main_models.DescribeDcdnDomainIpaConnDataRequest,
    ) -> main_models.DescribeDcdnDomainIpaConnDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_ipa_conn_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_conn_data_async(
        self,
        request: main_models.DescribeDcdnDomainIpaConnDataRequest,
    ) -> main_models.DescribeDcdnDomainIpaConnDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_conn_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_traffic_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIpaTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIpaTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_ipa_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIpaTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIpaTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_traffic_data(
        self,
        request: main_models.DescribeDcdnDomainIpaTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainIpaTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_ipa_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_traffic_data_async(
        self,
        request: main_models.DescribeDcdnDomainIpaTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainIpaTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_isp_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainIspDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIspDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIspData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIspDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_isp_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainIspDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainIspDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainIspData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainIspDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_isp_data(
        self,
        request: main_models.DescribeDcdnDomainIspDataRequest,
    ) -> main_models.DescribeDcdnDomainIspDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_isp_data_with_options(request, runtime)

    async def describe_dcdn_domain_isp_data_async(
        self,
        request: main_models.DescribeDcdnDomainIspDataRequest,
    ) -> main_models.DescribeDcdnDomainIspDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_isp_data_with_options_async(request, runtime)

    def describe_dcdn_domain_log_with_options(
        self,
        request: main_models.DescribeDcdnDomainLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainLog',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_log_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainLog',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_log(
        self,
        request: main_models.DescribeDcdnDomainLogRequest,
    ) -> main_models.DescribeDcdnDomainLogResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_log_with_options(request, runtime)

    async def describe_dcdn_domain_log_async(
        self,
        request: main_models.DescribeDcdnDomainLogRequest,
    ) -> main_models.DescribeDcdnDomainLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_log_with_options_async(request, runtime)

    def describe_dcdn_domain_log_ex_ttl_with_options(
        self,
        request: main_models.DescribeDcdnDomainLogExTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainLogExTtlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainLogExTtl',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainLogExTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_log_ex_ttl_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainLogExTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainLogExTtlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainLogExTtl',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainLogExTtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_log_ex_ttl(
        self,
        request: main_models.DescribeDcdnDomainLogExTtlRequest,
    ) -> main_models.DescribeDcdnDomainLogExTtlResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_log_ex_ttl_with_options(request, runtime)

    async def describe_dcdn_domain_log_ex_ttl_async(
        self,
        request: main_models.DescribeDcdnDomainLogExTtlRequest,
    ) -> main_models.DescribeDcdnDomainLogExTtlResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_log_ex_ttl_with_options_async(request, runtime)

    def describe_dcdn_domain_multi_usage_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainMultiUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainMultiUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainMultiUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_multi_usage_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainMultiUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainMultiUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainMultiUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_multi_usage_data(
        self,
        request: main_models.DescribeDcdnDomainMultiUsageDataRequest,
    ) -> main_models.DescribeDcdnDomainMultiUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_multi_usage_data_with_options(request, runtime)

    async def describe_dcdn_domain_multi_usage_data_async(
        self,
        request: main_models.DescribeDcdnDomainMultiUsageDataRequest,
    ) -> main_models.DescribeDcdnDomainMultiUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_multi_usage_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_bps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainOriginBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainOriginBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainOriginBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_origin_bps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainOriginBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainOriginBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainOriginBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_origin_bps_data(
        self,
        request: main_models.DescribeDcdnDomainOriginBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainOriginBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_origin_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_bps_data_async(
        self,
        request: main_models.DescribeDcdnDomainOriginBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainOriginBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_origin_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_traffic_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainOriginTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainOriginTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_origin_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainOriginTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainOriginTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_origin_traffic_data(
        self,
        request: main_models.DescribeDcdnDomainOriginTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainOriginTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_origin_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_traffic_data_async(
        self,
        request: main_models.DescribeDcdnDomainOriginTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainOriginTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_origin_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_property_with_options(
        self,
        request: main_models.DescribeDcdnDomainPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainProperty',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_property_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainProperty',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_property(
        self,
        request: main_models.DescribeDcdnDomainPropertyRequest,
    ) -> main_models.DescribeDcdnDomainPropertyResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_property_with_options(request, runtime)

    async def describe_dcdn_domain_property_async(
        self,
        request: main_models.DescribeDcdnDomainPropertyRequest,
    ) -> main_models.DescribeDcdnDomainPropertyResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_property_with_options_async(request, runtime)

    def describe_dcdn_domain_pv_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainPvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainPvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainPvData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_pv_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainPvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainPvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainPvData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainPvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_pv_data(
        self,
        request: main_models.DescribeDcdnDomainPvDataRequest,
    ) -> main_models.DescribeDcdnDomainPvDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_pv_data_with_options(request, runtime)

    async def describe_dcdn_domain_pv_data_async(
        self,
        request: main_models.DescribeDcdnDomainPvDataRequest,
    ) -> main_models.DescribeDcdnDomainPvDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_pv_data_with_options_async(request, runtime)

    def describe_dcdn_domain_qps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainQpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_qps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainQpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_qps_data(
        self,
        request: main_models.DescribeDcdnDomainQpsDataRequest,
    ) -> main_models.DescribeDcdnDomainQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_qps_data_async(
        self,
        request: main_models.DescribeDcdnDomainQpsDataRequest,
    ) -> main_models.DescribeDcdnDomainQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_qps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_qps_data_by_layer_with_options(
        self,
        request: main_models.DescribeDcdnDomainQpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainQpsDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainQpsDataByLayer',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainQpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_qps_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainQpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainQpsDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainQpsDataByLayer',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainQpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_qps_data_by_layer(
        self,
        request: main_models.DescribeDcdnDomainQpsDataByLayerRequest,
    ) -> main_models.DescribeDcdnDomainQpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_by_layer_with_options(request, runtime)

    async def describe_dcdn_domain_qps_data_by_layer_async(
        self,
        request: main_models.DescribeDcdnDomainQpsDataByLayerRequest,
    ) -> main_models.DescribeDcdnDomainQpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_qps_data_by_layer_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_bps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_bps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_bps_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_bps_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeByteHitRateData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeByteHitRateData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_byte_hit_rate_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_detail_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeDetailData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_detail_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeDetailData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_detail_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeDetailDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_detail_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeDetailDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_http_code_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_http_code_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_http_code_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_qps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeQpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_qps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeQpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_qps_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeQpsDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_qps_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeQpsDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeReqHitRateData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeReqHitRateData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_req_hit_rate_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_req_hit_rate_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_bps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeSrcBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_bps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeSrcBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_bps_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_bps_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_http_code_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeSrcHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeSrcHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_http_code_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_http_code_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_traffic_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeSrcTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeSrcTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_traffic_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_traffic_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_traffic_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRealTimeTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_traffic_data(
        self,
        request: main_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_traffic_data_async(
        self,
        request: main_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_region_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainRegionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRegionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRegionData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_region_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainRegionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainRegionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainRegionData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_region_data(
        self,
        request: main_models.DescribeDcdnDomainRegionDataRequest,
    ) -> main_models.DescribeDcdnDomainRegionDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_region_data_with_options(request, runtime)

    async def describe_dcdn_domain_region_data_async(
        self,
        request: main_models.DescribeDcdnDomainRegionDataRequest,
    ) -> main_models.DescribeDcdnDomainRegionDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_region_data_with_options_async(request, runtime)

    def describe_dcdn_domain_staging_config_with_options(
        self,
        request: main_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_staging_config_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_staging_config(
        self,
        request: main_models.DescribeDcdnDomainStagingConfigRequest,
    ) -> main_models.DescribeDcdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_staging_config_with_options(request, runtime)

    async def describe_dcdn_domain_staging_config_async(
        self,
        request: main_models.DescribeDcdnDomainStagingConfigRequest,
    ) -> main_models.DescribeDcdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_staging_config_with_options_async(request, runtime)

    def describe_dcdn_domain_top_refer_visit_with_options(
        self,
        request: main_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainTopReferVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainTopReferVisit',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_top_refer_visit_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainTopReferVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainTopReferVisit',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainTopReferVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_top_refer_visit(
        self,
        request: main_models.DescribeDcdnDomainTopReferVisitRequest,
    ) -> main_models.DescribeDcdnDomainTopReferVisitResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_top_refer_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_refer_visit_async(
        self,
        request: main_models.DescribeDcdnDomainTopReferVisitRequest,
    ) -> main_models.DescribeDcdnDomainTopReferVisitResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_top_url_visit_with_options(
        self,
        request: main_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainTopUrlVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainTopUrlVisit',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_top_url_visit_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainTopUrlVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainTopUrlVisit',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainTopUrlVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_top_url_visit(
        self,
        request: main_models.DescribeDcdnDomainTopUrlVisitRequest,
    ) -> main_models.DescribeDcdnDomainTopUrlVisitResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_top_url_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_url_visit_async(
        self,
        request: main_models.DescribeDcdnDomainTopUrlVisitRequest,
    ) -> main_models.DescribeDcdnDomainTopUrlVisitResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_top_url_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_traffic_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_traffic_data(
        self,
        request: main_models.DescribeDcdnDomainTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_traffic_data_async(
        self,
        request: main_models.DescribeDcdnDomainTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_usage_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.data_protocol):
            query['DataProtocol'] = request.data_protocol
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_usage_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.data_protocol):
            query['DataProtocol'] = request.data_protocol
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_usage_data(
        self,
        request: main_models.DescribeDcdnDomainUsageDataRequest,
    ) -> main_models.DescribeDcdnDomainUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_usage_data_with_options(request, runtime)

    async def describe_dcdn_domain_usage_data_async(
        self,
        request: main_models.DescribeDcdnDomainUsageDataRequest,
    ) -> main_models.DescribeDcdnDomainUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_usage_data_with_options_async(request, runtime)

    def describe_dcdn_domain_uv_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainUvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainUvData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_uv_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainUvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainUvData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_uv_data(
        self,
        request: main_models.DescribeDcdnDomainUvDataRequest,
    ) -> main_models.DescribeDcdnDomainUvDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_uv_data_with_options(request, runtime)

    async def describe_dcdn_domain_uv_data_async(
        self,
        request: main_models.DescribeDcdnDomainUvDataRequest,
    ) -> main_models.DescribeDcdnDomainUvDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_uv_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_bps_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainWebsocketBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_websocket_bps_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainWebsocketBpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_bps_data(
        self,
        request: main_models.DescribeDcdnDomainWebsocketBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_websocket_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_bps_data_async(
        self,
        request: main_models.DescribeDcdnDomainWebsocketBpsDataRequest,
    ) -> main_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_http_code_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainWebsocketHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_websocket_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainWebsocketHttpCodeData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_http_code_data(
        self,
        request: main_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_websocket_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_http_code_data_async(
        self,
        request: main_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
    ) -> main_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_traffic_data_with_options(
        self,
        request: main_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainWebsocketTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_websocket_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainWebsocketTrafficData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_traffic_data(
        self,
        request: main_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domain_websocket_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_traffic_data_async(
        self,
        request: main_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
    ) -> main_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domains_by_source_with_options(
        self,
        request: main_models.DescribeDcdnDomainsBySourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainsBySourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainsBySource',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainsBySourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domains_by_source_with_options_async(
        self,
        request: main_models.DescribeDcdnDomainsBySourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnDomainsBySourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnDomainsBySource',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnDomainsBySourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domains_by_source(
        self,
        request: main_models.DescribeDcdnDomainsBySourceRequest,
    ) -> main_models.DescribeDcdnDomainsBySourceResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_domains_by_source_with_options(request, runtime)

    async def describe_dcdn_domains_by_source_async(
        self,
        request: main_models.DescribeDcdnDomainsBySourceRequest,
    ) -> main_models.DescribeDcdnDomainsBySourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_domains_by_source_with_options_async(request, runtime)

    def describe_dcdn_er_usage_data_with_options(
        self,
        request: main_models.DescribeDcdnErUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnErUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.routine_id):
            query['RoutineID'] = request.routine_id
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnErUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnErUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_er_usage_data_with_options_async(
        self,
        request: main_models.DescribeDcdnErUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnErUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.routine_id):
            query['RoutineID'] = request.routine_id
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnErUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnErUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_er_usage_data(
        self,
        request: main_models.DescribeDcdnErUsageDataRequest,
    ) -> main_models.DescribeDcdnErUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_er_usage_data_with_options(request, runtime)

    async def describe_dcdn_er_usage_data_async(
        self,
        request: main_models.DescribeDcdnErUsageDataRequest,
    ) -> main_models.DescribeDcdnErUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_er_usage_data_with_options_async(request, runtime)

    def describe_dcdn_full_domains_block_ipconfig_with_options(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnFullDomainsBlockIPConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnFullDomainsBlockIPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_full_domains_block_ipconfig_with_options_async(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnFullDomainsBlockIPConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnFullDomainsBlockIPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_full_domains_block_ipconfig(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_full_domains_block_ipconfig_with_options(request, runtime)

    async def describe_dcdn_full_domains_block_ipconfig_async(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_full_domains_block_ipconfig_with_options_async(request, runtime)

    def describe_dcdn_full_domains_block_iphistory_with_options(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iplist):
            body['IPList'] = request.iplist
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnFullDomainsBlockIPHistory',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnFullDomainsBlockIPHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_full_domains_block_iphistory_with_options_async(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iplist):
            body['IPList'] = request.iplist
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnFullDomainsBlockIPHistory',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnFullDomainsBlockIPHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_full_domains_block_iphistory(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_full_domains_block_iphistory_with_options(request, runtime)

    async def describe_dcdn_full_domains_block_iphistory_async(
        self,
        request: main_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
    ) -> main_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_full_domains_block_iphistory_with_options_async(request, runtime)

    def describe_dcdn_https_domain_list_with_options(
        self,
        request: main_models.DescribeDcdnHttpsDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnHttpsDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnHttpsDomainList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnHttpsDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_https_domain_list_with_options_async(
        self,
        request: main_models.DescribeDcdnHttpsDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnHttpsDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnHttpsDomainList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnHttpsDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_https_domain_list(
        self,
        request: main_models.DescribeDcdnHttpsDomainListRequest,
    ) -> main_models.DescribeDcdnHttpsDomainListResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_https_domain_list_with_options(request, runtime)

    async def describe_dcdn_https_domain_list_async(
        self,
        request: main_models.DescribeDcdnHttpsDomainListRequest,
    ) -> main_models.DescribeDcdnHttpsDomainListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_https_domain_list_with_options_async(request, runtime)

    def describe_dcdn_ip_info_with_options(
        self,
        request: main_models.DescribeDcdnIpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ip_info_with_options_async(
        self,
        request: main_models.DescribeDcdnIpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ip_info(
        self,
        request: main_models.DescribeDcdnIpInfoRequest,
    ) -> main_models.DescribeDcdnIpInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ip_info_with_options(request, runtime)

    async def describe_dcdn_ip_info_async(
        self,
        request: main_models.DescribeDcdnIpInfoRequest,
    ) -> main_models.DescribeDcdnIpInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ip_info_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_cidr_with_options(
        self,
        request: main_models.DescribeDcdnIpaDomainCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaDomainCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaDomainCidr',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaDomainCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_domain_cidr_with_options_async(
        self,
        request: main_models.DescribeDcdnIpaDomainCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaDomainCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaDomainCidr',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaDomainCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_domain_cidr(
        self,
        request: main_models.DescribeDcdnIpaDomainCidrRequest,
    ) -> main_models.DescribeDcdnIpaDomainCidrResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ipa_domain_cidr_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_cidr_async(
        self,
        request: main_models.DescribeDcdnIpaDomainCidrRequest,
    ) -> main_models.DescribeDcdnIpaDomainCidrResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_cidr_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_configs_with_options(
        self,
        request: main_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: main_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaDomainConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_domain_configs(
        self,
        request: main_models.DescribeDcdnIpaDomainConfigsRequest,
    ) -> main_models.DescribeDcdnIpaDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_configs_async(
        self,
        request: main_models.DescribeDcdnIpaDomainConfigsRequest,
    ) -> main_models.DescribeDcdnIpaDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_detail_with_options(
        self,
        request: main_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaDomainDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_domain_detail_with_options_async(
        self,
        request: main_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaDomainDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_domain_detail(
        self,
        request: main_models.DescribeDcdnIpaDomainDetailRequest,
    ) -> main_models.DescribeDcdnIpaDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ipa_domain_detail_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_detail_async(
        self,
        request: main_models.DescribeDcdnIpaDomainDetailRequest,
    ) -> main_models.DescribeDcdnIpaDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_ipa_service_with_options(
        self,
        request: main_models.DescribeDcdnIpaServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_service_with_options_async(
        self,
        request: main_models.DescribeDcdnIpaServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_service(
        self,
        request: main_models.DescribeDcdnIpaServiceRequest,
    ) -> main_models.DescribeDcdnIpaServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ipa_service_with_options(request, runtime)

    async def describe_dcdn_ipa_service_async(
        self,
        request: main_models.DescribeDcdnIpaServiceRequest,
    ) -> main_models.DescribeDcdnIpaServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ipa_service_with_options_async(request, runtime)

    def describe_dcdn_ipa_user_domains_with_options(
        self,
        request: main_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not DaraCore.is_null(request.func_id):
            query['FuncId'] = request.func_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaUserDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_user_domains_with_options_async(
        self,
        request: main_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnIpaUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not DaraCore.is_null(request.func_id):
            query['FuncId'] = request.func_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnIpaUserDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnIpaUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_user_domains(
        self,
        request: main_models.DescribeDcdnIpaUserDomainsRequest,
    ) -> main_models.DescribeDcdnIpaUserDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_ipa_user_domains_with_options(request, runtime)

    async def describe_dcdn_ipa_user_domains_async(
        self,
        request: main_models.DescribeDcdnIpaUserDomainsRequest,
    ) -> main_models.DescribeDcdnIpaUserDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_ipa_user_domains_with_options_async(request, runtime)

    def describe_dcdn_kv_account_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnKvAccountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnKvAccount',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnKvAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_kv_account_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnKvAccountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnKvAccount',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnKvAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_kv_account(self) -> main_models.DescribeDcdnKvAccountResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_kv_account_with_options(runtime)

    async def describe_dcdn_kv_account_async(self) -> main_models.DescribeDcdnKvAccountResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_kv_account_with_options_async(runtime)

    def describe_dcdn_kv_account_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnKvAccountStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnKvAccountStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnKvAccountStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_kv_account_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnKvAccountStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnKvAccountStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnKvAccountStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_kv_account_status(self) -> main_models.DescribeDcdnKvAccountStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_kv_account_status_with_options(runtime)

    async def describe_dcdn_kv_account_status_async(self) -> main_models.DescribeDcdnKvAccountStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_kv_account_status_with_options_async(runtime)

    def describe_dcdn_kv_namespace_with_options(
        self,
        request: main_models.DescribeDcdnKvNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnKvNamespaceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnKvNamespace',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_kv_namespace_with_options_async(
        self,
        request: main_models.DescribeDcdnKvNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnKvNamespaceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnKvNamespace',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_kv_namespace(
        self,
        request: main_models.DescribeDcdnKvNamespaceRequest,
    ) -> main_models.DescribeDcdnKvNamespaceResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_kv_namespace_with_options(request, runtime)

    async def describe_dcdn_kv_namespace_async(
        self,
        request: main_models.DescribeDcdnKvNamespaceRequest,
    ) -> main_models.DescribeDcdnKvNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_kv_namespace_with_options_async(request, runtime)

    def describe_dcdn_l2ips_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnL2IpsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnL2Ips',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnL2IpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_l2ips_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnL2IpsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnL2Ips',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnL2IpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_l2ips(self) -> main_models.DescribeDcdnL2IpsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_l2ips_with_options(runtime)

    async def describe_dcdn_l2ips_async(self) -> main_models.DescribeDcdnL2IpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_l2ips_with_options_async(runtime)

    def describe_dcdn_l2vips_with_options(
        self,
        request: main_models.DescribeDcdnL2VipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnL2VipsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnL2Vips',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnL2VipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_l2vips_with_options_async(
        self,
        request: main_models.DescribeDcdnL2VipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnL2VipsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnL2Vips',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnL2VipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_l2vips(
        self,
        request: main_models.DescribeDcdnL2VipsRequest,
    ) -> main_models.DescribeDcdnL2VipsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_l2vips_with_options(request, runtime)

    async def describe_dcdn_l2vips_async(
        self,
        request: main_models.DescribeDcdnL2VipsRequest,
    ) -> main_models.DescribeDcdnL2VipsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_l2vips_with_options_async(request, runtime)

    def describe_dcdn_origin_site_health_status_with_options(
        self,
        request: main_models.DescribeDcdnOriginSiteHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnOriginSiteHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnOriginSiteHealthStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnOriginSiteHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_origin_site_health_status_with_options_async(
        self,
        request: main_models.DescribeDcdnOriginSiteHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnOriginSiteHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnOriginSiteHealthStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnOriginSiteHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_origin_site_health_status(
        self,
        request: main_models.DescribeDcdnOriginSiteHealthStatusRequest,
    ) -> main_models.DescribeDcdnOriginSiteHealthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_origin_site_health_status_with_options(request, runtime)

    async def describe_dcdn_origin_site_health_status_async(
        self,
        request: main_models.DescribeDcdnOriginSiteHealthStatusRequest,
    ) -> main_models.DescribeDcdnOriginSiteHealthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_origin_site_health_status_with_options_async(request, runtime)

    def describe_dcdn_real_time_delivery_field_with_options(
        self,
        request: main_models.DescribeDcdnRealTimeDeliveryFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRealTimeDeliveryField',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_real_time_delivery_field_with_options_async(
        self,
        request: main_models.DescribeDcdnRealTimeDeliveryFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRealTimeDeliveryField',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRealTimeDeliveryFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_real_time_delivery_field(
        self,
        request: main_models.DescribeDcdnRealTimeDeliveryFieldRequest,
    ) -> main_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_real_time_delivery_field_with_options(request, runtime)

    async def describe_dcdn_real_time_delivery_field_async(
        self,
        request: main_models.DescribeDcdnRealTimeDeliveryFieldRequest,
    ) -> main_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_real_time_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_refresh_quota_with_options(
        self,
        request: main_models.DescribeDcdnRefreshQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRefreshQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRefreshQuota',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_refresh_quota_with_options_async(
        self,
        request: main_models.DescribeDcdnRefreshQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRefreshQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRefreshQuota',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRefreshQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_refresh_quota(
        self,
        request: main_models.DescribeDcdnRefreshQuotaRequest,
    ) -> main_models.DescribeDcdnRefreshQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_refresh_quota_with_options(request, runtime)

    async def describe_dcdn_refresh_quota_async(
        self,
        request: main_models.DescribeDcdnRefreshQuotaRequest,
    ) -> main_models.DescribeDcdnRefreshQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_refresh_quota_with_options_async(request, runtime)

    def describe_dcdn_refresh_task_by_id_with_options(
        self,
        request: main_models.DescribeDcdnRefreshTaskByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRefreshTaskByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRefreshTaskById',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRefreshTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_refresh_task_by_id_with_options_async(
        self,
        request: main_models.DescribeDcdnRefreshTaskByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRefreshTaskByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRefreshTaskById',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRefreshTaskByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_refresh_task_by_id(
        self,
        request: main_models.DescribeDcdnRefreshTaskByIdRequest,
    ) -> main_models.DescribeDcdnRefreshTaskByIdResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_refresh_task_by_id_with_options(request, runtime)

    async def describe_dcdn_refresh_task_by_id_async(
        self,
        request: main_models.DescribeDcdnRefreshTaskByIdRequest,
    ) -> main_models.DescribeDcdnRefreshTaskByIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_refresh_task_by_id_with_options_async(request, runtime)

    def describe_dcdn_refresh_tasks_with_options(
        self,
        request: main_models.DescribeDcdnRefreshTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRefreshTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRefreshTasks',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_refresh_tasks_with_options_async(
        self,
        request: main_models.DescribeDcdnRefreshTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRefreshTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRefreshTasks',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRefreshTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_refresh_tasks(
        self,
        request: main_models.DescribeDcdnRefreshTasksRequest,
    ) -> main_models.DescribeDcdnRefreshTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_refresh_tasks_with_options(request, runtime)

    async def describe_dcdn_refresh_tasks_async(
        self,
        request: main_models.DescribeDcdnRefreshTasksRequest,
    ) -> main_models.DescribeDcdnRefreshTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_refresh_tasks_with_options_async(request, runtime)

    def describe_dcdn_region_and_isp_with_options(
        self,
        request: main_models.DescribeDcdnRegionAndIspRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRegionAndIspResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRegionAndIsp',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRegionAndIspResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_region_and_isp_with_options_async(
        self,
        request: main_models.DescribeDcdnRegionAndIspRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnRegionAndIspResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnRegionAndIsp',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnRegionAndIspResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_region_and_isp(
        self,
        request: main_models.DescribeDcdnRegionAndIspRequest,
    ) -> main_models.DescribeDcdnRegionAndIspResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_region_and_isp_with_options(request, runtime)

    async def describe_dcdn_region_and_isp_async(
        self,
        request: main_models.DescribeDcdnRegionAndIspRequest,
    ) -> main_models.DescribeDcdnRegionAndIspResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_region_and_isp_with_options_async(request, runtime)

    def describe_dcdn_report_with_options(
        self,
        request: main_models.DescribeDcdnReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.http_code):
            query['HttpCode'] = request.http_code
        if not DaraCore.is_null(request.is_overseas):
            query['IsOverseas'] = request.is_overseas
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnReport',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_report_with_options_async(
        self,
        request: main_models.DescribeDcdnReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.http_code):
            query['HttpCode'] = request.http_code
        if not DaraCore.is_null(request.is_overseas):
            query['IsOverseas'] = request.is_overseas
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnReport',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_report(
        self,
        request: main_models.DescribeDcdnReportRequest,
    ) -> main_models.DescribeDcdnReportResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_report_with_options(request, runtime)

    async def describe_dcdn_report_async(
        self,
        request: main_models.DescribeDcdnReportRequest,
    ) -> main_models.DescribeDcdnReportResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_report_with_options_async(request, runtime)

    def describe_dcdn_report_list_with_options(
        self,
        request: main_models.DescribeDcdnReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnReportList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_report_list_with_options_async(
        self,
        request: main_models.DescribeDcdnReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnReportList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_report_list(
        self,
        request: main_models.DescribeDcdnReportListRequest,
    ) -> main_models.DescribeDcdnReportListResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_report_list_with_options(request, runtime)

    async def describe_dcdn_report_list_async(
        self,
        request: main_models.DescribeDcdnReportListRequest,
    ) -> main_models.DescribeDcdnReportListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_report_list_with_options_async(request, runtime)

    def describe_dcdn_slsreal_time_log_type_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSLSRealTimeLogTypeResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSLSRealTimeLogType',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSLSRealTimeLogTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_slsreal_time_log_type_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSLSRealTimeLogTypeResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSLSRealTimeLogType',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSLSRealTimeLogTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_slsreal_time_log_type(self) -> main_models.DescribeDcdnSLSRealTimeLogTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_slsreal_time_log_type_with_options(runtime)

    async def describe_dcdn_slsreal_time_log_type_async(self) -> main_models.DescribeDcdnSLSRealTimeLogTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_slsreal_time_log_type_with_options_async(runtime)

    def describe_dcdn_slsrealtime_log_delivery_with_options(
        self,
        request: main_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSLSRealtimeLogDelivery',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSLSRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_slsrealtime_log_delivery_with_options_async(
        self,
        request: main_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSLSRealtimeLogDelivery',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSLSRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_slsrealtime_log_delivery(
        self,
        request: main_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
    ) -> main_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    async def describe_dcdn_slsrealtime_log_delivery_async(
        self,
        request: main_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
    ) -> main_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_slsrealtime_log_delivery_with_options_async(request, runtime)

    def describe_dcdn_smcertificate_detail_with_options(
        self,
        request: main_models.DescribeDcdnSMCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSMCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSMCertificateDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSMCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_smcertificate_detail_with_options_async(
        self,
        request: main_models.DescribeDcdnSMCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSMCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSMCertificateDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSMCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_smcertificate_detail(
        self,
        request: main_models.DescribeDcdnSMCertificateDetailRequest,
    ) -> main_models.DescribeDcdnSMCertificateDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_smcertificate_detail_with_options(request, runtime)

    async def describe_dcdn_smcertificate_detail_async(
        self,
        request: main_models.DescribeDcdnSMCertificateDetailRequest,
    ) -> main_models.DescribeDcdnSMCertificateDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_smcertificate_detail_with_options_async(request, runtime)

    def describe_dcdn_smcertificate_list_with_options(
        self,
        request: main_models.DescribeDcdnSMCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSMCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSMCertificateList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSMCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_smcertificate_list_with_options_async(
        self,
        request: main_models.DescribeDcdnSMCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSMCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSMCertificateList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSMCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_smcertificate_list(
        self,
        request: main_models.DescribeDcdnSMCertificateListRequest,
    ) -> main_models.DescribeDcdnSMCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_smcertificate_list_with_options(request, runtime)

    async def describe_dcdn_smcertificate_list_async(
        self,
        request: main_models.DescribeDcdnSMCertificateListRequest,
    ) -> main_models.DescribeDcdnSMCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_smcertificate_list_with_options_async(request, runtime)

    def describe_dcdn_sslcertificate_list_with_options(
        self,
        request: main_models.DescribeDcdnSSLCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSSLCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_keyword):
            query['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSSLCertificateList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSSLCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_sslcertificate_list_with_options_async(
        self,
        request: main_models.DescribeDcdnSSLCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSSLCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_keyword):
            query['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSSLCertificateList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSSLCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_sslcertificate_list(
        self,
        request: main_models.DescribeDcdnSSLCertificateListRequest,
    ) -> main_models.DescribeDcdnSSLCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_sslcertificate_list_with_options(request, runtime)

    async def describe_dcdn_sslcertificate_list_async(
        self,
        request: main_models.DescribeDcdnSSLCertificateListRequest,
    ) -> main_models.DescribeDcdnSSLCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_sslcertificate_list_with_options_async(request, runtime)

    def describe_dcdn_sec_func_info_with_options(
        self,
        request: main_models.DescribeDcdnSecFuncInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSecFuncInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sec_func_type):
            query['SecFuncType'] = request.sec_func_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSecFuncInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSecFuncInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_sec_func_info_with_options_async(
        self,
        request: main_models.DescribeDcdnSecFuncInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSecFuncInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sec_func_type):
            query['SecFuncType'] = request.sec_func_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSecFuncInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSecFuncInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_sec_func_info(
        self,
        request: main_models.DescribeDcdnSecFuncInfoRequest,
    ) -> main_models.DescribeDcdnSecFuncInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_sec_func_info_with_options(request, runtime)

    async def describe_dcdn_sec_func_info_async(
        self,
        request: main_models.DescribeDcdnSecFuncInfoRequest,
    ) -> main_models.DescribeDcdnSecFuncInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_sec_func_info_with_options_async(request, runtime)

    def describe_dcdn_sec_spec_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSecSpecInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSecSpecInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSecSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_sec_spec_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSecSpecInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSecSpecInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSecSpecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_sec_spec_info(self) -> main_models.DescribeDcdnSecSpecInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_sec_spec_info_with_options(runtime)

    async def describe_dcdn_sec_spec_info_async(self) -> main_models.DescribeDcdnSecSpecInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_sec_spec_info_with_options_async(runtime)

    def describe_dcdn_service_with_options(
        self,
        request: main_models.DescribeDcdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_service_with_options_async(
        self,
        request: main_models.DescribeDcdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_service(
        self,
        request: main_models.DescribeDcdnServiceRequest,
    ) -> main_models.DescribeDcdnServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_service_with_options(request, runtime)

    async def describe_dcdn_service_async(
        self,
        request: main_models.DescribeDcdnServiceRequest,
    ) -> main_models.DescribeDcdnServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_service_with_options_async(request, runtime)

    def describe_dcdn_staging_ip_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnStagingIpResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnStagingIp',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnStagingIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_staging_ip_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnStagingIpResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnStagingIp',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnStagingIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_staging_ip(self) -> main_models.DescribeDcdnStagingIpResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_staging_ip_with_options(runtime)

    async def describe_dcdn_staging_ip_async(self) -> main_models.DescribeDcdnStagingIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_staging_ip_with_options_async(runtime)

    def describe_dcdn_sub_list_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSubListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSubList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSubListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_sub_list_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnSubListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnSubList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnSubListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_sub_list(self) -> main_models.DescribeDcdnSubListResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_sub_list_with_options(runtime)

    async def describe_dcdn_sub_list_async(self) -> main_models.DescribeDcdnSubListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_sub_list_with_options_async(runtime)

    def describe_dcdn_tag_resources_with_options(
        self,
        request: main_models.DescribeDcdnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnTagResources',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_tag_resources_with_options_async(
        self,
        request: main_models.DescribeDcdnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnTagResources',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_tag_resources(
        self,
        request: main_models.DescribeDcdnTagResourcesRequest,
    ) -> main_models.DescribeDcdnTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_tag_resources_with_options(request, runtime)

    async def describe_dcdn_tag_resources_async(
        self,
        request: main_models.DescribeDcdnTagResourcesRequest,
    ) -> main_models.DescribeDcdnTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_tag_resources_with_options_async(request, runtime)

    def describe_dcdn_top_domains_by_flow_with_options(
        self,
        request: main_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnTopDomainsByFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnTopDomainsByFlow',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_top_domains_by_flow_with_options_async(
        self,
        request: main_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnTopDomainsByFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnTopDomainsByFlow',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_top_domains_by_flow(
        self,
        request: main_models.DescribeDcdnTopDomainsByFlowRequest,
    ) -> main_models.DescribeDcdnTopDomainsByFlowResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_top_domains_by_flow_with_options(request, runtime)

    async def describe_dcdn_top_domains_by_flow_async(
        self,
        request: main_models.DescribeDcdnTopDomainsByFlowRequest,
    ) -> main_models.DescribeDcdnTopDomainsByFlowResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_top_domains_by_flow_with_options_async(request, runtime)

    def describe_dcdn_user_bill_history_with_options(
        self,
        request: main_models.DescribeDcdnUserBillHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserBillHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserBillHistory',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserBillHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_bill_history_with_options_async(
        self,
        request: main_models.DescribeDcdnUserBillHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserBillHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserBillHistory',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserBillHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_bill_history(
        self,
        request: main_models.DescribeDcdnUserBillHistoryRequest,
    ) -> main_models.DescribeDcdnUserBillHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_bill_history_with_options(request, runtime)

    async def describe_dcdn_user_bill_history_async(
        self,
        request: main_models.DescribeDcdnUserBillHistoryRequest,
    ) -> main_models.DescribeDcdnUserBillHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_bill_history_with_options_async(request, runtime)

    def describe_dcdn_user_bill_type_with_options(
        self,
        request: main_models.DescribeDcdnUserBillTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserBillTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserBillType',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserBillTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_bill_type_with_options_async(
        self,
        request: main_models.DescribeDcdnUserBillTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserBillTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserBillType',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserBillTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_bill_type(
        self,
        request: main_models.DescribeDcdnUserBillTypeRequest,
    ) -> main_models.DescribeDcdnUserBillTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_bill_type_with_options(request, runtime)

    async def describe_dcdn_user_bill_type_async(
        self,
        request: main_models.DescribeDcdnUserBillTypeRequest,
    ) -> main_models.DescribeDcdnUserBillTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_bill_type_with_options_async(request, runtime)

    def describe_dcdn_user_certificate_expire_count_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserCertificateExpireCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserCertificateExpireCount',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserCertificateExpireCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_certificate_expire_count_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserCertificateExpireCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserCertificateExpireCount',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserCertificateExpireCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_certificate_expire_count(self) -> main_models.DescribeDcdnUserCertificateExpireCountResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_certificate_expire_count_with_options(runtime)

    async def describe_dcdn_user_certificate_expire_count_async(self) -> main_models.DescribeDcdnUserCertificateExpireCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_certificate_expire_count_with_options_async(runtime)

    def describe_dcdn_user_configs_with_options(
        self,
        request: main_models.DescribeDcdnUserConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_configs_with_options_async(
        self,
        request: main_models.DescribeDcdnUserConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserConfigs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_configs(
        self,
        request: main_models.DescribeDcdnUserConfigsRequest,
    ) -> main_models.DescribeDcdnUserConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_configs_with_options(request, runtime)

    async def describe_dcdn_user_configs_async(
        self,
        request: main_models.DescribeDcdnUserConfigsRequest,
    ) -> main_models.DescribeDcdnUserConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_configs_with_options_async(request, runtime)

    def describe_dcdn_user_domains_with_options(
        self,
        request: main_models.DescribeDcdnUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not DaraCore.is_null(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not DaraCore.is_null(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not DaraCore.is_null(request.coverage):
            query['Coverage'] = request.coverage
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.web_site_type):
            query['WebSiteType'] = request.web_site_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_domains_with_options_async(
        self,
        request: main_models.DescribeDcdnUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not DaraCore.is_null(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not DaraCore.is_null(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not DaraCore.is_null(request.coverage):
            query['Coverage'] = request.coverage
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.web_site_type):
            query['WebSiteType'] = request.web_site_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_domains(
        self,
        request: main_models.DescribeDcdnUserDomainsRequest,
    ) -> main_models.DescribeDcdnUserDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_domains_with_options(request, runtime)

    async def describe_dcdn_user_domains_async(
        self,
        request: main_models.DescribeDcdnUserDomainsRequest,
    ) -> main_models.DescribeDcdnUserDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_domains_with_options_async(request, runtime)

    def describe_dcdn_user_domains_by_func_with_options(
        self,
        request: main_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserDomainsByFuncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not DaraCore.is_null(request.func_id):
            query['FuncId'] = request.func_id
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserDomainsByFunc',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserDomainsByFuncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_domains_by_func_with_options_async(
        self,
        request: main_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserDomainsByFuncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not DaraCore.is_null(request.func_id):
            query['FuncId'] = request.func_id
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserDomainsByFunc',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserDomainsByFuncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_domains_by_func(
        self,
        request: main_models.DescribeDcdnUserDomainsByFuncRequest,
    ) -> main_models.DescribeDcdnUserDomainsByFuncResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_domains_by_func_with_options(request, runtime)

    async def describe_dcdn_user_domains_by_func_async(
        self,
        request: main_models.DescribeDcdnUserDomainsByFuncRequest,
    ) -> main_models.DescribeDcdnUserDomainsByFuncResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_domains_by_func_with_options_async(request, runtime)

    def describe_dcdn_user_quota_with_options(
        self,
        request: main_models.DescribeDcdnUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserQuota',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_quota_with_options_async(
        self,
        request: main_models.DescribeDcdnUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserQuota',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_quota(
        self,
        request: main_models.DescribeDcdnUserQuotaRequest,
    ) -> main_models.DescribeDcdnUserQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_quota_with_options(request, runtime)

    async def describe_dcdn_user_quota_async(
        self,
        request: main_models.DescribeDcdnUserQuotaRequest,
    ) -> main_models.DescribeDcdnUserQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_quota_with_options_async(request, runtime)

    def describe_dcdn_user_real_time_delivery_field_with_options(
        self,
        request: main_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserRealTimeDeliveryField',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_real_time_delivery_field_with_options_async(
        self,
        request: main_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserRealTimeDeliveryField',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserRealTimeDeliveryFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_real_time_delivery_field(
        self,
        request: main_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
    ) -> main_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    async def describe_dcdn_user_real_time_delivery_field_async(
        self,
        request: main_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
    ) -> main_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_real_time_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_user_resource_package_with_options(
        self,
        request: main_models.DescribeDcdnUserResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserResourcePackage',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_resource_package_with_options_async(
        self,
        request: main_models.DescribeDcdnUserResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserResourcePackage',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_resource_package(
        self,
        request: main_models.DescribeDcdnUserResourcePackageRequest,
    ) -> main_models.DescribeDcdnUserResourcePackageResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_resource_package_with_options(request, runtime)

    async def describe_dcdn_user_resource_package_async(
        self,
        request: main_models.DescribeDcdnUserResourcePackageRequest,
    ) -> main_models.DescribeDcdnUserResourcePackageResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_resource_package_with_options_async(request, runtime)

    def describe_dcdn_user_sec_drop_with_options(
        self,
        request: main_models.DescribeDcdnUserSecDropRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserSecDropResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.sec_func):
            query['SecFunc'] = request.sec_func
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserSecDrop',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserSecDropResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_sec_drop_with_options_async(
        self,
        request: main_models.DescribeDcdnUserSecDropRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserSecDropResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.sec_func):
            query['SecFunc'] = request.sec_func
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserSecDrop',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserSecDropResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_sec_drop(
        self,
        request: main_models.DescribeDcdnUserSecDropRequest,
    ) -> main_models.DescribeDcdnUserSecDropResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_with_options(request, runtime)

    async def describe_dcdn_user_sec_drop_async(
        self,
        request: main_models.DescribeDcdnUserSecDropRequest,
    ) -> main_models.DescribeDcdnUserSecDropResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_sec_drop_with_options_async(request, runtime)

    def describe_dcdn_user_sec_drop_by_minute_with_options(
        self,
        request: main_models.DescribeDcdnUserSecDropByMinuteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserSecDropByMinuteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object):
            query['Object'] = request.object
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sec_func):
            query['SecFunc'] = request.sec_func
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserSecDropByMinute',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserSecDropByMinuteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_sec_drop_by_minute_with_options_async(
        self,
        request: main_models.DescribeDcdnUserSecDropByMinuteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserSecDropByMinuteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object):
            query['Object'] = request.object
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sec_func):
            query['SecFunc'] = request.sec_func
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserSecDropByMinute',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserSecDropByMinuteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_sec_drop_by_minute(
        self,
        request: main_models.DescribeDcdnUserSecDropByMinuteRequest,
    ) -> main_models.DescribeDcdnUserSecDropByMinuteResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_by_minute_with_options(request, runtime)

    async def describe_dcdn_user_sec_drop_by_minute_async(
        self,
        request: main_models.DescribeDcdnUserSecDropByMinuteRequest,
    ) -> main_models.DescribeDcdnUserSecDropByMinuteResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_sec_drop_by_minute_with_options_async(request, runtime)

    def describe_dcdn_user_tags_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserTagsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserTags',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_tags_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserTagsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserTags',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_tags(self) -> main_models.DescribeDcdnUserTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_tags_with_options(runtime)

    async def describe_dcdn_user_tags_async(self) -> main_models.DescribeDcdnUserTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_tags_with_options_async(runtime)

    def describe_dcdn_user_vips_by_domain_with_options(
        self,
        request: main_models.DescribeDcdnUserVipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserVipsByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.available):
            query['Available'] = request.available
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserVipsByDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserVipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_vips_by_domain_with_options_async(
        self,
        request: main_models.DescribeDcdnUserVipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnUserVipsByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.available):
            query['Available'] = request.available
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnUserVipsByDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnUserVipsByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_vips_by_domain(
        self,
        request: main_models.DescribeDcdnUserVipsByDomainRequest,
    ) -> main_models.DescribeDcdnUserVipsByDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_user_vips_by_domain_with_options(request, runtime)

    async def describe_dcdn_user_vips_by_domain_async(
        self,
        request: main_models.DescribeDcdnUserVipsByDomainRequest,
    ) -> main_models.DescribeDcdnUserVipsByDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_user_vips_by_domain_with_options_async(request, runtime)

    def describe_dcdn_verify_content_with_options(
        self,
        request: main_models.DescribeDcdnVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnVerifyContent',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_verify_content_with_options_async(
        self,
        request: main_models.DescribeDcdnVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnVerifyContent',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_verify_content(
        self,
        request: main_models.DescribeDcdnVerifyContentRequest,
    ) -> main_models.DescribeDcdnVerifyContentResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_verify_content_with_options(request, runtime)

    async def describe_dcdn_verify_content_async(
        self,
        request: main_models.DescribeDcdnVerifyContentRequest,
    ) -> main_models.DescribeDcdnVerifyContentResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_verify_content_with_options_async(request, runtime)

    def describe_dcdn_waf_bot_app_key_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafBotAppKeyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafBotAppKey',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafBotAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_bot_app_key_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafBotAppKeyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafBotAppKey',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafBotAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_bot_app_key(self) -> main_models.DescribeDcdnWafBotAppKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_bot_app_key_with_options(runtime)

    async def describe_dcdn_waf_bot_app_key_async(self) -> main_models.DescribeDcdnWafBotAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_bot_app_key_with_options_async(runtime)

    def describe_dcdn_waf_default_rules_with_options(
        self,
        request: main_models.DescribeDcdnWafDefaultRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDefaultRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDefaultRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDefaultRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_default_rules_with_options_async(
        self,
        request: main_models.DescribeDcdnWafDefaultRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDefaultRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDefaultRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDefaultRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_default_rules(
        self,
        request: main_models.DescribeDcdnWafDefaultRulesRequest,
    ) -> main_models.DescribeDcdnWafDefaultRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_default_rules_with_options(request, runtime)

    async def describe_dcdn_waf_default_rules_async(
        self,
        request: main_models.DescribeDcdnWafDefaultRulesRequest,
    ) -> main_models.DescribeDcdnWafDefaultRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_default_rules_with_options_async(request, runtime)

    def describe_dcdn_waf_domain_with_options(
        self,
        request: main_models.DescribeDcdnWafDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_domain_with_options_async(
        self,
        request: main_models.DescribeDcdnWafDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_domain(
        self,
        request: main_models.DescribeDcdnWafDomainRequest,
    ) -> main_models.DescribeDcdnWafDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_domain_with_options(request, runtime)

    async def describe_dcdn_waf_domain_async(
        self,
        request: main_models.DescribeDcdnWafDomainRequest,
    ) -> main_models.DescribeDcdnWafDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_domain_with_options_async(request, runtime)

    def describe_dcdn_waf_domain_detail_with_options(
        self,
        request: main_models.DescribeDcdnWafDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDomainDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_domain_detail_with_options_async(
        self,
        request: main_models.DescribeDcdnWafDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDomainDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_domain_detail(
        self,
        request: main_models.DescribeDcdnWafDomainDetailRequest,
    ) -> main_models.DescribeDcdnWafDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_domain_detail_with_options(request, runtime)

    async def describe_dcdn_waf_domain_detail_async(
        self,
        request: main_models.DescribeDcdnWafDomainDetailRequest,
    ) -> main_models.DescribeDcdnWafDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_waf_domains_with_options(
        self,
        request: main_models.DescribeDcdnWafDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_domains_with_options_async(
        self,
        request: main_models.DescribeDcdnWafDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_domains(
        self,
        request: main_models.DescribeDcdnWafDomainsRequest,
    ) -> main_models.DescribeDcdnWafDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_domains_with_options(request, runtime)

    async def describe_dcdn_waf_domains_async(
        self,
        request: main_models.DescribeDcdnWafDomainsRequest,
    ) -> main_models.DescribeDcdnWafDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_domains_with_options_async(request, runtime)

    def describe_dcdn_waf_filter_info_with_options(
        self,
        request: main_models.DescribeDcdnWafFilterInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafFilterInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafFilterInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafFilterInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_filter_info_with_options_async(
        self,
        request: main_models.DescribeDcdnWafFilterInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafFilterInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafFilterInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafFilterInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_filter_info(
        self,
        request: main_models.DescribeDcdnWafFilterInfoRequest,
    ) -> main_models.DescribeDcdnWafFilterInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_filter_info_with_options(request, runtime)

    async def describe_dcdn_waf_filter_info_async(
        self,
        request: main_models.DescribeDcdnWafFilterInfoRequest,
    ) -> main_models.DescribeDcdnWafFilterInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_filter_info_with_options_async(request, runtime)

    def describe_dcdn_waf_geo_info_with_options(
        self,
        request: main_models.DescribeDcdnWafGeoInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafGeoInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafGeoInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafGeoInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_geo_info_with_options_async(
        self,
        request: main_models.DescribeDcdnWafGeoInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafGeoInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafGeoInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafGeoInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_geo_info(
        self,
        request: main_models.DescribeDcdnWafGeoInfoRequest,
    ) -> main_models.DescribeDcdnWafGeoInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_geo_info_with_options(request, runtime)

    async def describe_dcdn_waf_geo_info_async(
        self,
        request: main_models.DescribeDcdnWafGeoInfoRequest,
    ) -> main_models.DescribeDcdnWafGeoInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_geo_info_with_options_async(request, runtime)

    def describe_dcdn_waf_group_with_options(
        self,
        request: main_models.DescribeDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_group_with_options_async(
        self,
        request: main_models.DescribeDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_group(
        self,
        request: main_models.DescribeDcdnWafGroupRequest,
    ) -> main_models.DescribeDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_group_with_options(request, runtime)

    async def describe_dcdn_waf_group_async(
        self,
        request: main_models.DescribeDcdnWafGroupRequest,
    ) -> main_models.DescribeDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_group_with_options_async(request, runtime)

    def describe_dcdn_waf_groups_with_options(
        self,
        request: main_models.DescribeDcdnWafGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafGroups',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_groups_with_options_async(
        self,
        request: main_models.DescribeDcdnWafGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafGroups',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_groups(
        self,
        request: main_models.DescribeDcdnWafGroupsRequest,
    ) -> main_models.DescribeDcdnWafGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_groups_with_options(request, runtime)

    async def describe_dcdn_waf_groups_async(
        self,
        request: main_models.DescribeDcdnWafGroupsRequest,
    ) -> main_models.DescribeDcdnWafGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_groups_with_options_async(request, runtime)

    def describe_dcdn_waf_logs_with_options(
        self,
        request: main_models.DescribeDcdnWafLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafLogs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_logs_with_options_async(
        self,
        request: main_models.DescribeDcdnWafLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafLogs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_logs(
        self,
        request: main_models.DescribeDcdnWafLogsRequest,
    ) -> main_models.DescribeDcdnWafLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_logs_with_options(request, runtime)

    async def describe_dcdn_waf_logs_async(
        self,
        request: main_models.DescribeDcdnWafLogsRequest,
    ) -> main_models.DescribeDcdnWafLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_logs_with_options_async(request, runtime)

    def describe_dcdn_waf_policies_with_options(
        self,
        request: main_models.DescribeDcdnWafPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicies',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policies_with_options_async(
        self,
        request: main_models.DescribeDcdnWafPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicies',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policies(
        self,
        request: main_models.DescribeDcdnWafPoliciesRequest,
    ) -> main_models.DescribeDcdnWafPoliciesResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_policies_with_options(request, runtime)

    async def describe_dcdn_waf_policies_async(
        self,
        request: main_models.DescribeDcdnWafPoliciesRequest,
    ) -> main_models.DescribeDcdnWafPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_policies_with_options_async(request, runtime)

    def describe_dcdn_waf_policy_with_options(
        self,
        request: main_models.DescribeDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policy_with_options_async(
        self,
        request: main_models.DescribeDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policy(
        self,
        request: main_models.DescribeDcdnWafPolicyRequest,
    ) -> main_models.DescribeDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_policy_with_options(request, runtime)

    async def describe_dcdn_waf_policy_async(
        self,
        request: main_models.DescribeDcdnWafPolicyRequest,
    ) -> main_models.DescribeDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_policy_with_options_async(request, runtime)

    def describe_dcdn_waf_policy_domains_with_options(
        self,
        request: main_models.DescribeDcdnWafPolicyDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPolicyDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicyDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPolicyDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policy_domains_with_options_async(
        self,
        request: main_models.DescribeDcdnWafPolicyDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPolicyDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicyDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPolicyDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policy_domains(
        self,
        request: main_models.DescribeDcdnWafPolicyDomainsRequest,
    ) -> main_models.DescribeDcdnWafPolicyDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_policy_domains_with_options(request, runtime)

    async def describe_dcdn_waf_policy_domains_async(
        self,
        request: main_models.DescribeDcdnWafPolicyDomainsRequest,
    ) -> main_models.DescribeDcdnWafPolicyDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_policy_domains_with_options_async(request, runtime)

    def describe_dcdn_waf_policy_valid_domains_with_options(
        self,
        request: main_models.DescribeDcdnWafPolicyValidDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPolicyValidDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.domain_name_like):
            query['DomainNameLike'] = request.domain_name_like
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicyValidDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPolicyValidDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policy_valid_domains_with_options_async(
        self,
        request: main_models.DescribeDcdnWafPolicyValidDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafPolicyValidDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.domain_name_like):
            query['DomainNameLike'] = request.domain_name_like
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafPolicyValidDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafPolicyValidDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policy_valid_domains(
        self,
        request: main_models.DescribeDcdnWafPolicyValidDomainsRequest,
    ) -> main_models.DescribeDcdnWafPolicyValidDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_policy_valid_domains_with_options(request, runtime)

    async def describe_dcdn_waf_policy_valid_domains_async(
        self,
        request: main_models.DescribeDcdnWafPolicyValidDomainsRequest,
    ) -> main_models.DescribeDcdnWafPolicyValidDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_policy_valid_domains_with_options_async(request, runtime)

    def describe_dcdn_waf_rule_with_options(
        self,
        request: main_models.DescribeDcdnWafRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafRule',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_rule_with_options_async(
        self,
        request: main_models.DescribeDcdnWafRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafRule',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_rule(
        self,
        request: main_models.DescribeDcdnWafRuleRequest,
    ) -> main_models.DescribeDcdnWafRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_rule_with_options(request, runtime)

    async def describe_dcdn_waf_rule_async(
        self,
        request: main_models.DescribeDcdnWafRuleRequest,
    ) -> main_models.DescribeDcdnWafRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_rule_with_options_async(request, runtime)

    def describe_dcdn_waf_rules_with_options(
        self,
        request: main_models.DescribeDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_rules_with_options_async(
        self,
        request: main_models.DescribeDcdnWafRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafRules',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_rules(
        self,
        request: main_models.DescribeDcdnWafRulesRequest,
    ) -> main_models.DescribeDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_rules_with_options(request, runtime)

    async def describe_dcdn_waf_rules_async(
        self,
        request: main_models.DescribeDcdnWafRulesRequest,
    ) -> main_models.DescribeDcdnWafRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_rules_with_options_async(request, runtime)

    def describe_dcdn_waf_scenes_with_options(
        self,
        request: main_models.DescribeDcdnWafScenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafScenes',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_scenes_with_options_async(
        self,
        request: main_models.DescribeDcdnWafScenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafScenes',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_scenes(
        self,
        request: main_models.DescribeDcdnWafScenesRequest,
    ) -> main_models.DescribeDcdnWafScenesResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_scenes_with_options(request, runtime)

    async def describe_dcdn_waf_scenes_async(
        self,
        request: main_models.DescribeDcdnWafScenesRequest,
    ) -> main_models.DescribeDcdnWafScenesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_scenes_with_options_async(request, runtime)

    def describe_dcdn_waf_service_with_options(
        self,
        request: main_models.DescribeDcdnWafServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_service_with_options_async(
        self,
        request: main_models.DescribeDcdnWafServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_service(
        self,
        request: main_models.DescribeDcdnWafServiceRequest,
    ) -> main_models.DescribeDcdnWafServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_service_with_options(request, runtime)

    async def describe_dcdn_waf_service_async(
        self,
        request: main_models.DescribeDcdnWafServiceRequest,
    ) -> main_models.DescribeDcdnWafServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_service_with_options_async(request, runtime)

    def describe_dcdn_waf_spec_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafSpecInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafSpecInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_spec_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafSpecInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafSpecInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafSpecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_spec_info(self) -> main_models.DescribeDcdnWafSpecInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_spec_info_with_options(runtime)

    async def describe_dcdn_waf_spec_info_async(self) -> main_models.DescribeDcdnWafSpecInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_spec_info_with_options_async(runtime)

    def describe_dcdn_waf_usage_data_with_options(
        self,
        request: main_models.DescribeDcdnWafUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_usage_data_with_options_async(
        self,
        request: main_models.DescribeDcdnWafUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnWafUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnWafUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnWafUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_usage_data(
        self,
        request: main_models.DescribeDcdnWafUsageDataRequest,
    ) -> main_models.DescribeDcdnWafUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdn_waf_usage_data_with_options(request, runtime)

    async def describe_dcdn_waf_usage_data_async(
        self,
        request: main_models.DescribeDcdnWafUsageDataRequest,
    ) -> main_models.DescribeDcdnWafUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdn_waf_usage_data_with_options_async(request, runtime)

    def describe_dcdnsec_service_with_options(
        self,
        request: main_models.DescribeDcdnsecServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnsecServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnsecService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnsecServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdnsec_service_with_options_async(
        self,
        request: main_models.DescribeDcdnsecServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDcdnsecServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDcdnsecService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDcdnsecServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdnsec_service(
        self,
        request: main_models.DescribeDcdnsecServiceRequest,
    ) -> main_models.DescribeDcdnsecServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_dcdnsec_service_with_options(request, runtime)

    async def describe_dcdnsec_service_async(
        self,
        request: main_models.DescribeDcdnsecServiceRequest,
    ) -> main_models.DescribeDcdnsecServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dcdnsec_service_with_options_async(request, runtime)

    def describe_ddos_all_event_list_with_options(
        self,
        request: main_models.DescribeDdosAllEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosAllEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosAllEventList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosAllEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_all_event_list_with_options_async(
        self,
        request: main_models.DescribeDdosAllEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosAllEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosAllEventList',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosAllEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_all_event_list(
        self,
        request: main_models.DescribeDdosAllEventListRequest,
    ) -> main_models.DescribeDdosAllEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_all_event_list_with_options(request, runtime)

    async def describe_ddos_all_event_list_async(
        self,
        request: main_models.DescribeDdosAllEventListRequest,
    ) -> main_models.DescribeDdosAllEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_all_event_list_with_options_async(request, runtime)

    def describe_encrypt_routine_uid_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEncryptRoutineUidResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeEncryptRoutineUid',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEncryptRoutineUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_encrypt_routine_uid_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEncryptRoutineUidResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeEncryptRoutineUid',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEncryptRoutineUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_encrypt_routine_uid(self) -> main_models.DescribeEncryptRoutineUidResponse:
        runtime = RuntimeOptions()
        return self.describe_encrypt_routine_uid_with_options(runtime)

    async def describe_encrypt_routine_uid_async(self) -> main_models.DescribeEncryptRoutineUidResponse:
        runtime = RuntimeOptions()
        return await self.describe_encrypt_routine_uid_with_options_async(runtime)

    def describe_highlight_info_with_options(
        self,
        request: main_models.DescribeHighlightInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHighlightInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHighlightInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHighlightInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_highlight_info_with_options_async(
        self,
        request: main_models.DescribeHighlightInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHighlightInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHighlightInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHighlightInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_highlight_info(
        self,
        request: main_models.DescribeHighlightInfoRequest,
    ) -> main_models.DescribeHighlightInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_highlight_info_with_options(request, runtime)

    async def describe_highlight_info_async(
        self,
        request: main_models.DescribeHighlightInfoRequest,
    ) -> main_models.DescribeHighlightInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_highlight_info_with_options_async(request, runtime)

    def describe_kv_real_time_qps_data_with_options(
        self,
        request: main_models.DescribeKvRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKvRealTimeQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKvRealTimeQpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKvRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kv_real_time_qps_data_with_options_async(
        self,
        request: main_models.DescribeKvRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKvRealTimeQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKvRealTimeQpsData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKvRealTimeQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kv_real_time_qps_data(
        self,
        request: main_models.DescribeKvRealTimeQpsDataRequest,
    ) -> main_models.DescribeKvRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_kv_real_time_qps_data_with_options(request, runtime)

    async def describe_kv_real_time_qps_data_async(
        self,
        request: main_models.DescribeKvRealTimeQpsDataRequest,
    ) -> main_models.DescribeKvRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_kv_real_time_qps_data_with_options_async(request, runtime)

    def describe_kv_usage_data_with_options(
        self,
        request: main_models.DescribeKvUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKvUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.response_type):
            query['ResponseType'] = request.response_type
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKvUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKvUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kv_usage_data_with_options_async(
        self,
        request: main_models.DescribeKvUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKvUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.response_type):
            query['ResponseType'] = request.response_type
        if not DaraCore.is_null(request.split_by):
            query['SplitBy'] = request.split_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKvUsageData',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKvUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kv_usage_data(
        self,
        request: main_models.DescribeKvUsageDataRequest,
    ) -> main_models.DescribeKvUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_kv_usage_data_with_options(request, runtime)

    async def describe_kv_usage_data_async(
        self,
        request: main_models.DescribeKvUsageDataRequest,
    ) -> main_models.DescribeKvUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_kv_usage_data_with_options_async(request, runtime)

    def describe_rddomain_config_with_options(
        self,
        request: main_models.DescribeRDDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRDDomainConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRDDomainConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRDDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rddomain_config_with_options_async(
        self,
        request: main_models.DescribeRDDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRDDomainConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRDDomainConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRDDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rddomain_config(
        self,
        request: main_models.DescribeRDDomainConfigRequest,
    ) -> main_models.DescribeRDDomainConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_rddomain_config_with_options(request, runtime)

    async def describe_rddomain_config_async(
        self,
        request: main_models.DescribeRDDomainConfigRequest,
    ) -> main_models.DescribeRDDomainConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_rddomain_config_with_options_async(request, runtime)

    def describe_rddomains_with_options(
        self,
        request: main_models.DescribeRDDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRDDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRDDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRDDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rddomains_with_options_async(
        self,
        request: main_models.DescribeRDDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRDDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRDDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRDDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rddomains(
        self,
        request: main_models.DescribeRDDomainsRequest,
    ) -> main_models.DescribeRDDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_rddomains_with_options(request, runtime)

    async def describe_rddomains_async(
        self,
        request: main_models.DescribeRDDomainsRequest,
    ) -> main_models.DescribeRDDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_rddomains_with_options_async(request, runtime)

    def describe_routine_with_options(
        self,
        request: main_models.DescribeRoutineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoutine',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_with_options_async(
        self,
        request: main_models.DescribeRoutineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoutine',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine(
        self,
        request: main_models.DescribeRoutineRequest,
    ) -> main_models.DescribeRoutineResponse:
        runtime = RuntimeOptions()
        return self.describe_routine_with_options(request, runtime)

    async def describe_routine_async(
        self,
        request: main_models.DescribeRoutineRequest,
    ) -> main_models.DescribeRoutineResponse:
        runtime = RuntimeOptions()
        return await self.describe_routine_with_options_async(request, runtime)

    def describe_routine_canary_envs_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineCanaryEnvsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRoutineCanaryEnvs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineCanaryEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_canary_envs_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineCanaryEnvsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRoutineCanaryEnvs',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineCanaryEnvsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_canary_envs(self) -> main_models.DescribeRoutineCanaryEnvsResponse:
        runtime = RuntimeOptions()
        return self.describe_routine_canary_envs_with_options(runtime)

    async def describe_routine_canary_envs_async(self) -> main_models.DescribeRoutineCanaryEnvsResponse:
        runtime = RuntimeOptions()
        return await self.describe_routine_canary_envs_with_options_async(runtime)

    def describe_routine_code_revision_with_options(
        self,
        request: main_models.DescribeRoutineCodeRevisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineCodeRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoutineCodeRevision',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_code_revision_with_options_async(
        self,
        request: main_models.DescribeRoutineCodeRevisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineCodeRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoutineCodeRevision',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineCodeRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_code_revision(
        self,
        request: main_models.DescribeRoutineCodeRevisionRequest,
    ) -> main_models.DescribeRoutineCodeRevisionResponse:
        runtime = RuntimeOptions()
        return self.describe_routine_code_revision_with_options(request, runtime)

    async def describe_routine_code_revision_async(
        self,
        request: main_models.DescribeRoutineCodeRevisionRequest,
    ) -> main_models.DescribeRoutineCodeRevisionResponse:
        runtime = RuntimeOptions()
        return await self.describe_routine_code_revision_with_options_async(request, runtime)

    def describe_routine_related_domains_with_options(
        self,
        request: main_models.DescribeRoutineRelatedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineRelatedDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoutineRelatedDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineRelatedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_related_domains_with_options_async(
        self,
        request: main_models.DescribeRoutineRelatedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineRelatedDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoutineRelatedDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineRelatedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_related_domains(
        self,
        request: main_models.DescribeRoutineRelatedDomainsRequest,
    ) -> main_models.DescribeRoutineRelatedDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_routine_related_domains_with_options(request, runtime)

    async def describe_routine_related_domains_async(
        self,
        request: main_models.DescribeRoutineRelatedDomainsRequest,
    ) -> main_models.DescribeRoutineRelatedDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_routine_related_domains_with_options_async(request, runtime)

    def describe_routine_spec_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineSpecResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRoutineSpec',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_spec_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineSpecResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRoutineSpec',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_spec(self) -> main_models.DescribeRoutineSpecResponse:
        runtime = RuntimeOptions()
        return self.describe_routine_spec_with_options(runtime)

    async def describe_routine_spec_async(self) -> main_models.DescribeRoutineSpecResponse:
        runtime = RuntimeOptions()
        return await self.describe_routine_spec_with_options_async(runtime)

    def describe_routine_user_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineUserInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRoutineUserInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_user_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoutineUserInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRoutineUserInfo',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoutineUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_user_info(self) -> main_models.DescribeRoutineUserInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_routine_user_info_with_options(runtime)

    async def describe_routine_user_info_async(self) -> main_models.DescribeRoutineUserInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_routine_user_info_with_options_async(runtime)

    def describe_user_dcdn_ipa_status_with_options(
        self,
        request: main_models.DescribeUserDcdnIpaStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserDcdnIpaStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserDcdnIpaStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserDcdnIpaStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_dcdn_ipa_status_with_options_async(
        self,
        request: main_models.DescribeUserDcdnIpaStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserDcdnIpaStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserDcdnIpaStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserDcdnIpaStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_dcdn_ipa_status(
        self,
        request: main_models.DescribeUserDcdnIpaStatusRequest,
    ) -> main_models.DescribeUserDcdnIpaStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_dcdn_ipa_status_with_options(request, runtime)

    async def describe_user_dcdn_ipa_status_async(
        self,
        request: main_models.DescribeUserDcdnIpaStatusRequest,
    ) -> main_models.DescribeUserDcdnIpaStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_dcdn_ipa_status_with_options_async(request, runtime)

    def describe_user_dcdn_status_with_options(
        self,
        request: main_models.DescribeUserDcdnStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserDcdnStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserDcdnStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserDcdnStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_dcdn_status_with_options_async(
        self,
        request: main_models.DescribeUserDcdnStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserDcdnStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserDcdnStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserDcdnStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_dcdn_status(
        self,
        request: main_models.DescribeUserDcdnStatusRequest,
    ) -> main_models.DescribeUserDcdnStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_dcdn_status_with_options(request, runtime)

    async def describe_user_dcdn_status_async(
        self,
        request: main_models.DescribeUserDcdnStatusRequest,
    ) -> main_models.DescribeUserDcdnStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_dcdn_status_with_options_async(request, runtime)

    def describe_user_er_status_with_options(
        self,
        request: main_models.DescribeUserErStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserErStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserErStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserErStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_er_status_with_options_async(
        self,
        request: main_models.DescribeUserErStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserErStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserErStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserErStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_er_status(
        self,
        request: main_models.DescribeUserErStatusRequest,
    ) -> main_models.DescribeUserErStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_er_status_with_options(request, runtime)

    async def describe_user_er_status_async(
        self,
        request: main_models.DescribeUserErStatusRequest,
    ) -> main_models.DescribeUserErStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_er_status_with_options_async(request, runtime)

    def describe_user_logservice_status_with_options(
        self,
        request: main_models.DescribeUserLogserviceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserLogserviceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserLogserviceStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserLogserviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_logservice_status_with_options_async(
        self,
        request: main_models.DescribeUserLogserviceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserLogserviceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserLogserviceStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserLogserviceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_logservice_status(
        self,
        request: main_models.DescribeUserLogserviceStatusRequest,
    ) -> main_models.DescribeUserLogserviceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_logservice_status_with_options(request, runtime)

    async def describe_user_logservice_status_async(
        self,
        request: main_models.DescribeUserLogserviceStatusRequest,
    ) -> main_models.DescribeUserLogserviceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_logservice_status_with_options_async(request, runtime)

    def edit_routine_conf_with_options(
        self,
        tmp_req: main_models.EditRoutineConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditRoutineConfResponse:
        tmp_req.validate()
        request = main_models.EditRoutineConfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.env_conf):
            request.env_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditRoutineConf',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditRoutineConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_routine_conf_with_options_async(
        self,
        tmp_req: main_models.EditRoutineConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditRoutineConfResponse:
        tmp_req.validate()
        request = main_models.EditRoutineConfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.env_conf):
            request.env_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditRoutineConf',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditRoutineConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_routine_conf(
        self,
        request: main_models.EditRoutineConfRequest,
    ) -> main_models.EditRoutineConfResponse:
        runtime = RuntimeOptions()
        return self.edit_routine_conf_with_options(request, runtime)

    async def edit_routine_conf_async(
        self,
        request: main_models.EditRoutineConfRequest,
    ) -> main_models.EditRoutineConfResponse:
        runtime = RuntimeOptions()
        return await self.edit_routine_conf_with_options_async(request, runtime)

    def get_dcdn_kv_with_options(
        self,
        request: main_models.GetDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDcdnKvResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dcdn_kv_with_options_async(
        self,
        request: main_models.GetDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDcdnKvResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dcdn_kv(
        self,
        request: main_models.GetDcdnKvRequest,
    ) -> main_models.GetDcdnKvResponse:
        runtime = RuntimeOptions()
        return self.get_dcdn_kv_with_options(request, runtime)

    async def get_dcdn_kv_async(
        self,
        request: main_models.GetDcdnKvRequest,
    ) -> main_models.GetDcdnKvResponse:
        runtime = RuntimeOptions()
        return await self.get_dcdn_kv_with_options_async(request, runtime)

    def get_dcdn_kv_detail_with_options(
        self,
        request: main_models.GetDcdnKvDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDcdnKvDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDcdnKvDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDcdnKvDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dcdn_kv_detail_with_options_async(
        self,
        request: main_models.GetDcdnKvDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDcdnKvDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDcdnKvDetail',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDcdnKvDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dcdn_kv_detail(
        self,
        request: main_models.GetDcdnKvDetailRequest,
    ) -> main_models.GetDcdnKvDetailResponse:
        runtime = RuntimeOptions()
        return self.get_dcdn_kv_detail_with_options(request, runtime)

    async def get_dcdn_kv_detail_async(
        self,
        request: main_models.GetDcdnKvDetailRequest,
    ) -> main_models.GetDcdnKvDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_dcdn_kv_detail_with_options_async(request, runtime)

    def get_dcdn_kv_status_with_options(
        self,
        request: main_models.GetDcdnKvStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDcdnKvStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDcdnKvStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDcdnKvStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dcdn_kv_status_with_options_async(
        self,
        request: main_models.GetDcdnKvStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDcdnKvStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDcdnKvStatus',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDcdnKvStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dcdn_kv_status(
        self,
        request: main_models.GetDcdnKvStatusRequest,
    ) -> main_models.GetDcdnKvStatusResponse:
        runtime = RuntimeOptions()
        return self.get_dcdn_kv_status_with_options(request, runtime)

    async def get_dcdn_kv_status_async(
        self,
        request: main_models.GetDcdnKvStatusRequest,
    ) -> main_models.GetDcdnKvStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_dcdn_kv_status_with_options_async(request, runtime)

    def list_dcdn_kv_with_options(
        self,
        request: main_models.ListDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDcdnKvResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dcdn_kv_with_options_async(
        self,
        request: main_models.ListDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDcdnKvResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dcdn_kv(
        self,
        request: main_models.ListDcdnKvRequest,
    ) -> main_models.ListDcdnKvResponse:
        runtime = RuntimeOptions()
        return self.list_dcdn_kv_with_options(request, runtime)

    async def list_dcdn_kv_async(
        self,
        request: main_models.ListDcdnKvRequest,
    ) -> main_models.ListDcdnKvResponse:
        runtime = RuntimeOptions()
        return await self.list_dcdn_kv_with_options_async(request, runtime)

    def list_dcdn_real_time_delivery_project_with_options(
        self,
        request: main_models.ListDcdnRealTimeDeliveryProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDcdnRealTimeDeliveryProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDcdnRealTimeDeliveryProject',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDcdnRealTimeDeliveryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dcdn_real_time_delivery_project_with_options_async(
        self,
        request: main_models.ListDcdnRealTimeDeliveryProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDcdnRealTimeDeliveryProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDcdnRealTimeDeliveryProject',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDcdnRealTimeDeliveryProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dcdn_real_time_delivery_project(
        self,
        request: main_models.ListDcdnRealTimeDeliveryProjectRequest,
    ) -> main_models.ListDcdnRealTimeDeliveryProjectResponse:
        runtime = RuntimeOptions()
        return self.list_dcdn_real_time_delivery_project_with_options(request, runtime)

    async def list_dcdn_real_time_delivery_project_async(
        self,
        request: main_models.ListDcdnRealTimeDeliveryProjectRequest,
    ) -> main_models.ListDcdnRealTimeDeliveryProjectResponse:
        runtime = RuntimeOptions()
        return await self.list_dcdn_real_time_delivery_project_with_options_async(request, runtime)

    def modify_custom_domain_sample_rate_with_options(
        self,
        request: main_models.ModifyCustomDomainSampleRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomDomainSampleRateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_config_id):
            body['BaseConfigID'] = request.base_config_id
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.sink_id):
            body['SinkID'] = request.sink_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomDomainSampleRate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomDomainSampleRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_domain_sample_rate_with_options_async(
        self,
        request: main_models.ModifyCustomDomainSampleRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomDomainSampleRateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_config_id):
            body['BaseConfigID'] = request.base_config_id
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.sink_id):
            body['SinkID'] = request.sink_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomDomainSampleRate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomDomainSampleRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_domain_sample_rate(
        self,
        request: main_models.ModifyCustomDomainSampleRateRequest,
    ) -> main_models.ModifyCustomDomainSampleRateResponse:
        runtime = RuntimeOptions()
        return self.modify_custom_domain_sample_rate_with_options(request, runtime)

    async def modify_custom_domain_sample_rate_async(
        self,
        request: main_models.ModifyCustomDomainSampleRateRequest,
    ) -> main_models.ModifyCustomDomainSampleRateResponse:
        runtime = RuntimeOptions()
        return await self.modify_custom_domain_sample_rate_with_options_async(request, runtime)

    def modify_dcdn_domain_schdm_by_property_with_options(
        self,
        request: main_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDCdnDomainSchdmByPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.property):
            query['Property'] = request.property
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDCdnDomainSchdmByProperty',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_domain_schdm_by_property_with_options_async(
        self,
        request: main_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDCdnDomainSchdmByPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.property):
            query['Property'] = request.property
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDCdnDomainSchdmByProperty',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_domain_schdm_by_property(
        self,
        request: main_models.ModifyDCdnDomainSchdmByPropertyRequest,
    ) -> main_models.ModifyDCdnDomainSchdmByPropertyResponse:
        runtime = RuntimeOptions()
        return self.modify_dcdn_domain_schdm_by_property_with_options(request, runtime)

    async def modify_dcdn_domain_schdm_by_property_async(
        self,
        request: main_models.ModifyDCdnDomainSchdmByPropertyRequest,
    ) -> main_models.ModifyDCdnDomainSchdmByPropertyResponse:
        runtime = RuntimeOptions()
        return await self.modify_dcdn_domain_schdm_by_property_with_options_async(request, runtime)

    def modify_dcdn_waf_group_with_options(
        self,
        request: main_models.ModifyDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_group_with_options_async(
        self,
        request: main_models.ModifyDcdnWafGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafGroup',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_group(
        self,
        request: main_models.ModifyDcdnWafGroupRequest,
    ) -> main_models.ModifyDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_dcdn_waf_group_with_options(request, runtime)

    async def modify_dcdn_waf_group_async(
        self,
        request: main_models.ModifyDcdnWafGroupRequest,
    ) -> main_models.ModifyDcdnWafGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_dcdn_waf_group_with_options_async(request, runtime)

    def modify_dcdn_waf_policy_with_options(
        self,
        request: main_models.ModifyDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_policy_with_options_async(
        self,
        request: main_models.ModifyDcdnWafPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafPolicy',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_policy(
        self,
        request: main_models.ModifyDcdnWafPolicyRequest,
    ) -> main_models.ModifyDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_dcdn_waf_policy_with_options(request, runtime)

    async def modify_dcdn_waf_policy_async(
        self,
        request: main_models.ModifyDcdnWafPolicyRequest,
    ) -> main_models.ModifyDcdnWafPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_dcdn_waf_policy_with_options_async(request, runtime)

    def modify_dcdn_waf_policy_domains_with_options(
        self,
        request: main_models.ModifyDcdnWafPolicyDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafPolicyDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bind_domains):
            body['BindDomains'] = request.bind_domains
        if not DaraCore.is_null(request.method):
            body['Method'] = request.method
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.unbind_domains):
            body['UnbindDomains'] = request.unbind_domains
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafPolicyDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafPolicyDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_policy_domains_with_options_async(
        self,
        request: main_models.ModifyDcdnWafPolicyDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafPolicyDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bind_domains):
            body['BindDomains'] = request.bind_domains
        if not DaraCore.is_null(request.method):
            body['Method'] = request.method
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.unbind_domains):
            body['UnbindDomains'] = request.unbind_domains
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafPolicyDomains',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafPolicyDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_policy_domains(
        self,
        request: main_models.ModifyDcdnWafPolicyDomainsRequest,
    ) -> main_models.ModifyDcdnWafPolicyDomainsResponse:
        runtime = RuntimeOptions()
        return self.modify_dcdn_waf_policy_domains_with_options(request, runtime)

    async def modify_dcdn_waf_policy_domains_async(
        self,
        request: main_models.ModifyDcdnWafPolicyDomainsRequest,
    ) -> main_models.ModifyDcdnWafPolicyDomainsResponse:
        runtime = RuntimeOptions()
        return await self.modify_dcdn_waf_policy_domains_with_options_async(request, runtime)

    def modify_dcdn_waf_rule_with_options(
        self,
        request: main_models.ModifyDcdnWafRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.rule_config):
            body['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            body['RuleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafRule',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_rule_with_options_async(
        self,
        request: main_models.ModifyDcdnWafRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDcdnWafRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.rule_config):
            body['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            body['RuleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDcdnWafRule',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDcdnWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_rule(
        self,
        request: main_models.ModifyDcdnWafRuleRequest,
    ) -> main_models.ModifyDcdnWafRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_dcdn_waf_rule_with_options(request, runtime)

    async def modify_dcdn_waf_rule_async(
        self,
        request: main_models.ModifyDcdnWafRuleRequest,
    ) -> main_models.ModifyDcdnWafRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_dcdn_waf_rule_with_options_async(request, runtime)

    def open_dcdn_service_with_options(
        self,
        request: main_models.OpenDcdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenDcdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_type):
            query['BillType'] = request.bill_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.websocket_bill_type):
            query['WebsocketBillType'] = request.websocket_bill_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenDcdnService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDcdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_dcdn_service_with_options_async(
        self,
        request: main_models.OpenDcdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenDcdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_type):
            query['BillType'] = request.bill_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.websocket_bill_type):
            query['WebsocketBillType'] = request.websocket_bill_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenDcdnService',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDcdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_dcdn_service(
        self,
        request: main_models.OpenDcdnServiceRequest,
    ) -> main_models.OpenDcdnServiceResponse:
        runtime = RuntimeOptions()
        return self.open_dcdn_service_with_options(request, runtime)

    async def open_dcdn_service_async(
        self,
        request: main_models.OpenDcdnServiceRequest,
    ) -> main_models.OpenDcdnServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_dcdn_service_with_options_async(request, runtime)

    def preload_dcdn_object_caches_with_options(
        self,
        request: main_models.PreloadDcdnObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreloadDcdnObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.l_2preload):
            query['L2Preload'] = request.l_2preload
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_hashkey):
            query['QueryHashkey'] = request.query_hashkey
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.with_header):
            query['WithHeader'] = request.with_header
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreloadDcdnObjectCaches',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreloadDcdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_dcdn_object_caches_with_options_async(
        self,
        request: main_models.PreloadDcdnObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreloadDcdnObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.l_2preload):
            query['L2Preload'] = request.l_2preload
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_hashkey):
            query['QueryHashkey'] = request.query_hashkey
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.with_header):
            query['WithHeader'] = request.with_header
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreloadDcdnObjectCaches',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreloadDcdnObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_dcdn_object_caches(
        self,
        request: main_models.PreloadDcdnObjectCachesRequest,
    ) -> main_models.PreloadDcdnObjectCachesResponse:
        runtime = RuntimeOptions()
        return self.preload_dcdn_object_caches_with_options(request, runtime)

    async def preload_dcdn_object_caches_async(
        self,
        request: main_models.PreloadDcdnObjectCachesRequest,
    ) -> main_models.PreloadDcdnObjectCachesResponse:
        runtime = RuntimeOptions()
        return await self.preload_dcdn_object_caches_with_options_async(request, runtime)

    def publish_dcdn_staging_config_to_production_with_options(
        self,
        request: main_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishDcdnStagingConfigToProductionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishDcdnStagingConfigToProduction',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishDcdnStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_dcdn_staging_config_to_production_with_options_async(
        self,
        request: main_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishDcdnStagingConfigToProductionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishDcdnStagingConfigToProduction',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishDcdnStagingConfigToProductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_dcdn_staging_config_to_production(
        self,
        request: main_models.PublishDcdnStagingConfigToProductionRequest,
    ) -> main_models.PublishDcdnStagingConfigToProductionResponse:
        runtime = RuntimeOptions()
        return self.publish_dcdn_staging_config_to_production_with_options(request, runtime)

    async def publish_dcdn_staging_config_to_production_async(
        self,
        request: main_models.PublishDcdnStagingConfigToProductionRequest,
    ) -> main_models.PublishDcdnStagingConfigToProductionResponse:
        runtime = RuntimeOptions()
        return await self.publish_dcdn_staging_config_to_production_with_options_async(request, runtime)

    def publish_routine_code_revision_with_options(
        self,
        tmp_req: main_models.PublishRoutineCodeRevisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishRoutineCodeRevisionResponse:
        tmp_req.validate()
        request = main_models.PublishRoutineCodeRevisionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.envs):
            request.envs_shrink = Utils.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not DaraCore.is_null(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRoutineCodeRevision',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_routine_code_revision_with_options_async(
        self,
        tmp_req: main_models.PublishRoutineCodeRevisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishRoutineCodeRevisionResponse:
        tmp_req.validate()
        request = main_models.PublishRoutineCodeRevisionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.envs):
            request.envs_shrink = Utils.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not DaraCore.is_null(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRoutineCodeRevision',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRoutineCodeRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_routine_code_revision(
        self,
        request: main_models.PublishRoutineCodeRevisionRequest,
    ) -> main_models.PublishRoutineCodeRevisionResponse:
        runtime = RuntimeOptions()
        return self.publish_routine_code_revision_with_options(request, runtime)

    async def publish_routine_code_revision_async(
        self,
        request: main_models.PublishRoutineCodeRevisionRequest,
    ) -> main_models.PublishRoutineCodeRevisionResponse:
        runtime = RuntimeOptions()
        return await self.publish_routine_code_revision_with_options_async(request, runtime)

    def put_dcdn_kv_with_options(
        self,
        request: main_models.PutDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDcdnKvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.expiration_ttl):
            query['ExpirationTtl'] = request.expiration_ttl
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_dcdn_kv_with_options_async(
        self,
        request: main_models.PutDcdnKvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDcdnKvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.expiration_ttl):
            query['ExpirationTtl'] = request.expiration_ttl
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutDcdnKv',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_dcdn_kv(
        self,
        request: main_models.PutDcdnKvRequest,
    ) -> main_models.PutDcdnKvResponse:
        runtime = RuntimeOptions()
        return self.put_dcdn_kv_with_options(request, runtime)

    async def put_dcdn_kv_async(
        self,
        request: main_models.PutDcdnKvRequest,
    ) -> main_models.PutDcdnKvResponse:
        runtime = RuntimeOptions()
        return await self.put_dcdn_kv_with_options_async(request, runtime)

    def put_dcdn_kv_namespace_with_options(
        self,
        request: main_models.PutDcdnKvNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDcdnKvNamespaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutDcdnKvNamespace',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDcdnKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_dcdn_kv_namespace_with_options_async(
        self,
        request: main_models.PutDcdnKvNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDcdnKvNamespaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutDcdnKvNamespace',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDcdnKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_dcdn_kv_namespace(
        self,
        request: main_models.PutDcdnKvNamespaceRequest,
    ) -> main_models.PutDcdnKvNamespaceResponse:
        runtime = RuntimeOptions()
        return self.put_dcdn_kv_namespace_with_options(request, runtime)

    async def put_dcdn_kv_namespace_async(
        self,
        request: main_models.PutDcdnKvNamespaceRequest,
    ) -> main_models.PutDcdnKvNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.put_dcdn_kv_namespace_with_options_async(request, runtime)

    def put_dcdn_kv_with_high_capacity_with_options(
        self,
        request: main_models.PutDcdnKvWithHighCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDcdnKvWithHighCapacityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDcdnKvWithHighCapacity',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDcdnKvWithHighCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_dcdn_kv_with_high_capacity_with_options_async(
        self,
        request: main_models.PutDcdnKvWithHighCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDcdnKvWithHighCapacityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDcdnKvWithHighCapacity',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDcdnKvWithHighCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_dcdn_kv_with_high_capacity(
        self,
        request: main_models.PutDcdnKvWithHighCapacityRequest,
    ) -> main_models.PutDcdnKvWithHighCapacityResponse:
        runtime = RuntimeOptions()
        return self.put_dcdn_kv_with_high_capacity_with_options(request, runtime)

    async def put_dcdn_kv_with_high_capacity_async(
        self,
        request: main_models.PutDcdnKvWithHighCapacityRequest,
    ) -> main_models.PutDcdnKvWithHighCapacityResponse:
        runtime = RuntimeOptions()
        return await self.put_dcdn_kv_with_high_capacity_with_options_async(request, runtime)

    def refresh_dcdn_object_cache_by_cache_tag_with_options(
        self,
        request: main_models.RefreshDcdnObjectCacheByCacheTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDcdnObjectCacheByCacheTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_tag):
            query['CacheTag'] = request.cache_tag
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDcdnObjectCacheByCacheTag',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDcdnObjectCacheByCacheTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_dcdn_object_cache_by_cache_tag_with_options_async(
        self,
        request: main_models.RefreshDcdnObjectCacheByCacheTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDcdnObjectCacheByCacheTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_tag):
            query['CacheTag'] = request.cache_tag
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDcdnObjectCacheByCacheTag',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDcdnObjectCacheByCacheTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_dcdn_object_cache_by_cache_tag(
        self,
        request: main_models.RefreshDcdnObjectCacheByCacheTagRequest,
    ) -> main_models.RefreshDcdnObjectCacheByCacheTagResponse:
        runtime = RuntimeOptions()
        return self.refresh_dcdn_object_cache_by_cache_tag_with_options(request, runtime)

    async def refresh_dcdn_object_cache_by_cache_tag_async(
        self,
        request: main_models.RefreshDcdnObjectCacheByCacheTagRequest,
    ) -> main_models.RefreshDcdnObjectCacheByCacheTagResponse:
        runtime = RuntimeOptions()
        return await self.refresh_dcdn_object_cache_by_cache_tag_with_options_async(request, runtime)

    def refresh_dcdn_object_caches_with_options(
        self,
        request: main_models.RefreshDcdnObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDcdnObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDcdnObjectCaches',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDcdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_dcdn_object_caches_with_options_async(
        self,
        request: main_models.RefreshDcdnObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDcdnObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDcdnObjectCaches',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDcdnObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_dcdn_object_caches(
        self,
        request: main_models.RefreshDcdnObjectCachesRequest,
    ) -> main_models.RefreshDcdnObjectCachesResponse:
        runtime = RuntimeOptions()
        return self.refresh_dcdn_object_caches_with_options(request, runtime)

    async def refresh_dcdn_object_caches_async(
        self,
        request: main_models.RefreshDcdnObjectCachesRequest,
    ) -> main_models.RefreshDcdnObjectCachesResponse:
        runtime = RuntimeOptions()
        return await self.refresh_dcdn_object_caches_with_options_async(request, runtime)

    def refresh_er_object_caches_with_options(
        self,
        request: main_models.RefreshErObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshErObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.merge_domain_name):
            query['MergeDomainName'] = request.merge_domain_name
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.routine_id):
            query['RoutineId'] = request.routine_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshErObjectCaches',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshErObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_er_object_caches_with_options_async(
        self,
        request: main_models.RefreshErObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshErObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.merge_domain_name):
            query['MergeDomainName'] = request.merge_domain_name
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.routine_id):
            query['RoutineId'] = request.routine_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshErObjectCaches',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshErObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_er_object_caches(
        self,
        request: main_models.RefreshErObjectCachesRequest,
    ) -> main_models.RefreshErObjectCachesResponse:
        runtime = RuntimeOptions()
        return self.refresh_er_object_caches_with_options(request, runtime)

    async def refresh_er_object_caches_async(
        self,
        request: main_models.RefreshErObjectCachesRequest,
    ) -> main_models.RefreshErObjectCachesResponse:
        runtime = RuntimeOptions()
        return await self.refresh_er_object_caches_with_options_async(request, runtime)

    def refresh_er_object_caches_by_cache_tag_with_options(
        self,
        request: main_models.RefreshErObjectCachesByCacheTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshErObjectCachesByCacheTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_tag):
            query['CacheTag'] = request.cache_tag
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.merge_domain_name):
            query['MergeDomainName'] = request.merge_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshErObjectCachesByCacheTag',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshErObjectCachesByCacheTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_er_object_caches_by_cache_tag_with_options_async(
        self,
        request: main_models.RefreshErObjectCachesByCacheTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshErObjectCachesByCacheTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_tag):
            query['CacheTag'] = request.cache_tag
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.merge_domain_name):
            query['MergeDomainName'] = request.merge_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshErObjectCachesByCacheTag',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshErObjectCachesByCacheTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_er_object_caches_by_cache_tag(
        self,
        request: main_models.RefreshErObjectCachesByCacheTagRequest,
    ) -> main_models.RefreshErObjectCachesByCacheTagResponse:
        runtime = RuntimeOptions()
        return self.refresh_er_object_caches_by_cache_tag_with_options(request, runtime)

    async def refresh_er_object_caches_by_cache_tag_async(
        self,
        request: main_models.RefreshErObjectCachesByCacheTagRequest,
    ) -> main_models.RefreshErObjectCachesByCacheTagResponse:
        runtime = RuntimeOptions()
        return await self.refresh_er_object_caches_by_cache_tag_with_options_async(request, runtime)

    def rollback_dcdn_staging_config_with_options(
        self,
        request: main_models.RollbackDcdnStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackDcdnStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackDcdnStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackDcdnStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_dcdn_staging_config_with_options_async(
        self,
        request: main_models.RollbackDcdnStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackDcdnStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackDcdnStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackDcdnStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_dcdn_staging_config(
        self,
        request: main_models.RollbackDcdnStagingConfigRequest,
    ) -> main_models.RollbackDcdnStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.rollback_dcdn_staging_config_with_options(request, runtime)

    async def rollback_dcdn_staging_config_async(
        self,
        request: main_models.RollbackDcdnStagingConfigRequest,
    ) -> main_models.RollbackDcdnStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.rollback_dcdn_staging_config_with_options_async(request, runtime)

    def set_dcdn_domain_csrcertificate_with_options(
        self,
        request: main_models.SetDcdnDomainCSRCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainCSRCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainCSRCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainCSRCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_csrcertificate_with_options_async(
        self,
        request: main_models.SetDcdnDomainCSRCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainCSRCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainCSRCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainCSRCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_csrcertificate(
        self,
        request: main_models.SetDcdnDomainCSRCertificateRequest,
    ) -> main_models.SetDcdnDomainCSRCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_dcdn_domain_csrcertificate_with_options(request, runtime)

    async def set_dcdn_domain_csrcertificate_async(
        self,
        request: main_models.SetDcdnDomainCSRCertificateRequest,
    ) -> main_models.SetDcdnDomainCSRCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_dcdn_domain_csrcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_smcertificate_with_options(
        self,
        request: main_models.SetDcdnDomainSMCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainSMCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainSMCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainSMCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_smcertificate_with_options_async(
        self,
        request: main_models.SetDcdnDomainSMCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainSMCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainSMCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainSMCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_smcertificate(
        self,
        request: main_models.SetDcdnDomainSMCertificateRequest,
    ) -> main_models.SetDcdnDomainSMCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_dcdn_domain_smcertificate_with_options(request, runtime)

    async def set_dcdn_domain_smcertificate_async(
        self,
        request: main_models.SetDcdnDomainSMCertificateRequest,
    ) -> main_models.SetDcdnDomainSMCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_dcdn_domain_smcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_sslcertificate_with_options(
        self,
        request: main_models.SetDcdnDomainSSLCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainSSLCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainSSLCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_sslcertificate_with_options_async(
        self,
        request: main_models.SetDcdnDomainSSLCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainSSLCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainSSLCertificate',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_sslcertificate(
        self,
        request: main_models.SetDcdnDomainSSLCertificateRequest,
    ) -> main_models.SetDcdnDomainSSLCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_dcdn_domain_sslcertificate_with_options(request, runtime)

    async def set_dcdn_domain_sslcertificate_async(
        self,
        request: main_models.SetDcdnDomainSSLCertificateRequest,
    ) -> main_models.SetDcdnDomainSSLCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_dcdn_domain_sslcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_staging_config_with_options(
        self,
        request: main_models.SetDcdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_staging_config_with_options_async(
        self,
        request: main_models.SetDcdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnDomainStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnDomainStagingConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_staging_config(
        self,
        request: main_models.SetDcdnDomainStagingConfigRequest,
    ) -> main_models.SetDcdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.set_dcdn_domain_staging_config_with_options(request, runtime)

    async def set_dcdn_domain_staging_config_async(
        self,
        request: main_models.SetDcdnDomainStagingConfigRequest,
    ) -> main_models.SetDcdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_dcdn_domain_staging_config_with_options_async(request, runtime)

    def set_dcdn_full_domains_block_ipwith_options(
        self,
        request: main_models.SetDcdnFullDomainsBlockIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnFullDomainsBlockIPResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.block_interval):
            body['BlockInterval'] = request.block_interval
        if not DaraCore.is_null(request.iplist):
            body['IPList'] = request.iplist
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.update_type):
            body['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnFullDomainsBlockIP',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnFullDomainsBlockIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_full_domains_block_ipwith_options_async(
        self,
        request: main_models.SetDcdnFullDomainsBlockIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnFullDomainsBlockIPResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.block_interval):
            body['BlockInterval'] = request.block_interval
        if not DaraCore.is_null(request.iplist):
            body['IPList'] = request.iplist
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.update_type):
            body['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnFullDomainsBlockIP',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnFullDomainsBlockIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_full_domains_block_ip(
        self,
        request: main_models.SetDcdnFullDomainsBlockIPRequest,
    ) -> main_models.SetDcdnFullDomainsBlockIPResponse:
        runtime = RuntimeOptions()
        return self.set_dcdn_full_domains_block_ipwith_options(request, runtime)

    async def set_dcdn_full_domains_block_ip_async(
        self,
        request: main_models.SetDcdnFullDomainsBlockIPRequest,
    ) -> main_models.SetDcdnFullDomainsBlockIPResponse:
        runtime = RuntimeOptions()
        return await self.set_dcdn_full_domains_block_ipwith_options_async(request, runtime)

    def set_dcdn_user_config_with_options(
        self,
        request: main_models.SetDcdnUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.configs):
            query['Configs'] = request.configs
        if not DaraCore.is_null(request.function_id):
            query['FunctionId'] = request.function_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnUserConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_user_config_with_options_async(
        self,
        request: main_models.SetDcdnUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDcdnUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.configs):
            query['Configs'] = request.configs
        if not DaraCore.is_null(request.function_id):
            query['FunctionId'] = request.function_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDcdnUserConfig',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDcdnUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_user_config(
        self,
        request: main_models.SetDcdnUserConfigRequest,
    ) -> main_models.SetDcdnUserConfigResponse:
        runtime = RuntimeOptions()
        return self.set_dcdn_user_config_with_options(request, runtime)

    async def set_dcdn_user_config_async(
        self,
        request: main_models.SetDcdnUserConfigRequest,
    ) -> main_models.SetDcdnUserConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_dcdn_user_config_with_options_async(request, runtime)

    def set_routine_subdomain_with_options(
        self,
        tmp_req: main_models.SetRoutineSubdomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRoutineSubdomainResponse:
        tmp_req.validate()
        request = main_models.SetRoutineSubdomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.subdomains):
            request.subdomains_shrink = Utils.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        body = {}
        if not DaraCore.is_null(request.subdomains_shrink):
            body['Subdomains'] = request.subdomains_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetRoutineSubdomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRoutineSubdomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_routine_subdomain_with_options_async(
        self,
        tmp_req: main_models.SetRoutineSubdomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRoutineSubdomainResponse:
        tmp_req.validate()
        request = main_models.SetRoutineSubdomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.subdomains):
            request.subdomains_shrink = Utils.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        body = {}
        if not DaraCore.is_null(request.subdomains_shrink):
            body['Subdomains'] = request.subdomains_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetRoutineSubdomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRoutineSubdomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_routine_subdomain(
        self,
        request: main_models.SetRoutineSubdomainRequest,
    ) -> main_models.SetRoutineSubdomainResponse:
        runtime = RuntimeOptions()
        return self.set_routine_subdomain_with_options(request, runtime)

    async def set_routine_subdomain_async(
        self,
        request: main_models.SetRoutineSubdomainRequest,
    ) -> main_models.SetRoutineSubdomainResponse:
        runtime = RuntimeOptions()
        return await self.set_routine_subdomain_with_options_async(request, runtime)

    def start_dcdn_domain_with_options(
        self,
        request: main_models.StartDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dcdn_domain_with_options_async(
        self,
        request: main_models.StartDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dcdn_domain(
        self,
        request: main_models.StartDcdnDomainRequest,
    ) -> main_models.StartDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.start_dcdn_domain_with_options(request, runtime)

    async def start_dcdn_domain_async(
        self,
        request: main_models.StartDcdnDomainRequest,
    ) -> main_models.StartDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.start_dcdn_domain_with_options_async(request, runtime)

    def start_dcdn_ipa_domain_with_options(
        self,
        request: main_models.StartDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dcdn_ipa_domain_with_options_async(
        self,
        request: main_models.StartDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dcdn_ipa_domain(
        self,
        request: main_models.StartDcdnIpaDomainRequest,
    ) -> main_models.StartDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return self.start_dcdn_ipa_domain_with_options(request, runtime)

    async def start_dcdn_ipa_domain_async(
        self,
        request: main_models.StartDcdnIpaDomainRequest,
    ) -> main_models.StartDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return await self.start_dcdn_ipa_domain_with_options_async(request, runtime)

    def stop_dcdn_domain_with_options(
        self,
        request: main_models.StopDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dcdn_domain_with_options_async(
        self,
        request: main_models.StopDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dcdn_domain(
        self,
        request: main_models.StopDcdnDomainRequest,
    ) -> main_models.StopDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.stop_dcdn_domain_with_options(request, runtime)

    async def stop_dcdn_domain_async(
        self,
        request: main_models.StopDcdnDomainRequest,
    ) -> main_models.StopDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.stop_dcdn_domain_with_options_async(request, runtime)

    def stop_dcdn_ipa_domain_with_options(
        self,
        request: main_models.StopDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dcdn_ipa_domain_with_options_async(
        self,
        request: main_models.StopDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dcdn_ipa_domain(
        self,
        request: main_models.StopDcdnIpaDomainRequest,
    ) -> main_models.StopDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return self.stop_dcdn_ipa_domain_with_options(request, runtime)

    async def stop_dcdn_ipa_domain_async(
        self,
        request: main_models.StopDcdnIpaDomainRequest,
    ) -> main_models.StopDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return await self.stop_dcdn_ipa_domain_with_options_async(request, runtime)

    def tag_dcdn_resources_with_options(
        self,
        request: main_models.TagDcdnResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagDcdnResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagDcdnResources',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagDcdnResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_dcdn_resources_with_options_async(
        self,
        request: main_models.TagDcdnResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagDcdnResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagDcdnResources',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagDcdnResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_dcdn_resources(
        self,
        request: main_models.TagDcdnResourcesRequest,
    ) -> main_models.TagDcdnResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_dcdn_resources_with_options(request, runtime)

    async def tag_dcdn_resources_async(
        self,
        request: main_models.TagDcdnResourcesRequest,
    ) -> main_models.TagDcdnResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_dcdn_resources_with_options_async(request, runtime)

    def untag_dcdn_resources_with_options(
        self,
        request: main_models.UntagDcdnResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagDcdnResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagDcdnResources',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagDcdnResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_dcdn_resources_with_options_async(
        self,
        request: main_models.UntagDcdnResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagDcdnResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagDcdnResources',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagDcdnResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_dcdn_resources(
        self,
        request: main_models.UntagDcdnResourcesRequest,
    ) -> main_models.UntagDcdnResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_dcdn_resources_with_options(request, runtime)

    async def untag_dcdn_resources_async(
        self,
        request: main_models.UntagDcdnResourcesRequest,
    ) -> main_models.UntagDcdnResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_dcdn_resources_with_options_async(request, runtime)

    def update_dcdn_deliver_task_with_options(
        self,
        request: main_models.UpdateDcdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnDeliverTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deliver):
            body['Deliver'] = request.deliver
        if not DaraCore.is_null(request.deliver_id):
            body['DeliverId'] = request.deliver_id
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.reports):
            body['Reports'] = request.reports
        if not DaraCore.is_null(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnDeliverTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_deliver_task_with_options_async(
        self,
        request: main_models.UpdateDcdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnDeliverTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deliver):
            body['Deliver'] = request.deliver
        if not DaraCore.is_null(request.deliver_id):
            body['DeliverId'] = request.deliver_id
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.reports):
            body['Reports'] = request.reports
        if not DaraCore.is_null(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnDeliverTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_deliver_task(
        self,
        request: main_models.UpdateDcdnDeliverTaskRequest,
    ) -> main_models.UpdateDcdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return self.update_dcdn_deliver_task_with_options(request, runtime)

    async def update_dcdn_deliver_task_async(
        self,
        request: main_models.UpdateDcdnDeliverTaskRequest,
    ) -> main_models.UpdateDcdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_dcdn_deliver_task_with_options_async(request, runtime)

    def update_dcdn_domain_with_options(
        self,
        request: main_models.UpdateDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_domain_with_options_async(
        self,
        request: main_models.UpdateDcdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_domain(
        self,
        request: main_models.UpdateDcdnDomainRequest,
    ) -> main_models.UpdateDcdnDomainResponse:
        runtime = RuntimeOptions()
        return self.update_dcdn_domain_with_options(request, runtime)

    async def update_dcdn_domain_async(
        self,
        request: main_models.UpdateDcdnDomainRequest,
    ) -> main_models.UpdateDcdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.update_dcdn_domain_with_options_async(request, runtime)

    def update_dcdn_ipa_domain_with_options(
        self,
        request: main_models.UpdateDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_ipa_domain_with_options_async(
        self,
        request: main_models.UpdateDcdnIpaDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnIpaDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnIpaDomain',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_ipa_domain(
        self,
        request: main_models.UpdateDcdnIpaDomainRequest,
    ) -> main_models.UpdateDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return self.update_dcdn_ipa_domain_with_options(request, runtime)

    async def update_dcdn_ipa_domain_async(
        self,
        request: main_models.UpdateDcdnIpaDomainRequest,
    ) -> main_models.UpdateDcdnIpaDomainResponse:
        runtime = RuntimeOptions()
        return await self.update_dcdn_ipa_domain_with_options_async(request, runtime)

    def update_dcdn_slsrealtime_log_delivery_with_options(
        self,
        request: main_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_center):
            body['DataCenter'] = request.data_center
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not DaraCore.is_null(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not DaraCore.is_null(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not DaraCore.is_null(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnSLSRealtimeLogDelivery',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnSLSRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_slsrealtime_log_delivery_with_options_async(
        self,
        request: main_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_center):
            body['DataCenter'] = request.data_center
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not DaraCore.is_null(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not DaraCore.is_null(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not DaraCore.is_null(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnSLSRealtimeLogDelivery',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnSLSRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_slsrealtime_log_delivery(
        self,
        request: main_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
    ) -> main_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.update_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    async def update_dcdn_slsrealtime_log_delivery_async(
        self,
        request: main_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
    ) -> main_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.update_dcdn_slsrealtime_log_delivery_with_options_async(request, runtime)

    def update_dcdn_sub_task_with_options(
        self,
        request: main_models.UpdateDcdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnSubTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.report_ids):
            body['ReportIds'] = request.report_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnSubTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_sub_task_with_options_async(
        self,
        request: main_models.UpdateDcdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnSubTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.report_ids):
            body['ReportIds'] = request.report_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnSubTask',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_sub_task(
        self,
        request: main_models.UpdateDcdnSubTaskRequest,
    ) -> main_models.UpdateDcdnSubTaskResponse:
        runtime = RuntimeOptions()
        return self.update_dcdn_sub_task_with_options(request, runtime)

    async def update_dcdn_sub_task_async(
        self,
        request: main_models.UpdateDcdnSubTaskRequest,
    ) -> main_models.UpdateDcdnSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_dcdn_sub_task_with_options_async(request, runtime)

    def update_dcdn_user_real_time_delivery_field_with_options(
        self,
        request: main_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnUserRealTimeDeliveryField',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnUserRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_user_real_time_delivery_field_with_options_async(
        self,
        request: main_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDcdnUserRealTimeDeliveryField',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDcdnUserRealTimeDeliveryFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_user_real_time_delivery_field(
        self,
        request: main_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
    ) -> main_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        runtime = RuntimeOptions()
        return self.update_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    async def update_dcdn_user_real_time_delivery_field_async(
        self,
        request: main_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
    ) -> main_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        runtime = RuntimeOptions()
        return await self.update_dcdn_user_real_time_delivery_field_with_options_async(request, runtime)

    def upload_routine_code_with_options(
        self,
        request: main_models.UploadRoutineCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadRoutineCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_description):
            body['CodeDescription'] = request.code_description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadRoutineCode',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_routine_code_with_options_async(
        self,
        request: main_models.UploadRoutineCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadRoutineCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_description):
            body['CodeDescription'] = request.code_description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadRoutineCode',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRoutineCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_routine_code(
        self,
        request: main_models.UploadRoutineCodeRequest,
    ) -> main_models.UploadRoutineCodeResponse:
        runtime = RuntimeOptions()
        return self.upload_routine_code_with_options(request, runtime)

    async def upload_routine_code_async(
        self,
        request: main_models.UploadRoutineCodeRequest,
    ) -> main_models.UploadRoutineCodeResponse:
        runtime = RuntimeOptions()
        return await self.upload_routine_code_with_options_async(request, runtime)

    def upload_staging_routine_code_with_options(
        self,
        request: main_models.UploadStagingRoutineCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadStagingRoutineCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_description):
            body['CodeDescription'] = request.code_description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadStagingRoutineCode',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadStagingRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_staging_routine_code_with_options_async(
        self,
        request: main_models.UploadStagingRoutineCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadStagingRoutineCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code_description):
            body['CodeDescription'] = request.code_description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadStagingRoutineCode',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadStagingRoutineCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_staging_routine_code(
        self,
        request: main_models.UploadStagingRoutineCodeRequest,
    ) -> main_models.UploadStagingRoutineCodeResponse:
        runtime = RuntimeOptions()
        return self.upload_staging_routine_code_with_options(request, runtime)

    async def upload_staging_routine_code_async(
        self,
        request: main_models.UploadStagingRoutineCodeRequest,
    ) -> main_models.UploadStagingRoutineCodeResponse:
        runtime = RuntimeOptions()
        return await self.upload_staging_routine_code_with_options_async(request, runtime)

    def verify_dcdn_domain_owner_with_options(
        self,
        request: main_models.VerifyDcdnDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyDcdnDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyDcdnDomainOwner',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyDcdnDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_dcdn_domain_owner_with_options_async(
        self,
        request: main_models.VerifyDcdnDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyDcdnDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyDcdnDomainOwner',
            version = '2018-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyDcdnDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_dcdn_domain_owner(
        self,
        request: main_models.VerifyDcdnDomainOwnerRequest,
    ) -> main_models.VerifyDcdnDomainOwnerResponse:
        runtime = RuntimeOptions()
        return self.verify_dcdn_domain_owner_with_options(request, runtime)

    async def verify_dcdn_domain_owner_async(
        self,
        request: main_models.VerifyDcdnDomainOwnerRequest,
    ) -> main_models.VerifyDcdnDomainOwnerResponse:
        runtime = RuntimeOptions()
        return await self.verify_dcdn_domain_owner_with_options_async(request, runtime)
