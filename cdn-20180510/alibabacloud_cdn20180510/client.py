# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cdn20180510 import models as main_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-northeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'cdn.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cdn_domain_with_options(
        self,
        request: main_models.AddCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cdn_domain_with_options_async(
        self,
        request: main_models.AddCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cdn_domain(
        self,
        request: main_models.AddCdnDomainRequest,
    ) -> main_models.AddCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.add_cdn_domain_with_options(request, runtime)

    async def add_cdn_domain_async(
        self,
        request: main_models.AddCdnDomainRequest,
    ) -> main_models.AddCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.add_cdn_domain_with_options_async(request, runtime)

    def add_fctrigger_with_options(
        self,
        request: main_models.AddFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFCTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not DaraCore.is_null(request.event_meta_name):
            body['EventMetaName'] = request.event_meta_name
        if not DaraCore.is_null(request.event_meta_version):
            body['EventMetaVersion'] = request.event_meta_version
        if not DaraCore.is_null(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not DaraCore.is_null(request.notes):
            body['Notes'] = request.notes
        if not DaraCore.is_null(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_fctrigger_with_options_async(
        self,
        request: main_models.AddFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFCTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not DaraCore.is_null(request.event_meta_name):
            body['EventMetaName'] = request.event_meta_name
        if not DaraCore.is_null(request.event_meta_version):
            body['EventMetaVersion'] = request.event_meta_version
        if not DaraCore.is_null(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not DaraCore.is_null(request.notes):
            body['Notes'] = request.notes
        if not DaraCore.is_null(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_fctrigger(
        self,
        request: main_models.AddFCTriggerRequest,
    ) -> main_models.AddFCTriggerResponse:
        runtime = RuntimeOptions()
        return self.add_fctrigger_with_options(request, runtime)

    async def add_fctrigger_async(
        self,
        request: main_models.AddFCTriggerRequest,
    ) -> main_models.AddFCTriggerResponse:
        runtime = RuntimeOptions()
        return await self.add_fctrigger_with_options_async(request, runtime)

    def batch_add_cdn_domain_with_options(
        self,
        request: main_models.BatchAddCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddCdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action = 'BatchAddCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_cdn_domain_with_options_async(
        self,
        request: main_models.BatchAddCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddCdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action = 'BatchAddCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_cdn_domain(
        self,
        request: main_models.BatchAddCdnDomainRequest,
    ) -> main_models.BatchAddCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_add_cdn_domain_with_options(request, runtime)

    async def batch_add_cdn_domain_async(
        self,
        request: main_models.BatchAddCdnDomainRequest,
    ) -> main_models.BatchAddCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_add_cdn_domain_with_options_async(request, runtime)

    def batch_delete_cdn_domain_config_with_options(
        self,
        request: main_models.BatchDeleteCdnDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteCdnDomainConfigResponse:
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
            action = 'BatchDeleteCdnDomainConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteCdnDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_cdn_domain_config_with_options_async(
        self,
        request: main_models.BatchDeleteCdnDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteCdnDomainConfigResponse:
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
            action = 'BatchDeleteCdnDomainConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteCdnDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_cdn_domain_config(
        self,
        request: main_models.BatchDeleteCdnDomainConfigRequest,
    ) -> main_models.BatchDeleteCdnDomainConfigResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_cdn_domain_config_with_options(request, runtime)

    async def batch_delete_cdn_domain_config_async(
        self,
        request: main_models.BatchDeleteCdnDomainConfigRequest,
    ) -> main_models.BatchDeleteCdnDomainConfigResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_cdn_domain_config_with_options_async(request, runtime)

    def batch_describe_cdn_ip_info_with_options(
        self,
        request: main_models.BatchDescribeCdnIpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDescribeCdnIpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDescribeCdnIpInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDescribeCdnIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_describe_cdn_ip_info_with_options_async(
        self,
        request: main_models.BatchDescribeCdnIpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDescribeCdnIpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDescribeCdnIpInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDescribeCdnIpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_describe_cdn_ip_info(
        self,
        request: main_models.BatchDescribeCdnIpInfoRequest,
    ) -> main_models.BatchDescribeCdnIpInfoResponse:
        runtime = RuntimeOptions()
        return self.batch_describe_cdn_ip_info_with_options(request, runtime)

    async def batch_describe_cdn_ip_info_async(
        self,
        request: main_models.BatchDescribeCdnIpInfoRequest,
    ) -> main_models.BatchDescribeCdnIpInfoResponse:
        runtime = RuntimeOptions()
        return await self.batch_describe_cdn_ip_info_with_options_async(request, runtime)

    def batch_set_cdn_domain_config_with_options(
        self,
        request: main_models.BatchSetCdnDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetCdnDomainConfigResponse:
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
            action = 'BatchSetCdnDomainConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetCdnDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_cdn_domain_config_with_options_async(
        self,
        request: main_models.BatchSetCdnDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetCdnDomainConfigResponse:
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
            action = 'BatchSetCdnDomainConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetCdnDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_cdn_domain_config(
        self,
        request: main_models.BatchSetCdnDomainConfigRequest,
    ) -> main_models.BatchSetCdnDomainConfigResponse:
        runtime = RuntimeOptions()
        return self.batch_set_cdn_domain_config_with_options(request, runtime)

    async def batch_set_cdn_domain_config_async(
        self,
        request: main_models.BatchSetCdnDomainConfigRequest,
    ) -> main_models.BatchSetCdnDomainConfigResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_cdn_domain_config_with_options_async(request, runtime)

    def batch_set_gray_domain_function_with_options(
        self,
        request: main_models.BatchSetGrayDomainFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetGrayDomainFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetGrayDomainFunction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetGrayDomainFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_gray_domain_function_with_options_async(
        self,
        request: main_models.BatchSetGrayDomainFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetGrayDomainFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetGrayDomainFunction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetGrayDomainFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_gray_domain_function(
        self,
        request: main_models.BatchSetGrayDomainFunctionRequest,
    ) -> main_models.BatchSetGrayDomainFunctionResponse:
        runtime = RuntimeOptions()
        return self.batch_set_gray_domain_function_with_options(request, runtime)

    async def batch_set_gray_domain_function_async(
        self,
        request: main_models.BatchSetGrayDomainFunctionRequest,
    ) -> main_models.BatchSetGrayDomainFunctionResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_gray_domain_function_with_options_async(request, runtime)

    def batch_start_cdn_domain_with_options(
        self,
        request: main_models.BatchStartCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartCdnDomainResponse:
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
            action = 'BatchStartCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_cdn_domain_with_options_async(
        self,
        request: main_models.BatchStartCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartCdnDomainResponse:
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
            action = 'BatchStartCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_cdn_domain(
        self,
        request: main_models.BatchStartCdnDomainRequest,
    ) -> main_models.BatchStartCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_start_cdn_domain_with_options(request, runtime)

    async def batch_start_cdn_domain_async(
        self,
        request: main_models.BatchStartCdnDomainRequest,
    ) -> main_models.BatchStartCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_start_cdn_domain_with_options_async(request, runtime)

    def batch_stop_cdn_domain_with_options(
        self,
        request: main_models.BatchStopCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopCdnDomainResponse:
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
            action = 'BatchStopCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_cdn_domain_with_options_async(
        self,
        request: main_models.BatchStopCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopCdnDomainResponse:
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
            action = 'BatchStopCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_cdn_domain(
        self,
        request: main_models.BatchStopCdnDomainRequest,
    ) -> main_models.BatchStopCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_stop_cdn_domain_with_options(request, runtime)

    async def batch_stop_cdn_domain_async(
        self,
        request: main_models.BatchStopCdnDomainRequest,
    ) -> main_models.BatchStopCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_stop_cdn_domain_with_options_async(request, runtime)

    def batch_update_cdn_domain_with_options(
        self,
        request: main_models.BatchUpdateCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateCdnDomainResponse:
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
            action = 'BatchUpdateCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_cdn_domain_with_options_async(
        self,
        request: main_models.BatchUpdateCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateCdnDomainResponse:
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
            action = 'BatchUpdateCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_cdn_domain(
        self,
        request: main_models.BatchUpdateCdnDomainRequest,
    ) -> main_models.BatchUpdateCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_update_cdn_domain_with_options(request, runtime)

    async def batch_update_cdn_domain_async(
        self,
        request: main_models.BatchUpdateCdnDomainRequest,
    ) -> main_models.BatchUpdateCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_update_cdn_domain_with_options_async(request, runtime)

    def check_cdn_domain_exist_with_options(
        self,
        request: main_models.CheckCdnDomainExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCdnDomainExistResponse:
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
            action = 'CheckCdnDomainExist',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCdnDomainExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cdn_domain_exist_with_options_async(
        self,
        request: main_models.CheckCdnDomainExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCdnDomainExistResponse:
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
            action = 'CheckCdnDomainExist',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCdnDomainExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cdn_domain_exist(
        self,
        request: main_models.CheckCdnDomainExistRequest,
    ) -> main_models.CheckCdnDomainExistResponse:
        runtime = RuntimeOptions()
        return self.check_cdn_domain_exist_with_options(request, runtime)

    async def check_cdn_domain_exist_async(
        self,
        request: main_models.CheckCdnDomainExistRequest,
    ) -> main_models.CheckCdnDomainExistResponse:
        runtime = RuntimeOptions()
        return await self.check_cdn_domain_exist_with_options_async(request, runtime)

    def check_cdn_domain_icpwith_options(
        self,
        request: main_models.CheckCdnDomainICPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCdnDomainICPResponse:
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
            action = 'CheckCdnDomainICP',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCdnDomainICPResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cdn_domain_icpwith_options_async(
        self,
        request: main_models.CheckCdnDomainICPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCdnDomainICPResponse:
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
            action = 'CheckCdnDomainICP',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCdnDomainICPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cdn_domain_icp(
        self,
        request: main_models.CheckCdnDomainICPRequest,
    ) -> main_models.CheckCdnDomainICPResponse:
        runtime = RuntimeOptions()
        return self.check_cdn_domain_icpwith_options(request, runtime)

    async def check_cdn_domain_icp_async(
        self,
        request: main_models.CheckCdnDomainICPRequest,
    ) -> main_models.CheckCdnDomainICPResponse:
        runtime = RuntimeOptions()
        return await self.check_cdn_domain_icpwith_options_async(request, runtime)

    def create_cdn_certificate_signing_request_with_options(
        self,
        request: main_models.CreateCdnCertificateSigningRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCdnCertificateSigningRequestResponse:
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
            action = 'CreateCdnCertificateSigningRequest',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCdnCertificateSigningRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_certificate_signing_request_with_options_async(
        self,
        request: main_models.CreateCdnCertificateSigningRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCdnCertificateSigningRequestResponse:
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
            action = 'CreateCdnCertificateSigningRequest',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCdnCertificateSigningRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_certificate_signing_request(
        self,
        request: main_models.CreateCdnCertificateSigningRequestRequest,
    ) -> main_models.CreateCdnCertificateSigningRequestResponse:
        runtime = RuntimeOptions()
        return self.create_cdn_certificate_signing_request_with_options(request, runtime)

    async def create_cdn_certificate_signing_request_async(
        self,
        request: main_models.CreateCdnCertificateSigningRequestRequest,
    ) -> main_models.CreateCdnCertificateSigningRequestResponse:
        runtime = RuntimeOptions()
        return await self.create_cdn_certificate_signing_request_with_options_async(request, runtime)

    def create_cdn_deliver_task_with_options(
        self,
        request: main_models.CreateCdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCdnDeliverTaskResponse:
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
            action = 'CreateCdnDeliverTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_deliver_task_with_options_async(
        self,
        request: main_models.CreateCdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCdnDeliverTaskResponse:
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
            action = 'CreateCdnDeliverTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_deliver_task(
        self,
        request: main_models.CreateCdnDeliverTaskRequest,
    ) -> main_models.CreateCdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return self.create_cdn_deliver_task_with_options(request, runtime)

    async def create_cdn_deliver_task_async(
        self,
        request: main_models.CreateCdnDeliverTaskRequest,
    ) -> main_models.CreateCdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_cdn_deliver_task_with_options_async(request, runtime)

    def create_cdn_sub_task_with_options(
        self,
        request: main_models.CreateCdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCdnSubTaskResponse:
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
            action = 'CreateCdnSubTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_sub_task_with_options_async(
        self,
        request: main_models.CreateCdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCdnSubTaskResponse:
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
            action = 'CreateCdnSubTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_sub_task(
        self,
        request: main_models.CreateCdnSubTaskRequest,
    ) -> main_models.CreateCdnSubTaskResponse:
        runtime = RuntimeOptions()
        return self.create_cdn_sub_task_with_options(request, runtime)

    async def create_cdn_sub_task_async(
        self,
        request: main_models.CreateCdnSubTaskRequest,
    ) -> main_models.CreateCdnSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_cdn_sub_task_with_options_async(request, runtime)

    def create_real_time_log_delivery_with_options(
        self,
        request: main_models.CreateRealTimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRealTimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRealTimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_real_time_log_delivery_with_options_async(
        self,
        request: main_models.CreateRealTimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRealTimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRealTimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRealTimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_real_time_log_delivery(
        self,
        request: main_models.CreateRealTimeLogDeliveryRequest,
    ) -> main_models.CreateRealTimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.create_real_time_log_delivery_with_options(request, runtime)

    async def create_real_time_log_delivery_async(
        self,
        request: main_models.CreateRealTimeLogDeliveryRequest,
    ) -> main_models.CreateRealTimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.create_real_time_log_delivery_with_options_async(request, runtime)

    def create_usage_detail_data_export_task_with_options(
        self,
        request: main_models.CreateUsageDetailDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsageDetailDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsageDetailDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_usage_detail_data_export_task_with_options_async(
        self,
        request: main_models.CreateUsageDetailDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsageDetailDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsageDetailDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsageDetailDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_usage_detail_data_export_task(
        self,
        request: main_models.CreateUsageDetailDataExportTaskRequest,
    ) -> main_models.CreateUsageDetailDataExportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_usage_detail_data_export_task_with_options(request, runtime)

    async def create_usage_detail_data_export_task_async(
        self,
        request: main_models.CreateUsageDetailDataExportTaskRequest,
    ) -> main_models.CreateUsageDetailDataExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_usage_detail_data_export_task_with_options_async(request, runtime)

    def create_user_usage_data_export_task_with_options(
        self,
        request: main_models.CreateUserUsageDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserUsageDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserUsageDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_usage_data_export_task_with_options_async(
        self,
        request: main_models.CreateUserUsageDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserUsageDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserUsageDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserUsageDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_usage_data_export_task(
        self,
        request: main_models.CreateUserUsageDataExportTaskRequest,
    ) -> main_models.CreateUserUsageDataExportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_user_usage_data_export_task_with_options(request, runtime)

    async def create_user_usage_data_export_task_async(
        self,
        request: main_models.CreateUserUsageDataExportTaskRequest,
    ) -> main_models.CreateUserUsageDataExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_user_usage_data_export_task_with_options_async(request, runtime)

    def delete_cdn_deliver_task_with_options(
        self,
        request: main_models.DeleteCdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCdnDeliverTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCdnDeliverTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_deliver_task_with_options_async(
        self,
        request: main_models.DeleteCdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCdnDeliverTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCdnDeliverTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_deliver_task(
        self,
        request: main_models.DeleteCdnDeliverTaskRequest,
    ) -> main_models.DeleteCdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_cdn_deliver_task_with_options(request, runtime)

    async def delete_cdn_deliver_task_async(
        self,
        request: main_models.DeleteCdnDeliverTaskRequest,
    ) -> main_models.DeleteCdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_cdn_deliver_task_with_options_async(request, runtime)

    def delete_cdn_domain_with_options(
        self,
        request: main_models.DeleteCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_domain_with_options_async(
        self,
        request: main_models.DeleteCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCdnDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_domain(
        self,
        request: main_models.DeleteCdnDomainRequest,
    ) -> main_models.DeleteCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_cdn_domain_with_options(request, runtime)

    async def delete_cdn_domain_async(
        self,
        request: main_models.DeleteCdnDomainRequest,
    ) -> main_models.DeleteCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_cdn_domain_with_options_async(request, runtime)

    def delete_cdn_sub_task_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCdnSubTaskResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DeleteCdnSubTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_sub_task_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCdnSubTaskResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DeleteCdnSubTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_sub_task(self) -> main_models.DeleteCdnSubTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_cdn_sub_task_with_options(runtime)

    async def delete_cdn_sub_task_async(self) -> main_models.DeleteCdnSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_cdn_sub_task_with_options_async(runtime)

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
            version = '2018-05-10',
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
            version = '2018-05-10',
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

    def delete_fctrigger_with_options(
        self,
        request: main_models.DeleteFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFCTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fctrigger_with_options_async(
        self,
        request: main_models.DeleteFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFCTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_fctrigger(
        self,
        request: main_models.DeleteFCTriggerRequest,
    ) -> main_models.DeleteFCTriggerResponse:
        runtime = RuntimeOptions()
        return self.delete_fctrigger_with_options(request, runtime)

    async def delete_fctrigger_async(
        self,
        request: main_models.DeleteFCTriggerRequest,
    ) -> main_models.DeleteFCTriggerResponse:
        runtime = RuntimeOptions()
        return await self.delete_fctrigger_with_options_async(request, runtime)

    def delete_real_time_log_logstore_with_options(
        self,
        request: main_models.DeleteRealTimeLogLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRealTimeLogLogstoreResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRealTimeLogLogstore',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRealTimeLogLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_real_time_log_logstore_with_options_async(
        self,
        request: main_models.DeleteRealTimeLogLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRealTimeLogLogstoreResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRealTimeLogLogstore',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRealTimeLogLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_real_time_log_logstore(
        self,
        request: main_models.DeleteRealTimeLogLogstoreRequest,
    ) -> main_models.DeleteRealTimeLogLogstoreResponse:
        runtime = RuntimeOptions()
        return self.delete_real_time_log_logstore_with_options(request, runtime)

    async def delete_real_time_log_logstore_async(
        self,
        request: main_models.DeleteRealTimeLogLogstoreRequest,
    ) -> main_models.DeleteRealTimeLogLogstoreResponse:
        runtime = RuntimeOptions()
        return await self.delete_real_time_log_logstore_with_options_async(request, runtime)

    def delete_realtime_log_delivery_with_options(
        self,
        request: main_models.DeleteRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_realtime_log_delivery_with_options_async(
        self,
        request: main_models.DeleteRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_realtime_log_delivery(
        self,
        request: main_models.DeleteRealtimeLogDeliveryRequest,
    ) -> main_models.DeleteRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.delete_realtime_log_delivery_with_options(request, runtime)

    async def delete_realtime_log_delivery_async(
        self,
        request: main_models.DeleteRealtimeLogDeliveryRequest,
    ) -> main_models.DeleteRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.delete_realtime_log_delivery_with_options_async(request, runtime)

    def delete_specific_config_with_options(
        self,
        request: main_models.DeleteSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSpecificConfigResponse:
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
            action = 'DeleteSpecificConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_specific_config_with_options_async(
        self,
        request: main_models.DeleteSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSpecificConfigResponse:
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
            action = 'DeleteSpecificConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_specific_config(
        self,
        request: main_models.DeleteSpecificConfigRequest,
    ) -> main_models.DeleteSpecificConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_specific_config_with_options(request, runtime)

    async def delete_specific_config_async(
        self,
        request: main_models.DeleteSpecificConfigRequest,
    ) -> main_models.DeleteSpecificConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_specific_config_with_options_async(request, runtime)

    def delete_specific_staging_config_with_options(
        self,
        request: main_models.DeleteSpecificStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSpecificStagingConfigResponse:
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
            action = 'DeleteSpecificStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_specific_staging_config_with_options_async(
        self,
        request: main_models.DeleteSpecificStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSpecificStagingConfigResponse:
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
            action = 'DeleteSpecificStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSpecificStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_specific_staging_config(
        self,
        request: main_models.DeleteSpecificStagingConfigRequest,
    ) -> main_models.DeleteSpecificStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_specific_staging_config_with_options(request, runtime)

    async def delete_specific_staging_config_async(
        self,
        request: main_models.DeleteSpecificStagingConfigRequest,
    ) -> main_models.DeleteSpecificStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_specific_staging_config_with_options_async(request, runtime)

    def delete_usage_detail_data_export_task_with_options(
        self,
        request: main_models.DeleteUsageDetailDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsageDetailDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsageDetailDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_usage_detail_data_export_task_with_options_async(
        self,
        request: main_models.DeleteUsageDetailDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsageDetailDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsageDetailDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsageDetailDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_usage_detail_data_export_task(
        self,
        request: main_models.DeleteUsageDetailDataExportTaskRequest,
    ) -> main_models.DeleteUsageDetailDataExportTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_usage_detail_data_export_task_with_options(request, runtime)

    async def delete_usage_detail_data_export_task_async(
        self,
        request: main_models.DeleteUsageDetailDataExportTaskRequest,
    ) -> main_models.DeleteUsageDetailDataExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_usage_detail_data_export_task_with_options_async(request, runtime)

    def delete_user_usage_data_export_task_with_options(
        self,
        request: main_models.DeleteUserUsageDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserUsageDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserUsageDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_usage_data_export_task_with_options_async(
        self,
        request: main_models.DeleteUserUsageDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserUsageDataExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserUsageDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserUsageDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_usage_data_export_task(
        self,
        request: main_models.DeleteUserUsageDataExportTaskRequest,
    ) -> main_models.DeleteUserUsageDataExportTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_user_usage_data_export_task_with_options(request, runtime)

    async def delete_user_usage_data_export_task_async(
        self,
        request: main_models.DeleteUserUsageDataExportTaskRequest,
    ) -> main_models.DeleteUserUsageDataExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_usage_data_export_task_with_options_async(request, runtime)

    def describe_blocked_regions_with_options(
        self,
        request: main_models.DescribeBlockedRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlockedRegionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlockedRegions',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlockedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blocked_regions_with_options_async(
        self,
        request: main_models.DescribeBlockedRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlockedRegionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlockedRegions',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlockedRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blocked_regions(
        self,
        request: main_models.DescribeBlockedRegionsRequest,
    ) -> main_models.DescribeBlockedRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_blocked_regions_with_options(request, runtime)

    async def describe_blocked_regions_async(
        self,
        request: main_models.DescribeBlockedRegionsRequest,
    ) -> main_models.DescribeBlockedRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_blocked_regions_with_options_async(request, runtime)

    def describe_cdn_certificate_detail_with_options(
        self,
        request: main_models.DescribeCdnCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnCertificateDetailResponse:
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
            action = 'DescribeCdnCertificateDetail',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_certificate_detail_with_options_async(
        self,
        request: main_models.DescribeCdnCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnCertificateDetailResponse:
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
            action = 'DescribeCdnCertificateDetail',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_certificate_detail(
        self,
        request: main_models.DescribeCdnCertificateDetailRequest,
    ) -> main_models.DescribeCdnCertificateDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_certificate_detail_with_options(request, runtime)

    async def describe_cdn_certificate_detail_async(
        self,
        request: main_models.DescribeCdnCertificateDetailRequest,
    ) -> main_models.DescribeCdnCertificateDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_certificate_detail_with_options_async(request, runtime)

    def describe_cdn_certificate_detail_by_id_with_options(
        self,
        request: main_models.DescribeCdnCertificateDetailByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnCertificateDetailByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnCertificateDetailById',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnCertificateDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_certificate_detail_by_id_with_options_async(
        self,
        request: main_models.DescribeCdnCertificateDetailByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnCertificateDetailByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnCertificateDetailById',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnCertificateDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_certificate_detail_by_id(
        self,
        request: main_models.DescribeCdnCertificateDetailByIdRequest,
    ) -> main_models.DescribeCdnCertificateDetailByIdResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_certificate_detail_by_id_with_options(request, runtime)

    async def describe_cdn_certificate_detail_by_id_async(
        self,
        request: main_models.DescribeCdnCertificateDetailByIdRequest,
    ) -> main_models.DescribeCdnCertificateDetailByIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_certificate_detail_by_id_with_options_async(request, runtime)

    def describe_cdn_certificate_list_with_options(
        self,
        request: main_models.DescribeCdnCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnCertificateListResponse:
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
            action = 'DescribeCdnCertificateList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_certificate_list_with_options_async(
        self,
        request: main_models.DescribeCdnCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnCertificateListResponse:
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
            action = 'DescribeCdnCertificateList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_certificate_list(
        self,
        request: main_models.DescribeCdnCertificateListRequest,
    ) -> main_models.DescribeCdnCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_certificate_list_with_options(request, runtime)

    async def describe_cdn_certificate_list_async(
        self,
        request: main_models.DescribeCdnCertificateListRequest,
    ) -> main_models.DescribeCdnCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_certificate_list_with_options_async(request, runtime)

    def describe_cdn_condition_ipbinfo_with_options(
        self,
        request: main_models.DescribeCdnConditionIPBInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnConditionIPBInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnConditionIPBInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnConditionIPBInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_condition_ipbinfo_with_options_async(
        self,
        request: main_models.DescribeCdnConditionIPBInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnConditionIPBInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnConditionIPBInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnConditionIPBInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_condition_ipbinfo(
        self,
        request: main_models.DescribeCdnConditionIPBInfoRequest,
    ) -> main_models.DescribeCdnConditionIPBInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_condition_ipbinfo_with_options(request, runtime)

    async def describe_cdn_condition_ipbinfo_async(
        self,
        request: main_models.DescribeCdnConditionIPBInfoRequest,
    ) -> main_models.DescribeCdnConditionIPBInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_condition_ipbinfo_with_options_async(request, runtime)

    def describe_cdn_deleted_domains_with_options(
        self,
        request: main_models.DescribeCdnDeletedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDeletedDomainsResponse:
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
            action = 'DescribeCdnDeletedDomains',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDeletedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_deleted_domains_with_options_async(
        self,
        request: main_models.DescribeCdnDeletedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDeletedDomainsResponse:
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
            action = 'DescribeCdnDeletedDomains',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDeletedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_deleted_domains(
        self,
        request: main_models.DescribeCdnDeletedDomainsRequest,
    ) -> main_models.DescribeCdnDeletedDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_deleted_domains_with_options(request, runtime)

    async def describe_cdn_deleted_domains_async(
        self,
        request: main_models.DescribeCdnDeletedDomainsRequest,
    ) -> main_models.DescribeCdnDeletedDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_deleted_domains_with_options_async(request, runtime)

    def describe_cdn_deliver_list_with_options(
        self,
        request: main_models.DescribeCdnDeliverListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDeliverListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnDeliverList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDeliverListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_deliver_list_with_options_async(
        self,
        request: main_models.DescribeCdnDeliverListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDeliverListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnDeliverList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDeliverListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_deliver_list(
        self,
        request: main_models.DescribeCdnDeliverListRequest,
    ) -> main_models.DescribeCdnDeliverListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_deliver_list_with_options(request, runtime)

    async def describe_cdn_deliver_list_async(
        self,
        request: main_models.DescribeCdnDeliverListRequest,
    ) -> main_models.DescribeCdnDeliverListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_deliver_list_with_options_async(request, runtime)

    def describe_cdn_domain_atoa_logs_with_options(
        self,
        request: main_models.DescribeCdnDomainAtoaLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainAtoaLogsResponse:
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
            action = 'DescribeCdnDomainAtoaLogs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainAtoaLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_atoa_logs_with_options_async(
        self,
        request: main_models.DescribeCdnDomainAtoaLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainAtoaLogsResponse:
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
            action = 'DescribeCdnDomainAtoaLogs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainAtoaLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_atoa_logs(
        self,
        request: main_models.DescribeCdnDomainAtoaLogsRequest,
    ) -> main_models.DescribeCdnDomainAtoaLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_domain_atoa_logs_with_options(request, runtime)

    async def describe_cdn_domain_atoa_logs_async(
        self,
        request: main_models.DescribeCdnDomainAtoaLogsRequest,
    ) -> main_models.DescribeCdnDomainAtoaLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_domain_atoa_logs_with_options_async(request, runtime)

    def describe_cdn_domain_by_certificate_with_options(
        self,
        request: main_models.DescribeCdnDomainByCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainByCertificateResponse:
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
            action = 'DescribeCdnDomainByCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainByCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_by_certificate_with_options_async(
        self,
        request: main_models.DescribeCdnDomainByCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainByCertificateResponse:
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
            action = 'DescribeCdnDomainByCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainByCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_by_certificate(
        self,
        request: main_models.DescribeCdnDomainByCertificateRequest,
    ) -> main_models.DescribeCdnDomainByCertificateResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_domain_by_certificate_with_options(request, runtime)

    async def describe_cdn_domain_by_certificate_async(
        self,
        request: main_models.DescribeCdnDomainByCertificateRequest,
    ) -> main_models.DescribeCdnDomainByCertificateResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_domain_by_certificate_with_options_async(request, runtime)

    def describe_cdn_domain_configs_with_options(
        self,
        request: main_models.DescribeCdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainConfigsResponse:
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
            action = 'DescribeCdnDomainConfigs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_configs_with_options_async(
        self,
        request: main_models.DescribeCdnDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainConfigsResponse:
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
            action = 'DescribeCdnDomainConfigs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_configs(
        self,
        request: main_models.DescribeCdnDomainConfigsRequest,
    ) -> main_models.DescribeCdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_domain_configs_with_options(request, runtime)

    async def describe_cdn_domain_configs_async(
        self,
        request: main_models.DescribeCdnDomainConfigsRequest,
    ) -> main_models.DescribeCdnDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_domain_configs_with_options_async(request, runtime)

    def describe_cdn_domain_detail_with_options(
        self,
        request: main_models.DescribeCdnDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainDetailResponse:
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
            action = 'DescribeCdnDomainDetail',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_detail_with_options_async(
        self,
        request: main_models.DescribeCdnDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainDetailResponse:
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
            action = 'DescribeCdnDomainDetail',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_detail(
        self,
        request: main_models.DescribeCdnDomainDetailRequest,
    ) -> main_models.DescribeCdnDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_domain_detail_with_options(request, runtime)

    async def describe_cdn_domain_detail_async(
        self,
        request: main_models.DescribeCdnDomainDetailRequest,
    ) -> main_models.DescribeCdnDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_domain_detail_with_options_async(request, runtime)

    def describe_cdn_domain_logs_with_options(
        self,
        request: main_models.DescribeCdnDomainLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainLogsResponse:
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
            action = 'DescribeCdnDomainLogs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_logs_with_options_async(
        self,
        request: main_models.DescribeCdnDomainLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainLogsResponse:
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
            action = 'DescribeCdnDomainLogs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_logs(
        self,
        request: main_models.DescribeCdnDomainLogsRequest,
    ) -> main_models.DescribeCdnDomainLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_domain_logs_with_options(request, runtime)

    async def describe_cdn_domain_logs_async(
        self,
        request: main_models.DescribeCdnDomainLogsRequest,
    ) -> main_models.DescribeCdnDomainLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_domain_logs_with_options_async(request, runtime)

    def describe_cdn_domain_logs_ex_ttl_with_options(
        self,
        request: main_models.DescribeCdnDomainLogsExTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainLogsExTtlResponse:
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
            action = 'DescribeCdnDomainLogsExTtl',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainLogsExTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_logs_ex_ttl_with_options_async(
        self,
        request: main_models.DescribeCdnDomainLogsExTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainLogsExTtlResponse:
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
            action = 'DescribeCdnDomainLogsExTtl',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainLogsExTtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_logs_ex_ttl(
        self,
        request: main_models.DescribeCdnDomainLogsExTtlRequest,
    ) -> main_models.DescribeCdnDomainLogsExTtlResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_domain_logs_ex_ttl_with_options(request, runtime)

    async def describe_cdn_domain_logs_ex_ttl_async(
        self,
        request: main_models.DescribeCdnDomainLogsExTtlRequest,
    ) -> main_models.DescribeCdnDomainLogsExTtlResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_domain_logs_ex_ttl_with_options_async(request, runtime)

    def describe_cdn_domain_staging_config_with_options(
        self,
        request: main_models.DescribeCdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainStagingConfigResponse:
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
            action = 'DescribeCdnDomainStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_staging_config_with_options_async(
        self,
        request: main_models.DescribeCdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnDomainStagingConfigResponse:
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
            action = 'DescribeCdnDomainStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_staging_config(
        self,
        request: main_models.DescribeCdnDomainStagingConfigRequest,
    ) -> main_models.DescribeCdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_domain_staging_config_with_options(request, runtime)

    async def describe_cdn_domain_staging_config_async(
        self,
        request: main_models.DescribeCdnDomainStagingConfigRequest,
    ) -> main_models.DescribeCdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_domain_staging_config_with_options_async(request, runtime)

    def describe_cdn_full_domains_block_ipconfig_with_options(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnFullDomainsBlockIPConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.iplist):
            body['IPList'] = request.iplist
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnFullDomainsBlockIPConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnFullDomainsBlockIPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_full_domains_block_ipconfig_with_options_async(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnFullDomainsBlockIPConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.iplist):
            body['IPList'] = request.iplist
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnFullDomainsBlockIPConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnFullDomainsBlockIPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_full_domains_block_ipconfig(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPConfigRequest,
    ) -> main_models.DescribeCdnFullDomainsBlockIPConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_full_domains_block_ipconfig_with_options(request, runtime)

    async def describe_cdn_full_domains_block_ipconfig_async(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPConfigRequest,
    ) -> main_models.DescribeCdnFullDomainsBlockIPConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_full_domains_block_ipconfig_with_options_async(request, runtime)

    def describe_cdn_full_domains_block_iphistory_with_options(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnFullDomainsBlockIPHistoryResponse:
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
            action = 'DescribeCdnFullDomainsBlockIPHistory',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnFullDomainsBlockIPHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_full_domains_block_iphistory_with_options_async(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnFullDomainsBlockIPHistoryResponse:
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
            action = 'DescribeCdnFullDomainsBlockIPHistory',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnFullDomainsBlockIPHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_full_domains_block_iphistory(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPHistoryRequest,
    ) -> main_models.DescribeCdnFullDomainsBlockIPHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_full_domains_block_iphistory_with_options(request, runtime)

    async def describe_cdn_full_domains_block_iphistory_async(
        self,
        request: main_models.DescribeCdnFullDomainsBlockIPHistoryRequest,
    ) -> main_models.DescribeCdnFullDomainsBlockIPHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_full_domains_block_iphistory_with_options_async(request, runtime)

    def describe_cdn_https_domain_list_with_options(
        self,
        request: main_models.DescribeCdnHttpsDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnHttpsDomainListResponse:
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
            action = 'DescribeCdnHttpsDomainList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnHttpsDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_https_domain_list_with_options_async(
        self,
        request: main_models.DescribeCdnHttpsDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnHttpsDomainListResponse:
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
            action = 'DescribeCdnHttpsDomainList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnHttpsDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_https_domain_list(
        self,
        request: main_models.DescribeCdnHttpsDomainListRequest,
    ) -> main_models.DescribeCdnHttpsDomainListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_https_domain_list_with_options(request, runtime)

    async def describe_cdn_https_domain_list_async(
        self,
        request: main_models.DescribeCdnHttpsDomainListRequest,
    ) -> main_models.DescribeCdnHttpsDomainListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_https_domain_list_with_options_async(request, runtime)

    def describe_cdn_order_commodity_code_with_options(
        self,
        request: main_models.DescribeCdnOrderCommodityCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnOrderCommodityCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnOrderCommodityCode',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnOrderCommodityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_order_commodity_code_with_options_async(
        self,
        request: main_models.DescribeCdnOrderCommodityCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnOrderCommodityCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnOrderCommodityCode',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnOrderCommodityCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_order_commodity_code(
        self,
        request: main_models.DescribeCdnOrderCommodityCodeRequest,
    ) -> main_models.DescribeCdnOrderCommodityCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_order_commodity_code_with_options(request, runtime)

    async def describe_cdn_order_commodity_code_async(
        self,
        request: main_models.DescribeCdnOrderCommodityCodeRequest,
    ) -> main_models.DescribeCdnOrderCommodityCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_order_commodity_code_with_options_async(request, runtime)

    def describe_cdn_region_and_isp_with_options(
        self,
        request: main_models.DescribeCdnRegionAndIspRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnRegionAndIspResponse:
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
            action = 'DescribeCdnRegionAndIsp',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnRegionAndIspResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_region_and_isp_with_options_async(
        self,
        request: main_models.DescribeCdnRegionAndIspRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnRegionAndIspResponse:
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
            action = 'DescribeCdnRegionAndIsp',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnRegionAndIspResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_region_and_isp(
        self,
        request: main_models.DescribeCdnRegionAndIspRequest,
    ) -> main_models.DescribeCdnRegionAndIspResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_region_and_isp_with_options(request, runtime)

    async def describe_cdn_region_and_isp_async(
        self,
        request: main_models.DescribeCdnRegionAndIspRequest,
    ) -> main_models.DescribeCdnRegionAndIspResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_region_and_isp_with_options_async(request, runtime)

    def describe_cdn_report_with_options(
        self,
        request: main_models.DescribeCdnReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnReportResponse:
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
            action = 'DescribeCdnReport',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_report_with_options_async(
        self,
        request: main_models.DescribeCdnReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnReportResponse:
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
            action = 'DescribeCdnReport',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_report(
        self,
        request: main_models.DescribeCdnReportRequest,
    ) -> main_models.DescribeCdnReportResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_report_with_options(request, runtime)

    async def describe_cdn_report_async(
        self,
        request: main_models.DescribeCdnReportRequest,
    ) -> main_models.DescribeCdnReportResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_report_with_options_async(request, runtime)

    def describe_cdn_report_list_with_options(
        self,
        request: main_models.DescribeCdnReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnReportList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_report_list_with_options_async(
        self,
        request: main_models.DescribeCdnReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnReportList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_report_list(
        self,
        request: main_models.DescribeCdnReportListRequest,
    ) -> main_models.DescribeCdnReportListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_report_list_with_options(request, runtime)

    async def describe_cdn_report_list_async(
        self,
        request: main_models.DescribeCdnReportListRequest,
    ) -> main_models.DescribeCdnReportListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_report_list_with_options_async(request, runtime)

    def describe_cdn_smcertificate_detail_with_options(
        self,
        request: main_models.DescribeCdnSMCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSMCertificateDetailResponse:
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
            action = 'DescribeCdnSMCertificateDetail',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSMCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_smcertificate_detail_with_options_async(
        self,
        request: main_models.DescribeCdnSMCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSMCertificateDetailResponse:
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
            action = 'DescribeCdnSMCertificateDetail',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSMCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_smcertificate_detail(
        self,
        request: main_models.DescribeCdnSMCertificateDetailRequest,
    ) -> main_models.DescribeCdnSMCertificateDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_smcertificate_detail_with_options(request, runtime)

    async def describe_cdn_smcertificate_detail_async(
        self,
        request: main_models.DescribeCdnSMCertificateDetailRequest,
    ) -> main_models.DescribeCdnSMCertificateDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_smcertificate_detail_with_options_async(request, runtime)

    def describe_cdn_smcertificate_list_with_options(
        self,
        request: main_models.DescribeCdnSMCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSMCertificateListResponse:
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
            action = 'DescribeCdnSMCertificateList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSMCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_smcertificate_list_with_options_async(
        self,
        request: main_models.DescribeCdnSMCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSMCertificateListResponse:
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
            action = 'DescribeCdnSMCertificateList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSMCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_smcertificate_list(
        self,
        request: main_models.DescribeCdnSMCertificateListRequest,
    ) -> main_models.DescribeCdnSMCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_smcertificate_list_with_options(request, runtime)

    async def describe_cdn_smcertificate_list_async(
        self,
        request: main_models.DescribeCdnSMCertificateListRequest,
    ) -> main_models.DescribeCdnSMCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_smcertificate_list_with_options_async(request, runtime)

    def describe_cdn_sslcertificate_list_with_options(
        self,
        request: main_models.DescribeCdnSSLCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSSLCertificateListResponse:
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
            action = 'DescribeCdnSSLCertificateList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSSLCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_sslcertificate_list_with_options_async(
        self,
        request: main_models.DescribeCdnSSLCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSSLCertificateListResponse:
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
            action = 'DescribeCdnSSLCertificateList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSSLCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_sslcertificate_list(
        self,
        request: main_models.DescribeCdnSSLCertificateListRequest,
    ) -> main_models.DescribeCdnSSLCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_sslcertificate_list_with_options(request, runtime)

    async def describe_cdn_sslcertificate_list_async(
        self,
        request: main_models.DescribeCdnSSLCertificateListRequest,
    ) -> main_models.DescribeCdnSSLCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_sslcertificate_list_with_options_async(request, runtime)

    def describe_cdn_sec_func_info_with_options(
        self,
        request: main_models.DescribeCdnSecFuncInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSecFuncInfoResponse:
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
            action = 'DescribeCdnSecFuncInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSecFuncInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_sec_func_info_with_options_async(
        self,
        request: main_models.DescribeCdnSecFuncInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSecFuncInfoResponse:
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
            action = 'DescribeCdnSecFuncInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSecFuncInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_sec_func_info(
        self,
        request: main_models.DescribeCdnSecFuncInfoRequest,
    ) -> main_models.DescribeCdnSecFuncInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_sec_func_info_with_options(request, runtime)

    async def describe_cdn_sec_func_info_async(
        self,
        request: main_models.DescribeCdnSecFuncInfoRequest,
    ) -> main_models.DescribeCdnSecFuncInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_sec_func_info_with_options_async(request, runtime)

    def describe_cdn_service_with_options(
        self,
        request: main_models.DescribeCdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnServiceResponse:
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
            action = 'DescribeCdnService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_service_with_options_async(
        self,
        request: main_models.DescribeCdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnServiceResponse:
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
            action = 'DescribeCdnService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_service(
        self,
        request: main_models.DescribeCdnServiceRequest,
    ) -> main_models.DescribeCdnServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_service_with_options(request, runtime)

    async def describe_cdn_service_async(
        self,
        request: main_models.DescribeCdnServiceRequest,
    ) -> main_models.DescribeCdnServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_service_with_options_async(request, runtime)

    def describe_cdn_sub_list_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSubListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCdnSubList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSubListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_sub_list_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnSubListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCdnSubList',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnSubListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_sub_list(self) -> main_models.DescribeCdnSubListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_sub_list_with_options(runtime)

    async def describe_cdn_sub_list_async(self) -> main_models.DescribeCdnSubListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_sub_list_with_options_async(runtime)

    def describe_cdn_types_with_options(
        self,
        request: main_models.DescribeCdnTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnTypesResponse:
        request.validate()
        query = {}
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
            action = 'DescribeCdnTypes',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_types_with_options_async(
        self,
        request: main_models.DescribeCdnTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnTypesResponse:
        request.validate()
        query = {}
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
            action = 'DescribeCdnTypes',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_types(
        self,
        request: main_models.DescribeCdnTypesRequest,
    ) -> main_models.DescribeCdnTypesResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_types_with_options(request, runtime)

    async def describe_cdn_types_async(
        self,
        request: main_models.DescribeCdnTypesRequest,
    ) -> main_models.DescribeCdnTypesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_types_with_options_async(request, runtime)

    def describe_cdn_user_bill_history_with_options(
        self,
        request: main_models.DescribeCdnUserBillHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserBillHistoryResponse:
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
            action = 'DescribeCdnUserBillHistory',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserBillHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_bill_history_with_options_async(
        self,
        request: main_models.DescribeCdnUserBillHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserBillHistoryResponse:
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
            action = 'DescribeCdnUserBillHistory',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserBillHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_bill_history(
        self,
        request: main_models.DescribeCdnUserBillHistoryRequest,
    ) -> main_models.DescribeCdnUserBillHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_user_bill_history_with_options(request, runtime)

    async def describe_cdn_user_bill_history_async(
        self,
        request: main_models.DescribeCdnUserBillHistoryRequest,
    ) -> main_models.DescribeCdnUserBillHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_user_bill_history_with_options_async(request, runtime)

    def describe_cdn_user_bill_prediction_with_options(
        self,
        request: main_models.DescribeCdnUserBillPredictionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserBillPredictionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnUserBillPrediction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserBillPredictionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_bill_prediction_with_options_async(
        self,
        request: main_models.DescribeCdnUserBillPredictionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserBillPredictionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnUserBillPrediction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserBillPredictionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_bill_prediction(
        self,
        request: main_models.DescribeCdnUserBillPredictionRequest,
    ) -> main_models.DescribeCdnUserBillPredictionResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_user_bill_prediction_with_options(request, runtime)

    async def describe_cdn_user_bill_prediction_async(
        self,
        request: main_models.DescribeCdnUserBillPredictionRequest,
    ) -> main_models.DescribeCdnUserBillPredictionResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_user_bill_prediction_with_options_async(request, runtime)

    def describe_cdn_user_bill_type_with_options(
        self,
        request: main_models.DescribeCdnUserBillTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserBillTypeResponse:
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
            action = 'DescribeCdnUserBillType',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserBillTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_bill_type_with_options_async(
        self,
        request: main_models.DescribeCdnUserBillTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserBillTypeResponse:
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
            action = 'DescribeCdnUserBillType',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserBillTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_bill_type(
        self,
        request: main_models.DescribeCdnUserBillTypeRequest,
    ) -> main_models.DescribeCdnUserBillTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_user_bill_type_with_options(request, runtime)

    async def describe_cdn_user_bill_type_async(
        self,
        request: main_models.DescribeCdnUserBillTypeRequest,
    ) -> main_models.DescribeCdnUserBillTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_user_bill_type_with_options_async(request, runtime)

    def describe_cdn_user_configs_with_options(
        self,
        request: main_models.DescribeCdnUserConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnUserConfigs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_configs_with_options_async(
        self,
        request: main_models.DescribeCdnUserConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnUserConfigs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_configs(
        self,
        request: main_models.DescribeCdnUserConfigsRequest,
    ) -> main_models.DescribeCdnUserConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_user_configs_with_options(request, runtime)

    async def describe_cdn_user_configs_async(
        self,
        request: main_models.DescribeCdnUserConfigsRequest,
    ) -> main_models.DescribeCdnUserConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_user_configs_with_options_async(request, runtime)

    def describe_cdn_user_domains_by_func_with_options(
        self,
        request: main_models.DescribeCdnUserDomainsByFuncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserDomainsByFuncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.func_id):
            query['FuncId'] = request.func_id
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
            action = 'DescribeCdnUserDomainsByFunc',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserDomainsByFuncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_domains_by_func_with_options_async(
        self,
        request: main_models.DescribeCdnUserDomainsByFuncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserDomainsByFuncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.func_id):
            query['FuncId'] = request.func_id
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
            action = 'DescribeCdnUserDomainsByFunc',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserDomainsByFuncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_domains_by_func(
        self,
        request: main_models.DescribeCdnUserDomainsByFuncRequest,
    ) -> main_models.DescribeCdnUserDomainsByFuncResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_user_domains_by_func_with_options(request, runtime)

    async def describe_cdn_user_domains_by_func_async(
        self,
        request: main_models.DescribeCdnUserDomainsByFuncRequest,
    ) -> main_models.DescribeCdnUserDomainsByFuncResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_user_domains_by_func_with_options_async(request, runtime)

    def describe_cdn_user_quota_with_options(
        self,
        request: main_models.DescribeCdnUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserQuotaResponse:
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
            action = 'DescribeCdnUserQuota',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_quota_with_options_async(
        self,
        request: main_models.DescribeCdnUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserQuotaResponse:
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
            action = 'DescribeCdnUserQuota',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_quota(
        self,
        request: main_models.DescribeCdnUserQuotaRequest,
    ) -> main_models.DescribeCdnUserQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_user_quota_with_options(request, runtime)

    async def describe_cdn_user_quota_async(
        self,
        request: main_models.DescribeCdnUserQuotaRequest,
    ) -> main_models.DescribeCdnUserQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_user_quota_with_options_async(request, runtime)

    def describe_cdn_user_resource_package_with_options(
        self,
        request: main_models.DescribeCdnUserResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserResourcePackageResponse:
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
            action = 'DescribeCdnUserResourcePackage',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_resource_package_with_options_async(
        self,
        request: main_models.DescribeCdnUserResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnUserResourcePackageResponse:
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
            action = 'DescribeCdnUserResourcePackage',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnUserResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_resource_package(
        self,
        request: main_models.DescribeCdnUserResourcePackageRequest,
    ) -> main_models.DescribeCdnUserResourcePackageResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_user_resource_package_with_options(request, runtime)

    async def describe_cdn_user_resource_package_async(
        self,
        request: main_models.DescribeCdnUserResourcePackageRequest,
    ) -> main_models.DescribeCdnUserResourcePackageResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_user_resource_package_with_options_async(request, runtime)

    def describe_cdn_waf_domain_with_options(
        self,
        request: main_models.DescribeCdnWafDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnWafDomainResponse:
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
            action = 'DescribeCdnWafDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnWafDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_waf_domain_with_options_async(
        self,
        request: main_models.DescribeCdnWafDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnWafDomainResponse:
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
            action = 'DescribeCdnWafDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnWafDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_waf_domain(
        self,
        request: main_models.DescribeCdnWafDomainRequest,
    ) -> main_models.DescribeCdnWafDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_waf_domain_with_options(request, runtime)

    async def describe_cdn_waf_domain_async(
        self,
        request: main_models.DescribeCdnWafDomainRequest,
    ) -> main_models.DescribeCdnWafDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_waf_domain_with_options_async(request, runtime)

    def describe_certificate_info_by_idwith_options(
        self,
        request: main_models.DescribeCertificateInfoByIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertificateInfoByIDResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertificateInfoByID',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertificateInfoByIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificate_info_by_idwith_options_async(
        self,
        request: main_models.DescribeCertificateInfoByIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertificateInfoByIDResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertificateInfoByID',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertificateInfoByIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificate_info_by_id(
        self,
        request: main_models.DescribeCertificateInfoByIDRequest,
    ) -> main_models.DescribeCertificateInfoByIDResponse:
        runtime = RuntimeOptions()
        return self.describe_certificate_info_by_idwith_options(request, runtime)

    async def describe_certificate_info_by_id_async(
        self,
        request: main_models.DescribeCertificateInfoByIDRequest,
    ) -> main_models.DescribeCertificateInfoByIDResponse:
        runtime = RuntimeOptions()
        return await self.describe_certificate_info_by_idwith_options_async(request, runtime)

    def describe_custom_domain_sample_rate_with_options(
        self,
        request: main_models.DescribeCustomDomainSampleRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomDomainSampleRateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomDomainSampleRate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomDomainSampleRate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def describe_custom_log_config_with_options(
        self,
        request: main_models.DescribeCustomLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLogConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLogConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_log_config_with_options_async(
        self,
        request: main_models.DescribeCustomLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLogConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLogConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_log_config(
        self,
        request: main_models.DescribeCustomLogConfigRequest,
    ) -> main_models.DescribeCustomLogConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_log_config_with_options(request, runtime)

    async def describe_custom_log_config_async(
        self,
        request: main_models.DescribeCustomLogConfigRequest,
    ) -> main_models.DescribeCustomLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_log_config_with_options_async(request, runtime)

    def describe_domain_average_response_time_with_options(
        self,
        request: main_models.DescribeDomainAverageResponseTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAverageResponseTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
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
        if not DaraCore.is_null(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAverageResponseTime',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAverageResponseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_average_response_time_with_options_async(
        self,
        request: main_models.DescribeDomainAverageResponseTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAverageResponseTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
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
        if not DaraCore.is_null(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAverageResponseTime',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAverageResponseTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_average_response_time(
        self,
        request: main_models.DescribeDomainAverageResponseTimeRequest,
    ) -> main_models.DescribeDomainAverageResponseTimeResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_average_response_time_with_options(request, runtime)

    async def describe_domain_average_response_time_async(
        self,
        request: main_models.DescribeDomainAverageResponseTimeRequest,
    ) -> main_models.DescribeDomainAverageResponseTimeResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_average_response_time_with_options_async(request, runtime)

    def describe_domain_bps_data_with_options(
        self,
        request: main_models.DescribeDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsDataResponse:
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
            action = 'DescribeDomainBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_with_options_async(
        self,
        request: main_models.DescribeDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsDataResponse:
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
            action = 'DescribeDomainBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data(
        self,
        request: main_models.DescribeDomainBpsDataRequest,
    ) -> main_models.DescribeDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_bps_data_with_options(request, runtime)

    async def describe_domain_bps_data_async(
        self,
        request: main_models.DescribeDomainBpsDataRequest,
    ) -> main_models.DescribeDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_bps_data_with_options_async(request, runtime)

    def describe_domain_bps_data_by_layer_with_options(
        self,
        request: main_models.DescribeDomainBpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsDataByLayerResponse:
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
            action = 'DescribeDomainBpsDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeDomainBpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsDataByLayerResponse:
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
            action = 'DescribeDomainBpsDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data_by_layer(
        self,
        request: main_models.DescribeDomainBpsDataByLayerRequest,
    ) -> main_models.DescribeDomainBpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_bps_data_by_layer_with_options(request, runtime)

    async def describe_domain_bps_data_by_layer_async(
        self,
        request: main_models.DescribeDomainBpsDataByLayerRequest,
    ) -> main_models.DescribeDomainBpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_bps_data_by_layer_with_options_async(request, runtime)

    def describe_domain_bps_data_by_time_stamp_with_options(
        self,
        request: main_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsDataByTimeStampResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.isp_names):
            query['IspNames'] = request.isp_names
        if not DaraCore.is_null(request.location_names):
            query['LocationNames'] = request.location_names
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainBpsDataByTimeStamp',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsDataByTimeStampResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_by_time_stamp_with_options_async(
        self,
        request: main_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsDataByTimeStampResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.isp_names):
            query['IspNames'] = request.isp_names
        if not DaraCore.is_null(request.location_names):
            query['LocationNames'] = request.location_names
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainBpsDataByTimeStamp',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsDataByTimeStampResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data_by_time_stamp(
        self,
        request: main_models.DescribeDomainBpsDataByTimeStampRequest,
    ) -> main_models.DescribeDomainBpsDataByTimeStampResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_bps_data_by_time_stamp_with_options(request, runtime)

    async def describe_domain_bps_data_by_time_stamp_async(
        self,
        request: main_models.DescribeDomainBpsDataByTimeStampRequest,
    ) -> main_models.DescribeDomainBpsDataByTimeStampResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_bps_data_by_time_stamp_with_options_async(request, runtime)

    def describe_domain_cc_activity_log_with_options(
        self,
        request: main_models.DescribeDomainCcActivityLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCcActivityLogResponse:
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
            action = 'DescribeDomainCcActivityLog',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCcActivityLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_cc_activity_log_with_options_async(
        self,
        request: main_models.DescribeDomainCcActivityLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCcActivityLogResponse:
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
            action = 'DescribeDomainCcActivityLog',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCcActivityLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_cc_activity_log(
        self,
        request: main_models.DescribeDomainCcActivityLogRequest,
    ) -> main_models.DescribeDomainCcActivityLogResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_cc_activity_log_with_options(request, runtime)

    async def describe_domain_cc_activity_log_async(
        self,
        request: main_models.DescribeDomainCcActivityLogRequest,
    ) -> main_models.DescribeDomainCcActivityLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_cc_activity_log_with_options_async(request, runtime)

    def describe_domain_certificate_info_with_options(
        self,
        request: main_models.DescribeDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCertificateInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_certificate_info_with_options_async(
        self,
        request: main_models.DescribeDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCertificateInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_certificate_info(
        self,
        request: main_models.DescribeDomainCertificateInfoRequest,
    ) -> main_models.DescribeDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_certificate_info_with_options(request, runtime)

    async def describe_domain_certificate_info_async(
        self,
        request: main_models.DescribeDomainCertificateInfoRequest,
    ) -> main_models.DescribeDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_certificate_info_with_options_async(request, runtime)

    def describe_domain_cname_with_options(
        self,
        request: main_models.DescribeDomainCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCnameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCname',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_cname_with_options_async(
        self,
        request: main_models.DescribeDomainCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCnameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCname',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_cname(
        self,
        request: main_models.DescribeDomainCnameRequest,
    ) -> main_models.DescribeDomainCnameResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_cname_with_options(request, runtime)

    async def describe_domain_cname_async(
        self,
        request: main_models.DescribeDomainCnameRequest,
    ) -> main_models.DescribeDomainCnameResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_cname_with_options_async(request, runtime)

    def describe_domain_custom_log_config_with_options(
        self,
        request: main_models.DescribeDomainCustomLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCustomLogConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCustomLogConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_custom_log_config_with_options_async(
        self,
        request: main_models.DescribeDomainCustomLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCustomLogConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCustomLogConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_custom_log_config(
        self,
        request: main_models.DescribeDomainCustomLogConfigRequest,
    ) -> main_models.DescribeDomainCustomLogConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_custom_log_config_with_options(request, runtime)

    async def describe_domain_custom_log_config_async(
        self,
        request: main_models.DescribeDomainCustomLogConfigRequest,
    ) -> main_models.DescribeDomainCustomLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_custom_log_config_with_options_async(request, runtime)

    def describe_domain_detail_data_by_layer_with_options(
        self,
        request: main_models.DescribeDomainDetailDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDetailDataByLayerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDetailDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDetailDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_detail_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeDomainDetailDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDetailDataByLayerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDetailDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDetailDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_detail_data_by_layer(
        self,
        request: main_models.DescribeDomainDetailDataByLayerRequest,
    ) -> main_models.DescribeDomainDetailDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_detail_data_by_layer_with_options(request, runtime)

    async def describe_domain_detail_data_by_layer_async(
        self,
        request: main_models.DescribeDomainDetailDataByLayerRequest,
    ) -> main_models.DescribeDomainDetailDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_detail_data_by_layer_with_options_async(request, runtime)

    def describe_domain_hit_rate_data_with_options(
        self,
        request: main_models.DescribeDomainHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainHitRateDataResponse:
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
            action = 'DescribeDomainHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeDomainHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainHitRateDataResponse:
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
            action = 'DescribeDomainHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_hit_rate_data(
        self,
        request: main_models.DescribeDomainHitRateDataRequest,
    ) -> main_models.DescribeDomainHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_hit_rate_data_with_options(request, runtime)

    async def describe_domain_hit_rate_data_async(
        self,
        request: main_models.DescribeDomainHitRateDataRequest,
    ) -> main_models.DescribeDomainHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_http_code_data_with_options(
        self,
        request: main_models.DescribeDomainHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainHttpCodeDataResponse:
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
            action = 'DescribeDomainHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDomainHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainHttpCodeDataResponse:
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
            action = 'DescribeDomainHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_http_code_data(
        self,
        request: main_models.DescribeDomainHttpCodeDataRequest,
    ) -> main_models.DescribeDomainHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_http_code_data_with_options(request, runtime)

    async def describe_domain_http_code_data_async(
        self,
        request: main_models.DescribeDomainHttpCodeDataRequest,
    ) -> main_models.DescribeDomainHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_http_code_data_with_options_async(request, runtime)

    def describe_domain_http_code_data_by_layer_with_options(
        self,
        request: main_models.DescribeDomainHttpCodeDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainHttpCodeDataByLayerResponse:
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
            action = 'DescribeDomainHttpCodeDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainHttpCodeDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_http_code_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeDomainHttpCodeDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainHttpCodeDataByLayerResponse:
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
            action = 'DescribeDomainHttpCodeDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainHttpCodeDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_http_code_data_by_layer(
        self,
        request: main_models.DescribeDomainHttpCodeDataByLayerRequest,
    ) -> main_models.DescribeDomainHttpCodeDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_http_code_data_by_layer_with_options(request, runtime)

    async def describe_domain_http_code_data_by_layer_async(
        self,
        request: main_models.DescribeDomainHttpCodeDataByLayerRequest,
    ) -> main_models.DescribeDomainHttpCodeDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_http_code_data_by_layer_with_options_async(request, runtime)

    def describe_domain_ispdata_with_options(
        self,
        request: main_models.DescribeDomainISPDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainISPDataResponse:
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
            action = 'DescribeDomainISPData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainISPDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_ispdata_with_options_async(
        self,
        request: main_models.DescribeDomainISPDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainISPDataResponse:
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
            action = 'DescribeDomainISPData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainISPDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_ispdata(
        self,
        request: main_models.DescribeDomainISPDataRequest,
    ) -> main_models.DescribeDomainISPDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_ispdata_with_options(request, runtime)

    async def describe_domain_ispdata_async(
        self,
        request: main_models.DescribeDomainISPDataRequest,
    ) -> main_models.DescribeDomainISPDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_ispdata_with_options_async(request, runtime)

    def describe_domain_max_95bps_data_with_options(
        self,
        request: main_models.DescribeDomainMax95BpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainMax95BpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle):
            query['Cycle'] = request.cycle
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainMax95BpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainMax95BpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_max_95bps_data_with_options_async(
        self,
        request: main_models.DescribeDomainMax95BpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainMax95BpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle):
            query['Cycle'] = request.cycle
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainMax95BpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainMax95BpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_max_95bps_data(
        self,
        request: main_models.DescribeDomainMax95BpsDataRequest,
    ) -> main_models.DescribeDomainMax95BpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_max_95bps_data_with_options(request, runtime)

    async def describe_domain_max_95bps_data_async(
        self,
        request: main_models.DescribeDomainMax95BpsDataRequest,
    ) -> main_models.DescribeDomainMax95BpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_max_95bps_data_with_options_async(request, runtime)

    def describe_domain_multi_usage_data_with_options(
        self,
        request: main_models.DescribeDomainMultiUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainMultiUsageDataResponse:
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
            action = 'DescribeDomainMultiUsageData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainMultiUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_multi_usage_data_with_options_async(
        self,
        request: main_models.DescribeDomainMultiUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainMultiUsageDataResponse:
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
            action = 'DescribeDomainMultiUsageData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainMultiUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_multi_usage_data(
        self,
        request: main_models.DescribeDomainMultiUsageDataRequest,
    ) -> main_models.DescribeDomainMultiUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_multi_usage_data_with_options(request, runtime)

    async def describe_domain_multi_usage_data_async(
        self,
        request: main_models.DescribeDomainMultiUsageDataRequest,
    ) -> main_models.DescribeDomainMultiUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_multi_usage_data_with_options_async(request, runtime)

    def describe_domain_path_data_with_options(
        self,
        request: main_models.DescribeDomainPathDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainPathDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainPathData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainPathDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_path_data_with_options_async(
        self,
        request: main_models.DescribeDomainPathDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainPathDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainPathData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainPathDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_path_data(
        self,
        request: main_models.DescribeDomainPathDataRequest,
    ) -> main_models.DescribeDomainPathDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_path_data_with_options(request, runtime)

    async def describe_domain_path_data_async(
        self,
        request: main_models.DescribeDomainPathDataRequest,
    ) -> main_models.DescribeDomainPathDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_path_data_with_options_async(request, runtime)

    def describe_domain_pv_data_with_options(
        self,
        request: main_models.DescribeDomainPvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainPvDataResponse:
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
            action = 'DescribeDomainPvData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_pv_data_with_options_async(
        self,
        request: main_models.DescribeDomainPvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainPvDataResponse:
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
            action = 'DescribeDomainPvData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainPvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_pv_data(
        self,
        request: main_models.DescribeDomainPvDataRequest,
    ) -> main_models.DescribeDomainPvDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_pv_data_with_options(request, runtime)

    async def describe_domain_pv_data_async(
        self,
        request: main_models.DescribeDomainPvDataRequest,
    ) -> main_models.DescribeDomainPvDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_pv_data_with_options_async(request, runtime)

    def describe_domain_qps_data_with_options(
        self,
        request: main_models.DescribeDomainQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsDataResponse:
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
            action = 'DescribeDomainQpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_data_with_options_async(
        self,
        request: main_models.DescribeDomainQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsDataResponse:
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
            action = 'DescribeDomainQpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qps_data(
        self,
        request: main_models.DescribeDomainQpsDataRequest,
    ) -> main_models.DescribeDomainQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_qps_data_with_options(request, runtime)

    async def describe_domain_qps_data_async(
        self,
        request: main_models.DescribeDomainQpsDataRequest,
    ) -> main_models.DescribeDomainQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_qps_data_with_options_async(request, runtime)

    def describe_domain_qps_data_by_layer_with_options(
        self,
        request: main_models.DescribeDomainQpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsDataByLayerResponse:
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
            action = 'DescribeDomainQpsDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeDomainQpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsDataByLayerResponse:
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
            action = 'DescribeDomainQpsDataByLayer',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qps_data_by_layer(
        self,
        request: main_models.DescribeDomainQpsDataByLayerRequest,
    ) -> main_models.DescribeDomainQpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_qps_data_by_layer_with_options(request, runtime)

    async def describe_domain_qps_data_by_layer_async(
        self,
        request: main_models.DescribeDomainQpsDataByLayerRequest,
    ) -> main_models.DescribeDomainQpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_qps_data_by_layer_with_options_async(request, runtime)

    def describe_domain_real_time_bps_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeBpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_bps_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeBpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_bps_data(
        self,
        request: main_models.DescribeDomainRealTimeBpsDataRequest,
    ) -> main_models.DescribeDomainRealTimeBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_domain_real_time_bps_data_async(
        self,
        request: main_models.DescribeDomainRealTimeBpsDataRequest,
    ) -> main_models.DescribeDomainRealTimeBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeByteHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeByteHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeByteHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeByteHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeByteHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeByteHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeByteHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_byte_hit_rate_data(
        self,
        request: main_models.DescribeDomainRealTimeByteHitRateDataRequest,
    ) -> main_models.DescribeDomainRealTimeByteHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_domain_real_time_byte_hit_rate_data_async(
        self,
        request: main_models.DescribeDomainRealTimeByteHitRateDataRequest,
    ) -> main_models.DescribeDomainRealTimeByteHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_real_time_detail_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeDetailDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeDetailDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeDetailData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_detail_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeDetailDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeDetailDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeDetailData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_detail_data(
        self,
        request: main_models.DescribeDomainRealTimeDetailDataRequest,
    ) -> main_models.DescribeDomainRealTimeDetailDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_domain_real_time_detail_data_async(
        self,
        request: main_models.DescribeDomainRealTimeDetailDataRequest,
    ) -> main_models.DescribeDomainRealTimeDetailDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_domain_real_time_http_code_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeHttpCodeDataResponse:
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
            action = 'DescribeDomainRealTimeHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeHttpCodeDataResponse:
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
            action = 'DescribeDomainRealTimeHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_http_code_data(
        self,
        request: main_models.DescribeDomainRealTimeHttpCodeDataRequest,
    ) -> main_models.DescribeDomainRealTimeHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_domain_real_time_http_code_data_async(
        self,
        request: main_models.DescribeDomainRealTimeHttpCodeDataRequest,
    ) -> main_models.DescribeDomainRealTimeHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_domain_real_time_qps_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeQpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeQpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_qps_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeQpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeQpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_qps_data(
        self,
        request: main_models.DescribeDomainRealTimeQpsDataRequest,
    ) -> main_models.DescribeDomainRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_domain_real_time_qps_data_async(
        self,
        request: main_models.DescribeDomainRealTimeQpsDataRequest,
    ) -> main_models.DescribeDomainRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeReqHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeReqHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeReqHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealTimeReqHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_req_hit_rate_data(
        self,
        request: main_models.DescribeDomainRealTimeReqHitRateDataRequest,
    ) -> main_models.DescribeDomainRealTimeReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_domain_real_time_req_hit_rate_data_async(
        self,
        request: main_models.DescribeDomainRealTimeReqHitRateDataRequest,
    ) -> main_models.DescribeDomainRealTimeReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_bps_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeSrcBpsDataResponse:
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
            action = 'DescribeDomainRealTimeSrcBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_src_bps_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeSrcBpsDataResponse:
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
            action = 'DescribeDomainRealTimeSrcBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_src_bps_data(
        self,
        request: main_models.DescribeDomainRealTimeSrcBpsDataRequest,
    ) -> main_models.DescribeDomainRealTimeSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_domain_real_time_src_bps_data_async(
        self,
        request: main_models.DescribeDomainRealTimeSrcBpsDataRequest,
    ) -> main_models.DescribeDomainRealTimeSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_http_code_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
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
            action = 'DescribeDomainRealTimeSrcHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_src_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
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
            action = 'DescribeDomainRealTimeSrcHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeSrcHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_src_http_code_data(
        self,
        request: main_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
    ) -> main_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_src_http_code_data_with_options(request, runtime)

    async def describe_domain_real_time_src_http_code_data_async(
        self,
        request: main_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
    ) -> main_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_src_http_code_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_traffic_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeSrcTrafficDataResponse:
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
            action = 'DescribeDomainRealTimeSrcTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeSrcTrafficDataResponse:
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
            action = 'DescribeDomainRealTimeSrcTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_src_traffic_data(
        self,
        request: main_models.DescribeDomainRealTimeSrcTrafficDataRequest,
    ) -> main_models.DescribeDomainRealTimeSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_domain_real_time_src_traffic_data_async(
        self,
        request: main_models.DescribeDomainRealTimeSrcTrafficDataRequest,
    ) -> main_models.DescribeDomainRealTimeSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_domain_real_time_traffic_data_with_options(
        self,
        request: main_models.DescribeDomainRealTimeTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeTrafficDataResponse:
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
            action = 'DescribeDomainRealTimeTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDomainRealTimeTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealTimeTrafficDataResponse:
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
            action = 'DescribeDomainRealTimeTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealTimeTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_traffic_data(
        self,
        request: main_models.DescribeDomainRealTimeTrafficDataRequest,
    ) -> main_models.DescribeDomainRealTimeTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_domain_real_time_traffic_data_async(
        self,
        request: main_models.DescribeDomainRealTimeTrafficDataRequest,
    ) -> main_models.DescribeDomainRealTimeTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_domain_realtime_log_delivery_with_options(
        self,
        request: main_models.DescribeDomainRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_realtime_log_delivery_with_options_async(
        self,
        request: main_models.DescribeDomainRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_realtime_log_delivery(
        self,
        request: main_models.DescribeDomainRealtimeLogDeliveryRequest,
    ) -> main_models.DescribeDomainRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_realtime_log_delivery_with_options(request, runtime)

    async def describe_domain_realtime_log_delivery_async(
        self,
        request: main_models.DescribeDomainRealtimeLogDeliveryRequest,
    ) -> main_models.DescribeDomainRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_realtime_log_delivery_with_options_async(request, runtime)

    def describe_domain_region_data_with_options(
        self,
        request: main_models.DescribeDomainRegionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRegionDataResponse:
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
            action = 'DescribeDomainRegionData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_region_data_with_options_async(
        self,
        request: main_models.DescribeDomainRegionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRegionDataResponse:
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
            action = 'DescribeDomainRegionData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_region_data(
        self,
        request: main_models.DescribeDomainRegionDataRequest,
    ) -> main_models.DescribeDomainRegionDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_region_data_with_options(request, runtime)

    async def describe_domain_region_data_async(
        self,
        request: main_models.DescribeDomainRegionDataRequest,
    ) -> main_models.DescribeDomainRegionDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_region_data_with_options_async(request, runtime)

    def describe_domain_req_hit_rate_data_with_options(
        self,
        request: main_models.DescribeDomainReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainReqHitRateDataResponse:
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
            action = 'DescribeDomainReqHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_req_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeDomainReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainReqHitRateDataResponse:
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
            action = 'DescribeDomainReqHitRateData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_req_hit_rate_data(
        self,
        request: main_models.DescribeDomainReqHitRateDataRequest,
    ) -> main_models.DescribeDomainReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_req_hit_rate_data_with_options(request, runtime)

    async def describe_domain_req_hit_rate_data_async(
        self,
        request: main_models.DescribeDomainReqHitRateDataRequest,
    ) -> main_models.DescribeDomainReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_req_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_src_bps_data_with_options(
        self,
        request: main_models.DescribeDomainSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcBpsDataResponse:
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
            action = 'DescribeDomainSrcBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_bps_data_with_options_async(
        self,
        request: main_models.DescribeDomainSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcBpsDataResponse:
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
            action = 'DescribeDomainSrcBpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_bps_data(
        self,
        request: main_models.DescribeDomainSrcBpsDataRequest,
    ) -> main_models.DescribeDomainSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_src_bps_data_with_options(request, runtime)

    async def describe_domain_src_bps_data_async(
        self,
        request: main_models.DescribeDomainSrcBpsDataRequest,
    ) -> main_models.DescribeDomainSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_src_bps_data_with_options_async(request, runtime)

    def describe_domain_src_http_code_data_with_options(
        self,
        request: main_models.DescribeDomainSrcHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcHttpCodeDataResponse:
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
            action = 'DescribeDomainSrcHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_http_code_data_with_options_async(
        self,
        request: main_models.DescribeDomainSrcHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcHttpCodeDataResponse:
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
            action = 'DescribeDomainSrcHttpCodeData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_http_code_data(
        self,
        request: main_models.DescribeDomainSrcHttpCodeDataRequest,
    ) -> main_models.DescribeDomainSrcHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_src_http_code_data_with_options(request, runtime)

    async def describe_domain_src_http_code_data_async(
        self,
        request: main_models.DescribeDomainSrcHttpCodeDataRequest,
    ) -> main_models.DescribeDomainSrcHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_src_http_code_data_with_options_async(request, runtime)

    def describe_domain_src_qps_data_with_options(
        self,
        request: main_models.DescribeDomainSrcQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcQpsDataResponse:
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
            action = 'DescribeDomainSrcQpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_qps_data_with_options_async(
        self,
        request: main_models.DescribeDomainSrcQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcQpsDataResponse:
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
            action = 'DescribeDomainSrcQpsData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_qps_data(
        self,
        request: main_models.DescribeDomainSrcQpsDataRequest,
    ) -> main_models.DescribeDomainSrcQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_src_qps_data_with_options(request, runtime)

    async def describe_domain_src_qps_data_async(
        self,
        request: main_models.DescribeDomainSrcQpsDataRequest,
    ) -> main_models.DescribeDomainSrcQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_src_qps_data_with_options_async(request, runtime)

    def describe_domain_src_top_url_visit_with_options(
        self,
        request: main_models.DescribeDomainSrcTopUrlVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcTopUrlVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainSrcTopUrlVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_top_url_visit_with_options_async(
        self,
        request: main_models.DescribeDomainSrcTopUrlVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcTopUrlVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainSrcTopUrlVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcTopUrlVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_top_url_visit(
        self,
        request: main_models.DescribeDomainSrcTopUrlVisitRequest,
    ) -> main_models.DescribeDomainSrcTopUrlVisitResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_src_top_url_visit_with_options(request, runtime)

    async def describe_domain_src_top_url_visit_async(
        self,
        request: main_models.DescribeDomainSrcTopUrlVisitRequest,
    ) -> main_models.DescribeDomainSrcTopUrlVisitResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_src_top_url_visit_with_options_async(request, runtime)

    def describe_domain_src_traffic_data_with_options(
        self,
        request: main_models.DescribeDomainSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcTrafficDataResponse:
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
            action = 'DescribeDomainSrcTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDomainSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSrcTrafficDataResponse:
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
            action = 'DescribeDomainSrcTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_traffic_data(
        self,
        request: main_models.DescribeDomainSrcTrafficDataRequest,
    ) -> main_models.DescribeDomainSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_src_traffic_data_with_options(request, runtime)

    async def describe_domain_src_traffic_data_async(
        self,
        request: main_models.DescribeDomainSrcTrafficDataRequest,
    ) -> main_models.DescribeDomainSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_src_traffic_data_with_options_async(request, runtime)

    def describe_domain_top_client_ip_visit_with_options(
        self,
        request: main_models.DescribeDomainTopClientIpVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopClientIpVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopClientIpVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopClientIpVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_client_ip_visit_with_options_async(
        self,
        request: main_models.DescribeDomainTopClientIpVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopClientIpVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopClientIpVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopClientIpVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_client_ip_visit(
        self,
        request: main_models.DescribeDomainTopClientIpVisitRequest,
    ) -> main_models.DescribeDomainTopClientIpVisitResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_client_ip_visit_with_options(request, runtime)

    async def describe_domain_top_client_ip_visit_async(
        self,
        request: main_models.DescribeDomainTopClientIpVisitRequest,
    ) -> main_models.DescribeDomainTopClientIpVisitResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_client_ip_visit_with_options_async(request, runtime)

    def describe_domain_top_refer_visit_with_options(
        self,
        request: main_models.DescribeDomainTopReferVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopReferVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopReferVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_refer_visit_with_options_async(
        self,
        request: main_models.DescribeDomainTopReferVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopReferVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopReferVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopReferVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_refer_visit(
        self,
        request: main_models.DescribeDomainTopReferVisitRequest,
    ) -> main_models.DescribeDomainTopReferVisitResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_refer_visit_with_options(request, runtime)

    async def describe_domain_top_refer_visit_async(
        self,
        request: main_models.DescribeDomainTopReferVisitRequest,
    ) -> main_models.DescribeDomainTopReferVisitResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_domain_top_url_visit_with_options(
        self,
        request: main_models.DescribeDomainTopUrlVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopUrlVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopUrlVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_url_visit_with_options_async(
        self,
        request: main_models.DescribeDomainTopUrlVisitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopUrlVisitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopUrlVisit',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopUrlVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_url_visit(
        self,
        request: main_models.DescribeDomainTopUrlVisitRequest,
    ) -> main_models.DescribeDomainTopUrlVisitResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_url_visit_with_options(request, runtime)

    async def describe_domain_top_url_visit_async(
        self,
        request: main_models.DescribeDomainTopUrlVisitRequest,
    ) -> main_models.DescribeDomainTopUrlVisitResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_url_visit_with_options_async(request, runtime)

    def describe_domain_traffic_data_with_options(
        self,
        request: main_models.DescribeDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTrafficDataResponse:
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
            action = 'DescribeDomainTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_traffic_data_with_options_async(
        self,
        request: main_models.DescribeDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTrafficDataResponse:
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
            action = 'DescribeDomainTrafficData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_traffic_data(
        self,
        request: main_models.DescribeDomainTrafficDataRequest,
    ) -> main_models.DescribeDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_traffic_data_with_options(request, runtime)

    async def describe_domain_traffic_data_async(
        self,
        request: main_models.DescribeDomainTrafficDataRequest,
    ) -> main_models.DescribeDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_traffic_data_with_options_async(request, runtime)

    def describe_domain_usage_data_with_options(
        self,
        request: main_models.DescribeDomainUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainUsageDataResponse:
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
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainUsageData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_usage_data_with_options_async(
        self,
        request: main_models.DescribeDomainUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainUsageDataResponse:
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
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainUsageData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_usage_data(
        self,
        request: main_models.DescribeDomainUsageDataRequest,
    ) -> main_models.DescribeDomainUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_usage_data_with_options(request, runtime)

    async def describe_domain_usage_data_async(
        self,
        request: main_models.DescribeDomainUsageDataRequest,
    ) -> main_models.DescribeDomainUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_usage_data_with_options_async(request, runtime)

    def describe_domain_uv_data_with_options(
        self,
        request: main_models.DescribeDomainUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainUvDataResponse:
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
            action = 'DescribeDomainUvData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_uv_data_with_options_async(
        self,
        request: main_models.DescribeDomainUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainUvDataResponse:
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
            action = 'DescribeDomainUvData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_uv_data(
        self,
        request: main_models.DescribeDomainUvDataRequest,
    ) -> main_models.DescribeDomainUvDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_uv_data_with_options(request, runtime)

    async def describe_domain_uv_data_async(
        self,
        request: main_models.DescribeDomainUvDataRequest,
    ) -> main_models.DescribeDomainUvDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_uv_data_with_options_async(request, runtime)

    def describe_domain_verify_data_with_options(
        self,
        request: main_models.DescribeDomainVerifyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainVerifyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.global_resource_plan):
            query['GlobalResourcePlan'] = request.global_resource_plan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainVerifyData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainVerifyDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_verify_data_with_options_async(
        self,
        request: main_models.DescribeDomainVerifyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainVerifyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.global_resource_plan):
            query['GlobalResourcePlan'] = request.global_resource_plan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainVerifyData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainVerifyDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_verify_data(
        self,
        request: main_models.DescribeDomainVerifyDataRequest,
    ) -> main_models.DescribeDomainVerifyDataResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_verify_data_with_options(request, runtime)

    async def describe_domain_verify_data_async(
        self,
        request: main_models.DescribeDomainVerifyDataRequest,
    ) -> main_models.DescribeDomainVerifyDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_verify_data_with_options_async(request, runtime)

    def describe_domains_by_source_with_options(
        self,
        request: main_models.DescribeDomainsBySourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsBySourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainsBySource',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsBySourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_by_source_with_options_async(
        self,
        request: main_models.DescribeDomainsBySourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsBySourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainsBySource',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsBySourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains_by_source(
        self,
        request: main_models.DescribeDomainsBySourceRequest,
    ) -> main_models.DescribeDomainsBySourceResponse:
        runtime = RuntimeOptions()
        return self.describe_domains_by_source_with_options(request, runtime)

    async def describe_domains_by_source_async(
        self,
        request: main_models.DescribeDomainsBySourceRequest,
    ) -> main_models.DescribeDomainsBySourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_domains_by_source_with_options_async(request, runtime)

    def describe_domains_usage_by_day_with_options(
        self,
        request: main_models.DescribeDomainsUsageByDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsUsageByDayResponse:
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
            action = 'DescribeDomainsUsageByDay',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsUsageByDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_usage_by_day_with_options_async(
        self,
        request: main_models.DescribeDomainsUsageByDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsUsageByDayResponse:
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
            action = 'DescribeDomainsUsageByDay',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsUsageByDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains_usage_by_day(
        self,
        request: main_models.DescribeDomainsUsageByDayRequest,
    ) -> main_models.DescribeDomainsUsageByDayResponse:
        runtime = RuntimeOptions()
        return self.describe_domains_usage_by_day_with_options(request, runtime)

    async def describe_domains_usage_by_day_async(
        self,
        request: main_models.DescribeDomainsUsageByDayRequest,
    ) -> main_models.DescribeDomainsUsageByDayResponse:
        runtime = RuntimeOptions()
        return await self.describe_domains_usage_by_day_with_options_async(request, runtime)

    def describe_es_exception_data_with_options(
        self,
        request: main_models.DescribeEsExceptionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEsExceptionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEsExceptionData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEsExceptionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_es_exception_data_with_options_async(
        self,
        request: main_models.DescribeEsExceptionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEsExceptionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEsExceptionData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEsExceptionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_es_exception_data(
        self,
        request: main_models.DescribeEsExceptionDataRequest,
    ) -> main_models.DescribeEsExceptionDataResponse:
        runtime = RuntimeOptions()
        return self.describe_es_exception_data_with_options(request, runtime)

    async def describe_es_exception_data_async(
        self,
        request: main_models.DescribeEsExceptionDataRequest,
    ) -> main_models.DescribeEsExceptionDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_es_exception_data_with_options_async(request, runtime)

    def describe_es_execute_data_with_options(
        self,
        request: main_models.DescribeEsExecuteDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEsExecuteDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEsExecuteData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEsExecuteDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_es_execute_data_with_options_async(
        self,
        request: main_models.DescribeEsExecuteDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEsExecuteDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEsExecuteData',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEsExecuteDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_es_execute_data(
        self,
        request: main_models.DescribeEsExecuteDataRequest,
    ) -> main_models.DescribeEsExecuteDataResponse:
        runtime = RuntimeOptions()
        return self.describe_es_execute_data_with_options(request, runtime)

    async def describe_es_execute_data_async(
        self,
        request: main_models.DescribeEsExecuteDataRequest,
    ) -> main_models.DescribeEsExecuteDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_es_execute_data_with_options_async(request, runtime)

    def describe_fctrigger_with_options(
        self,
        request: main_models.DescribeFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFCTriggerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fctrigger_with_options_async(
        self,
        request: main_models.DescribeFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFCTriggerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fctrigger(
        self,
        request: main_models.DescribeFCTriggerRequest,
    ) -> main_models.DescribeFCTriggerResponse:
        runtime = RuntimeOptions()
        return self.describe_fctrigger_with_options(request, runtime)

    async def describe_fctrigger_async(
        self,
        request: main_models.DescribeFCTriggerRequest,
    ) -> main_models.DescribeFCTriggerResponse:
        runtime = RuntimeOptions()
        return await self.describe_fctrigger_with_options_async(request, runtime)

    def describe_ip_info_with_options(
        self,
        request: main_models.DescribeIpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_info_with_options_async(
        self,
        request: main_models.DescribeIpInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpInfo',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_info(
        self,
        request: main_models.DescribeIpInfoRequest,
    ) -> main_models.DescribeIpInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_info_with_options(request, runtime)

    async def describe_ip_info_async(
        self,
        request: main_models.DescribeIpInfoRequest,
    ) -> main_models.DescribeIpInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_info_with_options_async(request, runtime)

    def describe_ip_status_with_options(
        self,
        request: main_models.DescribeIpStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpStatus',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_status_with_options_async(
        self,
        request: main_models.DescribeIpStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpStatus',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_status(
        self,
        request: main_models.DescribeIpStatusRequest,
    ) -> main_models.DescribeIpStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_status_with_options(request, runtime)

    async def describe_ip_status_async(
        self,
        request: main_models.DescribeIpStatusRequest,
    ) -> main_models.DescribeIpStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_status_with_options_async(request, runtime)

    def describe_l2vips_by_domain_with_options(
        self,
        request: main_models.DescribeL2VipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL2VipsByDomainResponse:
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
            action = 'DescribeL2VipsByDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL2VipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_l2vips_by_domain_with_options_async(
        self,
        request: main_models.DescribeL2VipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL2VipsByDomainResponse:
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
            action = 'DescribeL2VipsByDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL2VipsByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_l2vips_by_domain(
        self,
        request: main_models.DescribeL2VipsByDomainRequest,
    ) -> main_models.DescribeL2VipsByDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_l2vips_by_domain_with_options(request, runtime)

    async def describe_l2vips_by_domain_async(
        self,
        request: main_models.DescribeL2VipsByDomainRequest,
    ) -> main_models.DescribeL2VipsByDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_l2vips_by_domain_with_options_async(request, runtime)

    def describe_preload_detail_by_id_with_options(
        self,
        request: main_models.DescribePreloadDetailByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreloadDetailByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreloadDetailById',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreloadDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_preload_detail_by_id_with_options_async(
        self,
        request: main_models.DescribePreloadDetailByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreloadDetailByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreloadDetailById',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreloadDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_preload_detail_by_id(
        self,
        request: main_models.DescribePreloadDetailByIdRequest,
    ) -> main_models.DescribePreloadDetailByIdResponse:
        runtime = RuntimeOptions()
        return self.describe_preload_detail_by_id_with_options(request, runtime)

    async def describe_preload_detail_by_id_async(
        self,
        request: main_models.DescribePreloadDetailByIdRequest,
    ) -> main_models.DescribePreloadDetailByIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_preload_detail_by_id_with_options_async(request, runtime)

    def describe_range_data_by_locate_and_isp_service_with_options(
        self,
        request: main_models.DescribeRangeDataByLocateAndIspServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRangeDataByLocateAndIspServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_names):
            query['IspNames'] = request.isp_names
        if not DaraCore.is_null(request.location_names):
            query['LocationNames'] = request.location_names
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRangeDataByLocateAndIspService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRangeDataByLocateAndIspServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_range_data_by_locate_and_isp_service_with_options_async(
        self,
        request: main_models.DescribeRangeDataByLocateAndIspServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRangeDataByLocateAndIspServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_names):
            query['IspNames'] = request.isp_names
        if not DaraCore.is_null(request.location_names):
            query['LocationNames'] = request.location_names
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRangeDataByLocateAndIspService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRangeDataByLocateAndIspServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_range_data_by_locate_and_isp_service(
        self,
        request: main_models.DescribeRangeDataByLocateAndIspServiceRequest,
    ) -> main_models.DescribeRangeDataByLocateAndIspServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_range_data_by_locate_and_isp_service_with_options(request, runtime)

    async def describe_range_data_by_locate_and_isp_service_async(
        self,
        request: main_models.DescribeRangeDataByLocateAndIspServiceRequest,
    ) -> main_models.DescribeRangeDataByLocateAndIspServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_range_data_by_locate_and_isp_service_with_options_async(request, runtime)

    def describe_realtime_delivery_acc_with_options(
        self,
        request: main_models.DescribeRealtimeDeliveryAccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRealtimeDeliveryAccResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
        if not DaraCore.is_null(request.project):
            query['Project'] = request.project
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRealtimeDeliveryAcc',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRealtimeDeliveryAccResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_realtime_delivery_acc_with_options_async(
        self,
        request: main_models.DescribeRealtimeDeliveryAccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRealtimeDeliveryAccResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
        if not DaraCore.is_null(request.project):
            query['Project'] = request.project
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRealtimeDeliveryAcc',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRealtimeDeliveryAccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_realtime_delivery_acc(
        self,
        request: main_models.DescribeRealtimeDeliveryAccRequest,
    ) -> main_models.DescribeRealtimeDeliveryAccResponse:
        runtime = RuntimeOptions()
        return self.describe_realtime_delivery_acc_with_options(request, runtime)

    async def describe_realtime_delivery_acc_async(
        self,
        request: main_models.DescribeRealtimeDeliveryAccRequest,
    ) -> main_models.DescribeRealtimeDeliveryAccResponse:
        runtime = RuntimeOptions()
        return await self.describe_realtime_delivery_acc_with_options_async(request, runtime)

    def describe_refresh_quota_with_options(
        self,
        request: main_models.DescribeRefreshQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRefreshQuotaResponse:
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
            action = 'DescribeRefreshQuota',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_refresh_quota_with_options_async(
        self,
        request: main_models.DescribeRefreshQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRefreshQuotaResponse:
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
            action = 'DescribeRefreshQuota',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRefreshQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_refresh_quota(
        self,
        request: main_models.DescribeRefreshQuotaRequest,
    ) -> main_models.DescribeRefreshQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_refresh_quota_with_options(request, runtime)

    async def describe_refresh_quota_async(
        self,
        request: main_models.DescribeRefreshQuotaRequest,
    ) -> main_models.DescribeRefreshQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_refresh_quota_with_options_async(request, runtime)

    def describe_refresh_task_by_id_with_options(
        self,
        request: main_models.DescribeRefreshTaskByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRefreshTaskByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRefreshTaskById',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRefreshTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_refresh_task_by_id_with_options_async(
        self,
        request: main_models.DescribeRefreshTaskByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRefreshTaskByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRefreshTaskById',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRefreshTaskByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_refresh_task_by_id(
        self,
        request: main_models.DescribeRefreshTaskByIdRequest,
    ) -> main_models.DescribeRefreshTaskByIdResponse:
        runtime = RuntimeOptions()
        return self.describe_refresh_task_by_id_with_options(request, runtime)

    async def describe_refresh_task_by_id_async(
        self,
        request: main_models.DescribeRefreshTaskByIdRequest,
    ) -> main_models.DescribeRefreshTaskByIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_refresh_task_by_id_with_options_async(request, runtime)

    def describe_refresh_tasks_with_options(
        self,
        request: main_models.DescribeRefreshTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRefreshTasksResponse:
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action = 'DescribeRefreshTasks',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_refresh_tasks_with_options_async(
        self,
        request: main_models.DescribeRefreshTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRefreshTasksResponse:
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action = 'DescribeRefreshTasks',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRefreshTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_refresh_tasks(
        self,
        request: main_models.DescribeRefreshTasksRequest,
    ) -> main_models.DescribeRefreshTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_refresh_tasks_with_options(request, runtime)

    async def describe_refresh_tasks_async(
        self,
        request: main_models.DescribeRefreshTasksRequest,
    ) -> main_models.DescribeRefreshTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_refresh_tasks_with_options_async(request, runtime)

    def describe_staging_ip_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStagingIpResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeStagingIp',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStagingIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_staging_ip_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStagingIpResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeStagingIp',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStagingIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_staging_ip(self) -> main_models.DescribeStagingIpResponse:
        runtime = RuntimeOptions()
        return self.describe_staging_ip_with_options(runtime)

    async def describe_staging_ip_async(self) -> main_models.DescribeStagingIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_staging_ip_with_options_async(runtime)

    def describe_tag_resources_with_options(
        self,
        request: main_models.DescribeTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagResourcesResponse:
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
            action = 'DescribeTagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_resources_with_options_async(
        self,
        request: main_models.DescribeTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagResourcesResponse:
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
            action = 'DescribeTagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_resources(
        self,
        request: main_models.DescribeTagResourcesRequest,
    ) -> main_models.DescribeTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    async def describe_tag_resources_async(
        self,
        request: main_models.DescribeTagResourcesRequest,
    ) -> main_models.DescribeTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_resources_with_options_async(request, runtime)

    def describe_top_domains_by_flow_with_options(
        self,
        request: main_models.DescribeTopDomainsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopDomainsByFlowResponse:
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
            action = 'DescribeTopDomainsByFlow',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_domains_by_flow_with_options_async(
        self,
        request: main_models.DescribeTopDomainsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopDomainsByFlowResponse:
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
            action = 'DescribeTopDomainsByFlow',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_domains_by_flow(
        self,
        request: main_models.DescribeTopDomainsByFlowRequest,
    ) -> main_models.DescribeTopDomainsByFlowResponse:
        runtime = RuntimeOptions()
        return self.describe_top_domains_by_flow_with_options(request, runtime)

    async def describe_top_domains_by_flow_async(
        self,
        request: main_models.DescribeTopDomainsByFlowRequest,
    ) -> main_models.DescribeTopDomainsByFlowResponse:
        runtime = RuntimeOptions()
        return await self.describe_top_domains_by_flow_with_options_async(request, runtime)

    def describe_user_cdn_status_with_options(
        self,
        request: main_models.DescribeUserCdnStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserCdnStatusResponse:
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
            action = 'DescribeUserCdnStatus',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserCdnStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_cdn_status_with_options_async(
        self,
        request: main_models.DescribeUserCdnStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserCdnStatusResponse:
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
            action = 'DescribeUserCdnStatus',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserCdnStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_cdn_status(
        self,
        request: main_models.DescribeUserCdnStatusRequest,
    ) -> main_models.DescribeUserCdnStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_cdn_status_with_options(request, runtime)

    async def describe_user_cdn_status_async(
        self,
        request: main_models.DescribeUserCdnStatusRequest,
    ) -> main_models.DescribeUserCdnStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_cdn_status_with_options_async(request, runtime)

    def describe_user_certificate_expire_count_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserCertificateExpireCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUserCertificateExpireCount',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserCertificateExpireCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_certificate_expire_count_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserCertificateExpireCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUserCertificateExpireCount',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserCertificateExpireCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_certificate_expire_count(self) -> main_models.DescribeUserCertificateExpireCountResponse:
        runtime = RuntimeOptions()
        return self.describe_user_certificate_expire_count_with_options(runtime)

    async def describe_user_certificate_expire_count_async(self) -> main_models.DescribeUserCertificateExpireCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_certificate_expire_count_with_options_async(runtime)

    def describe_user_configs_with_options(
        self,
        request: main_models.DescribeUserConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserConfigs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_configs_with_options_async(
        self,
        request: main_models.DescribeUserConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserConfigs',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_configs(
        self,
        request: main_models.DescribeUserConfigsRequest,
    ) -> main_models.DescribeUserConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_configs_with_options(request, runtime)

    async def describe_user_configs_async(
        self,
        request: main_models.DescribeUserConfigsRequest,
    ) -> main_models.DescribeUserConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_configs_with_options_async(request, runtime)

    def describe_user_domains_with_options(
        self,
        request: main_models.DescribeUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserDomains',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_domains_with_options_async(
        self,
        request: main_models.DescribeUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserDomains',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_domains(
        self,
        request: main_models.DescribeUserDomainsRequest,
    ) -> main_models.DescribeUserDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_domains_with_options(request, runtime)

    async def describe_user_domains_async(
        self,
        request: main_models.DescribeUserDomainsRequest,
    ) -> main_models.DescribeUserDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_domains_with_options_async(request, runtime)

    def describe_user_tags_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTagsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUserTags',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_tags_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTagsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUserTags',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_tags(self) -> main_models.DescribeUserTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_tags_with_options(runtime)

    async def describe_user_tags_async(self) -> main_models.DescribeUserTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_tags_with_options_async(runtime)

    def describe_user_usage_data_export_task_with_options(
        self,
        request: main_models.DescribeUserUsageDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserUsageDataExportTaskResponse:
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
            action = 'DescribeUserUsageDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_usage_data_export_task_with_options_async(
        self,
        request: main_models.DescribeUserUsageDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserUsageDataExportTaskResponse:
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
            action = 'DescribeUserUsageDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserUsageDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_usage_data_export_task(
        self,
        request: main_models.DescribeUserUsageDataExportTaskRequest,
    ) -> main_models.DescribeUserUsageDataExportTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_user_usage_data_export_task_with_options(request, runtime)

    async def describe_user_usage_data_export_task_async(
        self,
        request: main_models.DescribeUserUsageDataExportTaskRequest,
    ) -> main_models.DescribeUserUsageDataExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_usage_data_export_task_with_options_async(request, runtime)

    def describe_user_usage_detail_data_export_task_with_options(
        self,
        request: main_models.DescribeUserUsageDetailDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserUsageDetailDataExportTaskResponse:
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
            action = 'DescribeUserUsageDetailDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_usage_detail_data_export_task_with_options_async(
        self,
        request: main_models.DescribeUserUsageDetailDataExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserUsageDetailDataExportTaskResponse:
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
            action = 'DescribeUserUsageDetailDataExportTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserUsageDetailDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_usage_detail_data_export_task(
        self,
        request: main_models.DescribeUserUsageDetailDataExportTaskRequest,
    ) -> main_models.DescribeUserUsageDetailDataExportTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_user_usage_detail_data_export_task_with_options(request, runtime)

    async def describe_user_usage_detail_data_export_task_async(
        self,
        request: main_models.DescribeUserUsageDetailDataExportTaskRequest,
    ) -> main_models.DescribeUserUsageDetailDataExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_usage_detail_data_export_task_with_options_async(request, runtime)

    def describe_user_vips_by_domain_with_options(
        self,
        request: main_models.DescribeUserVipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserVipsByDomainResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserVipsByDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserVipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_vips_by_domain_with_options_async(
        self,
        request: main_models.DescribeUserVipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserVipsByDomainResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserVipsByDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserVipsByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_vips_by_domain(
        self,
        request: main_models.DescribeUserVipsByDomainRequest,
    ) -> main_models.DescribeUserVipsByDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_user_vips_by_domain_with_options(request, runtime)

    async def describe_user_vips_by_domain_async(
        self,
        request: main_models.DescribeUserVipsByDomainRequest,
    ) -> main_models.DescribeUserVipsByDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_vips_by_domain_with_options_async(request, runtime)

    def describe_verify_content_with_options(
        self,
        request: main_models.DescribeVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyContent',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_content_with_options_async(
        self,
        request: main_models.DescribeVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyContent',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_content(
        self,
        request: main_models.DescribeVerifyContentRequest,
    ) -> main_models.DescribeVerifyContentResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_content_with_options(request, runtime)

    async def describe_verify_content_async(
        self,
        request: main_models.DescribeVerifyContentRequest,
    ) -> main_models.DescribeVerifyContentResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_content_with_options_async(request, runtime)

    def disable_realtime_log_delivery_with_options(
        self,
        request: main_models.DisableRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_realtime_log_delivery_with_options_async(
        self,
        request: main_models.DisableRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_realtime_log_delivery(
        self,
        request: main_models.DisableRealtimeLogDeliveryRequest,
    ) -> main_models.DisableRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.disable_realtime_log_delivery_with_options(request, runtime)

    async def disable_realtime_log_delivery_async(
        self,
        request: main_models.DisableRealtimeLogDeliveryRequest,
    ) -> main_models.DisableRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.disable_realtime_log_delivery_with_options_async(request, runtime)

    def enable_realtime_log_delivery_with_options(
        self,
        request: main_models.EnableRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_realtime_log_delivery_with_options_async(
        self,
        request: main_models.EnableRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_realtime_log_delivery(
        self,
        request: main_models.EnableRealtimeLogDeliveryRequest,
    ) -> main_models.EnableRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.enable_realtime_log_delivery_with_options(request, runtime)

    async def enable_realtime_log_delivery_async(
        self,
        request: main_models.EnableRealtimeLogDeliveryRequest,
    ) -> main_models.EnableRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.enable_realtime_log_delivery_with_options_async(request, runtime)

    def get_gray_domain_function_with_options(
        self,
        request: main_models.GetGrayDomainFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGrayDomainFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            body['FunctionNames'] = request.function_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGrayDomainFunction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGrayDomainFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gray_domain_function_with_options_async(
        self,
        request: main_models.GetGrayDomainFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGrayDomainFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            body['FunctionNames'] = request.function_names
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGrayDomainFunction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGrayDomainFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gray_domain_function(
        self,
        request: main_models.GetGrayDomainFunctionRequest,
    ) -> main_models.GetGrayDomainFunctionResponse:
        runtime = RuntimeOptions()
        return self.get_gray_domain_function_with_options(request, runtime)

    async def get_gray_domain_function_async(
        self,
        request: main_models.GetGrayDomainFunctionRequest,
    ) -> main_models.GetGrayDomainFunctionResponse:
        runtime = RuntimeOptions()
        return await self.get_gray_domain_function_with_options_async(request, runtime)

    def list_domains_by_log_config_id_with_options(
        self,
        request: main_models.ListDomainsByLogConfigIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsByLogConfigIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomainsByLogConfigId',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsByLogConfigIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_by_log_config_id_with_options_async(
        self,
        request: main_models.ListDomainsByLogConfigIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsByLogConfigIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomainsByLogConfigId',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsByLogConfigIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains_by_log_config_id(
        self,
        request: main_models.ListDomainsByLogConfigIdRequest,
    ) -> main_models.ListDomainsByLogConfigIdResponse:
        runtime = RuntimeOptions()
        return self.list_domains_by_log_config_id_with_options(request, runtime)

    async def list_domains_by_log_config_id_async(
        self,
        request: main_models.ListDomainsByLogConfigIdRequest,
    ) -> main_models.ListDomainsByLogConfigIdResponse:
        runtime = RuntimeOptions()
        return await self.list_domains_by_log_config_id_with_options_async(request, runtime)

    def list_fctrigger_with_options(
        self,
        request: main_models.ListFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFCTriggerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fctrigger_with_options_async(
        self,
        request: main_models.ListFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFCTriggerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fctrigger(
        self,
        request: main_models.ListFCTriggerRequest,
    ) -> main_models.ListFCTriggerResponse:
        runtime = RuntimeOptions()
        return self.list_fctrigger_with_options(request, runtime)

    async def list_fctrigger_async(
        self,
        request: main_models.ListFCTriggerRequest,
    ) -> main_models.ListFCTriggerResponse:
        runtime = RuntimeOptions()
        return await self.list_fctrigger_with_options_async(request, runtime)

    def list_realtime_log_delivery_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeLogDeliveryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_log_delivery_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeLogDeliveryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_log_delivery(self) -> main_models.ListRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.list_realtime_log_delivery_with_options(runtime)

    async def list_realtime_log_delivery_async(self) -> main_models.ListRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.list_realtime_log_delivery_with_options_async(runtime)

    def list_realtime_log_delivery_domains_with_options(
        self,
        request: main_models.ListRealtimeLogDeliveryDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeLogDeliveryDomainsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRealtimeLogDeliveryDomains',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeLogDeliveryDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_log_delivery_domains_with_options_async(
        self,
        request: main_models.ListRealtimeLogDeliveryDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeLogDeliveryDomainsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRealtimeLogDeliveryDomains',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeLogDeliveryDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_log_delivery_domains(
        self,
        request: main_models.ListRealtimeLogDeliveryDomainsRequest,
    ) -> main_models.ListRealtimeLogDeliveryDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_realtime_log_delivery_domains_with_options(request, runtime)

    async def list_realtime_log_delivery_domains_async(
        self,
        request: main_models.ListRealtimeLogDeliveryDomainsRequest,
    ) -> main_models.ListRealtimeLogDeliveryDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_realtime_log_delivery_domains_with_options_async(request, runtime)

    def list_realtime_log_delivery_infos_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeLogDeliveryInfosResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRealtimeLogDeliveryInfos',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeLogDeliveryInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_log_delivery_infos_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRealtimeLogDeliveryInfosResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRealtimeLogDeliveryInfos',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRealtimeLogDeliveryInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_log_delivery_infos(self) -> main_models.ListRealtimeLogDeliveryInfosResponse:
        runtime = RuntimeOptions()
        return self.list_realtime_log_delivery_infos_with_options(runtime)

    async def list_realtime_log_delivery_infos_async(self) -> main_models.ListRealtimeLogDeliveryInfosResponse:
        runtime = RuntimeOptions()
        return await self.list_realtime_log_delivery_infos_with_options_async(runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not DaraCore.is_null(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not DaraCore.is_null(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_custom_log_config_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserCustomLogConfigResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListUserCustomLogConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_custom_log_config_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserCustomLogConfigResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListUserCustomLogConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_custom_log_config(self) -> main_models.ListUserCustomLogConfigResponse:
        runtime = RuntimeOptions()
        return self.list_user_custom_log_config_with_options(runtime)

    async def list_user_custom_log_config_async(self) -> main_models.ListUserCustomLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_user_custom_log_config_with_options_async(runtime)

    def modify_cdn_domain_with_options(
        self,
        request: main_models.ModifyCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnDomainResponse:
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
            action = 'ModifyCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdn_domain_with_options_async(
        self,
        request: main_models.ModifyCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnDomainResponse:
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
            action = 'ModifyCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdn_domain(
        self,
        request: main_models.ModifyCdnDomainRequest,
    ) -> main_models.ModifyCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.modify_cdn_domain_with_options(request, runtime)

    async def modify_cdn_domain_async(
        self,
        request: main_models.ModifyCdnDomainRequest,
    ) -> main_models.ModifyCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.modify_cdn_domain_with_options_async(request, runtime)

    def modify_cdn_domain_owner_with_options(
        self,
        request: main_models.ModifyCdnDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnDomainOwnerResponse:
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
            action = 'ModifyCdnDomainOwner',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdn_domain_owner_with_options_async(
        self,
        request: main_models.ModifyCdnDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnDomainOwnerResponse:
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
            action = 'ModifyCdnDomainOwner',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdn_domain_owner(
        self,
        request: main_models.ModifyCdnDomainOwnerRequest,
    ) -> main_models.ModifyCdnDomainOwnerResponse:
        runtime = RuntimeOptions()
        return self.modify_cdn_domain_owner_with_options(request, runtime)

    async def modify_cdn_domain_owner_async(
        self,
        request: main_models.ModifyCdnDomainOwnerRequest,
    ) -> main_models.ModifyCdnDomainOwnerResponse:
        runtime = RuntimeOptions()
        return await self.modify_cdn_domain_owner_with_options_async(request, runtime)

    def modify_cdn_domain_schdm_by_property_with_options(
        self,
        request: main_models.ModifyCdnDomainSchdmByPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnDomainSchdmByPropertyResponse:
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
            action = 'ModifyCdnDomainSchdmByProperty',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdn_domain_schdm_by_property_with_options_async(
        self,
        request: main_models.ModifyCdnDomainSchdmByPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnDomainSchdmByPropertyResponse:
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
            action = 'ModifyCdnDomainSchdmByProperty',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnDomainSchdmByPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdn_domain_schdm_by_property(
        self,
        request: main_models.ModifyCdnDomainSchdmByPropertyRequest,
    ) -> main_models.ModifyCdnDomainSchdmByPropertyResponse:
        runtime = RuntimeOptions()
        return self.modify_cdn_domain_schdm_by_property_with_options(request, runtime)

    async def modify_cdn_domain_schdm_by_property_async(
        self,
        request: main_models.ModifyCdnDomainSchdmByPropertyRequest,
    ) -> main_models.ModifyCdnDomainSchdmByPropertyResponse:
        runtime = RuntimeOptions()
        return await self.modify_cdn_domain_schdm_by_property_with_options_async(request, runtime)

    def modify_cdn_service_with_options(
        self,
        request: main_models.ModifyCdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCdnService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdn_service_with_options_async(
        self,
        request: main_models.ModifyCdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCdnService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdn_service(
        self,
        request: main_models.ModifyCdnServiceRequest,
    ) -> main_models.ModifyCdnServiceResponse:
        runtime = RuntimeOptions()
        return self.modify_cdn_service_with_options(request, runtime)

    async def modify_cdn_service_async(
        self,
        request: main_models.ModifyCdnServiceRequest,
    ) -> main_models.ModifyCdnServiceResponse:
        runtime = RuntimeOptions()
        return await self.modify_cdn_service_with_options_async(request, runtime)

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
            version = '2018-05-10',
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
            version = '2018-05-10',
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

    def modify_realtime_log_delivery_with_options(
        self,
        request: main_models.ModifyRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_realtime_log_delivery_with_options_async(
        self,
        request: main_models.ModifyRealtimeLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRealtimeLogDeliveryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRealtimeLogDelivery',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_realtime_log_delivery(
        self,
        request: main_models.ModifyRealtimeLogDeliveryRequest,
    ) -> main_models.ModifyRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.modify_realtime_log_delivery_with_options(request, runtime)

    async def modify_realtime_log_delivery_async(
        self,
        request: main_models.ModifyRealtimeLogDeliveryRequest,
    ) -> main_models.ModifyRealtimeLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.modify_realtime_log_delivery_with_options_async(request, runtime)

    def open_cdn_service_with_options(
        self,
        request: main_models.OpenCdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenCdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenCdnService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cdn_service_with_options_async(
        self,
        request: main_models.OpenCdnServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenCdnServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenCdnService',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenCdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cdn_service(
        self,
        request: main_models.OpenCdnServiceRequest,
    ) -> main_models.OpenCdnServiceResponse:
        runtime = RuntimeOptions()
        return self.open_cdn_service_with_options(request, runtime)

    async def open_cdn_service_async(
        self,
        request: main_models.OpenCdnServiceRequest,
    ) -> main_models.OpenCdnServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_cdn_service_with_options_async(request, runtime)

    def publish_gray_domain_config_with_options(
        self,
        request: main_models.PublishGrayDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishGrayDomainConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_country_id):
            body['CustomCountryId'] = request.custom_country_id
        if not DaraCore.is_null(request.custom_percent):
            body['CustomPercent'] = request.custom_percent
        if not DaraCore.is_null(request.custom_province_id):
            body['CustomProvinceId'] = request.custom_province_id
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishGrayDomainConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishGrayDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_gray_domain_config_with_options_async(
        self,
        request: main_models.PublishGrayDomainConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishGrayDomainConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_country_id):
            body['CustomCountryId'] = request.custom_country_id
        if not DaraCore.is_null(request.custom_percent):
            body['CustomPercent'] = request.custom_percent
        if not DaraCore.is_null(request.custom_province_id):
            body['CustomProvinceId'] = request.custom_province_id
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishGrayDomainConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishGrayDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_gray_domain_config(
        self,
        request: main_models.PublishGrayDomainConfigRequest,
    ) -> main_models.PublishGrayDomainConfigResponse:
        runtime = RuntimeOptions()
        return self.publish_gray_domain_config_with_options(request, runtime)

    async def publish_gray_domain_config_async(
        self,
        request: main_models.PublishGrayDomainConfigRequest,
    ) -> main_models.PublishGrayDomainConfigResponse:
        runtime = RuntimeOptions()
        return await self.publish_gray_domain_config_with_options_async(request, runtime)

    def publish_staging_config_to_production_with_options(
        self,
        request: main_models.PublishStagingConfigToProductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishStagingConfigToProductionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishStagingConfigToProduction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_staging_config_to_production_with_options_async(
        self,
        request: main_models.PublishStagingConfigToProductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishStagingConfigToProductionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishStagingConfigToProduction',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishStagingConfigToProductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_staging_config_to_production(
        self,
        request: main_models.PublishStagingConfigToProductionRequest,
    ) -> main_models.PublishStagingConfigToProductionResponse:
        runtime = RuntimeOptions()
        return self.publish_staging_config_to_production_with_options(request, runtime)

    async def publish_staging_config_to_production_async(
        self,
        request: main_models.PublishStagingConfigToProductionRequest,
    ) -> main_models.PublishStagingConfigToProductionResponse:
        runtime = RuntimeOptions()
        return await self.publish_staging_config_to_production_with_options_async(request, runtime)

    def push_object_cache_with_options(
        self,
        request: main_models.PushObjectCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushObjectCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.consistency_hash):
            query['ConsistencyHash'] = request.consistency_hash
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
            action = 'PushObjectCache',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushObjectCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_object_cache_with_options_async(
        self,
        request: main_models.PushObjectCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushObjectCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.consistency_hash):
            query['ConsistencyHash'] = request.consistency_hash
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
            action = 'PushObjectCache',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushObjectCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_object_cache(
        self,
        request: main_models.PushObjectCacheRequest,
    ) -> main_models.PushObjectCacheResponse:
        runtime = RuntimeOptions()
        return self.push_object_cache_with_options(request, runtime)

    async def push_object_cache_async(
        self,
        request: main_models.PushObjectCacheRequest,
    ) -> main_models.PushObjectCacheResponse:
        runtime = RuntimeOptions()
        return await self.push_object_cache_with_options_async(request, runtime)

    def refresh_object_cache_by_cache_tag_with_options(
        self,
        request: main_models.RefreshObjectCacheByCacheTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshObjectCacheByCacheTagResponse:
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
            action = 'RefreshObjectCacheByCacheTag',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshObjectCacheByCacheTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_object_cache_by_cache_tag_with_options_async(
        self,
        request: main_models.RefreshObjectCacheByCacheTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshObjectCacheByCacheTagResponse:
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
            action = 'RefreshObjectCacheByCacheTag',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshObjectCacheByCacheTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_object_cache_by_cache_tag(
        self,
        request: main_models.RefreshObjectCacheByCacheTagRequest,
    ) -> main_models.RefreshObjectCacheByCacheTagResponse:
        runtime = RuntimeOptions()
        return self.refresh_object_cache_by_cache_tag_with_options(request, runtime)

    async def refresh_object_cache_by_cache_tag_async(
        self,
        request: main_models.RefreshObjectCacheByCacheTagRequest,
    ) -> main_models.RefreshObjectCacheByCacheTagResponse:
        runtime = RuntimeOptions()
        return await self.refresh_object_cache_by_cache_tag_with_options_async(request, runtime)

    def refresh_object_caches_with_options(
        self,
        request: main_models.RefreshObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.object_path):
            body['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            body['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshObjectCaches',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_object_caches_with_options_async(
        self,
        request: main_models.RefreshObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.object_path):
            body['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            body['ObjectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshObjectCaches',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_object_caches(
        self,
        request: main_models.RefreshObjectCachesRequest,
    ) -> main_models.RefreshObjectCachesResponse:
        runtime = RuntimeOptions()
        return self.refresh_object_caches_with_options(request, runtime)

    async def refresh_object_caches_async(
        self,
        request: main_models.RefreshObjectCachesRequest,
    ) -> main_models.RefreshObjectCachesResponse:
        runtime = RuntimeOptions()
        return await self.refresh_object_caches_with_options_async(request, runtime)

    def rollback_staging_config_with_options(
        self,
        request: main_models.RollbackStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_staging_config_with_options_async(
        self,
        request: main_models.RollbackStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackStagingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_staging_config(
        self,
        request: main_models.RollbackStagingConfigRequest,
    ) -> main_models.RollbackStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.rollback_staging_config_with_options(request, runtime)

    async def rollback_staging_config_async(
        self,
        request: main_models.RollbackStagingConfigRequest,
    ) -> main_models.RollbackStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.rollback_staging_config_with_options_async(request, runtime)

    def set_cdn_domain_csrcertificate_with_options(
        self,
        request: main_models.SetCdnDomainCSRCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainCSRCertificateResponse:
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
            action = 'SetCdnDomainCSRCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainCSRCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_csrcertificate_with_options_async(
        self,
        request: main_models.SetCdnDomainCSRCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainCSRCertificateResponse:
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
            action = 'SetCdnDomainCSRCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainCSRCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_csrcertificate(
        self,
        request: main_models.SetCdnDomainCSRCertificateRequest,
    ) -> main_models.SetCdnDomainCSRCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_cdn_domain_csrcertificate_with_options(request, runtime)

    async def set_cdn_domain_csrcertificate_async(
        self,
        request: main_models.SetCdnDomainCSRCertificateRequest,
    ) -> main_models.SetCdnDomainCSRCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_cdn_domain_csrcertificate_with_options_async(request, runtime)

    def set_cdn_domain_smcertificate_with_options(
        self,
        request: main_models.SetCdnDomainSMCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainSMCertificateResponse:
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
            action = 'SetCdnDomainSMCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainSMCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_smcertificate_with_options_async(
        self,
        request: main_models.SetCdnDomainSMCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainSMCertificateResponse:
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
            action = 'SetCdnDomainSMCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainSMCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_smcertificate(
        self,
        request: main_models.SetCdnDomainSMCertificateRequest,
    ) -> main_models.SetCdnDomainSMCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_cdn_domain_smcertificate_with_options(request, runtime)

    async def set_cdn_domain_smcertificate_async(
        self,
        request: main_models.SetCdnDomainSMCertificateRequest,
    ) -> main_models.SetCdnDomainSMCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_cdn_domain_smcertificate_with_options_async(request, runtime)

    def set_cdn_domain_sslcertificate_with_options(
        self,
        request: main_models.SetCdnDomainSSLCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainSSLCertificateResponse:
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
            action = 'SetCdnDomainSSLCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_sslcertificate_with_options_async(
        self,
        request: main_models.SetCdnDomainSSLCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainSSLCertificateResponse:
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
            action = 'SetCdnDomainSSLCertificate',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_sslcertificate(
        self,
        request: main_models.SetCdnDomainSSLCertificateRequest,
    ) -> main_models.SetCdnDomainSSLCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_cdn_domain_sslcertificate_with_options(request, runtime)

    async def set_cdn_domain_sslcertificate_async(
        self,
        request: main_models.SetCdnDomainSSLCertificateRequest,
    ) -> main_models.SetCdnDomainSSLCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_cdn_domain_sslcertificate_with_options_async(request, runtime)

    def set_cdn_domain_staging_config_with_options(
        self,
        request: main_models.SetCdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainStagingConfigResponse:
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
            action = 'SetCdnDomainStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_staging_config_with_options_async(
        self,
        request: main_models.SetCdnDomainStagingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnDomainStagingConfigResponse:
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
            action = 'SetCdnDomainStagingConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_staging_config(
        self,
        request: main_models.SetCdnDomainStagingConfigRequest,
    ) -> main_models.SetCdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return self.set_cdn_domain_staging_config_with_options(request, runtime)

    async def set_cdn_domain_staging_config_async(
        self,
        request: main_models.SetCdnDomainStagingConfigRequest,
    ) -> main_models.SetCdnDomainStagingConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_cdn_domain_staging_config_with_options_async(request, runtime)

    def set_cdn_full_domains_block_ipwith_options(
        self,
        request: main_models.SetCdnFullDomainsBlockIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnFullDomainsBlockIPResponse:
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
            action = 'SetCdnFullDomainsBlockIP',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnFullDomainsBlockIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_full_domains_block_ipwith_options_async(
        self,
        request: main_models.SetCdnFullDomainsBlockIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCdnFullDomainsBlockIPResponse:
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
            action = 'SetCdnFullDomainsBlockIP',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCdnFullDomainsBlockIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_full_domains_block_ip(
        self,
        request: main_models.SetCdnFullDomainsBlockIPRequest,
    ) -> main_models.SetCdnFullDomainsBlockIPResponse:
        runtime = RuntimeOptions()
        return self.set_cdn_full_domains_block_ipwith_options(request, runtime)

    async def set_cdn_full_domains_block_ip_async(
        self,
        request: main_models.SetCdnFullDomainsBlockIPRequest,
    ) -> main_models.SetCdnFullDomainsBlockIPResponse:
        runtime = RuntimeOptions()
        return await self.set_cdn_full_domains_block_ipwith_options_async(request, runtime)

    def set_req_header_config_with_options(
        self,
        request: main_models.SetReqHeaderConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetReqHeaderConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetReqHeaderConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetReqHeaderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_req_header_config_with_options_async(
        self,
        request: main_models.SetReqHeaderConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetReqHeaderConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetReqHeaderConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetReqHeaderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_req_header_config(
        self,
        request: main_models.SetReqHeaderConfigRequest,
    ) -> main_models.SetReqHeaderConfigResponse:
        runtime = RuntimeOptions()
        return self.set_req_header_config_with_options(request, runtime)

    async def set_req_header_config_async(
        self,
        request: main_models.SetReqHeaderConfigRequest,
    ) -> main_models.SetReqHeaderConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_req_header_config_with_options_async(request, runtime)

    def set_waiting_room_config_with_options(
        self,
        request: main_models.SetWaitingRoomConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWaitingRoomConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_pct):
            query['AllowPct'] = request.allow_pct
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.gap_time):
            query['GapTime'] = request.gap_time
        if not DaraCore.is_null(request.max_time_wait):
            query['MaxTimeWait'] = request.max_time_wait
        if not DaraCore.is_null(request.wait_uri):
            query['WaitUri'] = request.wait_uri
        if not DaraCore.is_null(request.wait_url):
            query['WaitUrl'] = request.wait_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWaitingRoomConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWaitingRoomConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_waiting_room_config_with_options_async(
        self,
        request: main_models.SetWaitingRoomConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWaitingRoomConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_pct):
            query['AllowPct'] = request.allow_pct
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.gap_time):
            query['GapTime'] = request.gap_time
        if not DaraCore.is_null(request.max_time_wait):
            query['MaxTimeWait'] = request.max_time_wait
        if not DaraCore.is_null(request.wait_uri):
            query['WaitUri'] = request.wait_uri
        if not DaraCore.is_null(request.wait_url):
            query['WaitUrl'] = request.wait_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWaitingRoomConfig',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWaitingRoomConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_waiting_room_config(
        self,
        request: main_models.SetWaitingRoomConfigRequest,
    ) -> main_models.SetWaitingRoomConfigResponse:
        runtime = RuntimeOptions()
        return self.set_waiting_room_config_with_options(request, runtime)

    async def set_waiting_room_config_async(
        self,
        request: main_models.SetWaitingRoomConfigRequest,
    ) -> main_models.SetWaitingRoomConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_waiting_room_config_with_options_async(request, runtime)

    def start_cdn_domain_with_options(
        self,
        request: main_models.StartCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCdnDomainResponse:
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
            action = 'StartCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cdn_domain_with_options_async(
        self,
        request: main_models.StartCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartCdnDomainResponse:
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
            action = 'StartCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cdn_domain(
        self,
        request: main_models.StartCdnDomainRequest,
    ) -> main_models.StartCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.start_cdn_domain_with_options(request, runtime)

    async def start_cdn_domain_async(
        self,
        request: main_models.StartCdnDomainRequest,
    ) -> main_models.StartCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.start_cdn_domain_with_options_async(request, runtime)

    def stop_cdn_domain_with_options(
        self,
        request: main_models.StopCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCdnDomainResponse:
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
            action = 'StopCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cdn_domain_with_options_async(
        self,
        request: main_models.StopCdnDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCdnDomainResponse:
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
            action = 'StopCdnDomain',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cdn_domain(
        self,
        request: main_models.StopCdnDomainRequest,
    ) -> main_models.StopCdnDomainResponse:
        runtime = RuntimeOptions()
        return self.stop_cdn_domain_with_options(request, runtime)

    async def stop_cdn_domain_async(
        self,
        request: main_models.StopCdnDomainRequest,
    ) -> main_models.StopCdnDomainResponse:
        runtime = RuntimeOptions()
        return await self.stop_cdn_domain_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
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
            action = 'TagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
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
            action = 'TagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
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
            action = 'UntagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
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
            action = 'UntagResources',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_cdn_deliver_task_with_options(
        self,
        request: main_models.UpdateCdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCdnDeliverTaskResponse:
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
            action = 'UpdateCdnDeliverTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cdn_deliver_task_with_options_async(
        self,
        request: main_models.UpdateCdnDeliverTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCdnDeliverTaskResponse:
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
            action = 'UpdateCdnDeliverTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cdn_deliver_task(
        self,
        request: main_models.UpdateCdnDeliverTaskRequest,
    ) -> main_models.UpdateCdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return self.update_cdn_deliver_task_with_options(request, runtime)

    async def update_cdn_deliver_task_async(
        self,
        request: main_models.UpdateCdnDeliverTaskRequest,
    ) -> main_models.UpdateCdnDeliverTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_cdn_deliver_task_with_options_async(request, runtime)

    def update_cdn_sub_task_with_options(
        self,
        request: main_models.UpdateCdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCdnSubTaskResponse:
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
            action = 'UpdateCdnSubTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cdn_sub_task_with_options_async(
        self,
        request: main_models.UpdateCdnSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCdnSubTaskResponse:
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
            action = 'UpdateCdnSubTask',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cdn_sub_task(
        self,
        request: main_models.UpdateCdnSubTaskRequest,
    ) -> main_models.UpdateCdnSubTaskResponse:
        runtime = RuntimeOptions()
        return self.update_cdn_sub_task_with_options(request, runtime)

    async def update_cdn_sub_task_async(
        self,
        request: main_models.UpdateCdnSubTaskRequest,
    ) -> main_models.UpdateCdnSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_cdn_sub_task_with_options_async(request, runtime)

    def update_fctrigger_with_options(
        self,
        request: main_models.UpdateFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFCTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not DaraCore.is_null(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not DaraCore.is_null(request.notes):
            body['Notes'] = request.notes
        if not DaraCore.is_null(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_fctrigger_with_options_async(
        self,
        request: main_models.UpdateFCTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFCTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not DaraCore.is_null(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not DaraCore.is_null(request.notes):
            body['Notes'] = request.notes
        if not DaraCore.is_null(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFCTrigger',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_fctrigger(
        self,
        request: main_models.UpdateFCTriggerRequest,
    ) -> main_models.UpdateFCTriggerResponse:
        runtime = RuntimeOptions()
        return self.update_fctrigger_with_options(request, runtime)

    async def update_fctrigger_async(
        self,
        request: main_models.UpdateFCTriggerRequest,
    ) -> main_models.UpdateFCTriggerResponse:
        runtime = RuntimeOptions()
        return await self.update_fctrigger_with_options_async(request, runtime)

    def verify_domain_owner_with_options(
        self,
        request: main_models.VerifyDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyDomainOwnerResponse:
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
            action = 'VerifyDomainOwner',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_domain_owner_with_options_async(
        self,
        request: main_models.VerifyDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyDomainOwnerResponse:
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
            action = 'VerifyDomainOwner',
            version = '2018-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_domain_owner(
        self,
        request: main_models.VerifyDomainOwnerRequest,
    ) -> main_models.VerifyDomainOwnerResponse:
        runtime = RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)

    async def verify_domain_owner_async(
        self,
        request: main_models.VerifyDomainOwnerRequest,
    ) -> main_models.VerifyDomainOwnerResponse:
        runtime = RuntimeOptions()
        return await self.verify_domain_owner_with_options_async(request, runtime)
